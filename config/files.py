from commands import getoutput 
from modules.MCFile import MCFileCollection

def base_directory() :
    domainname = getoutput('hostname -d')
    d = {
            "hep.ph.ic.ac.uk" : "/vols/cms03/mastercode/test_files/",
            "localdomain" :     "~/Documents/mastercode_data/",
        }
    return d[fileset]

###############
# input files #
###############
def cmssm_test_input_file() :
    gd =  {
             "Chi2BranchName"    : "vars",
             "ContribBranchName" : "vars" ,
             "LHoodFile"         : "models/tester.lhood",
             "ModelFile"         : "models/tester.model",
             "PredictionIndex"   : 10,
             "SpectrumIndex"     : 117,
             "Inputs"            : 10,
         }
    fd = {
             "FileName"          : "%s/cmssm_test.root" % base_directory(),
             "Chi2TreeName"      : "tree",
             "ContribTreeName"   : "contribtree",
         }
    mcf = MFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd)

###############
# histo files #
###############
def cmssm_test_output_files() :
    fd = {
             "FileName"          : "%s/recalc_out.root" % base_directory()
             "Chi2TreeName"      : "tree",
             "Chi2BranchName"    : "vars",
             "ContribTreeName"   : "contribtree",
             "ContribBranchName" : "vars",
             "PredictionIndex"   : 10,
             "SpectrumIndex"     : 117,
             "Inputs"            : 10,
             "EntryDirectory"    : "entry_histograms",
             "DataDirectory"     : "data_histograms",
         }
    return [MCFile(fd)]
