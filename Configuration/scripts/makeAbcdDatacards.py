#!/usr/bin/env python

# Given a set of signal region bin edges and data and signal histograms, this script will create
# one datacard for each signal point that contains all signal and control regions along with
# rateParameters that implement the ABCD background estimate in combine.
#
# usage: makeAbcdDatacards.py -l CONFIG -w LIMIT_DIR -E ERA
# sample config: EEChannel/test/abcd_limit_cfg.py

import sys
import copy
import math
import DisplacedSUSY.StandardAnalysis.TreeBranchDefinitions as treeDefs
from collections import OrderedDict
from ROOT import TFile, Double
from DisplacedSUSY.Configuration.limitOptions import *
from DisplacedSUSY.Configuration.systematicsDefinitions import *
from DisplacedSUSY.StandardAnalysis.Options import *
from OSUT3Analysis.Configuration.configurationOptions import *


if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + re.sub (r".py$", r"", arguments.localConfig) + " import *")
else:
    print "No local config specified"
    sys.exit(0)

if arguments.condorDir:
    if not os.path.exists("limits/"+arguments.condorDir):
        os.system("mkdir limits/"+arguments.condorDir)
else:
    print "No output directory specified"
    sys.exit(0)

if not arguments.era in validEras:
  print
  print "Invalid or empty data-taking era specific (-E). Allowed eras:"
  print str(validEras)
  print
  sys.exit(0)
else:
    era = arguments.era


# class to represent rectangular prisms in d0-d0-pT space
class Region(object):
    def __init__(self, name, d0_0_lo, d0_0_hi, d0_1_lo, d0_1_hi, pt_lo, pt_hi):
        name_string = "{}_{:d}to{:d}um_{:d}to{:d}um_{:d}to{:d}GeV"
        self.name = name_string.format(name, d0_0_lo, d0_0_hi, d0_1_lo, d0_1_hi, pt_lo, pt_hi)
        self.name = self.name.replace('-1', 'Inf')
        # rename standard regions for brevity and legibility
        for name, nickname, in predefined_region_names.iteritems():
            self.name = self.name.replace(name, nickname)
        self.d0_0_lo = d0_0_lo
        self.d0_0_hi = d0_0_hi
        self.d0_1_lo = d0_1_lo
        self.d0_1_hi = d0_1_hi
        self.pt_lo = pt_lo
        self.pt_hi = pt_hi
        self.cr = self.name[:1] in ['A', 'B', 'C']
        self.label = self.name[0].lower() if self.cr else 'd'
        self.pt_subregions = None

    # only use name for equality checking because name uniquely defines region in d0-d0-pT space
    # fixme: update to handle nicknames properly
    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return self.name != other.name

    def __hash__(self):
        return hash(self.name)

    def get_d0s(self):
        return (self.d0_0_lo, self.d0_0_hi, self.d0_1_lo, self.d0_1_hi)

    # associate rate parameter name with region
    def set_param(self, rate_param):
        self.param = rate_param

    # identify regions that comprise self when added along pT axis
    def find_pt_subregions(self, unique_regions):
        self.pt_subregions = [r for r in unique_regions if r.get_d0s() == self.get_d0s() and self != r]

    # get bin numbers associated with given values; account for possible overflow inclusion
    def get_bins(self, hist, axis_name, lo, hi):
        if axis_name is "x":
            axis = hist.GetXaxis()
        elif axis_name is "y":
            axis = hist.GetYaxis()
        elif axis_name is "z":
            axis = hist.GetZaxis()
        else:
            print axis_name, "is not a recognized axis name. Try 'x', 'y', or 'z'."

        lo_bin = axis.FindBin(lo)
        # include overflow if hi is -1
        hi_bin = axis.GetNbins()+1 if hi is -1 else axis.FindBin(hi)-1

        if lo != axis.GetBinLowEdge(lo_bin) or (hi != -1 and hi != axis.GetBinUpEdge(hi_bin)):
            raise RuntimeError("Specified bin edge does not align with histogram bin edge")

        return (lo_bin, hi_bin)

    # get integral and number of unweighted events in region
    # account for weights associated with bin width in hists with variable-width bins
    def get_yield_and_num_events(self, hist):
        h = hist.hist
        (x_bin_lo, x_bin_hi) = self.get_bins(h, "x", self.d0_0_lo, self.d0_0_hi)
        (y_bin_lo, y_bin_hi) = self.get_bins(h, "y", self.d0_1_lo, self.d0_1_hi)
        (z_bin_lo, z_bin_hi) = self.get_bins(h, "z", self.pt_lo, self.pt_hi)

        error = Double()
        integral = h.IntegralAndError(x_bin_lo, x_bin_hi, y_bin_lo, y_bin_hi,
                                      z_bin_lo, z_bin_hi, error)

        # multiply yield and error by volume of last bin if histogram was created with
        # variable-width bin constructor
        if hist.var_bins:
            x_width = h.GetXaxis().GetBinWidth(h.GetXaxis().GetNbins())
            y_width = h.GetYaxis().GetBinWidth(h.GetYaxis().GetNbins())
            z_width = h.GetZaxis().GetBinWidth(h.GetZaxis().GetNbins())
            bin_factor = x_width * y_width * z_width
            integral *= bin_factor
            error *= bin_factor

        # round integral and error to same precision to avoid rare issue due to ROOT Double
        integral = round(integral, 15)
        error = round(error, 15)
        try:
            unweighted_events = (integral / error)**2
        except ZeroDivisionError:
            if integral == 0:
                unweighted_events = 0
            else:
                raise RuntimeError("Uncertainty is 0 while integral is nonzero. Check input hist.")
        integral *= hist.lumi_factor
        return (integral, int(round(unweighted_events)))

    def get_yield(self, hist):
        return self.get_yield_and_num_events(hist)[0]

    # get A, B, and C regions used in D=B*C/A; assume self is region D
    def get_control_regions(self, cr_min, cr_max):
        (d0_0_lo, d0_0_hi) = (self.d0_0_lo, self.d0_0_hi)
        (d0_1_lo, d0_1_hi) = (self.d0_1_lo, self.d0_1_hi)
        (pt_lo, pt_hi) = (self.pt_lo, self.pt_hi)
        self.control_regions = {
            # prompt region
            'A' : Region("A", cr_min, cr_max, cr_min, cr_max, pt_lo, pt_hi),
            # displaced-x/prompt-y sideband
            'B' : Region("B", d0_0_lo, d0_0_hi, cr_min, cr_max, pt_lo, pt_hi),
            # prompt-x/displaced-y sideband
            'C' : Region("C", cr_min, cr_max, d0_1_lo, d0_1_hi, pt_lo, pt_hi),
        }

    def get_abcd_estimate(self, hist, correction=1.0):
        a, _ = self.control_regions['A'].get_yield_and_num_events(hist)
        b, _ = self.control_regions['B'].get_yield_and_num_events(hist)
        c, _ = self.control_regions['C'].get_yield_and_num_events(hist)
        try:
            estimate = b*c/a * correction
        except ZeroDivisionError:
            estimate = 0.0
            print "Setting estimate to 0 because prompt region is empty"
            print "Make sure this is the behavior you want"
            print "Region B contain C contain {} and {} events, respectively".format(b, c)
        return estimate


# class to represent signal regions that can be rectangular or L-shaped and will have
# associated A, B, and C control regions
class SignalRegion(Region):
    def __init__(self, d0_min, d0_max, shape, cr_d0_min, cr_d0_max, d0_0_lo, d0_0_hi,
                 d0_1_lo, d0_1_hi, pt_lo, pt_hi):
        super(SignalRegion, self).__init__("SR", d0_0_lo, d0_0_hi, d0_1_lo, d0_1_hi, pt_lo, pt_hi)
        # rename standard regions for brevity and legibility
        for name, nickname, in predefined_sr_names.iteritems():
            self.name = self.name.replace(name, nickname)
        self.d0_min = d0_min
        self.d0_max = d0_max
        self.correction = None
        if shape == 'L':
            self.subregions = self.get_L_subregions()
        elif shape == 'L_inv':
            self.subregions = self.get_invL_subregions()
        elif shape == 'grid':
            self.subregions = self.get_grid_subregions()
        for r in self.subregions:
            r.get_control_regions(cr_d0_min, cr_d0_max)

    def set_abcd_correction(self, correction):
        self.correction = correction

    # get rectangular regions that make up rectangular or L-shaped region
    def get_L_subregions(self):
        (d0_0_lo, d0_0_hi) = (self.d0_0_lo, self.d0_0_hi)
        (d0_1_lo, d0_1_hi) = (self.d0_1_lo, self.d0_1_hi)
        (pt_lo, pt_hi) = (self.pt_lo, self.pt_hi)
        subregions = []
        # most-displaced region is rectangular and composed of only one subregion
        if d0_0_hi == d0_1_hi == d0_max:
            subregions.append(Region("SR", d0_0_lo, d0_0_hi, d0_1_lo, d0_1_hi, pt_lo, pt_hi))
        # all other regions are L-shaped and therefore composed of three rectangular subregions
        else:
            subregions.append(Region("SR", d0_0_lo, d0_0_hi, d0_1_lo, d0_1_hi, pt_lo, pt_hi))
            subregions.append(Region("SR", d0_0_hi, d0_max, d0_1_lo, d0_1_hi, pt_lo, pt_hi))
            subregions.append(Region("SR", d0_0_lo, d0_0_hi, d0_1_hi, d0_max, pt_lo, pt_hi))
        return subregions

    # get rectangular regions that make up rectangular or inverted-L shaped region
    def get_invL_subregions(self):
        (d0_0_lo, d0_0_hi) = (self.d0_0_lo, self.d0_0_hi)
        (d0_1_lo, d0_1_hi) = (self.d0_1_lo, self.d0_1_hi)
        (pt_lo, pt_hi) = (self.pt_lo, self.pt_hi)
        subregions = []
        # most-prompt region is rectangular and composed of only one subregion
        if d0_0_lo == d0_1_lo == d0_min:
            subregions.append(Region("SR", d0_0_lo, d0_0_hi, d0_1_lo, d0_1_hi, pt_lo, pt_hi))
        # more-displaced regions are shaped like an inverted L and composed of three subregions
        else:
            subregions.append(Region("SR", d0_0_lo, d0_0_hi, d0_1_lo, d0_1_hi, pt_lo, pt_hi))
            subregions.append(Region("SR", d0_0_lo, d0_0_hi, d0_min, d0_1_lo, pt_lo, pt_hi))
            subregions.append(Region("SR", d0_min, d0_1_lo, d0_1_lo, d0_1_hi, pt_lo, pt_hi))
        return subregions

    # get single rectangular subregion that makes up rectangular signal region
    def get_grid_subregions(self):
        (d0_0_lo, d0_0_hi) = (self.d0_0_lo, self.d0_0_hi)
        (d0_1_lo, d0_1_hi) = (self.d0_1_lo, self.d0_1_hi)
        (pt_lo, pt_hi) = (self.pt_lo, self.pt_hi)
        subregions = []
        # all regions are rectangular and composed of only one subregion
        subregions.append(Region("SR", d0_0_lo, d0_0_hi, d0_1_lo, d0_1_hi, pt_lo, pt_hi))
        return subregions

    # get integral and number of unweighted events in entire signal region
    def get_yield_and_num_events(self, hist):
        # return abcd estimate instead of integral when blinded
        if hist.blinded:
            abcd_estimate = self.get_abcd_estimate(hist)
            return (abcd_estimate, int(round(abcd_estimate)))

        (integral, unweighted_events) = (0, 0)
        for r in self.subregions:
            (i, e) = r.get_yield_and_num_events(hist)
            integral += i
            unweighted_events += e
        return (integral, unweighted_events)

    # get integral in entire signal region
    def get_yield(self, hist):
        return self.get_yield_and_num_events(hist)[0]

    def get_abcd_estimate(self, hist):
        estimate = 0.0
        for r in self.subregions:
            if self.correction is not None:
                estimate += r.get_abcd_estimate(hist, self.correction[0])
            else:
                estimate += r.get_abcd_estimate(hist)
            print "ABCD estimate in {} is {:.2f}".format(self.name, estimate)
        return estimate


    # specify D=B*C/A relationship using combine rateParameters
    # relationship will be more complex for non-rectangular regions
    def build_rate_param_func(self, unique_regions, pt_binned_crs):

        # add single control region (with possible subregions) to function string and arg list
        def add_cr(region, func, args):
            if region.pt_subregions:
                func += "("
                for r_pt in region.pt_subregions:
                    func += "@{}+".format(len(args))
                    args.append(next(x.param for x in unique_regions if x == r_pt))
                func = func[:-1] + ")"
            else:
                func += "@{}".format(len(args))
                args.append(region.param)
            return func, args

        # begin function string with correction, if applicable
        args = []
        if self.correction is not None:
            # if multiple regions have the same correction, they should refer to a single param
            duplicates = [r for r in unique_regions if not r.cr and r.correction == self.correction]
            if len(duplicates) > 1:
                self.correction_param = self.label + self.param[self.param.index('_'):]
            else:
                self.correction_param = self.param
            self.correction_param += "_correction"
            args.append(self.correction_param)
            func = "(@0*("
        else:
            func = "(("

        # add B and C regions
        # use params from unique regions that are equivalent to currently associated CRs
        all_regions = unique_regions + pt_binned_crs
        for r in self.subregions:
            a = next(cr for cr in all_regions if cr == r.control_regions['A'])
            b = next(cr for cr in all_regions if cr == r.control_regions['B'])
            c = next(cr for cr in all_regions if cr == r.control_regions['C'])
            (func, args) = add_cr(b, func, args)
            func += "*"
            (func, args) = add_cr(c, func, args)
            func += ")+"

        # add A region
        func = func[:-1] + "/"
        (func, args) = add_cr(a, func, args)
        func += ") {}".format(args[0])

        for arg in args[1:]:
            func += ",{}".format(arg)
        self.param_func = func


class Hist(object):
    def __init__(self, sample_info, blinded=True, interpolated=False, swap_axes=False,
                 lumi_factor=1.0):
        file_path = "condor/{}/{}".format(sample_info['dir'], sample_info['file'])
        hist_path = sample_info['hist']
        self.var_bins = sample_info['var_bins']
        self.blinded = sample_info['blinded']
        self.lumi_factor = lumi_factor
        self.hist = self.get_hist(file_path, hist_path, swap_axes)
        if interpolated:
            self.reweight_hist(file_path, hist_path, sample_info['name'])
            self.var_bins = False
        else:
            self.var_bins = sample_info['var_bins']
        self.num_input_evts = self.get_num_input_evts(file_path) if arguments.getEff else None

    def get_hist(self, file_path, hist_path, swap_axes):
        f = TFile(file_path)
        try:
            h = f.Get(hist_path).Clone()
        except ReferenceError:
            raise IOError("Could not load {} from {}".format(hist_path, file_path))
        h.SetDirectory(0)

        # swap x and y axes if necessary
        if swap_axes:
            h_old = h.Clone()
            h.Reset()
            h.GetXaxis().SetTitle(h_old.GetYaxis().GetTitle())
            h.GetYaxis().SetTitle(h_old.GetXaxis().GetTitle())
            # swap bin content to match new axes
            for z in range(1, h_old.GetNbinsZ()+1):
                for y in range(1, h_old.GetNbinsY()+1):
                    for x in range(1, h_old.GetNbinsX()+1):
                        c = h_old.GetBinContent(x, y, z)
                        e = h_old.GetBinError(x, y, z)
                        h.SetBinContent(y, x, z, c)
                        h.SetBinError(y, x, z, e)

        return h

    # update contents of d0-d0-pT hist to include lifetime weights for interpolated points
    def reweight_hist(self, file_path, hist_path, name):
        # access tree
        tree_file_path = file_path.replace("mergeOut", "mergeOutputHadd")
        selection = hist_path.split("Plotter")[0].split('/')[-1]
        tree_path = selection + "TreeMaker/Tree"
        tree_file = TFile(tree_file_path)
        try:
            tree = tree_file.Get(tree_path)
        except ReferenceError:
            raise IOError("Could not load {} from {}".format(tree_path, tree_file_path))

        # get lumi*xs weight
        f = TFile(file_path)
        try:
            h = f.Get(selection+"CutFlowPlotter/eventCounter").Clone()
        except ReferenceError:
            raise IOError("Could not load {} from {}".format(hist_path, file_path))
        lumi_xs_weight = h.Integral() / h.GetEntries()

        # identify proper lifetime weight
        src_ctau = get_ctau(file_path.split('/')[3])
        dst_ctau = get_ctau(name)
        if(stops):
            weight_branch_template = "eventvariable_lifetimeWeight_1000006_{}cmTo{}cm"
        elif(HToSS):
            weight_branch_template = "eventvariable_lifetimeWeight_9000006_{}cmTo{}cm"
        elif(GMSBstaus or GMSB):
            weight_branch_template = "eventvariable_lifetimeWeight_0000010_{}cmTo{}cm"
        weight_branch_name = weight_branch_template.format(mm_to_cm(src_ctau), mm_to_cm(dst_ctau))

        # identify branches that correspond to hist axes
        hist_name = hist_path.split('/')[-1]
        hist_legs = [x.split('_')[0] for x in hist_name.split("_vs_")]
        hist_to_branch_mapping = {
            'electronAbsD0[0]' : 'electron_beamspot_absD0Electron0',
            'electronAbsD0[1]' : 'electron_beamspot_absD0Electron1',
            'electronPt[0]'    : 'electron_ptElectron0',
            'electronPt[1]'    : 'electron_ptElectron1',
            'muonAbsD0[0]'     : 'muon_beamspot_absD0Muon0',
            'muonAbsD0[1]'     : 'muon_beamspot_absD0Muon1',
            'muonPt[0]'        : 'muon_ptMuon0',
            'muonPt[1]'        : 'muon_ptMuon1',
        }
        branches = [hist_to_branch_mapping[l] for l in hist_legs]

        # loop over events
        self.hist.Reset()
        try:
            n_evts = tree.GetEntries()
        except AttributeError:
            print "Unable to read ttree"
            return
        for evt_ix in range(tree.GetEntries()):
            # get total event weight, including lifetime weight
            tree.GetEntry(evt_ix)
            lifetime_weight = getattr(tree, weight_branch_name)
            weight_product = getattr(tree, "weights_weightProduct")
            weight_product *= lumi_xs_weight
            weight_product *= lifetime_weight

            # fill hist at proper d0, d0, pT point using new weight product
            (x, y, z) = tuple(map(lambda a: getattr(tree, a), branches))
            self.hist.Fill(x, y, z, weight_product)

    def get_num_input_evts(self, file_path):
        f = TFile(file_path)
        cutflow_path = "PreselectionCutFlowPlotter/cutFlow"
        try:
            cutflow = f.Get(cutflow_path).Clone()
        except ReferenceError:
            raise IOError("Could not load {} from {}".format(cutflow_path, file_path))
        cutflow.SetDirectory(0)

        return cutflow.GetBinContent(1)



def fancyTable(arrays):
    def areAllEqual(lst):
        return not lst or [lst[0]] * len(lst) == lst

    if not areAllEqual(map(len, arrays)):
        exit('Cannot print a table with unequal array lengths.')

    verticalMaxLengths = [max(value) for value in map(lambda * x:x, *[map(len, a) for a in arrays])]

    spacedLines = []
    for array in arrays:
        spacedLine = ''
        for i, field in enumerate(array):
            diff = verticalMaxLengths[i] - len(field)
            spacedLine += field + ' ' * (diff + 4)
        spacedLines.append(spacedLine)

    return '\n'.join(spacedLines)

def make_bins(bin_edges):
    return zip(bin_edges[:-1], bin_edges[1:])

# get factor to go between unweighted events and yields for rates taken from MC
def get_gamma_sf(y, e):
    try:
        return y/e
    except ZeroDivisionError:
        # the yield is necessarily 0 in this case
        return 0.0

# combine systemtic uncertainties across years, weighting by total yearly yields
def combine_systematics(uncertainties, yields, years):
    # return single year's systematics if only running one year
    if len(years) == 1:
        return uncertainties[years[0]]

    # make list of weights for each year according to yields
    yearly_yields = {}
    total = 0.0
    for year in years:
        yearly_yields[year] = sum((yields[sr][year] for sr in yields))
        total += yearly_yields[year]
    weights = {year : y/total for year, y in yearly_yields.iteritems()}

    # make a list of all relevant systematics and the years in which they are applied
    all_uncertainties = {}
    for year in years:
        for u in uncertainties[year].keys():
            if u in all_uncertainties:
                all_uncertainties[u].append(year)
            else:
                all_uncertainties[u] = [year]

    # weight systematics according to yield in each year
    weighted_systematics = {}
    for name, years_applied in all_uncertainties.iteritems():
        weighted_systematics[name] = {}
        lo_total, hi_total = 0, 0
        for year in years:
            if year in years_applied:
                # handle both symmetric and asymmetric uncertainties
                sys = uncertainties[year][name]['value'].split('/')
                if len(sys) == 1:
                    lo, hi = 2 - float(sys[0]), float(sys[0]) # assume systematic is < 100%
                elif len(sys) == 2:
                    lo, hi = float(sys[0]), float(sys[1])
                else:
                    print "Warning: invalid systematic value"
            else:
                lo, hi = 1, 1
            lo_total += lo*weights[year]
            hi_total += hi*weights[year]

        if round(1 - lo_total, 3) == round(hi_total - 1, 3):
            sys_val = str(round(hi_total, 3))
        else:
            sys_val = "{}/{}".format(round(lo_total, 3), round(hi_total, 3))

        weighted_systematics[name]['value'] = sys_val
        weighted_systematics[name]['applyList'] = uncertainties[years_applied[0]][name]['applyList']
        weighted_systematics[name]['channels'] = uncertainties[years_applied[0]][name]['channels']

    return weighted_systematics

# extract ctau from signal name
# assume signal name includes the ctau preceded by "_" and followed by "mm"
def get_ctau(name):
    if(HToSS):
        ctau = name.split('_')[2].split('mm')[0]
    else:
        ctau = name.split('_')[1].split('mm')[0]
    # check that ctau is just a number
    try:
        float(ctau.replace('p','.'))
    except ValueError:
        raise RuntimeError("Cannot parse {}; getting ctau of {}".format(name, ctau))
    return ctau

# extract mass from signal name
# assume signal name includes the mass as the first number (or third number for higgs)
def get_mass(name):
    ix = 2 if HToSS else 0
    mass = re.findall(r'\d+', name)[ix]
    return mass

def cm_to_mm(name):
    val = float(name.replace('p', '.'))
    val *= 10
    # write as integer if possible
    if int(val) == val:
        val = int(val)
    return str(val).replace('.', 'p')

def mm_to_cm(name):
    val = float(name.replace('p', '.'))
    val *= 0.1
    # write as integer if possible
    if int(val) == val:
        val = int(val)
    return str(val).replace('.', 'p')

# get signal file; handle interpolated points where filename and signal point name don't match
# assume branch definitions in TreeBranchDefinitions.py match current signal files
def find_signal_file(name):
    ctau = get_ctau(name)
    reweighting_pairs_mm = [(cm_to_mm(x), cm_to_mm(y)) for (x, y) in treeDefs.reweighting_pairs]
    try:
        src_ctau = next(x for (x, y) in reweighting_pairs_mm if y == ctau)
    except StopIteration:
        raise RuntimeError("Couldn't find source signal file for signal point " + name)

    return name.replace(ctau+"mm", src_ctau+"mm") + ".root"


####################################################################################################

# put bin edges in more useful form
d0_0_bins = make_bins(d0_0_bin_edges)
d0_1_bins = make_bins(d0_1_bin_edges)
if sr_shapes in ['L', 'L_inv']:
    d0_bins = zip(d0_0_bins, d0_1_bins)
elif sr_shapes == 'grid':
    d0_bins = [(x, y) for x in d0_0_bins for y in d0_1_bins]
else:
    raise RuntimeError("Unrecognized SR shape. Please enter 'L', 'L_inv', or 'grid'")

pt_bin_edges = pt_bin_edges[era]
pt_bins = make_bins(pt_bin_edges)
# assume inclusive signal region is symmetric in d0_0 and d0_1
sr_d0_min = d0_0_bin_edges[0]
sr_d0_max = d0_0_bin_edges[-1]

# define signal regions and associated control regions
signal_regions = []
for d0_0_bin, d0_1_bin in d0_bins:
    # only bin most-prompt region in pT
    if (d0_0_bin, d0_1_bin) == d0_bins[0]:
        for pt_bin in pt_bins:
            print "making signal region:", d0_0_bin, d0_1_bin, pt_bin
            signal_regions.append(SignalRegion(sr_d0_min, sr_d0_max, sr_shapes,
                                               *cr_d0_range + d0_0_bin + d0_1_bin + pt_bin))
    else:
        pt_bin = (pt_bin_edges[0], pt_bin_edges[-1])
        print "making signal region:", d0_0_bin, d0_1_bin, pt_bin
        signal_regions.append(SignalRegion(sr_d0_min, sr_d0_max, sr_shapes,
                                           *cr_d0_range + d0_0_bin + d0_1_bin + pt_bin))

# check that all signal regions have either a systematic uncertainty or correction
abcd_correlation_factors = abcd_correlation_factors[era]
abcd_systematics = abcd_systematics[era]
regions_in_cfg = abcd_correlation_factors.keys() + abcd_systematics.keys()
signal_region_names = [sr.name for sr in signal_regions]
if sorted(signal_region_names) != sorted(regions_in_cfg):
    raise RuntimeError("Signal regions do not match those listed in abcd_correlation_factors and "
                       "abcd_systematics")

# check that all regions with a correction also have an extrapolation systematic
abcd_extrapolation_systematics = abcd_extrapolation_systematics[era]
if abcd_correlation_factors.keys() != abcd_extrapolation_systematics.keys():
    raise RuntimeError("Every SR with a correction must also have an extrapolation systematic")

# get data yields and abcd estimates
# loop through regions in this particular order to build ordered list
years = datacardCombinations[era] if era in datacardCombinations else [era]
data_hists = {}
for year in years:
    data_hists[year] = Hist(data_samples[year], swap_axes=swap_axes)
data_yields = {}
ordered_regions = [sr for sr in signal_regions]
for sr in signal_regions:
    if sr.name in abcd_correlation_factors:
        sr.set_abcd_correction(abcd_correlation_factors[sr.name])

    # get data yields in all signal regions
    data_yields[sr.name] = {}
    for year in years:
        data_yields[sr.name][year] = sr.get_yield(data_hists[year])
    data_yields[sr.name]['total'] = sum(data_yields[sr.name].itervalues())

    # get data yields in all control regions
    for subregion in sr.subregions:
        for _, cr in sorted(subregion.control_regions.iteritems()):
            ordered_regions.append(cr)
            data_yields[cr.name] = {}
            for year in years:
                data_yields[cr.name][year] = cr.get_yield(data_hists[year])
            data_yields[cr.name]['total'] = sum(data_yields[cr.name].itervalues())

# create ordered, duplicate-free list of signal and control regions to use in datacards
unique_regions = list(OrderedDict.fromkeys(ordered_regions))

# account for CRs that can be constructed from combinations of other CRs along the pT axis
(pt_min, pt_max) = (pt_bin_edges[0], pt_bin_edges[-1])
max_pt_range_crs = [r for r in unique_regions if r.cr and r.pt_lo == pt_min and r.pt_hi == pt_max]
pt_binned_crs = []
for cr in max_pt_range_crs:
    cr.find_pt_subregions(unique_regions)
    if cr.pt_subregions:
        pt_binned_crs.append(cr)
        unique_regions.remove(cr)

# associate unique rateParam name to each unique region
region_ixs = {'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0}
for r in unique_regions:
    ix = str(region_ixs[r.label])
    r.set_param("{}{}_{}_{}".format(r.label, ix, era, channel))
    region_ixs[r.label] += 1

# create ABCD and correlation correction associations between params
for sr in signal_regions:
    sr.build_rate_param_func(unique_regions, pt_binned_crs)

# get all the relevant external systematic errors and put them in a dictionary
# match structure of global_systematic_uncertainties
external_systematics = {y : {} for y in years}
base_path = os.environ['CMSSW_BASE'] + "/src/DisplacedSUSY/Configuration/data/systematic_values"
for sys in external_systematic_uncertainties:
    sys_name, sys_channel, sys_year = sys.split('_')
    # skip systematics that don't apply to the current channel or era
    if sys_channel != channel or sys_year not in years:
        continue

    # use systematic value from stand-in year if scaling one year's sample to another's lumi
    standin_year = standin_signal_years[sys_year]
    if sys_year != standin_year:
        found_match = False
        for s in external_systematic_uncertainties:
            s_name, s_channel, s_year = s.split('_')
            # ignore last two characters of names to handle cases like muonPixelHitEff16_emu_2016
            if s_name[:-2] in sys_name[:-2] or s_name[:-2] in sys_name[:-2]:
                if s_channel == sys_channel and s_year == standin_year:
                    sys = s
                    found_match = True
                    break
        if not found_match:
            print "unable to find stand-in systematic for {}; skipping".format(sys)
            continue

    value_dict = {}
    with open("{}__{}.txt".format(base_path, sys)) as sys_file:
        for line in sys_file:
            line = line.rstrip("\n").split()
            dataset = line[0]
            if len(line) is 2:
                value_dict[dataset] = line[1]
            elif len(line) is 3:
                value_dict[dataset]= line[1]+"/"+line[2]
            else:
                raise RuntimeError("Unrecognized external systematic: ", line)
            # turn off systematic when the central yield is zero
            if (value_dict[dataset] == '0' or value_dict[dataset] == '0/0'):
                value_dict[dataset] = '-'
    external_systematics[sys_year][sys_name] = {
        'value' : value_dict,
        'applyList' : mc_normalized_processes,
        'channels' : [sys_channel],
    }

# build datacard elements that don't depend on signal
# build header
header = []
header.append("imax {} number of channels".format(len(unique_regions)))
header.append("jmax 1 number of backgrounds")
header.append("kmax * number of nuisance parameters")
header = "\n".join(header)

# build observed events table
bin_row = ["bin"]
obs_row = ["observation"]
for r in unique_regions:
    bin_row.append(r.name)
    obs_row.append(str(int(round(data_yields[r.name]['total']))))
observed_table = fancyTable([bin_row, obs_row])

# build abcd systematics rows
abcd_systematic_row = ["abcd_method_{}_{}".format(era, channel), "lnN", ""]
abcd_extrapolation_row = ["abcd_extrapolation_point_{}_{}".format(era, channel), "lnN", ""]
for r in unique_regions:
    abcd_systematic_row.append("-")
    abcd_extrapolation_row.append("-")
    if r.name in abcd_systematics:
        uncertainty = str(round(1+abcd_systematics[r.name], 2))
        abcd_systematic_row.append(uncertainty)
    else:
        abcd_systematic_row.append("-")
    if r.name in abcd_extrapolation_systematics:
        uncertainty = str(round(1+abcd_extrapolation_systematics[r.name], 2))
        abcd_extrapolation_row.append(uncertainty)
    else:
        abcd_extrapolation_row.append("-")
abcd_sys_rows = [abcd_systematic_row, abcd_extrapolation_row]

# build abcd table
abcd_rows = []
correlation_correction_rows = []
for r in unique_regions:
    abcd_row = [r.param, "rateParam", r.name, "background"]
    if r.cr:
        cr_yield = int(round(data_yields[r.name]['total']))
        # constrain rateParams to +- ~5 sigma
        err = math.sqrt(cr_yield)
        lo_bound = int(round(max(0, cr_yield - 5*err)))
        hi_bound = int(round(cr_yield + 5*err))
        abcd_row.append("{} [{},{}]".format(cr_yield, lo_bound, hi_bound))
    else:
        abcd_row.append(r.param_func)
    abcd_rows.append(abcd_row)
    if not r.cr and r.correction is not None:
        # constrain params to +- ~5 sigma
        lo_bound = max(0, r.correction[0] - 5*r.correction[1])
        hi_bound = r.correction[0] + 5*r.correction[1]
        correction_string = "{} {} [{lo},{hi}]".format(*r.correction, lo=lo_bound, hi=hi_bound)
        correction_row = [r.correction_param, "param", "", "", correction_string]
        if correction_row not in correlation_correction_rows:
            correlation_correction_rows.append(correction_row)
abcd_table = fancyTable(abcd_rows + correlation_correction_rows)

signal_effs = {}
# write a datacard for each signal point
for signal_name in signal_points:
    # get basic signal info; name and file may differ due to lifetime interpolation
    signal_name = signal_name.replace('.', 'p') # rename sub-mm samples to match sample names
    signal_file = find_signal_file(signal_name)
    interpolated = get_ctau(signal_name) != get_ctau(signal_file)
    signal_hists = {}
    for year in years:
        standin_year = standin_signal_years[year]
        signal_samples[standin_year]['name'] = signal_name
        signal_samples[standin_year]['file'] = signal_file
        lumi_factor = lumi[year]/lumi[standin_year]
        signal_hists[year] = Hist(signal_samples[standin_year], interpolated=interpolated,
                                  swap_axes=swap_axes, lumi_factor=lumi_factor)

    # replace specific gmsb signal names with generic "gmsb" to facilitate channel combination
    datacard_signal_name = signal_name.replace("staus", "gmsb").replace("sleptons", "gmsb")
    # get process type (e.g. stopToLB, sleptons, etc) to differentiate signal stat names
    process_type = signal_name
    for i, c in enumerate(signal_name):
        if c.isdigit() or c == '_':
            process_type = signal_name[:i]
            break

    # get signal yields
    signal_yields = {}
    signal_num_evts = {}
    signal_sf = {}
    signal_exists = False
    #inclusive_sr_num_evts = 0
    inclusive_sr_yield = 0
    for r in unique_regions:
        signal_yields[r.name] = {}
        signal_num_evts[r.name] = {}
        signal_sf[r.name] = {}
        total_yield = 0.0
        total_events = 0.0
        for year in years:
            (y, e) = r.get_yield_and_num_events(signal_hists[year])
            signal_yields[r.name][year] = y
            signal_num_evts[r.name][year] = int(round(e))
            signal_sf[r.name][year] = get_gamma_sf(y, e)
            total_yield += y
            total_events += e
            if y > 0:
                signal_exists = True
        signal_yields[r.name]['total'] = total_yield
        signal_num_evts[r.name]['total'] = int(round(total_events))
        signal_sf[r.name]['total'] = get_gamma_sf(total_yield, total_events)
        if not r.cr:
            #print total_yield
            #inclusive_sr_num_evts += total_events
            inclusive_sr_yield += total_yield
    if not signal_exists:
        print "skipping {} because signal yields are 0".format(signal_name)
        continue

    # get signal efficiency if requested
    if arguments.getEff:
        input_evts = sum((signal_hists[y].num_input_evts for y in years))
        eff = inclusive_sr_yield / input_evts
        # double selectron and smuon efficiencies to match single NLSP assumptions
        if GMSB and not GMSBstaus:
            eff *= 2

        # store in dictionary to later print in summary table
        ctau = get_ctau(signal_name)
        mass = get_mass(signal_name)
        if ctau not in signal_effs:
            signal_effs[ctau] = {}
        signal_effs[ctau][mass] = eff



    # build datacard elements that depend on signal
    # build rate table
    label_row = ["-------------RATES----------------", "", ""] + len(unique_regions)*["", ""]
    empty_row = ["", "", ""] + len(unique_regions)*["", ""]
    bin_row = ["bin", "", ""]
    process_row = ["process", "", ""]
    process_ix_row = ["process", "", ""]
    rate_row = ["rate", "", ""]
    for r in unique_regions:
        # append signal column
        bin_row.append(r.name)
        process_row.append(datacard_signal_name)
        process_ix_row.append("0")
        rate_row.append("{:.3g}".format(signal_yields[r.name]['total']))
        # append background column
        bin_row.append(r.name)
        process_row.append("background")
        process_ix_row.append("1")
        rate_row.append(str(1.0)) # rate is always 1 for background; actual rate set by rateParams
    rate_table = [empty_row, empty_row, label_row, bin_row, process_row, process_ix_row, rate_row]

    # build stat uncertainties table
    label_row = ["----STATISTICAL UNCERTAINTIES-----", "", ""] + len(unique_regions)*["", ""]
    stat_uncertainties_rows = []
    for r in unique_regions:
        # add row for each region
        name = "{}_stat_{}_{}_{}".format(process_type, era, channel, r.name)
        row = [name, 'gmN', str(signal_num_evts[r.name]['total'])]
        # place scale factor in correct column and dashes in all others
        r_ix = unique_regions.index(r)
        dashes_before = 2*r_ix
        dashes_after = 2*(len(unique_regions)-r_ix) - 1
        row.extend(dashes_before*["-"])
        row.append("{:.3g}".format(signal_sf[r.name]['total']))
        row.extend(dashes_after*["-"])
        stat_uncertainties_rows.append(row)
    stat_uncertainties_table = [empty_row, empty_row, label_row] + stat_uncertainties_rows

    # combine global and external systematics
    systematic_uncertainties = copy.deepcopy(global_systematic_uncertainties)
    for year in years:
        # add external systematics with proper value for the current signal point
        for name, sys in external_systematics[year].iteritems():
            systematic_uncertainties[year][name] = {
                'value'     : sys['value'][signal_name],
                'applyList' : sys['applyList'],
                'channels'  : sys['channels'],
            }
    all_systematics = combine_systematics(systematic_uncertainties, signal_yields, years)

    # build systematic uncertainties table
    label_row = ["-----SYSTEMATIC UNCERTAINTIES-----", "", ""] + len(unique_regions)*["", ""]
    systematics_rows = []
    for name, uncertainty in sorted(all_systematics.iteritems()):
        # skip uncertainties that don't apply to the current channel
        if channel not in uncertainty['channels']:
            continue
        row = [name,'lnN','']
        for r in unique_regions:
            if 'signal' in uncertainty['applyList']:
                row.append(uncertainty['value'])
            else:
                row.append('-')
            if "background" in uncertainty['applyList']:
                row.append(uncertainty['value'])
            else:
                row.append('-')
        systematics_rows.append(row)
    sys_uncertainties_table = [empty_row, empty_row, label_row] + abcd_sys_rows + systematics_rows

    # build combined rates and uncertainties table
    main_tables = fancyTable(rate_table + stat_uncertainties_table + sys_uncertainties_table)

    # write datacard
    datacard_name = 'datacard_{}.txt'.format(datacard_signal_name)
    datacard_path = 'limits/{}/{}'.format(arguments.condorDir, datacard_name)
    #print "making", datacard_name
    print "{0: <20} {1}".format(signal_name, inclusive_sr_yield)
    with open(datacard_path, 'w') as datacard:
        datacard.write(header)
        datacard.write("\n\n")
        datacard.write("\n--------OBSERVED EVENTS----------\n")
        datacard.write(observed_table)
        datacard.write("\n")
        datacard.write(main_tables)
        datacard.write("\n\n")
        datacard.write("\n-------ABCD IMPLEMENTATION--------\n")
        datacard.write(abcd_table)

# print signal efficiency table in latex format
if arguments.getEff:
    precision = 5
    ctaus = sorted(signal_effs.keys())
    masses = sorted(signal_effs[ctaus[0]].keys())
    header_template = len(masses)*" & {}\\GeV" + " \\\\"
    print
    print header_template.format(*masses)
    print "\\hline"
    for ctau in ctaus:
        effs = [100*round(signal_effs[ctau].get(mass, 0), precision) for mass in masses]
        line_template = "{}\\cm " + len(masses)*"& {}\\% " + "\\\\"
        print line_template.format(float(ctau)/10, *effs)
    print
