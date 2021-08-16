**Instructions for creating d0-d0 plots in paper and supplemental material:
**

emu 2018 background MC + diagram (paper):
```cd CMSSW_10_2_12/src/DisplacedSUSY/EMuChannel/test```

in PreselectionOptions.py, have:
```
datasets = [
     'Background',
]
```

```../../Configuration/scripts/makeD0plotsFromTrees.py -l PreselectionOptions.py -w EMuPreselection_2018Analysis_14Dec2020 -d```

emu data (supplemental material):
```cd CMSSW_10_2_12/src/DisplacedSUSY/EMuChannel/test```

in PreselectionOptions.py, have:
```
datasets = [
    'MuonEG_2016_postHIP',
    'MuonEG_2017_withoutB',
    'MuonEG_2018',
]
```

```../../Configuration/scripts/makeD0plotsFromTrees.py -l PreselectionOptions.py -w EMuPreselection_AllData_1Mar2021```


ee data (supplemental material):
```cd CMSSW_10_2_12/src/DisplacedSUSY/EEChannel/test```

in PreselectionOptions.py, have:
```
datasets = [
    'DoubleEG_2016_postHIP',
    'DoubleEG_2017',
    'EGamma_2018',
]
```

```../../Configuration/scripts/makeD0plotsFromTrees.py -l PreselectionOptions.py -w EEPreselection_AllData_1Mar2021```


mumu data (supplemental material):
cd CMSSW_10_2_12/src/DisplacedSUSY/MuMuChannel/test

in PreselectionOptions.py, have:
```
datasets = [
    'DoubleMu_2016_postHIP',
    'DoubleMu_2017_withoutB',
    'DoubleMu_2018',
]
```

```../../Configuration/scripts/makeD0plotsFromTrees.py -l PreselectionOptions.py -w MuMuPreselection_AllData_1Mar2021```


emu signal (supplemental material):
```cd CMSSW_10_2_12/src/DisplacedSUSY/EMuChannel/test```

in PreselectionOptions.py, have:
```
datasets = [
    'stopToLB1500_10mm_2016',
    'stopToLB1500_10mm_2017',
    'stopToLB1500_10mm_2018',
]
```

```../../Configuration/scripts/makeD0plotsFromTrees.py -l PreselectionOptions.py -w EMuPreselection_AllData_1Mar2021 -s```
