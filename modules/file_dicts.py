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

def cmssm_test_input_files() :
    # output / global options
    gd = cmssm_test_file_histo_dict() 
#    gd["StartEntry"] = 1
#    gd["EndEntry"]   = 4000
    
    # input files: 1 dict per file
    fd = {
             "FileName"          : "%s/cmssm_test.root" % base_directory(),
             "Chi2TreeName"      : "tree",
             "ContribTreeName"   : "contribtree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)


###############
# histo files #
###############
def cmssm_test_file_histo_dict() :
    return {
        "FileName"          : "%s/recalc_out.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 10,
        "SpectrumIndex"     : 117,
        "Inputs"            : 10,
        "LHoodFile"         : "models/tester.lhood" ,
        "ModelFile"         : "models/tester.model" ,
        "Inputs"            : 10,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "MinChi2"           : 1,
        "MaxChi2"           : 25,
     }
def cmssm_test_file_histo() :
    return [MCFile( cmssm_test_file_histo_dict() )]

#def nuhm1_MCMh_MC7_for_recalc() :
#    # output / global options
#    gd =  {
#             "Chi2BranchName"    : "vars",
#             "ContribBranchName" : "vars" ,
#             "LHoodFile"         : "models/tester.lhood" ,
#             "ModelFile"         : "models/tester.model" ,
#             "PredictionIndex"   : 12,
#             "SpectrumIndex"     : 119,
#             "Inputs"            : 12,
#             "OutputFile"        : "%s/test_MCMh_nuhm1.root" % base_directory(),
#             "StartEntry"        : 0,
#             "EndEntry"          : 2,
#         }
#    #gd["StartEntry"] = 0
#    #gd["EndEntry"] = 2
#    fd = {
#             "FileName"          : "%s/new-nuhm1-MC75-source.root" % base_directory() ,
#             "Chi2TreeName"      : "tree",
#             "ContribTreeName"   : "contribtree",
#         }
#    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
#    return MCFileCollection( [ mcf ], gd)

#def nuhm1_test_file_histo_dict() :
#    return {
#        "FileName"          : "%s/sam-test-file3.root" % base_directory() ,
#        "Chi2TreeName"      : "tree",
#        "Chi2BranchName"    : "vars",
#        "ContribTreeName"   : "contribtree",
#        "ContribBranchName" : "vars",
#        "PredictionIndex"   : 12,
#        "SpectrumIndex"     : 119,
#        "Inputs"            : 12,
#        "EntryDirectory"    : "entry_histograms",
#        "DataDirectory"     : "data_histograms",
#    }
#def nuhm1_test_file_histo() :
#    return [MCFile( nuhm1_test_file_histo_dict() )]
#
#def nuhm1_MCMh_MC7_dict() :
#    return {
#        "FileName"          : "%s/test_MCMh_nuhm1.root" % base_directory() ,
#        "Chi2TreeName"      : "tree",
#        "Chi2BranchName"    : "vars",
#        "ContribTreeName"   : "contribtree",
#        "ContribBranchName" : "vars",
#        "PredictionIndex"   : 12,
#        "SpectrumIndex"     : 119,
#        "Inputs"            : 12,
#        "EntryDirectory"    : "entry_histograms",
#        "DataDirectory"     : "data_histograms",
#    }
#def nuhm1_test_file_histo() :
#    return [MCFile( nuhm1_MCMh_MC7_dict() )]
