#!/usr/bin/env python

# Given a set of signal region bin edges and data and signal histograms, this script will create
# one datacard for each signal point that contains all signal and control regions along with
# rateParameters that implement the ABCD background estimate in combine.
#
# usage: makeAbcdDatacards.py -l CONFIG -w LIMIT_DIR -E ERA
# sample config: EEChannel/test/abcd_limit_cfg.py

import sys
from collections import OrderedDict
from ROOT import TFile, Double
from DisplacedSUSY.Configuration.limitOptions import *
from DisplacedSUSY.Configuration.systematicsDefinitions import *
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


# class to represent rectangular prisms in d0-d0-pT space
class Region(object):
    def __init__(self, name, d0_0_lo, d0_0_hi, d0_1_lo, d0_1_hi, pt_lo, pt_hi):
        self.name = "{}_{:d}to{:d}um_{:d}to{:d}um_{:d}to{:d}GeV".format(name, d0_0_lo, d0_0_hi,
                                                                        d0_1_lo, d0_1_hi,
                                                                        pt_lo, pt_hi)
        self.name = self.name.replace('-1', 'Inf')
        self.d0_0_lo = d0_0_lo
        self.d0_0_hi = d0_0_hi
        self.d0_1_lo = d0_1_lo
        self.d0_1_hi = d0_1_hi
        self.pt_lo = pt_lo
        self.pt_hi = pt_hi
        self.cr = self.name[:1] in ['A', 'B', 'C']

    # only use name for equality checking because name uniquely defines region in d0-d0-pT space
    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return self.name != other.name

    def __hash__(self):
        return hash(self.name)

    # associate rate parameter name with region
    def set_param(self, rate_param):
        self.param = rate_param

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
        return (integral, int(round(unweighted_events)))

    def get_yield(self, hist):
        return self.get_yield_and_num_events(hist)[0]

    # get A, B, and C regions used in D=B*C/A; assume self is region D
    def get_control_regions(self, cr_min, cr_max):
        self.control_regions = {
            # prompt region
            'A' : Region("A", cr_min, cr_max, cr_min, cr_max, self.pt_lo, self.pt_hi),
            # displaced-x/prompt-y sideband
            'B' : Region("B", self.d0_0_lo, self.d0_0_hi, cr_min, cr_max, self.pt_lo, self.pt_hi),
            # prompt-x/displaced-y sideband
            'C' : Region("C", cr_min, cr_max, self.d0_1_lo, self.d0_1_hi, self.pt_lo, self.pt_hi),
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
        subregions = []
        # most-displaced region is rectangular and composed of only one subregion
        if self.d0_0_hi == self.d0_1_hi == self.d0_max:
            subregions.append(Region("SR", self.d0_0_lo, self.d0_0_hi, self.d0_1_lo, self.d0_1_hi,
                                     self.pt_lo, self.pt_hi))
        # all other regions are L-shaped and therefore composed of three rectangular subregions
        else:
            subregions.append(Region("SR", self.d0_0_lo, self.d0_0_hi, self.d0_1_lo, self.d0_1_hi,
                                     self.pt_lo, self.pt_hi))
            subregions.append(Region("SR", self.d0_0_hi, self.d0_max, self.d0_1_lo, self.d0_1_hi,
                                     self.pt_lo, self.pt_hi))
            subregions.append(Region("SR", self.d0_0_lo, self.d0_0_hi, self.d0_1_hi, self.d0_max,
                                     self.pt_lo, self.pt_hi))
        return subregions

    # get rectangular regions that make up rectangular or inverted-L shaped region
    def get_invL_subregions(self):
        subregions = []
        # most-prompt region is rectangular and composed of only one subregion
        if self.d0_0_lo == self.d0_1_lo == self.d0_min:
            subregions.append(Region("SR", self.d0_0_lo, self.d0_0_hi, self.d0_1_lo, self.d0_1_hi,
                                     self.pt_lo, self.pt_hi))
        # more-displaced regions are shaped like an inverted L and composed of three subregions
        else:
            subregions.append(Region("SR", self.d0_0_lo, self.d0_0_hi, self.d0_1_lo, self.d0_1_hi,
                                     self.pt_lo, self.pt_hi))
            subregions.append(Region("SR", self.d0_0_lo, self.d0_0_hi, self.d0_min, self.d0_1_lo,
                                     self.pt_lo, self.pt_hi))
            subregions.append(Region("SR", self.d0_min, self.d0_1_lo, self.d0_1_lo, self.d0_1_hi,
                                     self.pt_lo, self.pt_hi))
        return subregions

    # get single rectangular subregion that makes up rectangular signal region
    def get_grid_subregions(self):
        subregions = []
        # all regions are rectangular and composed of only one subregion
        subregions.append(Region("SR", self.d0_0_lo, self.d0_0_hi, self.d0_1_lo, self.d0_1_hi,
                                 self.pt_lo, self.pt_hi))
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
                estimate += r.get_abcd_estimate(hist, self.correction)
            else:
                estimate += r.get_abcd_estimate(hist)
        return estimate

    # specify D=B*C/A relationship using combine rateParameters
    # relationship will be more complex for non-rectangular regions
    def build_rate_param_func(self, unique_regions):
        if self.correction is not None:
            func = "(@0*(@1*@2"
            ix = 3
        else:
            func = "((@0*@1"
            ix = 2
        for r in self.subregions[1:]:
            func += "+@{}*@{}".format(ix, ix+1)
            ix +=2
        func += ")/@{}) ".format(ix)

        if self.correction is not None:
            self.correction_param = self.param+"_correction"
            func += "{},".format(self.correction_param)

        # find unique regions that are equivalent to currently associated control regions
        for r in self.subregions:
            a = next(cr.param for cr in unique_regions if cr.name == r.control_regions['A'].name)
            b = next(cr.param for cr in unique_regions if cr.name == r.control_regions['B'].name)
            c = next(cr.param for cr in unique_regions if cr.name == r.control_regions['C'].name)
            func += "{},{},".format(b, c)
        func += a

        self.param_func = func


class Hist(object):
    def __init__(self, sample_info, blinded=True):
        file_path = "condor/{}/{}".format(sample_info['dir'], sample_info['file'])
        self.hist = self.get_hist(file_path, sample_info['hist'])
        self.var_bins = sample_info['var_bins']
        self.blinded = sample_info['blinded']

    def get_hist(self, file_path, hist_path):
        f = TFile(file_path)
        try:
            h = f.Get(hist_path).Clone()
        except ReferenceError:
            raise IOError("Could not load {} from {}".format(hist_path, file_path))
        h.SetDirectory(0)
        return h

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
        return round(y/e, 7)
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
        val = 0
        for year in years:
            if year in years_applied:
                val += float(uncertainties[year][name]['value']) * weights[year]
            else:
                val += weights[year]
        weighted_systematics[name]['value'] = str(round(val, 3))
        weighted_systematics[name]['applyList'] = uncertainties[years_applied[0]][name]['applyList']

    return weighted_systematics

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

pt_bins = make_bins(pt_bin_edges)
# assume inclusive signal region is symmetric in d0_0 and d0_1
sr_d0_min = d0_0_bin_edges[0]
sr_d0_max = d0_0_bin_edges[-1]

# define signal regions and associated control regions
signal_regions = []
for pt_bin in pt_bins:
    for d0_0_bin, d0_1_bin in d0_bins:
        signal_regions.append(SignalRegion(sr_d0_min, sr_d0_max, sr_shapes,
                                           *cr_d0_range + d0_0_bin + d0_1_bin + pt_bin))

# check that all signal regions have either a systematic uncertainty or correction
regions_in_cfg = abcd_correlation_factors.keys() + abcd_systematics.keys()
signal_region_names = [sr.name for sr in signal_regions]
if sorted(signal_region_names) != sorted(regions_in_cfg):
    raise RuntimeError("Signal regions do not match those listed in abcd_correlation_factors and "
                       "abcd_systematics")

# get data yields and abcd estimates in all signal regions
data_yields = {}
data_hist = Hist(data)
ordered_regions = [sr for sr in signal_regions]
for sr in signal_regions:
    if sr.name in abcd_correlation_factors:
        sr.set_abcd_correction(abcd_correlation_factors[sr.name][0])
    data_yields[sr.name] = sr.get_yield(data_hist)
    # get data yields in all control regions
    for subregion in sr.subregions:
        for _, cr in sorted(subregion.control_regions.iteritems()):
            ordered_regions.append(cr)
            data_yields[cr.name] = cr.get_yield(data_hist) if arguments.era == "run2" else 0.0

# create duplicate-free list of signal and control regions to use in datacards
unique_regions = list(OrderedDict.fromkeys(ordered_regions))

# associate unique rateParam name to each unique region
region_ixs = {'a':0, 'b' : 0, 'c' : 0, 'd' : 0}
for r in unique_regions:
    region_type = r.name[0].lower() if r.cr else 'd'
    r.set_param(region_type + str(region_ixs[region_type]))
    region_ixs[region_type] += 1

# create ABCD and correlation correction associations between params
for sr in signal_regions:
    sr.build_rate_param_func(unique_regions)

# get all the external systematic errors and put them in a dictionary
# fixme: this needs to be tested after external systematics files are updated
systematics_dictionary = {}
for sys_name in external_systematic_uncertainties:
    systematics_dictionary[sys_name] = {}
    base_path = os.environ['CMSSW_BASE'] + "/src/DisplacedSUSY/Configuration/data/systematic_values"
    with open("{}__{}_{}.txt".format(base_path, sys_name, arguments.era)) as sys_file:
        for r in unique_regions:
            systematic[r.name] = {}
            for line in sys_file:
                line = line.rstrip("\n").split(" ")
                dataset = line[0]
                if len(line) is 2:
                    systematic[r.name][dataset] = line[1]
                elif len(line) is 3:
                    systematic[r.name][dataset]= line[1]+"/"+line[2]

                # turn off systematic when the central yield is zero
                if (systematic[r.name][dataset] == '0' or systematic[r.name][dataset] == '0/0'):
                    systematic[r.name][dataset] = '-'

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
    obs_row.append(str(int(round(data_yields[r.name]))))
observed_table = fancyTable([bin_row, obs_row])

# build abcd systematics row
# fixme: these values will probably be moved to systematicsDefinitions or an external file
abcd_systematic_row = ["abcd_method", "lnN", ""]
for r in unique_regions:
    abcd_systematic_row.append("-")
    if r.name in abcd_systematics:
        uncertainty = str(round(1+abcd_systematics[r.name], 2))
        abcd_systematic_row.append(uncertainty)
    else:
        abcd_systematic_row.append("-")

# build abcd table
abcd_rows = []
correlation_correction_rows = []
for r in unique_regions:
    abcd_row = [r.param, "rateParam", r.name, "background"]
    if r.cr:
        abcd_row.append(str(int(round(data_yields[r.name]))))
    else:
        abcd_row.append(r.param_func)
    abcd_rows.append(abcd_row)
    if not r.cr and r.correction is not None:
        correction_string = "{} {}".format(*abcd_correlation_factors[r.name])
        correction_row = [r.correction_param, "param", "", "", correction_string]
        correlation_correction_rows.append(correction_row)
abcd_table = fancyTable(abcd_rows + correlation_correction_rows)

# write a datacard for each signal point
years = ['2016', '2017', '2018'] if arguments.era == 'run2' else [arguments.era]
for signal_name in signal_points:
    # get basic signal info
    signal_name = signal_name.replace('.', 'p') # rename sub-mm samples to match sample names
    signal_file = signal_name + ".root"
    signal_hists = {}
    for year in years:
        signal_samples[year]['name'] = signal_name
        signal_samples[year]['file'] = signal_file
        signal_hists[year] = Hist(signal_samples[year])

    # get signal yields
    signal_yields = {}
    signal_num_evts = {}
    signal_sf = {}
    for r in unique_regions:
        signal_yields[r.name] = {}
        signal_num_evts[r.name] = {}
        signal_sf[r.name] = {}
        total_yield = 0.0
        total_events = 0.0
        for year in years:
            (y, e) = r.get_yield_and_num_events(signal_hists[year])
            signal_yields[r.name][year] = round(y, 7)
            signal_num_evts[r.name][year] = int(round(e))
            signal_sf[r.name][year] = get_gamma_sf(y, e)
            total_yield += y
            total_events += e
        signal_yields[r.name]['total'] = total_yield
        signal_num_evts[r.name]['total'] = int(round(total_events))
        signal_sf[r.name]['total'] = get_gamma_sf(total_yield, total_events)

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
        process_row.append(signal_name)
        process_ix_row.append("0")
        rate_row.append(str(signal_yields[r.name]['total']))
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
        name = 'signal_stat_' + r.name
        row = [name, 'gmN', str(signal_num_evts[r.name]['total'])]
        # place scale factor in correct column and dashes in all others
        r_ix = unique_regions.index(r)
        dashes_before = 2*r_ix
        dashes_after = 2*(len(unique_regions)-r_ix) - 1
        row.extend(dashes_before*["-"])
        row.append(str(signal_sf[r.name]['total']))
        row.extend(dashes_after*["-"])
        stat_uncertainties_rows.append(row)
    stat_uncertainties_table = [empty_row, empty_row, label_row] + stat_uncertainties_rows

    # build global systematics rows
    global_systematics = combine_systematics(global_systematic_uncertainties, signal_yields, years)
    global_systematics_rows = []
    for name, uncertainty in sorted(global_systematics.iteritems()):
        row = [name,'lnN','']
        for r in unique_regions:
            if 'signal' in uncertainty['applyList']:
                row.append(uncertainty['value'])
            else:
                row.append('-')
            if (arguments.era == "run2" and "background" in uncertainty['applyList']):
                row.append(uncertainty['value'])
            else:
                row.append('-')
        global_systematics_rows.append(row)

    # build systematic uncertainties table
    label_row = ["-----SYSTEMATIC UNCERTAINTIES-----", "", ""] + len(unique_regions)*["", ""]
    external_systematics_rows = []
    for name, uncertainty in systematics_dictionary.iteritems():
        row = [name,"lnN",""]
        for r in unique_regions:
            # append signal column
            if signal_name in uncertainty[r.name]:
                row.append(uncertainty[r.name][signal_name])
            else:
                row.append('-')
            # append background column
            if (arguments.era == "run2" and "background" in uncertainty[r.name]):
                row.append(uncertainty[r.name]["background"])
            else:
                row.append('-')
        external_systematics_rows.append(row)
    sys_uncertainties_table = [empty_row, empty_row, label_row, abcd_systematic_row]
    sys_uncertainties_table += global_systematics_rows + external_systematics_rows

    # build combined rates and uncertainties table
    main_tables = fancyTable(rate_table + stat_uncertainties_table + sys_uncertainties_table)

    # write datacard
    datacard_name = 'datacard_{}.txt'.format(signal_name)
    datacard_path = 'limits/{}/{}'.format(arguments.condorDir, datacard_name)
    print "making", datacard_name
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
