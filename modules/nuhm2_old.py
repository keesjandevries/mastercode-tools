
import getpass, socket, os

from commands import getoutput
from modules.mcfile import MCFileCollection
from modules.mcfile import MCFile

def base_directory() :
    return  "/srv/localstage/kjd110/"

def vols_directory() :
    return  "/vols/cms04/kjd110/nuhm2_old"

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

def nuhm2_old_combined_input( ) :
    # output / global options
    gd = nuhm2_old_combined_histo_dict()
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 50000
    dir = base_directory()
#    steps=[f.replace('dmdata_force_out_','').replace('.root','') for f in os.listdir(dir) if 'dmdata_force_out_' in f and '.root' in f]
    files=[f for f in os.listdir(dir) if 'dmdata_force_out_' in f and '.root' in f]
    fds=[]
#    for i in steps:
    for f in files:
        fd = {
#                 "FileName"          : "%s/dmdata_force_out_%s.root" % (base_directory(),steps )
                 "FileName"          : "%s/%s" % (base_directory(),f ),
                 "Chi2TreeName"      : "tree",
             }
        fds.append(fd)
    mcfs = [MCFile( fd, warn = False ) for fd in fds]  
    return MCFileCollection(  mcfs , gd, warn = False)


def nuhm2_old_combined_histo_dict() :
    d= {
        "FileName"          : "%s/nuhm2_old_combined.root" % (vols_directory(),  ),
        "PredictionIndex"   : 12,
        "SpectrumIndex"     : 119,
        "Inputs"            : 7, 
        "ModelFile"         : "models/mc7.model",
#        "MinChi2"           : 0,
        "MaxChi2"           : 45, 
        "MinContrib"        : 0,
     }
    d.update(standard_names())
    return d

def nuhm2_old_combined_histo() :
    return [MCFile(nuhm2_old_combined_histo_dict() )]


##########################################################################################
