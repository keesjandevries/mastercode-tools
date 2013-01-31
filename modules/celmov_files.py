import getpass
import socket

from commands import getoutput
from modules.mcfile import MCFileCollection
from modules.mcfile import MCFile

def base_directory() :
    return  "/vols/cms04/kjd110/mc8/"

##########################################################################################

def standard_names():
    return{
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
                    }


##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################

def cmssm_mc8_all_stable_stau_input() :
    # output / global options
    gd = cmssm_mc8_all_stable_stau_histo_dict()
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 50000

    fd = {
             "FileName"          : "%s/cmssm_combine_sampling.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)


def cmssm_mc8_all_stable_stau_histo_dict() :
    d= {
        "FileName"          : "%s/cmssm_mc8_all_stable_stau.root" % base_directory(),
        "PredictionIndex"   : 10,
        "SpectrumIndex"     : 117,
        "Inputs"            : 7, 
        "LHoodFile"         : "models/mc8-all.lhood",
        "ModelFile"         : "models/mc8.model" ,
        "LongLivedStua"     : True,
#        "MinChi2"           : 0,
#        "MaxChi2"           : 45, 
        "MinContrib"        : 0,
     }
    d.update(standard_names())
    return d

def cmssm_mc8_all_stable_stau_histo() :
    return [MCFile(cmssm_mc8_all_stable_stau_histo_dict() )]


##########################################################################################
