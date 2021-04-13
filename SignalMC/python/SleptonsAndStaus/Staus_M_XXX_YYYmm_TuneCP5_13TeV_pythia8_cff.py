FLAVOR = 'stau'
COM_ENERGY = 13000. # GeV
MASS_POINT = XXX   # GeV
CROSS_SECTION = ZZZ # pb
CTAU_POINT = YYY # mm
PROCESS_FILE = 'SimG4Core/CustomPhysics/data/RhadronProcessList.txt'
PARTICLE_FILE = 'DisplacedSUSY/SignalMC/data/geant4_staus_%s_%smm.txt'  % (MASS_POINT, CTAU_POINT)
USE_REGGE = False
GRIDPACK = '/eos/uscms/store/user/lpclonglived/DisplacedLeptons/GMSBgridpacks/staus_%s_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz' % (MASS_POINT)
SLHA_TABLE="""
##******************************************************************
##                      MadGraph/MadEvent                          *
##******************************************************************
## Les Houches friendly file for the (MS)SM parameters of MadGraph *
##      SM parameter set and decay widths produced by MSSMCalc     *
##******************************************************************
##*Please note the following IMPORTANT issues:                     *
##                                                                 *
##0. REFRAIN from editing this file by hand! Some of the parame-   *
##   ters are not independent. Always use a calculator.            *
##                                                                 *
##1. alpha_S(MZ) has been used in the calculation of the parameters*
##   This value is KEPT by madgraph when no pdf are used lpp(i)=0, *
##   but, for consistency, it will be reset by madgraph to the     *
##   value expected IF the pdfs for collisions with hadrons are    *
##   used.                                                         *
##                                                                 *
##2. Values of the charm and bottom kinematic (pole) masses are    *
##   those used in the matrix elements and phase space UNLESS they *
##   are set to ZERO from the start in the model (particles.dat)   *
##   This happens, for example,  when using 5-flavor QCD where     *
##   charm and bottom are treated as partons in the initial state  *
##   and a zero mass might be hardwired in the model definition.   *
##                                                                 *
##       The SUSY decays have calculated using SDECAY 1.1a         *
##                                                                 *
##******************************************************************
#
BLOCK DCINFO  # Decay Program information
     1   SDECAY      # decay calculator
     2   1.1a        # version number
#
BLOCK SPINFO  # Spectrum calculator information
     1   ISASUGRA
     2   7.81
#
BLOCK MODSEL  # Model selection
     1     1   #
#
BLOCK SMINPUTS  # Standard Model inputs
     1     1.25778332E+02   # alpha_em^-1(M_Z)^MSbar
     2     1.16570000E-05   # G_F [GeV^-2]
     3     1.17200002E-01   # alpha_S(M_Z)^MSbar
     4     9.11876000E+01   # M_Z pole mass
     5     4.25000000E+00   # mb(mb)^MSbar
     6     1.72500000E+02   # mt pole mass (extracted)
     7     1.77682000E+00   # mtau pole mass (extracted)
#
BLOCK MINPAR  # Input parameters - minimal models
     1     6.00000000E+02   #  m_0
     2     3.00000000E+02   #  m_{1/2}
     3     1.00000000E+01   #  tan(beta)
     4     1.00000000E+00   #  sign(mu)
#
BLOCK EXTPAR  # Input parameters - non-minimal models
     0     2.21278347E+16   #  Input scale
#
BLOCK MASS  # Mass Spectrum
# PDG code           mass       particle
         5     4.80000000E+00   # b-quark pole mass (extracted)
         6     1.72500000E+02   # t-quark pole mass (not read by ME)
        15     1.77682000E+00   # tau pole mass (not read by ME)
        23     9.11876000E+01   # Z pole mass (not read by ME)
        24     8.03990000E+01   # W+
        25     1.25000000E+02   # h
        35     7.49062561E+05   # H
        36     7.43967712E+05   # A
        37     7.53755432E+05   # H+
   1000001    4.50000000E+05  #
   2000001    4.50000000E+05  #
   1000002    4.50000000E+05  #
   2000002    4.50000000E+05  #
   1000003    4.50000000E+05  #
   2000003    4.50000000E+05  #
   1000004    4.50000000E+05  #
   2000004    4.50000000E+05  #
   1000005    4.50000000E+05  #
   2000005    4.50000000E+05  #
   1000006    4.50000000E+05  #
   2000006    4.50000000E+05  #
   1000011    MSTAU  #
   2000011    MSTAU  #
   1000012    4.50000000E+05  #
   1000013    MSTAU  #
   2000013    MSTAU  #
   1000014    4.50000000E+05  #
   1000015    MSTAU  #
   2000015    MSTAU  #
   1000016    4.50000000E+05  #
   1000021    4.50000000E+05  #
   1000022    4.50000000E+05  #
   1000023    4.50000000E+05  #
   1000025    4.50000000E+05  #
   1000035    4.50000000E+05  #
   1000024    4.50000000E+05  #
   1000037    4.50000000E+05  #
   1000039    1.00000000E-07  # Gravitino
#
BLOCK NMIX  # Neutralino Mixing Matrix
  1  1     1.00000000E+00   # N_11
  1  2     0.00000000E+00   # N_12
  1  3     0.00000000E+00   # N_13
  1  4     0.00000000E+00   # N_14
  2  1     0.00000000E+00   # N_21
  2  2     1.00000000E+00   # N_22
  2  3     0.00000000E+00   # N_23
  2  4     0.00000000E+00   # N_24
  3  1     0.00000000E+00   # N_31
  3  2     0.00000000E+00   # N_32
  3  3     1.00000000E+00   # N_33
  3  4     0.00000000E+00   # N_34
  4  1     0.00000000E+00   # N_41
  4  2     0.00000000E+00   # N_42
  4  3     0.00000000E+00   # N_43
  4  4     1.00000000E+00   # N_44
#
BLOCK UMIX  # Chargino Mixing Matrix U
  1  1     1.00000000E+00   # U_11
  1  2     0.00000000E+00   # U_12
  2  1     0.00000000E+00   # U_21
  2  2     1.00000000E+00   # U_22
#
BLOCK VMIX  # Chargino Mixing Matrix V
  1  1     1.00000000E+00   # V_11
  1  2     0.00000000E+00   # V_12
  2  1     0.00000000E+00   # V_21
  2  2     1.00000000E+00   # V_22
#
BLOCK STOPMIX  # Stop Mixing Matrix
  1  1     1.00000000E+00   # O_{11}
  1  2     0.00000000E+00   # O_{12}
  2  1     0.00000000E+00   # O_{21}
  2  2     1.00000000E+00   # O_{22}
#
BLOCK SBOTMIX  # Sbottom Mixing Matrix
  1  1     1.00000000E+00   # O_{11}
  1  2     0.00000000E+00   # O_{12}
  2  1     0.00000000E+00   # O_{21}
  2  2     1.00000000E+00   # O_{22}
#
Block SELMIX
    1   1 1.000000e+00 # RRl11
    2   2 1.000000e+00 # RRl22
    3   3 2.8248721e-01 # RRl33
    3   6 9.5927111e-01 # RRl36
    4   4 1.000000e+00 # RRl44
    5   5 1.000000e+00 # RRl55
    6   3 9.592711e-01 # RRl63
    6   6 -2.824872e-01 # RRl66
#
BLOCK ALPHA  # Higgs mixing
          -1.02914833E-01   # Mixing angle in the neutral Higgs boson sector
#
BLOCK HMIX Q=  6.61219971E+02  # DRbar Higgs Parameters
     1     4.12454407E+02   #  mu(Q)
     2     9.36003455E+00   # tanb (extracted)
     3     2.50607727E+02   #  Higgs vev at Q
     4     5.53487938E+05   #  m_A^2(Q)
#
BLOCK GAUGE Q=  6.61219971E+02  # The gauge couplings
     3     1.07381373E+00   # g3(Q) MSbar
#
BLOCK AU Q=  6.61219971E+02  # The trilinear couplings
  3  3    -5.32061523E+02   # A_t(Q) DRbar
  1  1     0.000000e+00 # dummy
  2  2     0.000000e+00 # dummy
#
BLOCK AD Q=  6.61219971E+02  # The trilinear couplings
  3  3    -8.07902039E+02   # A_b(Q) DRbar
  1  1     0.000000e+00 # dummy
  2  2     0.000000e+00 # dummy
#
BLOCK AE Q=  6.61219971E+02  # The trilinear couplings
  3  3    -1.81115051E+02   # A_tau(Q) DRbar
  1  1     0.000000e+00 # dummy
  2  2     0.000000e+00 # dummy
#
BLOCK YU Q=  6.61219971E+02  # The Yukawa couplings
  3  3     8.85841429E-01   # y_t(Q) (extracted)
  1  1     0.000000e+00 # dummy
  2  2     0.000000e+00 # dummy
#
BLOCK YD Q=  6.61219971E+02  # The Yukawa couplings
  3  3     1.36232540E-01   # y_b(Q) (extracted)
  1  1     0.000000e+00 # dummy
  2  2     0.000000e+00 # dummy
#
BLOCK YE Q=  6.61219971E+02  # The Yukawa couplings
  3  3     1.01981103E-01   # y_tau(Q) (extracted)
  1  1     0.000000e+00 # dummy
  2  2     0.000000e+00 # dummy
#
BLOCK MSOFT Q=  6.61219971E+02  # The soft SUSY breaking masses at the scale Q
     1     1.24019547E+02   #  M_1(Q)
     2     2.32185043E+02   #  M_2(Q)
     3     6.86750671E+02   #  M_3(Q)
    21     3.23374943E+04   # mH1^2(Q)
    22    -1.28800134E+05   # mH2^2(Q)
    31     6.29402649E+02   #  MeL(Q)
    32     6.29402649E+02   #  MmuL(Q)
    33     6.26662476E+02   #  MtauL(Q)
    34     6.08800842E+02   #  MeR(Q)
    35     6.08800842E+02   #  MmuR(Q)
    36     6.03154236E+02   #  MtauR(Q)
    41     8.48326294E+02   #  MqL1(Q)
    42     8.48326294E+02   #  MqL2(Q)
    43     7.40788147E+02   #  MqL3(Q)
    44     8.34092896E+02   #  MuR(Q)
    45     8.34092896E+02   #  McR(Q)
    46     5.90198242E+02   #  MtR(Q)
    47     8.32408752E+02   #  MdR(Q)
    48     8.32408752E+02   #  MsR(Q)
    49     8.31454102E+02   #  MbR(Q)
#
#
#
#                             =================
#                             |The decay table|
#                             =================
#
# - The multi-body decays for the inos, stops and sbottoms are included.
#
# - The SUSY decays of the top quark are included.
#
#
#         PDG            Width
DECAY        23     2.49520000E+00   # Z width (SM calculation)
DECAY        24     2.08500000E+00   # W width (SM calculation)
#
#         PDG            Width
DECAY         6     1.02218095E+00   # top decays
#          BR         NDA      ID1       ID2
     1.00000000E+00    2           5        24   # BR(t ->  b    W+)
     0.00000000E+00    2           5        37   # BR(t ->  b    H+)
     0.00000000E+00    2     1000006   1000022   # BR(t -> ~t_1 ~chi_10)
     0.00000000E+00    2     1000006   1000023   # BR(t -> ~t_1 ~chi_20)
     0.00000000E+00    2     1000006   1000025   # BR(t -> ~t_1 ~chi_30)
     0.00000000E+00    2     1000006   1000035   # BR(t -> ~t_1 ~chi_40)
     0.00000000E+00    2     2000006   1000022   # BR(t -> ~t_2 ~chi_10)
     0.00000000E+00    2     2000006   1000023   # BR(t -> ~t_2 ~chi_20)
     0.00000000E+00    2     2000006   1000025   # BR(t -> ~t_2 ~chi_30)
     0.00000000E+00    2     2000006   1000035   # BR(t -> ~t_2 ~chi_40)
#
#         PDG            Width
DECAY        25     1.65461618E-03   # h decays
#          BR         NDA      ID1       ID2
     1.47339152E-01    2          15       -15   # BR(H1 -> tau- tau+)
     7.81441418E-01    2           5        -5   # BR(H1 -> b bb)
     6.76395564E-02    2          24       -24   # BR(H1 -> W+ W-)
     3.57987415E-03    2          23        23   # BR(H1 -> Z Z)
#
#         PDG            Width
DECAY        35     1.26118245E+00   # H decays
#          BR         NDA      ID1       ID2
     1.21586159E-01    2          15       -15   # BR(H -> tau- tau+)
     2.21890882E-01    2           6        -6   # BR(H -> t tb)
     6.50784860E-01    2           5        -5   # BR(H -> b bb)
     1.26971777E-03    2          24       -24   # BR(H -> W+ W-)
     6.21230085E-04    2          23        23   # BR(H -> Z Z)
     0.00000000E+00    2          24       -37   # BR(H -> W+ H-)
     0.00000000E+00    2         -24        37   # BR(H -> W- H+)
     0.00000000E+00    2          37       -37   # BR(H -> H+ H-)
     3.84715147E-03    2          25        25   # BR(H -> h h)
     0.00000000E+00    2          36        36   # BR(H -> A A)
#
#         PDG            Width
DECAY        36     1.32606570E+00   # A decays
#          BR         NDA      ID1       ID2
     1.14768736E-01    2          15       -15   # BR(A -> tau- tau+)
     2.69728288E-01    2           6        -6   # BR(A -> t tb)
     6.14379413E-01    2           5        -5   # BR(A -> b bb)
     1.12356280E-03    2          23        25   # BR(A -> Z h)
     0.00000000E+00    2          23        35   # BR(A -> Z H)
     0.00000000E+00    2          24       -37   # BR(A -> W+ H-)
     0.00000000E+00    2         -24        37   # BR(A -> W- H+)
#
#         PDG            Width
DECAY        37     1.27808456E+00   # H+ decays
#          BR         NDA      ID1       ID2
     1.20644761E-01    2         -15        16   # BR(H+ -> tau+ nu_tau)
     8.78124903E-01    2           6        -5   # BR(H+ -> t bb)
     1.23033590E-03    2          24        25   # BR(H+ -> W+ h)
     0.00000000E+00    2          24        35   # BR(H+ -> W+ H)
     0.00000000E+00    2          24        36   # BR(H+ -> W+ A)
#
#         PDG            Width
DECAY   1000021     7.40992706E-02   # gluino decays
#           BR         NDA      ID1       ID2       ID3
     2.50000000E-01    3     1000022         1        -1   # BR(~g -> ~chi_10 d  db)
     2.50000000E-01    3     1000022         2        -2   # BR(~g -> ~chi_10 u  ub)
     2.50000000E-01    3     1000022         3        -3   # BR(~g -> ~chi_10 s  sb)
     2.50000000E-01    3     1000022         4        -4   # BR(~g -> ~chi_10 c  cb)
#
#         PDG            Width
DECAY   1000006     5.69449678E+00   # stop1 decays
#          BR         NDA      ID1       ID2
     1.88206930E-01    2     1000022         6   # BR(~t_1 -> ~chi_10 t )
     9.44603249E-02    2     1000023         6   # BR(~t_1 -> ~chi_20 t )
     1.70455913E-01    2     1000025         6   # BR(~t_1 -> ~chi_30 t )
     2.29109632E-02    2     1000035         6   # BR(~t_1 -> ~chi_40 t )
     2.42095992E-01    2     1000024         5   # BR(~t_1 -> ~chi_1+ b )
     2.81869877E-01    2     1000037         5   # BR(~t_1 -> ~chi_2+ b )
     0.00000000E+00    2     1000021         6   # BR(~t_1 -> ~g      t )
     0.00000000E+00    2     1000005        37   # BR(~t_1 -> ~b_1    H+)
     0.00000000E+00    2     2000005        37   # BR(~t_1 -> ~b_2    H+)
     0.00000000E+00    2     1000005        24   # BR(~t_1 -> ~b_1    W+)
     0.00000000E+00    2     2000005        24   # BR(~t_1 -> ~b_2    W+)
#
#         PDG            Width
DECAY   2000006     1.47683155E+01   # stop2 decays
#          BR         NDA      ID1       ID2
     1.04775334E-02    2     1000022         6   # BR(~t_2 -> ~chi_10 t )
     1.13972560E-01    2     1000023         6   # BR(~t_2 -> ~chi_20 t )
     1.57562942E-01    2     1000025         6   # BR(~t_2 -> ~chi_30 t )
     2.57314086E-01    2     1000035         6   # BR(~t_2 -> ~chi_40 t )
     2.40022120E-01    2     1000024         5   # BR(~t_2 -> ~chi_1+ b )
     1.04238005E-01    2     1000037         5   # BR(~t_2 -> ~chi_2+ b )
     0.00000000E+00    2     1000021         6   # BR(~t_2 -> ~g      t )
     4.81590640E-02    2     1000006        25   # BR(~t_2 -> ~t_1    h )
     0.00000000E+00    2     1000006        35   # BR(~t_2 -> ~t_1    H )
     0.00000000E+00    2     1000006        36   # BR(~t_2 -> ~t_1    A )
     0.00000000E+00    2     1000005        37   # BR(~t_2 -> ~b_1    H+)
     0.00000000E+00    2     2000005        37   # BR(~t_2 -> ~b_2    H+)
     6.82536895E-02    2     1000006        23   # BR(~t_2 -> ~t_1    Z )
     0.00000000E+00    2     1000005        24   # BR(~t_2 -> ~b_1    W+)
     0.00000000E+00    2     2000005        24   # BR(~t_2 -> ~b_2    W+)
#
#         PDG            Width
DECAY   1000005     1.37684102E+01   # sbottom1 decays
#          BR         NDA      ID1       ID2
     1.24979039E-02    2     1000022         5   # BR(~b_1 -> ~chi_10 b )
     1.62963740E-01    2     1000023         5   # BR(~b_1 -> ~chi_20 b )
     5.39620118E-03    2     1000025         5   # BR(~b_1 -> ~chi_30 b )
     1.32454160E-02    2     1000035         5   # BR(~b_1 -> ~chi_40 b )
     2.97894492E-01    2    -1000024         6   # BR(~b_1 -> ~chi_1- t )
     3.94674666E-01    2    -1000037         6   # BR(~b_1 -> ~chi_2- t )
     1.30886580E-02    2     1000021         5   # BR(~b_1 -> ~g      b )
     0.00000000E+00    2     1000006       -37   # BR(~b_1 -> ~t_1    H-)
     0.00000000E+00    2     2000006       -37   # BR(~b_1 -> ~t_2    H-)
     1.00238923E-01    2     1000006       -24   # BR(~b_1 -> ~t_1    W-)
     0.00000000E+00    2     2000006       -24   # BR(~b_1 -> ~t_2    W-)
#
#         PDG            Width
DECAY   2000005     4.02050211E+00   # sbottom2 decays
#          BR         NDA      ID1       ID2
     1.16939193E-01    2     1000022         5   # BR(~b_2 -> ~chi_10 b )
     9.67521720E-04    2     1000023         5   # BR(~b_2 -> ~chi_20 b )
     2.44620085E-02    2     1000025         5   # BR(~b_2 -> ~chi_30 b )
     2.54122057E-02    2     1000035         5   # BR(~b_2 -> ~chi_40 b )
     9.99862983E-04    2    -1000024         6   # BR(~b_2 -> ~chi_1- t )
     6.61498667E-02    2    -1000037         6   # BR(~b_2 -> ~chi_2- t )
     7.55931029E-01    2     1000021         5   # BR(~b_2 -> ~g      b )
     0.00000000E+00    2     1000005        25   # BR(~b_2 -> ~b_1    h )
     0.00000000E+00    2     1000005        35   # BR(~b_2 -> ~b_1    H )
     0.00000000E+00    2     1000005        36   # BR(~b_2 -> ~b_1    A )
     0.00000000E+00    2     1000006       -37   # BR(~b_2 -> ~t_1    H-)
     0.00000000E+00    2     2000006       -37   # BR(~b_2 -> ~t_2    H-)
     0.00000000E+00    2     1000005        23   # BR(~b_2 -> ~b_1    Z )
     9.13831226E-03    2     1000006       -24   # BR(~b_2 -> ~t_1    W-)
     0.00000000E+00    2     2000006       -24   # BR(~b_2 -> ~t_2    W-)
#
#         PDG            Width
DECAY   1000002     1.31301150E+01   # sup_L decays
#          BR         NDA      ID1       ID2
     5.97240819E-03    2     1000022         2   # BR(~u_L -> ~chi_10 u)
     2.13814900E-01    2     1000023         2   # BR(~u_L -> ~chi_20 u)
     6.54997799E-04    2     1000025         2   # BR(~u_L -> ~chi_30 u)
     1.15708854E-02    2     1000035         2   # BR(~u_L -> ~chi_40 u)
     4.34593064E-01    2     1000024         1   # BR(~u_L -> ~chi_1+ d)
     1.55107464E-02    2     1000037         1   # BR(~u_L -> ~chi_2+ d)
     3.17882998E-01    2     1000021         2   # BR(~u_L -> ~g      u)
#
#         PDG            Width
DECAY   2000002     5.45626401E+00   # sup_R decays
#          BR         NDA      ID1       ID2
     3.56050387E-01    2     1000022         2   # BR(~u_R -> ~chi_10 u)
     1.95018645E-03    2     1000023         2   # BR(~u_R -> ~chi_20 u)
     5.79103054E-04    2     1000025         2   # BR(~u_R -> ~chi_30 u)
     2.22793094E-03    2     1000035         2   # BR(~u_R -> ~chi_40 u)
     0.00000000E+00    2     1000024         1   # BR(~u_R -> ~chi_1+ d)
     0.00000000E+00    2     1000037         1   # BR(~u_R -> ~chi_2+ d)
     6.39192393E-01    2     1000021         2   # BR(~u_R -> ~g      u)
#
#         PDG            Width
DECAY   1000001     1.31836627E+01   # sdown_L decays
#          BR         NDA      ID1       ID2
     1.36015082E-02    2     1000022         1   # BR(~d_L -> ~chi_10 d)
     2.00968062E-01    2     1000023         1   # BR(~d_L -> ~chi_20 d)
     1.12614606E-03    2     1000025         1   # BR(~d_L -> ~chi_30 d)
     1.52229825E-02    2     1000035         1   # BR(~d_L -> ~chi_40 d)
     3.97020140E-01    2    -1000024         2   # BR(~d_L -> ~chi_1- u)
     4.05217275E-02    2    -1000037         2   # BR(~d_L -> ~chi_2- u)
     3.31539434E-01    2     1000021         1   # BR(~d_L -> ~g      d)
#
#         PDG            Width
DECAY   2000001     3.95203891E+00   # sdown_R decays
#          BR         NDA      ID1       ID2
     1.22809923E-01    2     1000022         1   # BR(~d_R -> ~chi_10 d)
     6.72575606E-04    2     1000023         1   # BR(~d_R -> ~chi_20 d)
     1.99604669E-04    2     1000025         1   # BR(~d_R -> ~chi_30 d)
     7.67849884E-04    2     1000035         1   # BR(~d_R -> ~chi_40 d)
     0.00000000E+00    2    -1000024         2   # BR(~d_R -> ~chi_1- u)
     0.00000000E+00    2    -1000037         2   # BR(~d_R -> ~chi_2- u)
     8.75550047E-01    2     1000021         1   # BR(~d_R -> ~g      d)
#
#         PDG            Width
DECAY   1000004     1.31301150E+01   # scharm_L decays
#          BR         NDA      ID1       ID2
     5.97240819E-03    2     1000022         4   # BR(~c_L -> ~chi_10 c)
     2.13814900E-01    2     1000023         4   # BR(~c_L -> ~chi_20 c)
     6.54997799E-04    2     1000025         4   # BR(~c_L -> ~chi_30 c)
     1.15708854E-02    2     1000035         4   # BR(~c_L -> ~chi_40 c)
     4.34593064E-01    2     1000024         3   # BR(~c_L -> ~chi_1+ s)
     1.55107464E-02    2     1000037         3   # BR(~c_L -> ~chi_2+ s)
     3.17882998E-01    2     1000021         4   # BR(~c_L -> ~g      c)
#
#         PDG            Width
DECAY   2000004     5.45626401E+00   # scharm_R decays
#          BR         NDA      ID1       ID2
     3.56050387E-01    2     1000022         4   # BR(~c_R -> ~chi_10 c)
     1.95018645E-03    2     1000023         4   # BR(~c_R -> ~chi_20 c)
     5.79103054E-04    2     1000025         4   # BR(~c_R -> ~chi_30 c)
     2.22793094E-03    2     1000035         4   # BR(~c_R -> ~chi_40 c)
     0.00000000E+00    2     1000024         3   # BR(~c_R -> ~chi_1+ s)
     0.00000000E+00    2     1000037         3   # BR(~c_R -> ~chi_2+ s)
     6.39192393E-01    2     1000021         4   # BR(~c_R -> ~g      c)
#
#         PDG            Width
DECAY   1000003     1.31836627E+01   # sstrange_L decays
#          BR         NDA      ID1       ID2
     1.36015082E-02    2     1000022         3   # BR(~s_L -> ~chi_10 s)
     2.00968062E-01    2     1000023         3   # BR(~s_L -> ~chi_20 s)
     1.12614606E-03    2     1000025         3   # BR(~s_L -> ~chi_30 s)
     1.52229825E-02    2     1000035         3   # BR(~s_L -> ~chi_40 s)
     3.97020140E-01    2    -1000024         4   # BR(~s_L -> ~chi_1- c)
     4.05217275E-02    2    -1000037         4   # BR(~s_L -> ~chi_2- c)
     3.31539434E-01    2     1000021         3   # BR(~s_L -> ~g      s)
#
#         PDG            Width
DECAY   2000003     3.95203891E+00   # sstrange_R decays
#          BR         NDA      ID1       ID2
     1.22809923E-01    2     1000022         3   # BR(~s_R -> ~chi_10 s)
     6.72575606E-04    2     1000023         3   # BR(~s_R -> ~chi_20 s)
     1.99604669E-04    2     1000025         3   # BR(~s_R -> ~chi_30 s)
     7.67849884E-04    2     1000035         3   # BR(~s_R -> ~chi_40 s)
     0.00000000E+00    2    -1000024         4   # BR(~s_R -> ~chi_1- c)
     0.00000000E+00    2    -1000037         4   # BR(~s_R -> ~chi_2- c)
     8.75550047E-01    2     1000021         3   # BR(~s_R -> ~g      s)
#
#         PDG            Width
DECAY   1000011     0.00000000E+00   # stable selectron_L
#          BR         NDA      ID1       ID2
#
#         PDG            Width
DECAY   2000011     0.00000000E+00   # stable selectron_R
#          BR         NDA      ID1       ID2
#
#         PDG            Width
DECAY   1000013     0.00000000E+00   # stable smuon_L
#          BR         NDA      ID1       ID2
#
#         PDG            Width
DECAY   2000013     0.00000000E+00   # stable smuon_R
#          BR         NDA      ID1       ID2
#
#         PDG            Width
DECAY   1000015     0.00000000E+00   # stable stau_1
#          BR         NDA      ID1       ID2
#
#         PDG            Width
DECAY   2000015     0.00000000E+00   # stable stau_2
#          BR         NDA      ID1       ID2
#
#         PDG            Width
DECAY   1000012     6.07250223E+00   # snu_eL decays
#          BR         NDA      ID1       ID2
     1.42806354E-01    2     1000022        12   # BR(~nu_eL -> ~chi_10 nu_e)
     2.51079690E-01    2     1000023        12   # BR(~nu_eL -> ~chi_20 nu_e)
     1.34732524E-03    2     1000025        12   # BR(~nu_eL -> ~chi_30 nu_e)
     1.36914726E-02    2     1000035        12   # BR(~nu_eL -> ~chi_40 nu_e)
     5.79974054E-01    2     1000024        11   # BR(~nu_eL -> ~chi_1+ e-)
     1.11011047E-02    2     1000037        11   # BR(~nu_eL -> ~chi_2+ e-)
#
#         PDG            Width
DECAY   1000014     6.07250223E+00   # snu_muL decays
#          BR         NDA      ID1       ID2
     1.42806354E-01    2     1000022        14   # BR(~nu_muL -> ~chi_10 nu_mu)
     2.51079690E-01    2     1000023        14   # BR(~nu_muL -> ~chi_20 nu_mu)
     1.34732524E-03    2     1000025        14   # BR(~nu_muL -> ~chi_30 nu_mu)
     1.36914726E-02    2     1000035        14   # BR(~nu_muL -> ~chi_40 nu_mu)
     5.79974054E-01    2     1000024        13   # BR(~nu_muL -> ~chi_1+ mu-)
     1.11011047E-02    2     1000037        13   # BR(~nu_muL -> ~chi_2+ mu-)
#
#         PDG            Width
DECAY   1000016     6.07063864E+00   # snu_tauL decays
#          BR         NDA      ID1       ID2
     1.42115898E-01    2     1000022        16   # BR(~nu_tauL -> ~chi_10 nu_tau)
     2.49372798E-01    2     1000023        16   # BR(~nu_tauL -> ~chi_20 nu_tau)
     1.32244004E-03    2     1000025        16   # BR(~nu_tauL -> ~chi_30 nu_tau)
     1.34038264E-02    2     1000035        16   # BR(~nu_tauL -> ~chi_40 nu_tau)
     5.77998382E-01    2     1000024        15   # BR(~nu_tauL -> ~chi_1+ tau-)
     1.57866549E-02    2     1000037        15   # BR(~nu_tauL -> ~chi_2+ tau-)
     0.00000000E+00    2    -1000015       -37   # BR(~nu_tauL -> ~tau_1+ H-)
     0.00000000E+00    2    -2000015       -37   # BR(~nu_tauL -> ~tau_2+ H-)
     0.00000000E+00    2    -1000015       -24   # BR(~nu_tauL -> ~tau_1+ W-)
     0.00000000E+00    2    -2000015       -24   # BR(~nu_tauL -> ~tau_2+ W-)
#
#         PDG            Width
DECAY   1000024     7.00367294E-03   # chargino1+ decays
#          BR         NDA      ID1       ID2
     0.00000000E+00    2     1000002        -1   # BR(~chi_1+ -> ~u_L   db)
     0.00000000E+00    2     2000002        -1   # BR(~chi_1+ -> ~u_R   db)
     0.00000000E+00    2    -1000001         2   # BR(~chi_1+ -> ~d_L*  u )
     0.00000000E+00    2    -2000001         2   # BR(~chi_1+ -> ~d_R*  u )
     0.00000000E+00    2     1000004        -3   # BR(~chi_1+ -> ~c_L   sb)
     0.00000000E+00    2     2000004        -3   # BR(~chi_1+ -> ~c_R   sb)
     0.00000000E+00    2    -1000003         4   # BR(~chi_1+ -> ~s_L*  c )
     0.00000000E+00    2    -2000003         4   # BR(~chi_1+ -> ~s_R*  c )
     0.00000000E+00    2     1000006        -5   # BR(~chi_1+ -> ~t_1   bb)
     0.00000000E+00    2     2000006        -5   # BR(~chi_1+ -> ~t_2   bb)
     0.00000000E+00    2    -1000005         6   # BR(~chi_1+ -> ~b_1*  t )
     0.00000000E+00    2    -2000005         6   # BR(~chi_1+ -> ~b_2*  t )
     0.00000000E+00    2     1000012       -11   # BR(~chi_1+ -> ~nu_eL  e+  )
     0.00000000E+00    2     1000014       -13   # BR(~chi_1+ -> ~nu_muL  mu+ )
     0.00000000E+00    2     1000016       -15   # BR(~chi_1+ -> ~nu_tau1 tau+)
     0.00000000E+00    2    -1000011        12   # BR(~chi_1+ -> ~e_L+    nu_e)
     0.00000000E+00    2    -2000011        12   # BR(~chi_1+ -> ~e_R+    nu_e)
     0.00000000E+00    2    -1000013        14   # BR(~chi_1+ -> ~mu_L+   nu_mu)
     0.00000000E+00    2    -2000013        14   # BR(~chi_1+ -> ~mu_R+   nu_mu)
     0.00000000E+00    2    -1000015        16   # BR(~chi_1+ -> ~tau_1+  nu_tau)
     0.00000000E+00    2    -2000015        16   # BR(~chi_1+ -> ~tau_2+  nu_tau)
     1.00000000E+00    2     1000022        24   # BR(~chi_1+ -> ~chi_10  W+)
     0.00000000E+00    2     1000023        24   # BR(~chi_1+ -> ~chi_20  W+)
     0.00000000E+00    2     1000025        24   # BR(~chi_1+ -> ~chi_30  W+)
     0.00000000E+00    2     1000035        24   # BR(~chi_1+ -> ~chi_40  W+)
     0.00000000E+00    2     1000022        37   # BR(~chi_1+ -> ~chi_10  H+)
     0.00000000E+00    2     1000023        37   # BR(~chi_1+ -> ~chi_20  H+)
     0.00000000E+00    2     1000025        37   # BR(~chi_1+ -> ~chi_30  H+)
     0.00000000E+00    2     1000035        37   # BR(~chi_1+ -> ~chi_40  H+)
#
#         PDG            Width
DECAY   1000037     2.23350902E+00   # chargino2+ decays
#          BR         NDA      ID1       ID2
     0.00000000E+00    2     1000002        -1   # BR(~chi_2+ -> ~u_L   db)
     0.00000000E+00    2     2000002        -1   # BR(~chi_2+ -> ~u_R   db)
     0.00000000E+00    2    -1000001         2   # BR(~chi_2+ -> ~d_L*  u )
     0.00000000E+00    2    -2000001         2   # BR(~chi_2+ -> ~d_R*  u )
     0.00000000E+00    2     1000004        -3   # BR(~chi_2+ -> ~c_L   sb)
     0.00000000E+00    2     2000004        -3   # BR(~chi_2+ -> ~c_R   sb)
     0.00000000E+00    2    -1000003         4   # BR(~chi_2+ -> ~s_L*  c )
     0.00000000E+00    2    -2000003         4   # BR(~chi_2+ -> ~s_R*  c )
     0.00000000E+00    2     1000006        -5   # BR(~chi_2+ -> ~t_1   bb)
     0.00000000E+00    2     2000006        -5   # BR(~chi_2+ -> ~t_2   bb)
     0.00000000E+00    2    -1000005         6   # BR(~chi_2+ -> ~b_1*  t )
     0.00000000E+00    2    -2000005         6   # BR(~chi_2+ -> ~b_2*  t )
     0.00000000E+00    2     1000012       -11   # BR(~chi_2+ -> ~nu_eL  e+  )
     0.00000000E+00    2     1000014       -13   # BR(~chi_2+ -> ~nu_muL  mu+ )
     0.00000000E+00    2     1000016       -15   # BR(~chi_2+ -> ~nu_tau1 tau+)
     0.00000000E+00    2    -1000011        12   # BR(~chi_2+ -> ~e_L+    nu_e)
     0.00000000E+00    2    -2000011        12   # BR(~chi_2+ -> ~e_R+    nu_e)
     0.00000000E+00    2    -1000013        14   # BR(~chi_2+ -> ~mu_L+   nu_mu)
     0.00000000E+00    2    -2000013        14   # BR(~chi_2+ -> ~mu_R+   nu_mu)
     0.00000000E+00    2    -1000015        16   # BR(~chi_2+ -> ~tau_1+  nu_tau)
     0.00000000E+00    2    -2000015        16   # BR(~chi_2+ -> ~tau_2+  nu_tau)
     3.13898343E-01    2     1000024        23   # BR(~chi_2+ -> ~chi_1+  Z )
     9.42923324E-02    2     1000022        24   # BR(~chi_2+ -> ~chi_10  W+)
     3.63297283E-01    2     1000023        24   # BR(~chi_2+ -> ~chi_20  W+)
     0.00000000E+00    2     1000025        24   # BR(~chi_2+ -> ~chi_30  W+)
     0.00000000E+00    2     1000035        24   # BR(~chi_2+ -> ~chi_40  W+)
     2.28512042E-01    2     1000024        25   # BR(~chi_2+ -> ~chi_1+  h )
     0.00000000E+00    2     1000024        35   # BR(~chi_2+ -> ~chi_1+  H )
     0.00000000E+00    2     1000024        36   # BR(~chi_2+ -> ~chi_1+  A )
     0.00000000E+00    2     1000022        37   # BR(~chi_2+ -> ~chi_10  H+)
     0.00000000E+00    2     1000023        37   # BR(~chi_2+ -> ~chi_20  H+)
     0.00000000E+00    2     1000025        37   # BR(~chi_2+ -> ~chi_30  H+)
     0.00000000E+00    2     1000035        37   # BR(~chi_2+ -> ~chi_40  H+)
#
#         PDG            Width
DECAY   1000022     1.00000000E-01   # neutralino1 decays
##         BR         NDA      ID1       ID2
     1.00000000E+00    2     1000039        23   #  BR(~chi_10 -> ~G Z)
#
#         PDG            Width
DECAY   1000023     9.37327589E-04   # neutralino2 decays
#          BR         NDA      ID1       ID2
     1.00000000E+00    2     1000022        23   # BR(~chi_20 -> ~chi_10   Z )
     0.00000000E+00    2     1000024       -24   # BR(~chi_20 -> ~chi_1+   W-)
     0.00000000E+00    2    -1000024        24   # BR(~chi_20 -> ~chi_1-   W+)
     0.00000000E+00    2     1000037       -24   # BR(~chi_20 -> ~chi_2+   W-)
     0.00000000E+00    2    -1000037        24   # BR(~chi_20 -> ~chi_2-   W+)
     0.00000000E+00    2     1000022        25   # BR(~chi_20 -> ~chi_10   h )
     0.00000000E+00    2     1000022        35   # BR(~chi_20 -> ~chi_10   H )
     0.00000000E+00    2     1000022        36   # BR(~chi_20 -> ~chi_10   A )
     0.00000000E+00    2     1000024       -37   # BR(~chi_20 -> ~chi_1+   H-)
     0.00000000E+00    2    -1000024        37   # BR(~chi_20 -> ~chi_1-   H+)
     0.00000000E+00    2     1000037       -37   # BR(~chi_20 -> ~chi_2+   H-)
     0.00000000E+00    2    -1000037        37   # BR(~chi_20 -> ~chi_2-   H+)
     0.00000000E+00    2     1000002        -2   # BR(~chi_20 -> ~u_L      ub)
     0.00000000E+00    2    -1000002         2   # BR(~chi_20 -> ~u_L*     u )
     0.00000000E+00    2     2000002        -2   # BR(~chi_20 -> ~u_R      ub)
     0.00000000E+00    2    -2000002         2   # BR(~chi_20 -> ~u_R*     u )
     0.00000000E+00    2     1000001        -1   # BR(~chi_20 -> ~d_L      db)
     0.00000000E+00    2    -1000001         1   # BR(~chi_20 -> ~d_L*     d )
     0.00000000E+00    2     2000001        -1   # BR(~chi_20 -> ~d_R      db)
     0.00000000E+00    2    -2000001         1   # BR(~chi_20 -> ~d_R*     d )
     0.00000000E+00    2     1000004        -4   # BR(~chi_20 -> ~c_L      cb)
     0.00000000E+00    2    -1000004         4   # BR(~chi_20 -> ~c_L*     c )
     0.00000000E+00    2     2000004        -4   # BR(~chi_20 -> ~c_R      cb)
     0.00000000E+00    2    -2000004         4   # BR(~chi_20 -> ~c_R*     c )
     0.00000000E+00    2     1000003        -3   # BR(~chi_20 -> ~s_L      sb)
     0.00000000E+00    2    -1000003         3   # BR(~chi_20 -> ~s_L*     s )
     0.00000000E+00    2     2000003        -3   # BR(~chi_20 -> ~s_R      sb)
     0.00000000E+00    2    -2000003         3   # BR(~chi_20 -> ~s_R*     s )
     0.00000000E+00    2     1000006        -6   # BR(~chi_20 -> ~t_1      tb)
     0.00000000E+00    2    -1000006         6   # BR(~chi_20 -> ~t_1*     t )
     0.00000000E+00    2     2000006        -6   # BR(~chi_20 -> ~t_2      tb)
     0.00000000E+00    2    -2000006         6   # BR(~chi_20 -> ~t_2*     t )
     0.00000000E+00    2     1000005        -5   # BR(~chi_20 -> ~b_1      bb)
     0.00000000E+00    2    -1000005         5   # BR(~chi_20 -> ~b_1*     b )
     0.00000000E+00    2     2000005        -5   # BR(~chi_20 -> ~b_2      bb)
     0.00000000E+00    2    -2000005         5   # BR(~chi_20 -> ~b_2*     b )
     0.00000000E+00    2     1000011       -11   # BR(~chi_20 -> ~e_L-     e+)
     0.00000000E+00    2    -1000011        11   # BR(~chi_20 -> ~e_L+     e-)
     0.00000000E+00    2     2000011       -11   # BR(~chi_20 -> ~e_R-     e+)
     0.00000000E+00    2    -2000011        11   # BR(~chi_20 -> ~e_R+     e-)
     0.00000000E+00    2     1000013       -13   # BR(~chi_20 -> ~mu_L-    mu+)
     0.00000000E+00    2    -1000013        13   # BR(~chi_20 -> ~mu_L+    mu-)
     0.00000000E+00    2     2000013       -13   # BR(~chi_20 -> ~mu_R-    mu+)
     0.00000000E+00    2    -2000013        13   # BR(~chi_20 -> ~mu_R+    mu-)
     0.00000000E+00    2     1000015       -15   # BR(~chi_20 -> ~tau_1-   tau+)
     0.00000000E+00    2    -1000015        15   # BR(~chi_20 -> ~tau_1+   tau-)
     0.00000000E+00    2     2000015       -15   # BR(~chi_20 -> ~tau_2-   tau+)
     0.00000000E+00    2    -2000015        15   # BR(~chi_20 -> ~tau_2+   tau-)
     0.00000000E+00    2     1000012       -12   # BR(~chi_20 -> ~nu_eL    nu_eb)
     0.00000000E+00    2    -1000012        12   # BR(~chi_20 -> ~nu_eL*   nu_e )
     0.00000000E+00    2     1000014       -14   # BR(~chi_20 -> ~nu_muL   nu_mub)
     0.00000000E+00    2    -1000014        14   # BR(~chi_20 -> ~nu_muL*  nu_mu )
     0.00000000E+00    2     1000016       -16   # BR(~chi_20 -> ~nu_tau1  nu_taub)
     0.00000000E+00    2    -1000016        16   # BR(~chi_20 -> ~nu_tau1* nu_tau )
#
#         PDG            Width
DECAY   1000025     2.16222723E+00   # neutralino3 decays
#          BR         NDA      ID1       ID2
     1.12205625E-01    2     1000022        23   # BR(~chi_30 -> ~chi_10   Z )
     2.42360898E-01    2     1000023        23   # BR(~chi_30 -> ~chi_20   Z )
     3.06499253E-01    2     1000024       -24   # BR(~chi_30 -> ~chi_1+   W-)
     3.06499253E-01    2    -1000024        24   # BR(~chi_30 -> ~chi_1-   W+)
     0.00000000E+00    2     1000037       -24   # BR(~chi_30 -> ~chi_2+   W-)
     0.00000000E+00    2    -1000037        24   # BR(~chi_30 -> ~chi_2-   W+)
     2.16639745E-02    2     1000022        25   # BR(~chi_30 -> ~chi_10   h )
     0.00000000E+00    2     1000022        35   # BR(~chi_30 -> ~chi_10   H )
     0.00000000E+00    2     1000022        36   # BR(~chi_30 -> ~chi_10   A )
     1.07709952E-02    2     1000023        25   # BR(~chi_30 -> ~chi_20   h )
     0.00000000E+00    2     1000023        35   # BR(~chi_30 -> ~chi_20   H )
     0.00000000E+00    2     1000023        36   # BR(~chi_30 -> ~chi_20   A )
     0.00000000E+00    2     1000024       -37   # BR(~chi_30 -> ~chi_1+   H-)
     0.00000000E+00    2    -1000024        37   # BR(~chi_30 -> ~chi_1-   H+)
     0.00000000E+00    2     1000037       -37   # BR(~chi_30 -> ~chi_2+   H-)
     0.00000000E+00    2    -1000037        37   # BR(~chi_30 -> ~chi_2-   H+)
     0.00000000E+00    2     1000002        -2   # BR(~chi_30 -> ~u_L      ub)
     0.00000000E+00    2    -1000002         2   # BR(~chi_30 -> ~u_L*     u )
     0.00000000E+00    2     2000002        -2   # BR(~chi_30 -> ~u_R      ub)
     0.00000000E+00    2    -2000002         2   # BR(~chi_30 -> ~u_R*     u )
     0.00000000E+00    2     1000001        -1   # BR(~chi_30 -> ~d_L      db)
     0.00000000E+00    2    -1000001         1   # BR(~chi_30 -> ~d_L*     d )
     0.00000000E+00    2     2000001        -1   # BR(~chi_30 -> ~d_R      db)
     0.00000000E+00    2    -2000001         1   # BR(~chi_30 -> ~d_R*     d )
     0.00000000E+00    2     1000004        -4   # BR(~chi_30 -> ~c_L      cb)
     0.00000000E+00    2    -1000004         4   # BR(~chi_30 -> ~c_L*     c )
     0.00000000E+00    2     2000004        -4   # BR(~chi_30 -> ~c_R      cb)
     0.00000000E+00    2    -2000004         4   # BR(~chi_30 -> ~c_R*     c )
     0.00000000E+00    2     1000003        -3   # BR(~chi_30 -> ~s_L      sb)
     0.00000000E+00    2    -1000003         3   # BR(~chi_30 -> ~s_L*     s )
     0.00000000E+00    2     2000003        -3   # BR(~chi_30 -> ~s_R      sb)
     0.00000000E+00    2    -2000003         3   # BR(~chi_30 -> ~s_R*     s )
     0.00000000E+00    2     1000006        -6   # BR(~chi_30 -> ~t_1      tb)
     0.00000000E+00    2    -1000006         6   # BR(~chi_30 -> ~t_1*     t )
     0.00000000E+00    2     2000006        -6   # BR(~chi_30 -> ~t_2      tb)
     0.00000000E+00    2    -2000006         6   # BR(~chi_30 -> ~t_2*     t )
     0.00000000E+00    2     1000005        -5   # BR(~chi_30 -> ~b_1      bb)
     0.00000000E+00    2    -1000005         5   # BR(~chi_30 -> ~b_1*     b )
     0.00000000E+00    2     2000005        -5   # BR(~chi_30 -> ~b_2      bb)
     0.00000000E+00    2    -2000005         5   # BR(~chi_30 -> ~b_2*     b )
     0.00000000E+00    2     1000011       -11   # BR(~chi_30 -> ~e_L-     e+)
     0.00000000E+00    2    -1000011        11   # BR(~chi_30 -> ~e_L+     e-)
     0.00000000E+00    2     2000011       -11   # BR(~chi_30 -> ~e_R-     e+)
     0.00000000E+00    2    -2000011        11   # BR(~chi_30 -> ~e_R+     e-)
     0.00000000E+00    2     1000013       -13   # BR(~chi_30 -> ~mu_L-    mu+)
     0.00000000E+00    2    -1000013        13   # BR(~chi_30 -> ~mu_L+    mu-)
     0.00000000E+00    2     2000013       -13   # BR(~chi_30 -> ~mu_R-    mu+)
     0.00000000E+00    2    -2000013        13   # BR(~chi_30 -> ~mu_R+    mu-)
     0.00000000E+00    2     1000015       -15   # BR(~chi_30 -> ~tau_1-   tau+)
     0.00000000E+00    2    -1000015        15   # BR(~chi_30 -> ~tau_1+   tau-)
     0.00000000E+00    2     2000015       -15   # BR(~chi_30 -> ~tau_2-   tau+)
     0.00000000E+00    2    -2000015        15   # BR(~chi_30 -> ~tau_2+   tau-)
     0.00000000E+00    2     1000012       -12   # BR(~chi_30 -> ~nu_eL    nu_eb)
     0.00000000E+00    2    -1000012        12   # BR(~chi_30 -> ~nu_eL*   nu_e )
     0.00000000E+00    2     1000014       -14   # BR(~chi_30 -> ~nu_muL   nu_mub)
     0.00000000E+00    2    -1000014        14   # BR(~chi_30 -> ~nu_muL*  nu_mu )
     0.00000000E+00    2     1000016       -16   # BR(~chi_30 -> ~nu_tau1  nu_taub)
     0.00000000E+00    2    -1000016        16   # BR(~chi_30 -> ~nu_tau1* nu_tau )
#
#         PDG            Width
DECAY   1000035     2.37932556E+00   # neutralino4 decays
#          BR         NDA      ID1       ID2
     2.36489274E-02    2     1000022        23   # BR(~chi_40 -> ~chi_10   Z )
     1.94410793E-02    2     1000023        23   # BR(~chi_40 -> ~chi_20   Z )
     0.00000000E+00    2     1000025        23   # BR(~chi_40 -> ~chi_30   Z )
     3.39474740E-01    2     1000024       -24   # BR(~chi_40 -> ~chi_1+   W-)
     3.39474740E-01    2    -1000024        24   # BR(~chi_40 -> ~chi_1-   W+)
     0.00000000E+00    2     1000037       -24   # BR(~chi_40 -> ~chi_2+   W-)
     0.00000000E+00    2    -1000037        24   # BR(~chi_40 -> ~chi_2-   W+)
     9.26914543E-02    2     1000022        25   # BR(~chi_40 -> ~chi_10   h )
     0.00000000E+00    2     1000022        35   # BR(~chi_40 -> ~chi_10   H )
     0.00000000E+00    2     1000022        36   # BR(~chi_40 -> ~chi_10   A )
     1.85269058E-01    2     1000023        25   # BR(~chi_40 -> ~chi_20   h )
     0.00000000E+00    2     1000023        35   # BR(~chi_40 -> ~chi_20   H )
     0.00000000E+00    2     1000023        36   # BR(~chi_40 -> ~chi_20   A )
     0.00000000E+00    2     1000025        25   # BR(~chi_40 -> ~chi_30   h )
     0.00000000E+00    2     1000025        35   # BR(~chi_40 -> ~chi_30   H )
     0.00000000E+00    2     1000025        36   # BR(~chi_40 -> ~chi_30   A )
     0.00000000E+00    2     1000024       -37   # BR(~chi_40 -> ~chi_1+   H-)
     0.00000000E+00    2    -1000024        37   # BR(~chi_40 -> ~chi_1-   H+)
     0.00000000E+00    2     1000037       -37   # BR(~chi_40 -> ~chi_2+   H-)
     0.00000000E+00    2    -1000037        37   # BR(~chi_40 -> ~chi_2-   H+)
     0.00000000E+00    2     1000002        -2   # BR(~chi_40 -> ~u_L      ub)
     0.00000000E+00    2    -1000002         2   # BR(~chi_40 -> ~u_L*     u )
     0.00000000E+00    2     2000002        -2   # BR(~chi_40 -> ~u_R      ub)
     0.00000000E+00    2    -2000002         2   # BR(~chi_40 -> ~u_R*     u )
     0.00000000E+00    2     1000001        -1   # BR(~chi_40 -> ~d_L      db)
     0.00000000E+00    2    -1000001         1   # BR(~chi_40 -> ~d_L*     d )
     0.00000000E+00    2     2000001        -1   # BR(~chi_40 -> ~d_R      db)
     0.00000000E+00    2    -2000001         1   # BR(~chi_40 -> ~d_R*     d )
     0.00000000E+00    2     1000004        -4   # BR(~chi_40 -> ~c_L      cb)
     0.00000000E+00    2    -1000004         4   # BR(~chi_40 -> ~c_L*     c )
     0.00000000E+00    2     2000004        -4   # BR(~chi_40 -> ~c_R      cb)
     0.00000000E+00    2    -2000004         4   # BR(~chi_40 -> ~c_R*     c )
     0.00000000E+00    2     1000003        -3   # BR(~chi_40 -> ~s_L      sb)
     0.00000000E+00    2    -1000003         3   # BR(~chi_40 -> ~s_L*     s )
     0.00000000E+00    2     2000003        -3   # BR(~chi_40 -> ~s_R      sb)
     0.00000000E+00    2    -2000003         3   # BR(~chi_40 -> ~s_R*     s )
     0.00000000E+00    2     1000006        -6   # BR(~chi_40 -> ~t_1      tb)
     0.00000000E+00    2    -1000006         6   # BR(~chi_40 -> ~t_1*     t )
     0.00000000E+00    2     2000006        -6   # BR(~chi_40 -> ~t_2      tb)
     0.00000000E+00    2    -2000006         6   # BR(~chi_40 -> ~t_2*     t )
     0.00000000E+00    2     1000005        -5   # BR(~chi_40 -> ~b_1      bb)
     0.00000000E+00    2    -1000005         5   # BR(~chi_40 -> ~b_1*     b )
     0.00000000E+00    2     2000005        -5   # BR(~chi_40 -> ~b_2      bb)
     0.00000000E+00    2    -2000005         5   # BR(~chi_40 -> ~b_2*     b )
     0.00000000E+00    2     1000011       -11   # BR(~chi_40 -> ~e_L-     e+)
     0.00000000E+00    2    -1000011        11   # BR(~chi_40 -> ~e_L+     e-)
     0.00000000E+00    2     2000011       -11   # BR(~chi_40 -> ~e_R-     e+)
     0.00000000E+00    2    -2000011        11   # BR(~chi_40 -> ~e_R+     e-)
     0.00000000E+00    2     1000013       -13   # BR(~chi_40 -> ~mu_L-    mu+)
     0.00000000E+00    2    -1000013        13   # BR(~chi_40 -> ~mu_L+    mu-)
     0.00000000E+00    2     2000013       -13   # BR(~chi_40 -> ~mu_R-    mu+)
     0.00000000E+00    2    -2000013        13   # BR(~chi_40 -> ~mu_R+    mu-)
     0.00000000E+00    2     1000015       -15   # BR(~chi_40 -> ~tau_1-   tau+)
     0.00000000E+00    2    -1000015        15   # BR(~chi_40 -> ~tau_1+   tau-)
     0.00000000E+00    2     2000015       -15   # BR(~chi_40 -> ~tau_2-   tau+)
     0.00000000E+00    2    -2000015        15   # BR(~chi_40 -> ~tau_2+   tau-)
     0.00000000E+00    2     1000012       -12   # BR(~chi_40 -> ~nu_eL    nu_eb)
     0.00000000E+00    2    -1000012        12   # BR(~chi_40 -> ~nu_eL*   nu_e )
     0.00000000E+00    2     1000014       -14   # BR(~chi_40 -> ~nu_muL   nu_mub)
     0.00000000E+00    2    -1000014        14   # BR(~chi_40 -> ~nu_muL*  nu_mu )
     0.00000000E+00    2     1000016       -16   # BR(~chi_40 -> ~nu_tau1  nu_taub)
     0.00000000E+00    2    -1000016        16   # BR(~chi_40 -> ~nu_tau1* nu_tau )
#         PDG            Width
DECAY   1000039     0.00000000E+00   # stable gravitino
"""

import FWCore.ParameterSet.Config as cms

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring(GRIDPACK),
    nEvents = cms.untracked.uint32(5000),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *

#need the pythia hadronizer, not the generator, as the generation was already done in the madgraph gridpacks
generator = cms.EDFilter("Pythia8HadronizerFilter",
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(1),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(COM_ENERGY),
    crossSection = cms.untracked.double(CROSS_SECTION),
    maxEventsToPrint = cms.untracked.int32(0),
    SLHATableForPythia8 = cms.string('%s' % SLHA_TABLE),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        pythia8PSweightsSettingsBlock,
        processParameters = cms.vstring(
            'SUSY:all = off',
            'SUSY:qqbar2sleptonantislepton= on',
            '1000011:mayDecay = false', #left-handed selectron
            '-1000011:mayDecay = false',
            '2000011:mayDecay = false', #right-handed selectron
            '-2000011:mayDecay = false',
            '1000013:mayDecay = false', #left-handed smuon
            '-1000013:mayDecay = false',
            '2000013:mayDecay = false', #right-handed smuon
            '-2000013:mayDecay = false',
            '1000015:mayDecay = false', #left-handed stau
            '-1000015:mayDecay = false',
            '2000015:mayDecay = false', #right-handed stau
            '-2000015:mayDecay = false',
            '1000039:mayDecay = false', #gravitino
        ),
        parameterSets = cms.vstring(
            'pythia8CommonSettings',
            'pythia8CP5Settings',
            'pythia8PSweightsSettings',
            'processParameters'
        )
    )
)

generator.hscpFlavor = cms.untracked.string(FLAVOR)
generator.massPoint = cms.untracked.int32(MASS_POINT)
generator.particleFile = cms.untracked.string(PARTICLE_FILE)
generator.processFile = cms.untracked.string(PROCESS_FILE)
generator.useregge = cms.bool(USE_REGGE)

ProductionFilterSequence = cms.Sequence(externalLHEProducer*generator)
