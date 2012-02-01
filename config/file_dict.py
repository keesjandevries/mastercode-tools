#! /usr/bin/env python

def files() :
    d = {
        "~/Documents/mastercode_data/cmssm_test.root" :
            { 
                "Chi2TreeName"      : "tree",
                "Chi2BranchName"    : "vars",
                "ContribTreeName"   : "contribtree",
                "ContribBranchName" : "vars",
                "PredictionIndex"   : 10,
                "SpectrumIndex"     : 74,
                "Inputs"            : 10,
                "MinContrib"        : 0.0,
                "EntryDirectory"    : "entry_histograms",
                "DataDirectory"     : "data_histograms",
            }
        }
    return d

def recalc_files() :
    d = {
        "~/Documents/mastercode_data/cmssm_test.root" :
            {
                "Chi2TreeName"      : "tree",
                "Chi2BranchName"    : "vars",
                "ContribTreeName"   : "contribtree",
                "ContribBranchName" : "vars",
                "ModelFile"         : "models/tester.model"
            }
        }
    return d
