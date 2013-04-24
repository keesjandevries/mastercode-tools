
import getpass, socket, os

from commands import getoutput
from modules.mcfile import MCFileCollection
from modules.mcfile import MCFile

def input_directory() :
#    return  "/vols/cms04/kjd110/my_fork_mastercode/mastercode-rewrite/temp/"
    return  "/vols/cms04/kjd110/tmp-mcpp-old-ss-fh/mastercode-rewrite/temp/"

def output_directory() :
    return  "/vols/cms04/kjd110/test_mcpp_cmssm/"

def mcpp_temp_directory() :
    return  "/vols/cms04/kjd110/tmp-mcpp-old-ss-fh/mastercode-rewrite/temp/"

def mcpp_cmssm_base_directory():
#    return "/vols/cms04/kjd110/mcpp_cmssm_old_big/"
#    return "/vols/cms04/kjd110/mcpp_cmssm_old_mult/"
#    return "/vols/cms04/kjd110/mcpp_cmssm_box_pre_lhc/"
    return "/vols/cms04/kjd110/mcpp_cmssm_old_error_handling"
#    return "/vols/cms04/kjd110/mcpp_cmssm_old_error_hand_mult"

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

def mcpp_cmssm_test_input( ) :
    # output / global options
    gd = mcpp_cmssm_test_histo_dict()
    fd = {
#                 "FileName"          : "%s/%s" % (input_directory(),"my_first_serious_test.root" ),
                 "FileName"          : "%s/%s" % (input_directory(),"test.root" ),
                 "Chi2TreeName"      : "tree",
             }
    mcfs = [MCFile( fd, warn = False )]  
    return MCFileCollection(  mcfs , gd, warn = False)


def mcpp_cmssm_test_histo_dict() :
    d= {
        "FileName"          : "%s/mcpp_cmssm_test.root" % (output_directory(),  ),
        "PredictionIndex"   : 10,
        "SpectrumIndex"     : 74,
        "Inputs"            : 7, 
        "LHoodFile"         : "models/mc8-all.lhood" ,
        "ModelFile"         : "models/mc8.model" ,
#        "ModelFile"         : "models/mc7.model" ,
     }
    d.update(standard_names())
    return d

def mcpp_cmssm_test_histo() :
    return [MCFile(mcpp_cmssm_test_histo_dict() )]


##########################################################################################
def mcpp_cmssm_sub_dirs(dir_n):
    return "subdir_{}".format(dir_n)

def mcpp_cmssm_dir_all_steps_input(dir_n) :
    dir=mcpp_cmssm_base_directory()+'/'+mcpp_cmssm_sub_dirs(dir_n)
    print dir
    import os
    steps=[int(f.replace('mcpp_cmssm-step-','').replace('.root','')) for f in os.listdir(dir) if 'mcpp_cmssm-step-' in f and '.root' in f]
    try:
        steps.pop(steps.index(max(steps)))
    except ValueError:
        return None
    gd = mcpp_cmssm_histo_dict(dir_n)
    fds=[]
    for step in steps:
        fd = {
                 "FileName"          : "%s/%s/mcpp_cmssm-step-%i.root" % (mcpp_cmssm_base_directory(),mcpp_cmssm_sub_dirs(dir_n), step) ,
                 "Chi2TreeName"      : "tree",
             }
        fds.append(fd)
    mcfs = [MCFile( fd, warn = False ) for fd in fds ]  
    return MCFileCollection(  mcfs , gd, warn = False)


def mcpp_cmssm_histo_dict( dir_n) :
    d= {
        "FileName"          : "%s/%s/mcpp_cmssm_all.root" % (mcpp_cmssm_base_directory(), mcpp_cmssm_sub_dirs(dir_n) ),
        "PredictionIndex"   : 10,
        "SpectrumIndex"     : 74,
        "Inputs"            : 7, 
        "Chi2BranchName"    : "vars",
#        "ModelFile"         : "models/mc8.model",
#        "LHoodFile"         : "models/mc8-all.lhood",
        "ModelFile"         : "models/mc7.model" ,
#        "MinChi2"           : 0,
#        "MaxChi2"           : 45, 
        "MinContrib"        : 0,
     }
    d.update(standard_names())
    return d

def mcpp_cmssm_histo(dir_n) :
    return [MCFile(mcpp_cmssm_histo_dict(dir_n) )]

def mcpp_cmssm_histo_range(range_begin, range_end) :
    return [MCFile(mcpp_cmssm_histo_dict(dir_n) ) for dir_n in range(range_begin,range_end)]

##########################################################################################

def mcpp_cmssm_combined_input(begin=1,end=100 ) :
    # output / global options
    gd = mcpp_cmssm_combined_histo_dict()
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 50000
    fds=[]
    for dir_n in range(begin,end):
        fd = {
                 "FileName"          : "%s/%s/mcpp_cmssm_all.root" % (mcpp_cmssm_base_directory(), mcpp_cmssm_sub_dirs(dir_n) ),
                 "Chi2TreeName"      : "tree",
             }
        fds.append(fd)
    mcfs = [MCFile( fd, warn = False ) for fd in fds ]  
    return MCFileCollection(  mcfs , gd, warn = False)


def mcpp_cmssm_combined_histo_dict() :
    d= {
        "FileName"          : "%s/mcpp_cmssm_all_combined.root" % mcpp_cmssm_base_directory() ,
        "PredictionIndex"   : 10,
        "SpectrumIndex"     : 74,
        "Inputs"            : 7, 
        "ModelFile"         : "models/mc8.model",
        "LHoodFile"         : "models/mc8-all.lhood",
#        "ModelFile"         : "models/mc7.model" ,
#        "MinChi2"           : 0,
#        "MaxChi2"           : 45, 
        "MinContrib"        : 0,
     }
    d.update(standard_names())
    return d

def mcpp_cmssm_combined_histo() :
    return [MCFile(mcpp_cmssm_combined_histo_dict() )]


##########################################################################################

def mcpp_cmssm_mc8_m0_m12_old_input( ) :
    # output / global options
    gd = mcpp_cmssm_mc8_m0_m12_old_histo_dict()
    fd = {
#                 "FileName"          : "%s/%s" % (input_directory(),"my_first_serious_test.root" ),
#                 "FileName"          : mcpp_temp_directory()+"ab_test.root",
                 "FileName"          : mcpp_temp_directory()+"m0_m12_mc8_all_recalculated.root",
                 "Chi2TreeName"      : "tree",
             }
    mcfs = [MCFile( fd, warn = False )]  
    return MCFileCollection(  mcfs , gd, warn = False)


def mcpp_cmssm_mc8_m0_m12_old_histo_dict() :
    d= {
        "FileName"          : mcpp_temp_directory()+"cmssm_mc8_m0_m12_old.root",
        "PredictionIndex"   : 10,
        "SpectrumIndex"     : 74,
        "Inputs"            : 7, 
        "LHoodFile"         : "models/mc8-all.lhood" ,
        "ModelFile"         : "models/mc8.model" ,
#        "ModelFile"         : "models/mc7.model" ,
     }
    d.update(standard_names())
    d[    "Chi2BranchName"] = "invars"
    return d

def mcpp_cmssm_mc8_m0_m12_old_histo() :
    return [MCFile(mcpp_cmssm_mc8_m0_m12_old_histo_dict() )]


##########################################################################################

def mcpp_cmssm_mc8_m0_m12_new_input( ) :
    # output / global options
    gd = mcpp_cmssm_mc8_m0_m12_new_histo_dict()
    fd = {
#                 "FileName"          : "%s/%s" % (input_directory(),"my_first_serious_test.root" ),
#                 "FileName"          : mcpp_temp_directory()+"ab_test.root",
                 "FileName"          : mcpp_temp_directory()+"m0_m12_mc8_all_recalculated.root",
                 "Chi2TreeName"      : "tree",
             }
    mcfs = [MCFile( fd, warn = False )]  
    return MCFileCollection(  mcfs , gd, warn = False)


def mcpp_cmssm_mc8_m0_m12_new_histo_dict() :
    d= {
        "FileName"          : mcpp_temp_directory()+"cmssm_mc8_m0_m12_new.root",
        "PredictionIndex"   : 10,
        "SpectrumIndex"     : 74,
        "Inputs"            : 7, 
        "LHoodFile"         : "models/mc8-all.lhood" ,
        "ModelFile"         : "models/mc8.model" ,
#        "ModelFile"         : "models/mc7.model" ,
     }
    d.update(standard_names())
    d[    "Chi2BranchName"] = "outvars"
    return d

def mcpp_cmssm_mc8_m0_m12_new_histo() :
    return [MCFile(mcpp_cmssm_mc8_m0_m12_new_histo_dict() )]


##########################################################################################
