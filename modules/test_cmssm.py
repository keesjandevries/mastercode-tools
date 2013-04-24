
import getpass, socket, os

from commands import getoutput
from modules.mcfile import MCFileCollection
from modules.mcfile import MCFile

def vols_directory() :
    return  "/vols/cms04/kjd110/mc8"

def test_directory() :
    return  "/vols/cms04/kjd110/test_cpp_vs_python"

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

def cmssm_test_vs_cpp_input( ) :
    # output / global options
    gd = cmssm_test_vs_cpp_histo_dict()
    dir = vols_directory()
    fd = {
             "FileName"          : "%s/cmssm_test.root" % vols_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcfs = [MCFile( fd, warn = False ) ]  
    return MCFileCollection(  mcfs , gd, warn = False)


def cmssm_test_vs_cpp_histo_dict() :
    d= {
        "FileName"          : "%s/cmssm_test_vs_cpp.root" % test_directory(),
        "PredictionIndex"   : 10,
        "SpectrumIndex"     : 117,
        "Inputs"            : 7, 
        "ModelFile"         : "models/test_one.model",
#        "MinChi2"           : 0,
#        "MaxChi2"           : 45, 
        "MinContrib"        : 0,
     }
    d.update(standard_names())
    return d

def cmssm_test_vs_cpp_histo() :
    return [MCFile(cmssm_test_vs_cpp_histo_dict() )]


##########################################################################################
