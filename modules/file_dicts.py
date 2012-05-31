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
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)

def nuhm1_test_input_files() :
    gd = nuhm1_test_file_histo_dict()
    fd = {
             "FileName"          : "%s/nuhm1_large_test.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)

def cmssm_MCMh_mh125_input() :   
    # output / global options
    gd = cmssm_MCMh_mh125_histo_dict()   
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 50000
    
    # input files: 1 dict per file
    fd = {
             # copied from /vols/cms03/kjd110/Mar2012-CMSSM-AB-output/dm_aab_force_out.root
             "FileName"          : "%s/dm_aab_force_out.root" % base_directory(),  
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)

def cmssm_MCMh_MC7_input() :   
    # output / global options
    gd = cmssm_MCMh_MC7_histo_dict()   
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 50000
    
    # input files: 1 dict per file
    fd = {
             # copied from /vols/cms03/kjd110/Mar2012-CMSSM-AB-output/dm_aab_force_out.root
             "FileName"          : "%s/dm_aab_force_out.root" % base_directory(),  
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)


def cmssm_MC8_all_input() :   
    # output / global options
    gd = cmssm_MC8_all_histo_dict()   
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 50000
    
    # input files: 1 dict per file
    fd = {
             # copied from /vols/cms03/kjd110/Mar2012-CMSSM-AB-output/dm_aab_force_out.root
             "FileName"          : "%s/dm_aab_force_out.root" % base_directory(),  
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    fd2= {
             "FileName"          : "/vols/cms03/kjd110/May2012-cmssm-mh125/dm_cmssm_May2012_short.root" ,  
             "Chi2TreeName"      : "tree",
         }
    mcf2= MCFile( fd2,warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    fd3= {
             "FileName"          : "/vols/cms03/kjd110/May2012-cmssm-mh125/dm_cmssm_May2012_medium.root" ,  
             "Chi2TreeName"      : "tree",
         }
    mcf3= MCFile( fd3,warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf,mcf2,mcf3 ], gd, warn = False)

def nuhm1_test_input() :
    gd = nuhm1_test_histo_dict()
    gd["StartEntry"] = 16737459     # 16385171: ./Point.py -c "mA0=300" "tanb=20"on MC8 all
    gd["EndEntry"]   = 16737460
    fd = {
             "FileName"          : "%s/new-nuhm1-MC75-source.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)

def nuhm1_MCMh_mh125_input() :
    gd = nuhm1_MCMh_mh125_histo_dict()
#    gd["StartEntry"] = 208280      
#    gd["EndEntry"]   = 208295 
    fd = {
             "FileName"          : "%s/new-nuhm1-MC75-source.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)

def nuhm1_MC8_all_input() :
    gd = nuhm1_MC8_all_histo_dict()
#    gd["StartEntry"] = 0      
#    gd["EndEntry"]   = 208295 
    fd = {
             "FileName"          : "%s/new-nuhm1-MC75-source.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)

def nuhm1_Bsmm2012_input() :
    gd = nuhm1_Bsmm2012_histo_dict()
#    gd["StartEntry"] = 208280 
#    gd["EndEntry"]   = 208295 
    fd = {
             "FileName"          : "%s/new-nuhm1-MC75-source.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)

def nuhm1_MCMh_MC7_input() :
    gd = nuhm1_MCMh_MC7_histo_dict()
    gd["StartEntry"] = 208288
    gd["EndEntry"]   = 208290
    fd = {
             "FileName"          : "%s/new-nuhm1-MC75-source.root" % base_directory(),
             "Chi2TreeName"      : "tree",
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
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 10,
        "SpectrumIndex"     : 117,
        "Inputs"            : 10, # FIXME: check this number is right!!!
#        "LHoodFile"         : "models/tester.lhood" ,
        "ModelFile"         : "models/tester.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "MinChi2"           : 0,
        "MaxChi2"           : 1e9,
        "MinContrib"        : 0,
     }
def cmssm_test_file_histo() :
    return [MCFile( cmssm_test_file_histo_dict() )]

def nuhm1_test_file_histo_dict() :
    return {
        "FileName"          : "%s/nuhm1_recalc_out.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 12,
        "SpectrumIndex"     : 119,
        "Inputs"            : 10, # FIXME: check this number is right!!!
#        "LHoodFile"         : "models/tester.lhood" ,
        "ModelFile"         : "models/tester.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "MinChi2"           : 0,
        "MaxChi2"           : 1e9,
        "MinContrib"        : 0,
     }

def cmssm_MCMh_mh125_histo_dict() :
    return {
        "FileName"          : "%s/cmssm_MCMh_mh125.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 10,
        "SpectrumIndex"     : 117,
        "Inputs"            : 10, # FIXME: check this number is right!!!
        "LHoodFile"         : "models/MC7.lhood",     
        "ModelFile"         : "models/MCMh-mh125.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "MinChi2"           : 0,
        "MaxChi2"           : 1e9,
        "MinContrib"        : 0,
     }
def cmssm_MCMh_mh125_histo() :
    return [MCFile(cmssm_MCMh_mh125_histo_dict() )]

def cmssm_MCMh_MC7_histo_dict() :
    return {
        "FileName"          : "%s/cmssm_MCMh_MC7.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 10,
        "SpectrumIndex"     : 117,
        "Inputs"            : 10, # FIXME: check this number is right!!!
        "LHoodFile"         : "models/MC7.lhood" ,
        "ModelFile"         : "models/MC7.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "MinChi2"           : 0,
        "MaxChi2"           : 1e9,
        "MinContrib"        : 0,
     }
def cmssm_MCMh_MC7_histo() :
    return [MCFile(cmssm_MCMh_MC7_histo_dict() )]

def cmssm_MC8_all_histo_dict() :
    return {
        "FileName"          : "%s/cmssm_MC8_all.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 10,
        "SpectrumIndex"     : 117,
        "Inputs"            : 10, # FIXME: check this number is right!!!
        "LHoodFile"         : "models/MC8-All.lhood" ,
        "ModelFile"         : "models/MC8.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "MinChi2"           : 0,
        "MaxChi2"           : 1e9,
        "MinContrib"        : 0,
     }
def cmssm_MC8_all_histo() :
    return [MCFile(cmssm_MC8_all_histo_dict() )]

def nuhm1_test_histo_dict() :
    return {
        "FileName"          : "%s/nuhm1_test.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 12,
        "SpectrumIndex"     : 119,
        "Inputs"            : 12, # FIXME: check this number is right!!!
        "LHoodFile"         : "models/MC8-All.lhood" ,
        "ModelFile"         : "models/MC8.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "MinChi2"           : 0,
        "MaxChi2"           : 1e9,
        "MinContrib"        : 0,
        "MaxMADiff"         : 0.4,
     }
def nuhm1_test_histo() :
    return [MCFile(nuhm1_test_histo_dict() )]

def nuhm1_MCMh_mh125_histo_dict() :
    return {
        "FileName"          : "%s/nuhm1_MCMh_mh125.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 12,
        "SpectrumIndex"     : 119,
        "Inputs"            : 12, # FIXME: check this number is right!!!
        "LHoodFile"         : "models/MC7.lhood",     
        "ModelFile"         : "models/MCMh-mh125.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "MinChi2"           : 0,
        "MaxChi2"           : 1e9,
        "MinContrib"        : 0,
        "MaxMADiff"         : 0.4,
     }
def nuhm1_MCMh_mh125_histo() :
    return [MCFile(nuhm1_MCMh_mh125_histo_dict() )]

def nuhm1_MC8_all_histo_dict() :
    return {
        "FileName"          : "%s/nuhm1_MC8_all.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 12,
        "SpectrumIndex"     : 119,
        "Inputs"            : 12, # FIXME: check this number is right!!!
        "LHoodFile"         : "models/MC8-All.lhood" ,
        "ModelFile"         : "models/MC8.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "MinChi2"           : 0,
        "MaxChi2"           : 1e9,
        "MinContrib"        : 0,
        "MaxMADiff"         : 0.4,
     }
def nuhm1_MC8_all_histo() :
    return [MCFile(nuhm1_MC8_all_histo_dict() )]

def nuhm1_Bsmm2012_histo_dict() :
    return {
        "FileName"          : "%s/nuhm1_Bsmm2012.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 12,
        "SpectrumIndex"     : 119,
        "Inputs"            : 12, # FIXME: check this number is right!!!
        "LHoodFile"         : "models/Bsmm-All.lhood" ,
        "ModelFile"         : "models/tester.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "MinChi2"           : 0,
        "MaxChi2"           : 1e9,
        "MinContrib"        : 0,
     }
def nuhm1_Bsmm2012_histo() :
    return [MCFile(nuhm1_Bsmm2012_histo_dict() )]

def nuhm1_MCMh_MC7_histo_dict() :
    return {
        "FileName"          : "%s/nuhm1_MCMH_MC7.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 12,
        "SpectrumIndex"     : 119,
        "Inputs"            : 12, # FIXME: check this number is right!!!
        "LHoodFile"         : "models/MC7.lhood" ,
        "ModelFile"         : "models/MC7.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "MinChi2"           : 0,
        "MaxChi2"           : 1e9,
        "MinContrib"        : 0,
     }
def nuhm1_MCMh_MC7_histo() :
    return [MCFile(nuhm1_MCMh_MC7_histo_dict() )]
