import getpass
import socket

from commands import getoutput 
from modules.MCFile import MCFileCollection
from modules.MCFile import MCFile

def base_directory() :
    user = getpass.getuser()
    fqdn = socket.getfqdn()

    imperial_users = { "sr505"  : "/vols/cms03/mastercode/test_files/",
                       "kjd110" : "/vols/cms04/kjd110/test-sam-py-plotting/",
                     }
    imperial_hosts = ["lx0%d.hep.ph.ic.ac.uk" % node for node in range(4,7) ]

    d = {
            "localhost.localdomain" :  {
                    "hyper"  : "~/Documents/01_mastercode_data/",
                },
        }

    d.update( dict.fromkeys(imperial_hosts, imperial_users) )
    return d[fqdn][user]

###############
# input files #
###############
def cmssm_test_input_files() :
    gd =  {
             "Chi2BranchName"    : "vars",
             "ContribBranchName" : "vars" ,
             "BestFitEntryName"  : "BestFitEntry",
             #"LHoodFile"         : "models/tester.lhood",
             "ModelFile"         : "models/tester.model",
             "PredictionIndex"   : 10,
             "SpectrumIndex"     : 117,
             "Inputs"            : 10,
             "OutputFile"        : "%s/recalc_out.root" % base_directory(),
#            "MinChi2"           : 1,
             "MaxChi2"           : 25,
#             "StartEntry"        : 1,
             "EndEntry"          : 4000,
         }
    fd = {
             "FileName"          : "%s/cmssm_test.root" % base_directory(),
             "Chi2TreeName"      : "tree",
             "ContribTreeName"   : "contribtree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd)

def nuhm1_MCMh_MC7_for_recalc() :
    gd =  {
             "Chi2BranchName"    : "vars",
             "ContribBranchName" : "vars" ,
             "LHoodFile"         : "models/nuhm1-MCMh-MC7.lhood",
             "ModelFile"         : "models/nuhm1-MCMh-MC7.model",
             "PredictionIndex"   : 12,
             "SpectrumIndex"     : 119,
             "Inputs"            : 12,
             "OutputFile"        : "%s/test_MCMh_nuhm1.root" % base_directory(),
             "StartIndex"        : 0,
             "EndIndex"          : 2,
         }
    fd = {
             "FileName"          : "%s/new-nuhm1-MC75-source.root" % base_directory() ,
             "Chi2TreeName"      : "tree",
             "ContribTreeName"   : "contribtree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd)
###############
# histo files #
###############
def cmssm_test_output_files() :
    fd = {
             "FileName"          : "%s/recalc_out.root" % base_directory(),
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



def nuhm1_test_output_files() :
    fd = {
             "FileName"          : "%s/sam-test-file3.root" % base_directory() ,
             "Chi2TreeName"      : "tree",
             "Chi2BranchName"    : "vars",
             "ContribTreeName"   : "contribtree",
             "ContribBranchName" : "vars",
             "PredictionIndex"   : 12,
             "SpectrumIndex"     : 119,
             "Inputs"            : 12,
             "EntryDirectory"    : "entry_histograms",
             "DataDirectory"     : "data_histograms",
         }
    return [MCFile(fd)]

def nuhm1_MCMh_MC7() :
    fd = {
             "FileName"          : "%s/test_MCMh_nuhm1.root" % base_directory() ,
             "Chi2TreeName"      : "tree",
             "Chi2BranchName"    : "vars",
             "ContribTreeName"   : "contribtree",
             "ContribBranchName" : "vars",
             "PredictionIndex"   : 12,
             "SpectrumIndex"     : 119,
             "Inputs"            : 12,
             "EntryDirectory"    : "entry_histograms",
             "DataDirectory"     : "data_histograms",
         }
    return [MCFile(fd)]
