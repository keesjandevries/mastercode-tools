import getpass
import socket

from commands import getoutput
from modules.mcfile import MCFileCollection
from modules.mcfile import MCFile

def base_directory() :
    return  "/vols/cms04/kjd110/multinest_output/"

def iter_directory() :
    return  "/vols/cms04/kjd110/multinest_cmssm-1000-live-10-step-200-iter/"

def boxes_directory():
#  return "/vols/cms04/kjd110/small_mn_parallel/"
    return "/vols/cms04/kjd110/mn_parallel/"

def boxes_N_directory(n):
    dir = ("/vols/cms04/kjd110/mn_parallel_%i/" % n)
    return dir

def cmssm_boxes_sub_dirs(i):
    l=[    
"0_0_1666_2_1333_1333_4999_24",
"0_0_1666_24_1333_1333_4999_46",
"0_0_1666_46_1333_1333_4999_68",
"0_0_-1667_2_1333_1333_1666_24",
"0_0_-1667_24_1333_1333_1666_46",
"0_0_-1667_46_1333_1333_1666_68",
"0_0_-5000_2_1333_1333_-1667_24",
"0_0_-5000_24_1333_1333_-1667_46",
"0_0_-5000_46_1333_1333_-1667_68",
"0_1333_1666_2_1333_2666_4999_24",
"0_1333_1666_24_1333_2666_4999_46",
"0_1333_1666_46_1333_2666_4999_68",
"0_1333_-1667_2_1333_2666_1666_24",
"0_1333_-1667_24_1333_2666_1666_46",
"0_1333_-1667_46_1333_2666_1666_68",
"0_1333_-5000_2_1333_2666_-1667_24",
"0_1333_-5000_24_1333_2666_-1667_46",
"0_1333_-5000_46_1333_2666_-1667_68",
"0_2666_1666_2_1333_3999_4999_24",
"0_2666_1666_24_1333_3999_4999_46",
"0_2666_1666_46_1333_3999_4999_68",
"0_2666_-1667_2_1333_3999_1666_24",
"0_2666_-1667_24_1333_3999_1666_46",
"0_2666_-1667_46_1333_3999_1666_68",
"0_2666_-5000_2_1333_3999_-1667_24",
"0_2666_-5000_24_1333_3999_-1667_46",
"0_2666_-5000_46_1333_3999_-1667_68",
"1333_0_1666_2_2666_1333_4999_24",
"1333_0_1666_24_2666_1333_4999_46",
"1333_0_1666_46_2666_1333_4999_68",
"1333_0_-1667_2_2666_1333_1666_24",
"1333_0_-1667_24_2666_1333_1666_46",
"1333_0_-1667_46_2666_1333_1666_68",
"1333_0_-5000_2_2666_1333_-1667_24",
"1333_0_-5000_24_2666_1333_-1667_46",
"1333_0_-5000_46_2666_1333_-1667_68",
"1333_1333_1666_2_2666_2666_4999_24",
"1333_1333_1666_24_2666_2666_4999_46",
"1333_1333_1666_46_2666_2666_4999_68",
"1333_1333_-1667_2_2666_2666_1666_24",
"1333_1333_-1667_24_2666_2666_1666_46",
"1333_1333_-1667_46_2666_2666_1666_68",
"1333_1333_-5000_2_2666_2666_-1667_24",
"1333_1333_-5000_24_2666_2666_-1667_46",
"1333_1333_-5000_46_2666_2666_-1667_68",
"1333_2666_1666_2_2666_3999_4999_24",
"1333_2666_1666_24_2666_3999_4999_46",
"1333_2666_1666_46_2666_3999_4999_68",
"1333_2666_-1667_2_2666_3999_1666_24",
"1333_2666_-1667_24_2666_3999_1666_46",
"1333_2666_-1667_46_2666_3999_1666_68",
"1333_2666_-5000_2_2666_3999_-1667_24",
"1333_2666_-5000_24_2666_3999_-1667_46",
"1333_2666_-5000_46_2666_3999_-1667_68",
"2666_0_1666_2_3999_1333_4999_24",
"2666_0_1666_24_3999_1333_4999_46",
"2666_0_1666_46_3999_1333_4999_68",
"2666_0_-1667_2_3999_1333_1666_24",
"2666_0_-1667_24_3999_1333_1666_46",
"2666_0_-1667_46_3999_1333_1666_68",
"2666_0_-5000_2_3999_1333_-1667_24",
"2666_0_-5000_24_3999_1333_-1667_46",
"2666_0_-5000_46_3999_1333_-1667_68",
"2666_1333_1666_2_3999_2666_4999_24",
"2666_1333_1666_24_3999_2666_4999_46",
"2666_1333_1666_46_3999_2666_4999_68",
"2666_1333_-1667_2_3999_2666_1666_24",
"2666_1333_-1667_24_3999_2666_1666_46",
"2666_1333_-1667_46_3999_2666_1666_68",
"2666_1333_-5000_2_3999_2666_-1667_24",
"2666_1333_-5000_24_3999_2666_-1667_46",
"2666_1333_-5000_46_3999_2666_-1667_68",
"2666_2666_1666_2_3999_3999_4999_24",
"2666_2666_1666_24_3999_3999_4999_46",
"2666_2666_1666_46_3999_3999_4999_68",
"2666_2666_-1667_2_3999_3999_1666_24",
"2666_2666_-1667_24_3999_3999_1666_46",
"2666_2666_-1667_46_3999_3999_1666_68",
"2666_2666_-5000_2_3999_3999_-1667_24",
"2666_2666_-5000_24_3999_3999_-1667_46",
"2666_2666_-5000_46_3999_3999_-1667_68",
]
    return l[i]



def cmssm_boxes_N_sub_dirs(i):
    l=[    
"0_0_1666_2_1333_1333_4999_24",
"0_0_1666_24_1333_1333_4999_46",
"0_0_1666_46_1333_1333_4999_68",
"0_0_-1667_2_1333_1333_1666_24",
"0_0_-1667_24_1333_1333_1666_46",
"0_0_-1667_46_1333_1333_1666_68",
"0_0_-5000_2_1333_1333_-1667_24",
"0_0_-5000_24_1333_1333_-1667_46",
"0_0_-5000_46_1333_1333_-1667_68",
"0_1333_1666_24_1333_2666_4999_46",
"0_1333_1666_46_1333_2666_4999_68",
"0_1333_-1667_24_1333_2666_1666_46",
"0_1333_-1667_46_1333_2666_1666_68",
"0_1333_-5000_24_1333_2666_-1667_46",
"0_1333_-5000_46_1333_2666_-1667_68",
"1333_0_1666_2_2666_1333_4999_24",
"1333_0_1666_24_2666_1333_4999_46",
"1333_0_1666_46_2666_1333_4999_68",
"1333_0_-1667_2_2666_1333_1666_24",
"1333_0_-1667_24_2666_1333_1666_46",
"1333_0_-1667_46_2666_1333_1666_68",
"1333_0_-5000_2_2666_1333_-1667_24",
"1333_0_-5000_24_2666_1333_-1667_46",
"1333_0_-5000_46_2666_1333_-1667_68",
"1333_1333_1666_24_2666_2666_4999_46",
"1333_1333_1666_46_2666_2666_4999_68",
"1333_1333_-1667_46_2666_2666_1666_68",
"1333_1333_-5000_24_2666_2666_-1667_46",
"1333_1333_-5000_46_2666_2666_-1667_68",
"2666_0_1666_2_3999_1333_4999_24",
"2666_0_1666_24_3999_1333_4999_46",
"2666_0_1666_46_3999_1333_4999_68",
"2666_0_-1667_2_3999_1333_1666_24",
"2666_0_-1667_24_3999_1333_1666_46",
"2666_0_-1667_46_3999_1333_1666_68",
"2666_0_-5000_2_3999_1333_-1667_24",
"2666_0_-5000_24_3999_1333_-1667_46",
"2666_0_-5000_46_3999_1333_-1667_68",
"2666_1333_1666_24_3999_2666_4999_46",
"2666_1333_1666_46_3999_2666_4999_68",
"2666_1333_-1667_24_3999_2666_1666_46",
"2666_1333_-1667_46_3999_2666_1666_68",
"2666_1333_-5000_46_3999_2666_-1667_68",]
    return l[i]

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

def cmssm_multinest_first_input() :
    # output / global options
    gd = cmssm_multinest_first_histo_dict()
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 50000

    fd = {
             "FileName"          : "%s/cmssm-10000-iterations-1000-points.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)


def cmssm_multinest_first_histo_dict() :
    d= {
        "FileName"          : "%s/cmssm_multinest_first.root" % base_directory(),
        "PredictionIndex"   : 10,
        "SpectrumIndex"     : 74,
        "Inputs"            : 7, 
        "ModelFile"         : "models/mc7.model",
#        "MinChi2"           : 0,
#        "MaxChi2"           : 45, 
        "MinContrib"        : 0,
     }
    d.update(standard_names())
    return d

def cmssm_multinest_first_histo() :
    return [MCFile(cmssm_multinest_first_histo_dict() )]


##########################################################################################

def cmssm_multinest_iters_input( iters) :
    # output / global options
    gd = cmssm_multinest_iters_histo_dict(iters)
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 50000
    fds=[]
    for iter in range(1,iters+1):
        fd = {
                 "FileName"          : "%s/cmssm-1000-live-%i-step-200-iter.root" % (iter_directory(),iter) ,
                 "Chi2TreeName"      : "tree",
             }
        fds.append(fd)
    mcfs = [MCFile( fd, warn = False ) for fd in fds ]  
    return MCFileCollection(  mcfs , gd, warn = False)


def cmssm_multinest_iters_histo_dict( iters) :
    d= {
        "FileName"          : "%s/cmssm_multinest_%i_iters.root" % (iter_directory(),iters),
        "PredictionIndex"   : 10,
        "SpectrumIndex"     : 74,
        "Inputs"            : 7, 
        "ModelFile"         : "models/mc7.model",
#        "MinChi2"           : 0,
#        "MaxChi2"           : 45, 
        "MinContrib"        : 0,
     }
    d.update(standard_names())
    return d

def cmssm_multinest_iters_histo(iters) :
    return [MCFile(cmssm_multinest_iters_histo_dict(iters) )]

def cmssm_multinest_all_iters_histo_list() :
    return [MCFile(cmssm_multinest_iters_histo_dict(iter) ) for iter in range(1,11)]


##########################################################################################

def cmssm_mn_boxes_input(box_n ) :
    # output / global options
    gd = cmssm_mn_boxes_histo_dict(box_n)
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 50000
    fds=[]
    for step in range(1,11):
        fd = {
                 "FileName"          : "%s/%s/cmssm-step-%i.root" % (boxes_directory(),cmssm_boxes_sub_dirs(box_n), step) ,
                 "Chi2TreeName"      : "tree",
             }
        fds.append(fd)
    mcfs = [MCFile( fd, warn = False ) for fd in fds ]  
    return MCFileCollection(  mcfs , gd, warn = False)


def cmssm_mn_boxes_histo_dict( box_n) :
    d= {
        "FileName"          : "%s/%s/cmssm_all.root" % (boxes_directory(), cmssm_boxes_sub_dirs(box_n) ),
        "PredictionIndex"   : 10,
        "SpectrumIndex"     : 74,
        "Inputs"            : 7, 
        "ModelFile"         : "models/mc7.model",
#        "MinChi2"           : 0,
#        "MaxChi2"           : 45, 
        "MinContrib"        : 0,
     }
    d.update(standard_names())
    return d

def cmssm_mn_boxes_histo(box_n) :
    return [MCFile(cmssm_mn_boxes_histo_dict(box_n) )]

def cmssm_mn_boxes_histo_range(range_begin, range_end) :
    return [MCFile(cmssm_mn_boxes_histo_dict(box_n) ) for box_n in range(range_begin,range_end)]

##########################################################################################

def cmssm_mn_boxes_N_input(box_n,N ) :
    # output / global options
    gd = cmssm_mn_boxes_N_histo_dict(box_n,N)
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 50000
    fds=[]
    for step in range(11,41):
        fd = {
                 "FileName"          : "%s/%s/cmssm-step-%i.root" % (boxes_N_directory(N),cmssm_boxes_N_sub_dirs(box_n), step) ,
                 "Chi2TreeName"      : "tree",
             }
        fds.append(fd)
    mcfs = [MCFile( fd, warn = False ) for fd in fds ]  
    return MCFileCollection(  mcfs , gd, warn = False)


def cmssm_mn_boxes_N_histo_dict( box_n,N) :
    d= {
        "FileName"          : "%s/%s/cmssm_all.root" % (boxes_N_directory(N), cmssm_boxes_N_sub_dirs(box_n) ),
        "PredictionIndex"   : 10,
        "SpectrumIndex"     : 74,
        "Inputs"            : 7, 
        "ModelFile"         : "models/mc7.model",
#        "MinChi2"           : 0,
#        "MaxChi2"           : 45, 
        "MinContrib"        : 0,
     }
    d.update(standard_names())
    return d

def cmssm_mn_boxes_N_histo(box_n) :
    return [MCFile(cmssm_mn_boxes_N_histo_dict(box_n) )]

def cmssm_mn_boxes_N_histo_range(range_begin, range_end) :
    return [MCFile(cmssm_mn_boxes_N_histo_dict(box_n) ) for box_n in range(range_begin,range_end)]

##########################################################################################

def cmssm_mn_boxes_combined_input( ) :
    # output / global options
    gd = cmssm_mn_boxes_combined_histo_dict()
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 50000
    fds=[]
    for box_n in range(0,81):
        fd = {
                 "FileName"          : "%s/%s/cmssm_all.root" % (boxes_directory(), cmssm_boxes_sub_dirs(box_n) ),
                 "Chi2TreeName"      : "tree",
             }
        fds.append(fd)
    mcfs = [MCFile( fd, warn = False ) for fd in fds ]  
    return MCFileCollection(  mcfs , gd, warn = False)


def cmssm_mn_boxes_combined_histo_dict() :
    d= {
        "FileName"          : "%s/cmssm_all_boxes_combined.root" % (boxes_directory(),  ),
        "PredictionIndex"   : 10,
        "SpectrumIndex"     : 74,
        "Inputs"            : 7, 
        "ModelFile"         : "models/mc7.model",
#        "MinChi2"           : 0,
#        "MaxChi2"           : 45, 
        "MinContrib"        : 0,
     }
    d.update(standard_names())
    return d

def cmssm_mn_boxes_combined_histo() :
    return [MCFile(cmssm_mn_boxes_combined_histo_dict() )]


##########################################################################################

def cmssm_mn_boxes_N_combined_input(N ) :
    # output / global options
    gd = cmssm_mn_boxes_N_combined_histo_dict(N)
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 50000
    fds=[]
    for box_n in range(0,43):
        fd = {
                 "FileName"          : "%s/%s/cmssm_all.root" % (boxes_N_directory(N), cmssm_boxes_N_sub_dirs(box_n) ),
                 "Chi2TreeName"      : "tree",
             }
        fds.append(fd)
    mcfs = [MCFile( fd, warn = False ) for fd in fds ]  
    return MCFileCollection(  mcfs , gd, warn = False)


def cmssm_mn_boxes_N_combined_histo_dict(N) :
    d= {
        "FileName"          : "%s/cmssm_all_boxes_N_combined.root" % (boxes_N_directory(N),  ),
        "PredictionIndex"   : 10,
        "SpectrumIndex"     : 74,
        "Inputs"            : 7, 
        "ModelFile"         : "models/mc7.model",
#        "MinChi2"           : 0,
#        "MaxChi2"           : 45, 
        "MinContrib"        : 0,
     }
    d.update(standard_names())
    return d

def cmssm_mn_boxes_N_combined_histo(N) :
    return [MCFile(cmssm_mn_boxes_N_combined_histo_dict(N) )]


##########################################################################################

def cmssm_multinest_all_sessions_comb_input() :
    # output / global options
    gd = cmssm_multinest_all_sessions_comb_histo_dict()
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 50000

    fd = {
             "FileName"          : "%s/cmssm_all_boxes_combined.root" % boxes_directory(),
             "Chi2TreeName"      : "tree",
         }
    fd1= {
             "FileName"          : "%s/cmssm_all_boxes_N_combined.root" % boxes_N_directory(1),
             "Chi2TreeName"      : "tree",
         }
    fd2= {
             "FileName"          : "%s/cmssm_all_boxes_N_combined.root" % boxes_N_directory(2),
             "Chi2TreeName"      : "tree",
         }
#    fd3= {
#             "FileName"          : "%s/cmssm_all_boxes_N_combined.root" % boxes_N_directory(3),
#             "Chi2TreeName"      : "tree",
#         }
#    mcfs = [MCFile( fdict, warn = False ) in [fd, fd1 ,fd2,fd3 ]] 
    mcfs = [MCFile( fdict, warn = False ) for fdict in [fd, fd1 ,fd2, ]] 
    return MCFileCollection( mcfs , gd, warn = False)


def cmssm_multinest_all_sessions_comb_histo_dict() :
    d= {
        "FileName"          : "%s/cmssm_multinest_all_med_sessions_comb.root" % base_directory(),
        "PredictionIndex"   : 10,
        "SpectrumIndex"     : 74,
        "Inputs"            : 7, 
        "ModelFile"         : "models/mc7.model",
#        "MinChi2"           : 0,
#        "MaxChi2"           : 45, 
        "MinContrib"        : 0,
     }
    d.update(standard_names())
    return d

def cmssm_multinest_all_sessions_comb_histo() :
    return [MCFile(cmssm_multinest_all_sessions_comb_histo_dict() )]


##########################################################################################
