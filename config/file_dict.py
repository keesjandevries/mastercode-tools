#! /usr/bin/env python

def files() :
    d = {
        "/home/hyper/Documents/mastercode_data/cmssm_test.root" :
            { 
                "Chi2TreeName"      : "tree",
                "Chi2BranchName"    : "vars",
                "ContribTreeName"   : "contribtree",
                "ContribBranchName" : "vars",
                "PredictionIndex"   : 10,
                "SpectrumIndex"     : 74,
                "EntryDirectory"    : "entry_histograms",
                "DataDirectory"     : "data_histograms",
            }
        }
    return d
