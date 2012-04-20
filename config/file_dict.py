#! /usr/bin/env python

def files( filset ) :
    base_dir = base_directory( fileset )
    d = {
        "%s/recalc_out.root" % base_dir :
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

def recalc_files( fileset ) :
    base_dir = base_directory( fileset )
    d = {
        "%s/recalc_out.root" % base_dir :
            {
                "InputFiles"         :  [ "%s/cmssm_test.root" % base_dir, ],
                "Chi2TreeNames"      :  [ "tree" ],
                "Chi2BranchNames"    :  [ "vars" ],
                "ContribTreeNames"   :  [ "contribtree" ],
                "ContribBranchNames" :  [ "vars" ] ,
                "ModelFiles "        :  [ "models/tester.model" ] ,
#                "LHoodFiles"         : [ "models/tester.lhood" ],
#                "StartEntries"       : [ 0 ],
#                "EndEntries"         : [ 1 ],
            }
        }
    return d

def base_directory( fileset ) :
    d = {
            "hep.ph.ic.ac.uk" : "/vols/cms03/mastercode/test_files/",
            "localdomain" :     "~/Documents/mastercode_data/",
        }
    return d[fileset]
