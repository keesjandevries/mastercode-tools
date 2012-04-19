#! /usr/bin/env python

def files() :
    d = {
        "/vols/cms03/mastercode/test_files/recalc_out.root" :
            { 
                "Chi2TreeName"      : "tree",
                "Chi2BranchName"    : "vars",
                "ContribTreeName"   : "contribtree",
                "ContribBranchName" : "vars",
                "PredictionIndex"   : 10,
                "SpectrumIndex"     : 117,
                "Inputs"            : 10,
                "MinContrib"        : 0.0,
                "EntryDirectory"    : "entry_histograms",
                "DataDirectory"     : "data_histograms",
            }
        }
    return d

def recalc_files() :
    d = {
        "/vols/cms03/mastercode/test_files/cmssm_test.root" :
            {
                "Chi2TreeName"      : "tree",
                "Chi2BranchName"    : "vars",
                "ContribTreeName"   : "contribtree",
                "ContribBranchName" : "vars",
                "ModelFile"         : "models/tester.model",
#                "LHoodFile"         : "models/tester.lhood",
#                "StartEntry"        : 0,
#                "EndEntry"          : 1,
            }
        }
    return d
