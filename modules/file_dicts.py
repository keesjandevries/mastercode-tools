import getpass
import socket

from commands import getoutput
from modules.mcfile import MCFileCollection
from modules.mcfile import MCFile

def base_directory() :
    user = getpass.getuser()
    fqdn = socket.getfqdn()

    imperial_users = { "sr505"  : "/vols/cms03/mastercode/test_files/",
                       "kjd110" : "/vols/cms04/kjd110/mc8/",
                     }
    imperial_hosts = [ "lx0%d.hep.ph.ic.ac.uk" % node for node in range(4,7) ] + ["heppc52.hep.ph.ic.ac.uk", "heppc157.hep.ph.ic.ac.uk","heppc101.hep.ph.ic.ac.uk" ]

    d = {
            "localhost.localdomain" :  {
                    "hyper"  : "~/Documents/01_mastercode_data/",
                },
        }

    d.update( dict.fromkeys(imperial_hosts, imperial_users) )
#    return d[fqdn][user]
    return "/vols/cms04/kjd110/mc8/"

def cmssm_test_input_files() :
    # output / global options
    gd = cmssm_test_file_histo_dict()
#    gd["StartEntry"] = 100000
#    gd["EndEntry"]   = 101000

    # input files: 1 dict per file
    fd0 = {
             "FileName"          : "%s/cmssm_test.root" % base_directory(),
#             "FileName"          : "%s/cmssm_test_KO.root" % base_directory(),
#             "FileName"          : "%s/cmssm_combine_sampling_KO.root" % base_directory(),
    #         "FileName"          : "/vols/cms03/kjd110/May2012-cmssm-mh125/dm_cmssm_mh125_May2012.root" ,
             "Chi2TreeName"      : "tree",
         }
    fd1 = {
             "FileName"          : "%s/cmssm_SuFla_no_bug_selected.root" % base_directory(),
    #         "FileName"          : "/vols/cms03/kjd110/May2012-cmssm-mh125/dm_cmssm_mh125_May2012.root" ,
             "Chi2TreeName"      : "tree",
         }
    fd2= {
             "FileName"          : "/vols/cms03/kjd110/dm-ab-output-SuFla-resampling-cmssm/dm_ab_cmssm_SuFla_selected_the_rest.root",
    #         "FileName"          : "/vols/cms03/kjd110/May2012-cmssm-mh125/dm_cmssm_mh125_May2012.root" ,
             "Chi2TreeName"      : "chi2tree",
         }
    fd3= {
             "FileName"          : "/vols/cms03/kjd110/dm-ab-output-SuFla-resampling-cmssm/dm_ab_cmssm_SuFla_selected_1000.root",
    #         "FileName"          : "/vols/cms03/kjd110/May2012-cmssm-mh125/dm_cmssm_mh125_May2012.root" ,
             "Chi2TreeName"      : "chi2tree",
         }
    fd4= {
             "FileName"          : "/vols/cms03/kjd110/dm-ab-output-SuFla-resampling-cmssm/dm_ab_cmssm_SuFla_selected_1.root",
    #         "FileName"          : "/vols/cms03/kjd110/May2012-cmssm-mh125/dm_cmssm_mh125_May2012.root" ,
             "Chi2TreeName"      : "chi2tree",
         }
    fd5= {
             "FileName"          : "/vols/cms03/kjd110/dm-ab-output-SuFla-resampling-cmssm/dm_ab_cmssm_SuFla_triangle.root",
    #         "FileName"          : "/vols/cms03/kjd110/May2012-cmssm-mh125/dm_cmssm_mh125_May2012.root" ,
             "Chi2TreeName"      : "tree",
         }
    fd6= {
             "FileName"          : "/vols/cms04/kjd110/mc8/cmssm_mc8_all.root",
             "Chi2TreeName"      : "tree",
         }
    fd7= {
             #"FileName"          : "/vols/cms03/kjd110/June2012-cmssm-mh125-bsmm/June2012-cmssm-mh125-bsmm.root",
             "FileName"          : "/vols/cms03/kjd110/June2012-cmssm-mh125-bsmm/dm_June2012-cmssm-mh125-bsmmBUGGED.root",
             "Chi2TreeName"      : "tree",
         }
    #mcfs = [MCFile( fd, warn = False ) for fd in [fd3 ,fd2,fd4,fd1,fd5]] # dont warn us on missing attributes as they're handled by MCFC
    mcfs = [MCFile( fd, warn = False ) for fd in [fd0]] # dont warn us on missing attributes as they're handled by MCFC
#    mcfs = [MCFile( fd, warn = False ) for fd in [fd7]] # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection(  mcfs, gd, warn = False)

def nuhm1_test_input_files() :
    gd = nuhm1_test_file_histo_dict()
    fd0 = {
#             "FileName"          : "%s/nuhm1_large_test.root" % base_directory(),
             "FileName"          : "%s/nuhm1_combine_sampling_KO.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    fd1= {
             "FileName"          : "/vols/cms03/kjd110/dm-ab-output-SuFla-resampling-nuhm1/dm_ab_nuhm1_SuFla_lowtanb_lowMA.root" ,
             "Chi2TreeName"      : "tree",
         }
    fd2= {
             "FileName"          : "/vols/cms03/kjd110/dm-ab-output-SuFla-resampling-nuhm1/dm_ab_nuhm1_SuFla_selected_the_rest.root",
             "Chi2TreeName"      : "chi2tree",
         }
    fd3= {
             "FileName"          : "/vols/cms03/kjd110/dm-ab-output-SuFla-resampling-nuhm1/dm_ab_nuhm1_SuFla_lowtanb.root",
             "Chi2TreeName"      : "tree",
         }
    fd4= {
             "FileName"          : "%s/nuhm1_from_cmssm.root" % base_directory(),
             "Chi2TreeName"      : "chi2tree",
         }
#    mcfs = [MCFile( fd, warn = False ) for fd in [fd2,fd1,fd3,fd4]] # dont warn us on missing attributes as they're handled by MCFC
    mcfs = [MCFile( fd, warn = False ) for fd in [fd0]] # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection(  mcfs, gd, warn = False)

def cmssm_mcmh_mh125_input() :
    # output / global options
    gd = cmssm_mcmh_mh125_histo_dict()
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 50000

    # input files: 1 dict per file
    fd = {
#             "FileName"          : "%s/cmssm_combine_sampling.root" % base_directory(),
             "FileName"          : "%s/cmssm_combine_sampling_KO.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)

def cmssm_SuFla_no_bug_selected_input() :
    # output / global options
    gd = cmssm_SuFla_no_bug_selected_histo_dict()
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 2357

    # input files: 1 dict per file
    fd = {
             "FileName"          : "%s/cmssm_for_resampling.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)

def cmssm_SuFla_triangle_input() :
    # output / global options
    gd = cmssm_SuFla_triangle_histo_dict()
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 2357

    # input files: 1 dict per file
    fd = {
             "FileName"          : "%s/cmssm_for_resampling.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)

def cmssm_SuFla_selected_input() :
    # output / global options
    gd = cmssm_SuFla_selected_histo_dict()
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 2357

    # input files: 1 dict per file
    fd = {
             "FileName"          : "%s/cmssm_for_resampling.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)

def cmssm_pre_lhc_input() :
    # output / global options
    gd = cmssm_pre_lhc_histo_dict()
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 50000

    # input files: 1 dict per file
    fd = {
#             "FileName"          : "%s/cmssm_combine_sampling.root" % base_directory(),
             "FileName"          : "%s/cmssm_pre_lhc_temp_in.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)

def nuhm1_pre_lhc_input() :
    # output / global options
    gd = nuhm1_pre_lhc_histo_dict()
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 50000

    # input files: 1 dict per file
    fd = {
#             "FileName"          : "%s/cmssm_combine_sampling.root" % base_directory(),
             "FileName"          : "%s/nuhm1_pre_lhc_including_cmssm_KO_50_7_14.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)

def cmssm_mcmh_mc7_input() :
    # output / global options
    gd = cmssm_mcmh_mc7_histo_dict()
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 50000

    # input files: 1 dict per file
    fd = {
#             "FileName"          : "%s/cmssm_combine_sampling.root" % base_directory(),
             "FileName"          : "%s/cmssm_combine_sampling_KO.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)


def cmssm_mc8_drop_atlas_input() :
    # output / global options
    gd = cmssm_mc8_drop_atlas_histo_dict()
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 50000

    # input files: 1 dict per file
    fd = {
             "FileName"          : "%s/cmssm_combine_sampling.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)

def cmssm_mc8_drop_bsmm_input() :
    # output / global options
    gd = cmssm_mc8_drop_bsmm_histo_dict()
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 50000

    # input files: 1 dict per file
    fd = {
             "FileName"          : "%s/cmssm_combine_sampling.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)

def cmssm_combine_sampling_input() :
    # output / global options
    gd = cmssm_combine_sampling_histo_dict()
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 50000

    # input files: 1 dict per file
    fd1 = {
             "FileName"          : "/vols/cms03/kjd110/Mar2012-CMSSM-AB-output/dm_aab_force_out.root",
             "Chi2TreeName"      : "tree",
         }
    fd2= { 
             "FileName"          : "/vols/cms03/kjd110/June2012-cmssm-mh125-bsmm/dm_June2012-cmssm-mh125-bsmm.root",  
             "Chi2TreeName"      : "tree",
         }
    fd3= {
             "FileName"          : "/vols/cms03/kjd110/June2012-cmssm-mh125-bsmm-holes/dm_June2012-cmssm-mh125-bsmm-holes.root",
             "Chi2TreeName"      : "tree",
         }
    fd4= {
             "FileName"          : "/vols/cms03/kjd110/June2012-cmssm-mh125-bsmm-holes-no-g2/dm_June2012-cmssm-mh125-bsmm-holes-no-g2.root",
             "Chi2TreeName"      : "tree",
         }
    fd5= {
             "FileName"          : "/vols/cms03/kjd110/June2012-cmssm-mh125/dm_June2012_cmssm_mh125.root",  
             "Chi2TreeName"      : "tree",
         }
    fd6= {
             "FileName"          : "/vols/cms03/kjd110/May2012-cmssm-mh125/dm_cmssm_mh125_May2012.root" ,  
             "Chi2TreeName"      : "tree",
         }
    fd7= {
             "FileName"          : "/vols/cms03/kjd110/June2012-cmssm-mh125-bsmm-pre-Gino-fix-last/dm_June2012-cmssm-mh125-bsmm-pre-Gino-fix-last.root", 
             "Chi2TreeName"      : "tree",
         }
    
    fd8 = {
             "FileName"          : "%s/cmssm_SuFla_no_bug_selected.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    fd9= {
             "FileName"          : "/vols/cms03/kjd110/dm-ab-output-SuFla-resampling-cmssm/dm_ab_cmssm_SuFla_selected_the_rest.root",
             "Chi2TreeName"      : "chi2tree",
         }
    fd10={
             "FileName"          : "/vols/cms03/kjd110/dm-ab-output-SuFla-resampling-cmssm/dm_ab_cmssm_SuFla_selected_1000.root",
             "Chi2TreeName"      : "chi2tree",
         }
    fd11={
             "FileName"          : "/vols/cms03/kjd110/dm-ab-output-SuFla-resampling-cmssm/dm_ab_cmssm_SuFla_selected_1.root",
             "Chi2TreeName"      : "chi2tree",
         }
    fd13={
             "FileName"          : "/vols/cms03/kjd110/dm-ab-output-SuFla-resampling-cmssm/dm_ab_cmssm_SuFla_triangle.root",
             "Chi2TreeName"      : "tree",
         }
#    mcfs= [MCFile( fd,warn = False ) for fd in [fd1, fd2, fd3, fd4, fd5, fd6 ]] # dont warn us on missing attributes as they're handled by MCFC
#    mcfs= [MCFile( fd,warn = False ) for fd in [fd1, fd2, fd3, fd4, fd5, fd6,fd7 ]] 
    mcfs= [MCFile( fd,warn = False ) for fd in [fd8, fd9, fd10, fd11,  fd13 ]] 
    return MCFileCollection(  mcfs, gd, warn = False)

def cmssm_mc8_drop_mh_input() :
    # output / global options
    gd = cmssm_mc8_drop_mh_histo_dict()
    fd = {
#             "FileName"          : "%s/cmssm_combine_sampling.root" % base_directory(),
             "FileName"          : "%s/cmssm_combine_sampling_KO.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)

def cmssm_mc8_all_Xenon2012LogUnc_input() :
    # output / global options
    gd = cmssm_mc8_all_Xenon2012LogUnc_histo_dict()
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 50000

    # input files: 1 dict per file
    fd = {
#             "FileName"          : "%s/cmssm_combine_sampling.root" % base_directory(),
             "FileName"          : "%s/cmssm_combine_sampling_KO.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)

def cmssm_mc8_Nov12_bsmm_no_g2_input() :
    # output / global options
    gd = cmssm_mc8_Nov12_bsmm_no_g2_histo_dict()
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 50000

    # input files: 1 dict per file
    fd = {
             "FileName"          : "%s/cmssm_combine_sampling.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)

def cmssm_mc8_HCP12_bsmm_input() :
    # output / global options
    gd = cmssm_mc8_HCP12_bsmm_histo_dict()
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 50000

    # input files: 1 dict per file
    fd = {
             "FileName"          : "%s/cmssm_combine_sampling.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)

def cmssm_mc8_Nov12_bsmm_input() :
    # output / global options
    gd = cmssm_mc8_Nov12_bsmm_histo_dict()
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 50000

    # input files: 1 dict per file
    fd = {
             "FileName"          : "%s/cmssm_combine_sampling.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)

def cmssm_mc8_all_input() :
    # output / global options
    gd = cmssm_mc8_all_histo_dict()
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 50000

    # input files: 1 dict per file
    fd = {
             "FileName"          : "%s/cmssm_combine_sampling.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)

def cmssm_mc8_drop_Xenon2012_input() :
    # output / global options
    gd = cmssm_mc8_drop_Xenon2012_histo_dict()
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 50000

    # input files: 1 dict per file
    fd = {
             "FileName"          : "%s/cmssm_combine_sampling.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)

#def nuhm1_test_input() :
#    gd = nuhm1_test_histo_dict()
##    gd["StartEntry"] = 16737459     # 16385171: ./Point.py -c "mA0=300" "tanb=20"on MC8 all
##    gd["EndEntry"]   = 16737460
#    fd = {
#             "FileName"          : "%s/nuhm1_combine_sampling_KO.root" % base_directory(),
##             "FileName"          : "%s/nuhm1_combine_sampling.root" % base_directory(),
#             "Chi2TreeName"      : "tree",
#         }
#    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
#    return MCFileCollection( [ mcf ], gd, warn = False)

def nuhm1_combine_sampling_input() :
    gd = nuhm1_combine_sampling_histo_dict()
#    gd["StartEntry"] = 754260      # 16385171: ./Point.py -c "mA0=300" "tanb=20"on MC8 all
#    gd["EndEntry"]   = 754280
    fd1 = {
             "FileName"          : "/vols/cms03/kjd110/Mar2012-NUHM1-AB-output/dm_aab_force_out.root" ,
             "Chi2TreeName"      : "tree",
         }
    fd2 = {
             "FileName"          : "/vols/cms03/kjd110/Apr-2012-NUHM1-mh125-sampling/dm_apr25-kees-sampling.root",
             "Chi2TreeName"      : "tree",
         }
    fd3 = {
             "FileName"          : "/vols/cms03/kjd110/Apr-2012-NUHM1-mh125-sampling/dm_mh118.root" ,
             "Chi2TreeName"      : "tree",
         }
    fd4 = {
             "FileName"          : "/vols/cms03/kjd110/Apr-2012-NUHM1-mh125-sampling/dm_mh121.root" ,
             "Chi2TreeName"      : "tree",
         }
    fd5 = {
             "FileName"          : "/vols/cms03/kjd110/Apr-2012-NUHM1-mh125-sampling/dm_mh123.root" ,
             "Chi2TreeName"      : "tree",
         }
    fd6 = {
             "FileName"          : "/vols/cms03/kjd110/June-2012-nuhm1-mh125-bsmm-bf/dm_June-2012-nuhm1-mh125-bsmm-bf.root",
             "Chi2TreeName"      : "tree",
         }
    fd7 = {
             "FileName"          : "/vols/cms03/kjd110/June-2012-nuhm1-mh125-bsmm/dm_June-2012-nuhm1-mh125-bsmm.root",
             "Chi2TreeName"      : "tree",
         }
    fd8 = {
             "FileName"          : "/vols/cms03/kjd110/June-2012-nuhm1-mh125-bsmm-no-g2/dm_June-2012-nuhm1-mh125-bsmm-no-g2.root",
             "Chi2TreeName"      : "tree",
         }
#    fd9 = {
#             "FileName"          : "/vols/cms03/kjd110/June-2012-nuhm1-from-cmssm/dm_June-2012-nuhm1-from-cmssm.root" ,
#             "Chi2TreeName"      : "tree",
#         }
#    fd10= {
#             "FileName"          : "/vols/cms03/kjd110/June-2012-nuhm1-from-cmssm/dm_mc7_sampling_nuhm1_from_cmssm.root",
#             "Chi2TreeName"      : "tree",
#         }
    fd11= {
             "FileName"          : "/vols/cms03/kjd110/June-2012-nuhm1-mh125-bsmm-pre-Gino-fix-last/dm_June-2012-nuhm1-mh125-bsmm-pre-Gino-fix-last.root",
             "Chi2TreeName"      : "tree",
         }
    ############################################################################################################# After -Gino's fix
    fd21= {
             "FileName"          : "/vols/cms03/kjd110/dm-ab-output-SuFla-resampling-nuhm1/dm_ab_nuhm1_SuFla_lowtanb_lowMA.root" ,
             "Chi2TreeName"      : "tree",
         }
    fd22= {
             "FileName"          : "/vols/cms03/kjd110/dm-ab-output-SuFla-resampling-nuhm1/dm_ab_nuhm1_SuFla_selected_the_rest.root",
             "Chi2TreeName"      : "chi2tree",
         }
    fd23= {
             "FileName"          : "/vols/cms03/kjd110/dm-ab-output-SuFla-resampling-nuhm1/dm_ab_nuhm1_SuFla_lowtanb.root",
             "Chi2TreeName"      : "tree",
         }
    fd24= {
             "FileName"          : "%s/nuhm1_from_cmssm.root" % base_directory(),
             "Chi2TreeName"      : "chi2tree",
         }
#    mcf = [MCFile( fd, warn = False ) for fd in [fd1,fd2,fd3,fd4,fd5,fd6,fd7,fd8,fd9,fd10]]
    #mcf = [MCFile( fd, warn = False ) for fd in [fd1,fd2,fd3,fd4,fd5,fd6,fd7,fd8,fd11]]
    mcf = [MCFile( fd, warn = False ) for fd in [fd21,fd22,fd23,fd24]]
    return MCFileCollection(  mcf , gd, warn = False)

def nuhm1_mcmh_mh125_input() :
    gd = nuhm1_mcmh_mh125_histo_dict()
#    gd["StartEntry"] = 208280
#    gd["EndEntry"]   = 208295
    fd = {
#             "FileName"          : "%s/nuhm1_combine_sampling.root" % base_directory(),
             "FileName"          : "%s/nuhm1_combine_sampling_KO.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)

def nuhm1_mc8_drop_atlas_input() :
    gd = nuhm1_mc8_drop_atlas_histo_dict()
#    gd["StartEntry"] = 0      
#    gd["EndEntry"]   = 2 
    fd = {
             "FileName"          : "%s/nuhm1_combine_sampling.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)

def nuhm1_mc8_drop_bsmm_input() :
    gd = nuhm1_mc8_drop_bsmm_histo_dict()
#    gd["StartEntry"] = 0      
#    gd["EndEntry"]   = 208295 
#    gd["EndEntry"]   = 2 
    fd = {
             "FileName"          : "%s/nuhm1_combine_sampling.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)

def nuhm1_mc8_all_Xenon2012LogUnc_input() :
    gd = nuhm1_mc8_all_Xenon2012LogUnc_histo_dict()
#    gd["StartEntry"] = 0      
#    gd["EndEntry"]   = 208295 
    fd = {
             "FileName"          : "%s/nuhm1_combine_sampling_KO.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)

def nuhm1_mc8_region_c_char_nlsp_input() :
    gd = nuhm1_mc8_region_c_char_nlsp_histo_dict()
#    gd["StartEntry"] = 0      
#    gd["EndEntry"]   = 1      
    fd = {
             "FileName"          : "%s/nuhm1_mc8_region_c.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)


def nuhm1_mc8_region_c_input() :
    gd = nuhm1_mc8_region_c_histo_dict()
#    gd["StartEntry"] = 0      
#    gd["EndEntry"]   = 208295 
    fd = {
             "FileName"          : "%s/nuhm1_combine_sampling.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)

def nuhm1_mc8_all_input() :
    gd = nuhm1_mc8_all_histo_dict()
#    gd["StartEntry"] = 0      
#    gd["EndEntry"]   = 208295 
    fd = {
             "FileName"          : "%s/nuhm1_combine_sampling.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)


def nuhm1_mc8_Nov12_bsmm_no_g2_input() :
    gd = nuhm1_mc8_Nov12_bsmm_no_g2_histo_dict()
#    gd["StartEntry"] = 0      
#    gd["EndEntry"]   = 208295 
    fd = {
             "FileName"          : "%s/nuhm1_combine_sampling.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)

def nuhm1_mc8_HCP12_bsmm_input() :
    gd = nuhm1_mc8_HCP12_bsmm_histo_dict()
#    gd["StartEntry"] = 0      
#    gd["EndEntry"]   = 208295 
    fd = {
             "FileName"          : "%s/nuhm1_combine_sampling.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)

def nuhm1_mc8_Nov12_bsmm_input() :
    gd = nuhm1_mc8_Nov12_bsmm_histo_dict()
#    gd["StartEntry"] = 0      
#    gd["EndEntry"]   = 208295 
    fd = {
             "FileName"          : "%s/nuhm1_combine_sampling.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)

def nuhm1_mc8_drop_Xenon2012_input() :
    gd = nuhm1_mc8_drop_Xenon2012_histo_dict()
#    gd["StartEntry"] = 0      
#    gd["EndEntry"]   = 208295 
    fd = {
             "FileName"          : "%s/nuhm1_combine_sampling.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)

def nuhm1_mc8_drop_mh_input() :
    gd = nuhm1_mc8_drop_mh_histo_dict()
#    gd["StartEntry"] = 0      
#    gd["EndEntry"]   = 208295 
    fd = {
             "FileName"          : "%s/nuhm1_combine_sampling.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)

def nuhm1_bsmm2012_input() :
    gd = nuhm1_bsmm2012_histo_dict()
#    gd["StartEntry"] = 208280
#    gd["EndEntry"]   = 208295
    fd = {
             "FileName"          : "%s/nuhm1_combine_sampling.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)

def nuhm1_SuFla_no_bug_selected_input() :
    gd = nuhm1_SuFla_no_bug_selected_histo_dict()
#    gd["StartEntry"] = 208288
    #gd["EndEntry"]   = 20000
    fd = {
             "FileName"          : "%s/nuhm1_for_resampling.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)

def nuhm1_SuFla_lowtanb_input() :
    gd = nuhm1_SuFla_lowtanb_histo_dict()
#    gd["StartEntry"] = 208288
    #gd["EndEntry"]   = 20000
    fd = {
             "FileName"          : "%s/nuhm1_for_resampling.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)

def nuhm1_SuFla_selected_input() :
    gd = nuhm1_SuFla_selected_histo_dict()
#    gd["StartEntry"] = 208288
    #gd["EndEntry"]   = 20000
    fd = {
             "FileName"          : "%s/nuhm1_for_resampling.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)

def nuhm1_mcmh_mc7_input() :
    gd = nuhm1_mcmh_mc7_histo_dict()
#    gd["StartEntry"] = 208288
#    gd["EndEntry"]   = 208290
    fd = {
             "FileName"          : "%s/nuhm1_combine_sampling.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)

###############
# histo files #
###############
def cmssm_test_file_histo_dict() :
    return {
#        "FileName"          : "%s/recalc_out.root" % base_directory(),
#        "FileName"          : "%s/recalc_out_KO_mc8.root" % base_directory(),
#        "FileName"          : "%s/recalc_out_KO_mc8_ssiplot.root" % base_directory(),
#        "FileName"          : "%s/recalc_out_KO_mc7.root" % base_directory(),
        "FileName"          : "%s/recalc_out_KO.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 10,
#        "SpectrumIndex"     : 124,
#        "SpectrumIndex"     : 122,
        "SpectrumIndex"     : 117,
#        "SpectrumIndex"     : 74,
        "Inputs"            :  7, # FIXME: check this number is right!!!
#        "LHoodFile"         : "models/mc8-all.lhood" ,
        "ModelFile"         : "models/mc8.model" ,

#        "LHoodFile"         : "models/test.lhood" ,
#        "ModelFile"         : "models/test.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "MinChi2"           : 0,
        "MaxChi2"           : 1e9,
        "MinContrib"        : 0,
     }
def cmssm_test_file_histo() :
    return [MCFile( cmssm_test_file_histo_dict() )]

def nuhm1_test_file_histo_dict() :
    return {
#        "FileName"          : "%s/nuhm1_recalc_out.root" % base_directory(),
#        "FileName"          : "%s/nuhm1_recalc_out_KO_mc8.root" % base_directory(),
        "FileName"          : "%s/nuhm1_recalc_out_KO_mc8_ssiplot.root" % base_directory(),
        "Chi2TreeName"      : "tree",
#        "Chi2TreeName"      : "chi2tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 12,
        "SpectrumIndex"     : 126,
#        "SpectrumIndex"     : 119,
        "Inputs"            : 8, # FIXME: check this number is right!!!
#        "LHoodFile"         : "models/tester.lhood" ,
#        "ModelFile"         : "models/tester.model" ,
#        "LHoodFile"         : "models/mc8-all.lhood" ,
        "LHoodFile"         : "models/mc8-all.lhood",
        "ModelFile"         : "models/mc8.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "MaxMADiff"         : 0.45,
#       "SurgicalAmputation": True,
        "MinChi2"           : 0,
        "MaxChi2"           : 45,
        "MinContrib"        : 0,
     }
def nuhm1_test_file_histo() :
    return [MCFile( nuhm1_test_file_histo_dict() )]

def cmssm_mcmh_mh125_histo_dict() :
    return {
#        "FileName"          : "%s/cmssm_mcmh_mh125.root" % base_directory(),
        "FileName"          : "%s/cmssm_mcmh_mh125_ssi.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 10,
#        "SpectrumIndex"     : 117,
        "SpectrumIndex"     : 124,
        "Inputs"            : 7, # FIXME: check this number is right!!!
        "LHoodFile"         : "models/mc7.lhood",
        "ModelFile"         : "models/mcmh-mh125.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "MinChi2"           : 0,
#        "MaxChi2"           : 1e9,
        "MaxChi2"           : 45.,
        "MinContrib"        : 0,
        "MaxMADiff"         : 0.4,
     }
def cmssm_mcmh_mh125_histo() :
    return [MCFile(cmssm_mcmh_mh125_histo_dict() )]

def cmssm_SuFla_no_bug_selected_histo_dict() :
    return {
        "FileName"          : "%s/cmssm_SuFla_no_bug_selected.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 10,
        "SpectrumIndex"     : 117,
        "Inputs"            : 7, # FIXME: check this number is right!!!
        "ModelFile"         : "models/mc7.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "SelectSuFlaNoneBugPoints": True,
        "MinChi2"           : 0,
        "MaxChi2"           : 1e9,
        "MinContrib"        : 0,
     }
def cmssm_SuFla_no_bug_selected_histo() :
    return [MCFile(cmssm_SuFla_no_bug_selected_histo_dict() )]

def cmssm_SuFla_triangle_histo_dict() :
    return {
        "FileName"          : "%s/cmssm_SuFla_triangle.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 10,
        "SpectrumIndex"     : 117,
        "Inputs"            : 7, # FIXME: check this number is right!!!
        "ModelFile"         : "models/mc7.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "SelectSuFlaCMSSMLowerTrianglePoints": True,
        "MinChi2"           : 0,
        "MaxChi2"           : 1e9,
        "MinContrib"        : 0,
     }
def cmssm_SuFla_triangle_histo() :
    return [MCFile(cmssm_SuFla_triangle_histo_dict() )]

def cmssm_SuFla_selected_histo_dict() :
    return {
        "FileName"          : "%s/cmssm_SuFla_selected.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 10,
        "SpectrumIndex"     : 117,
        "Inputs"            : 7, # FIXME: check this number is right!!!
        "ModelFile"         : "models/mc7.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "SelectSuFlaBugPoints": True,
        "MinChi2"           : 0,
        "MaxChi2"           : 1e9,
        "MinContrib"        : 0,
     }
def cmssm_SuFla_selected_histo() :
    return [MCFile(cmssm_SuFla_selected_histo_dict() )]

def cmssm_pre_lhc_histo_dict() :
    return {
        "FileName"          : "%s/cmssm_pre_lhc.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 10,
#        "SpectrumIndex"     : 117,
        "SpectrumIndex"     : 124,
        "Inputs"            : 7, # FIXME: check this number is right!!!
        "ModelFile"         : "models/mc7.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "MinChi2"           : 0,
        "MaxChi2"           : 1e9,
#        "MaxChi2"           : 45.,
        "MinContrib"        : 0,
     }
def cmssm_pre_lhc_histo() :
    return [MCFile(cmssm_pre_lhc_histo_dict() )]

def cmssm_mcmh_mc7_histo_dict() :
    return {
        "FileName"          : "%s/cmssm_mcmh_mc7.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 10,
#        "SpectrumIndex"     : 117,
        "SpectrumIndex"     : 124,
        "Inputs"            : 7, # FIXME: check this number is right!!!
        "LHoodFile"         : "models/mc7.lhood" ,
        "ModelFile"         : "models/mc7.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "MinChi2"           : 0,
        "MaxChi2"           : 1e9,
#        "MaxChi2"           : 45.,
        "MinContrib"        : 0,
     }
def cmssm_mcmh_mc7_histo() :
    return [MCFile(cmssm_mcmh_mc7_histo_dict() )]

def cmssm_mc8_drop_bsmm_histo_dict() :
    return {
        "FileName"          : "%s/cmssm_mc8_drop_bsmm.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 10,
        "SpectrumIndex"     : 117,
        "Inputs"            : 7, # FIXME: check this number is right!!!
        "LHoodFile"         : "models/mc8-drop_bsmm.lhood" ,
        "ModelFile"         : "models/mc8.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "MinChi2"           : 0,
#        "MaxChi2"           : 50, 
        "MaxChi2"           : 45.,
        "MinContrib"        : 0,
#        "MaxMADiff"         : 0.4,
     }
def cmssm_mc8_drop_bsmm_histo() :
    return [MCFile(cmssm_mc8_drop_bsmm_histo_dict() )]

def cmssm_mc8_drop_atlas_histo_dict() :
    return {
        "FileName"          : "%s/cmssm_mc8_drop_atlas.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 10,
        "SpectrumIndex"     : 117,
        "Inputs"            : 7, # FIXME: check this number is right!!!
        "LHoodFile"         : "models/mc8-drop_atlas.lhood" ,
        "ModelFile"         : "models/mc8.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "MinChi2"           : 0,
#        "MaxChi2"           : 50, 
        "MaxChi2"           : 45.,
        "MinContrib"        : 0,
#        "MaxMADiff"         : 0.4,
     }
def cmssm_mc8_drop_atlas_histo() :
    return [MCFile(cmssm_mc8_drop_atlas_histo_dict() )]

def cmssm_mc8_all_Xenon2012LogUnc_histo_dict() :
    return {
        "FileName"          : "%s/cmssm_mc8_all_Xenon2012LogUnc.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 10,
#        "SpectrumIndex"     : 117,
        "SpectrumIndex"     : 124,
        "Inputs"            : 7, # FIXME: check this number is right!!!
        "LHoodFile"         : "models/mc8-all_Xenon2012LogUnc.lhood" ,
        "ModelFile"         : "models/mc8.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "MinChi2"           : 0,
        "MaxChi2"           : 45, 
        "MinContrib"        : 0,
    #    "MaxMADiff"         : 0.4,
     }
def cmssm_mc8_all_Xenon2012LogUnc_histo() :
    return [MCFile(cmssm_mc8_all_Xenon2012LogUnc_histo_dict() )]

def cmssm_mc8_Nov12_bsmm_no_g2_histo_dict() :
    return {
        "FileName"          : "%s/cmssm_mc8_Nov12_bsmm_no_g2.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 10,
        "SpectrumIndex"     : 117,
        "Inputs"            : 7, # FIXME: check this number is right!!!
        "LHoodFile"         : "models/mc8-all.lhood" ,
        "ModelFile"         : "models/mc8_bsmm_no_g2_12.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "MinChi2"           : 0,
        "MaxChi2"           : 45, 
        "MinContrib"        : 0,
#        "LongLivedStuaTanbCut": True,
    #    "MaxMADiff"         : 0.4,
     }
def cmssm_mc8_Nov12_bsmm_no_g2_histo() :
    return [MCFile(cmssm_mc8_Nov12_bsmm_no_g2_histo_dict() )]

def cmssm_mc8_HCP12_bsmm_histo_dict() :
    return {
        "FileName"          : "%s/cmssm_mc8_HCP12_bsmm.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 10,
        "SpectrumIndex"     : 117,
        "Inputs"            : 7, # FIXME: check this number is right!!!
        "LHoodFile"         : "models/mc8-HCP12.lhood" ,
        "ModelFile"         : "models/mc8.model",
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "MinChi2"           : 0,
        "MaxChi2"           : 45, 
        "MinContrib"        : 0,
#        "LongLivedStuaTanbCut": True,
    #    "MaxMADiff"         : 0.4,
     }
def cmssm_mc8_HCP12_bsmm_histo() :
    return [MCFile(cmssm_mc8_HCP12_bsmm_histo_dict() )]

def cmssm_mc8_Nov12_bsmm_histo_dict() :
    return {
        "FileName"          : "%s/cmssm_mc8_Nov12_bsmm.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 10,
        "SpectrumIndex"     : 117,
        "Inputs"            : 7, # FIXME: check this number is right!!!
        "LHoodFile"         : "models/mc8-all.lhood" ,
        "ModelFile"         : "models/mc8_bsmm12.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "MinChi2"           : 0,
        "MaxChi2"           : 45, 
        "MinContrib"        : 0,
#        "LongLivedStuaTanbCut": True,
    #    "MaxMADiff"         : 0.4,
     }
def cmssm_mc8_Nov12_bsmm_histo() :
    return [MCFile(cmssm_mc8_Nov12_bsmm_histo_dict() )]

def cmssm_mc8_all_histo_dict() :
    return {
        "FileName"          : "%s/cmssm_mc8_all.root" % base_directory(),
#        "FileName"          : "%s/cmssm_mc8_all_tanb_cut.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 10,
#        "SpectrumIndex"     : 117,
        "SpectrumIndex"     : 124,
        "Inputs"            : 7, # FIXME: check this number is right!!!
        "LHoodFile"         : "models/mc8-all.lhood" ,
        "ModelFile"         : "models/mc8.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "MinChi2"           : 0,
        "MaxChi2"           : 45, 
        "MinContrib"        : 0,
        "LongLivedStuaTanbCut": True,
    #    "MaxMADiff"         : 0.4,
     }
def cmssm_mc8_all_histo() :
    return [MCFile(cmssm_mc8_all_histo_dict() )]

def cmssm_mc8_all_tanb_cut_histo_dict() :
    return {
        "FileName"          : "%s/cmssm_mc8_all_tanb_cut.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 10,
#        "SpectrumIndex"     : 117,
        "SpectrumIndex"     : 124,
        "Inputs"            : 7, # FIXME: check this number is right!!!
        "LHoodFile"         : "models/mc8-all.lhood" ,
        "ModelFile"         : "models/mc8.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "MinChi2"           : 0,
        "MaxChi2"           : 45, 
        "MinContrib"        : 0,
        "LongLivedStuaTanbCut": True,
    #    "MaxMADiff"         : 0.4,
     }
def cmssm_mc8_all_tanb_cut_histo() :
    return [MCFile(cmssm_mc8_all_tanb_cut_histo_dict() )]

def cmssm_mc8_drop_Xenon2012_histo_dict() :
    return {
        "FileName"          : "%s/cmssm_mc8_drop_Xenon2012.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 10,
        "SpectrumIndex"     : 117,
        "Inputs"            : 7, # FIXME: check this number is right!!!
        "LHoodFile"         : "models/mc8-drop_Xenon2012.lhood" ,
        "ModelFile"         : "models/mc8.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "MinChi2"           : 0,
        "MaxChi2"           : 45, 
        "MinContrib"        : 0,
    #    "MaxMADiff"         : 0.4,
     }
def cmssm_mc8_drop_Xenon2012_histo() :
    return [MCFile(cmssm_mc8_drop_Xenon2012_histo_dict() )]

def cmssm_mc8_drop_mh_histo_dict() :
    return {
        "FileName"          : "%s/cmssm_mc8_drop_mh.root" % base_directory(),
#        "FileName"          : "%s/cmssm_mc8_Xenon2012_drop_mh.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 10,
#        "SpectrumIndex"     : 117,
        "SpectrumIndex"     : 124,
        "Inputs"            : 7, # FIXME: check this number is right!!!
#        "LHoodFile"         : "models/mc8-all.lhood" ,
        "LHoodFile"         : "models/mc8-all.lhood",
        "ModelFile"         : "models/mc8-drop_mh.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "MinChi2"           : 30.38,
        "MaxChi2"           : 45.,
        "MinContrib"        : 0,
     }
def cmssm_mc8_drop_mh_histo() :
    return [MCFile(cmssm_mc8_drop_mh_histo_dict() )]

def cmssm_combine_sampling_histo_dict() :
    return {
        "FileName"          : "%s/cmssm_combine_sampling.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 10,
        "SpectrumIndex"     : 117,
        "Inputs"            : 7, # FIXME: check this number is right!!!
#        "LHoodFile"         : "models/mc7.lhood" ,
#        "ModelFile"         : "models/mcmh-mh125.model" ,
        "ModelFile"         : "models/mc7.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "MinChi2"           : 0,
#        "MaxChi2"           : 1e9,
        "MaxChi2"           : 45, 
        "MinContrib"        : 0,
    #    "MaxMADiff"         : 0.4,
     }
def cmssm_combine_sampling_histo() :
    return [MCFile(cmssm_combine_sampling_histo_dict() )]

#def nuhm1_test_histo_dict() :
#    return {
#        "FileName"          : "%s/nuhm1_test.root" % base_directory(),
#        "Chi2TreeName"      : "tree",
#        "Chi2BranchName"    : "vars",
#        "ContribTreeName"   : "contribtree",
#        "ContribBranchName" : "vars",
#        "LHoodTreeName"     : "lhoodtree",
#        "LHoodBranchName"   : "vars",
#        "BestFitEntryName"  : "BestFitEntry",
#        "PredictionIndex"   : 12,
#        "SpectrumIndex"     : 119,
#        "Inputs"            : 8, # FIXME: check this number is right!!!
#        "LHoodFile"         : "models/test.lhood" ,
#        "ModelFile"         : "models/test.model" ,
#        "EntryDirectory"    : "entry_histograms",
#        "DataDirectory"     : "data_histograms",
#        "MinChi2"           : 0,
#        "MaxChi2"           : 1e9,
#        "MinContrib"        : 0,
#        "MaxMADiff"         : 0.5,
#     }
#def nuhm1_test_histo() :
#    return [MCFile(nuhm1_test_histo_dict() )]

def nuhm1_combine_sampling_histo_dict() :
    return {
        "FileName"          : "%s/nuhm1_combine_sampling.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 12,
        "SpectrumIndex"     : 119,
        "Inputs"            : 8, # FIXME: check this number is right!!!
   #     "LHoodFile"         : "models/mc7.lhood",
   #     "ModelFile"         : "models/mcmh-mh125.model" ,
        "ModelFile"         : "models/mc7.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "MinChi2"           : 0,
#        "MaxChi2"           : 1e9 ,
        "MaxChi2"           : 45, 
        "MinContrib"        : 0,
    #    "MaxMADiff"         : 0.45,
#       "SurgicalAmputation": True,
     }
def nuhm1_combine_sampling_histo() :
    return [MCFile(nuhm1_combine_sampling_histo_dict() )]

def nuhm1_mcmh_mh125_histo_dict() :
    return {
#        "FileName"          : "%s/nuhm1_mcmh_mh125.root" % base_directory(),
        "FileName"          : "%s/nuhm1_mcmh_mh125_ssi.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 12,
        "SpectrumIndex"     : 126,
#        "SpectrumIndex"     : 119,
        "Inputs"            : 8, # FIXME: check this number is right!!!
        "LHoodFile"         : "models/mc7.lhood",
        "ModelFile"         : "models/mcmh-mh125.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "MinChi2"           : 0,
#        "MaxChi2"           : 1e9,
        "MaxChi2"           : 45.,
        "MinContrib"        : 0.,
        "MaxMADiff"         : 0.45,
     }
def nuhm1_mcmh_mh125_histo() :
    return [MCFile(nuhm1_mcmh_mh125_histo_dict() )]

def nuhm1_mc8_drop_bsmm_histo_dict() :
    return {
        "FileName"          : "%s/nuhm1_mc8_drop_bsmm.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 12,
        "SpectrumIndex"     : 119,
        "Inputs"            : 8, # FIXME: check this number is right!!!
        "LHoodFile"         : "models/mc8-drop_bsmm.lhood" ,
        "ModelFile"         : "models/mc8.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "MinChi2"           : 0,
#        "MaxChi2"           : 1e9,
        "MaxChi2"           : 45.,
        "MinContrib"        : 0,
        "MaxMADiff"         : 0.45,
     }
def nuhm1_mc8_drop_bsmm_histo() :
    return [MCFile(nuhm1_mc8_drop_bsmm_histo_dict() )]

def nuhm1_mc8_drop_atlas_histo_dict() :
    return {
        "FileName"          : "%s/nuhm1_mc8_drop_atlas.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 12,
        "SpectrumIndex"     : 119,
        "Inputs"            : 8, # FIXME: check this number is right!!!
        "LHoodFile"         : "models/mc8-drop_atlas.lhood" ,
        "ModelFile"         : "models/mc8.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "MinChi2"           : 0,
#        "MaxChi2"           : 1e9,
        "MaxChi2"           : 45.,
        "MinContrib"        : 0,
        "MaxMADiff"         : 0.45,
     }
def nuhm1_mc8_drop_atlas_histo() :
    return [MCFile(nuhm1_mc8_drop_atlas_histo_dict() )]

def nuhm1_mc8_drop_Xenon2012_histo_dict() :
    return {
        "FileName"          : "%s/nuhm1_mc8_drop_Xenon2012.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 12,
        "SpectrumIndex"     : 119,
#        "SpectrumIndex"     : 126,
        "Inputs"            : 8, # FIXME: check this number is right!!!
        "LHoodFile"         : "models/mc8-drop_Xenon2012.lhood" ,
        "ModelFile"         : "models/mc8.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "MinChi2"           : 0,
#        "MaxChi2"           : 1e9,
        "MaxChi2"           : 45.,
        "MinContrib"        : 0,
        "MaxMADiff"         : 0.45,
     }
def nuhm1_mc8_drop_Xenon2012_histo() :
    return [MCFile(nuhm1_mc8_drop_Xenon2012_histo_dict() )]

def nuhm1_mc8_all_Xenon2012LogUnc_histo_dict() :
    return {
        "FileName"          : "%s/nuhm1_mc8_all_Xenon2012LogUnc.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 12,
#        "SpectrumIndex"     : 119,
        "SpectrumIndex"     : 126,
        "Inputs"            : 8, # FIXME: check this number is right!!!
        "LHoodFile"         : "models/mc8-all_Xenon2012LogUnc.lhood" ,
        "ModelFile"         : "models/mc8.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "MinChi2"           : 0,
#        "MaxChi2"           : 1e9,
        "MaxChi2"           : 45.,
        "MinContrib"        : 0,
        "MaxMADiff"         : 0.45,
     }
def nuhm1_mc8_all_Xenon2012LogUnc_histo() :
    return [MCFile(nuhm1_mc8_all_Xenon2012LogUnc_histo_dict() )]

def nuhm1_mc8_Nov12_bsmm_no_g2_histo_dict() :
    return {
        "FileName"          : "%s/nuhm1_mc8_Nov12_bsmm_no_g2.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 12,
        "SpectrumIndex"     : 119,
#        "SpectrumIndex"     : 126,
        "Inputs"            : 8, # FIXME: check this number is right!!!
        "LHoodFile"         : "models/mc8-all.lhood" ,
        "ModelFile"         : "models/mc8_bsmm_no_g2_12.model",
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "MinChi2"           : 0,
#        "MaxChi2"           : 1e9,
        "MaxChi2"           : 45.,
        "MinContrib"        : 0,
        "MaxMADiff"         : 0.45,
     }
def nuhm1_mc8_Nov12_bsmm_no_g2_histo() :
    return [MCFile(nuhm1_mc8_Nov12_bsmm_no_g2_histo_dict() )]

def nuhm1_mc8_HCP12_bsmm_histo_dict() :
    return {
        "FileName"          : "%s/nuhm1_mc8_HCP12_bsmm.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 12,
        "SpectrumIndex"     : 119,
#        "SpectrumIndex"     : 126,
        "Inputs"            : 8, # FIXME: check this number is right!!!
        "LHoodFile"         : "models/mc8-HCP12.lhood" ,
        "ModelFile"         : "models/mc8.model",
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "MinChi2"           : 0,
#        "MaxChi2"           : 1e9,
        "MaxChi2"           : 45.,
        "MinContrib"        : 0,
        "MaxMADiff"         : 0.45,
     }
def nuhm1_mc8_HCP12_bsmm_histo() :
    return [MCFile(nuhm1_mc8_HCP12_bsmm_histo_dict() )]

def nuhm1_mc8_Nov12_bsmm_histo_dict() :
    return {
        "FileName"          : "%s/nuhm1_mc8_Nov12_bsmm.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 12,
        "SpectrumIndex"     : 119,
#        "SpectrumIndex"     : 126,
        "Inputs"            : 8, # FIXME: check this number is right!!!
        "LHoodFile"         : "models/mc8-all.lhood" ,
        "ModelFile"         : "models/mc8_bsmm12.model",
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "MinChi2"           : 0,
#        "MaxChi2"           : 1e9,
        "MaxChi2"           : 45.,
        "MinContrib"        : 0,
        "MaxMADiff"         : 0.45,
     }
def nuhm1_mc8_Nov12_bsmm_histo() :
    return [MCFile(nuhm1_mc8_Nov12_bsmm_histo_dict() )]

def nuhm1_mc8_all_histo_dict() :
    return {
        "FileName"          : "%s/nuhm1_mc8_all.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 12,
#        "SpectrumIndex"     : 119,
        "SpectrumIndex"     : 126,
        "Inputs"            : 8, # FIXME: check this number is right!!!
        "LHoodFile"         : "models/mc8-all.lhood" ,
        "ModelFile"         : "models/mc8.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "MinChi2"           : 0,
#        "MaxChi2"           : 1e9,
        "MaxChi2"           : 45.,
        "MinContrib"        : 0,
        "MaxMADiff"         : 0.45,
     }
def nuhm1_mc8_all_histo() :
    return [MCFile(nuhm1_mc8_all_histo_dict() )]

def nuhm1_mc8_region_c_char_nlsp_histo_dict() :
    return {
        "FileName"          : "%s/nuhm1_mc8_region_c_char_nlsp.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 12,
        "SpectrumIndex"     : 119,
#        "SpectrumIndex"     : 126,
        "Inputs"            : 8, # FIXME: check this number is right!!!
        "LHoodFile"         : "models/mc8-all.lhood" ,
        "ModelFile"         : "models/mc8.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "MinChi2"           : 0,
#        "MaxChi2"           : 1e9,
        "SelectRegionC"     : True,
        "CharginoNLSPCut"   : True, 
        "MaxChi2"           : 45.,
        "MinContrib"        : 0,
        "MaxMADiff"         : 0.45,
     }
def nuhm1_mc8_region_c_char_nlsp_histo() :
    return [MCFile(nuhm1_mc8_region_c_char_nlsp_histo_dict() )]

def nuhm1_mc8_region_c_histo_dict() :
    return {
        "FileName"          : "%s/nuhm1_mc8_region_c.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 12,
        "SpectrumIndex"     : 119,
#        "SpectrumIndex"     : 126,
        "Inputs"            : 8, # FIXME: check this number is right!!!
        "LHoodFile"         : "models/mc8-all.lhood" ,
        "ModelFile"         : "models/mc8.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "MinChi2"           : 0,
#        "MaxChi2"           : 1e9,
        "SelectRegionC"     : True,
        "MaxChi2"           : 45.,
        "MinContrib"        : 0,
        "MaxMADiff"         : 0.45,
     }
def nuhm1_mc8_region_c_histo() :
    return [MCFile(nuhm1_mc8_region_c_histo_dict() )]

def nuhm1_mc8_drop_mh_histo_dict() :
    return {
        "FileName"          : "%s/nuhm1_mc8_drop_mh.root" % base_directory(),
#        "FileName"          : "%s/nuhm1_mc8_Xenon2012_drop_mh.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 12,
        "SpectrumIndex"     : 119,
        "Inputs"            : 8, # FIXME: check this number is right!!!
        "LHoodFile"         : "models/mc8-all.lhood",
        "ModelFile"         : "models/mc8-drop_mh.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "MinChi2"           : 30.4,
        "MaxChi2"           : 45. ,
        "MinContrib"        : 0,
        "MaxMADiff"         : 0.45,
     }
def nuhm1_mc8_drop_mh_histo() :
    return [MCFile(nuhm1_mc8_drop_mh_histo_dict() )]

def nuhm1_bsmm2012_histo_dict() :
    return {
        "FileName"          : "%s/nuhm1_bsmm2012.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 12,
        "SpectrumIndex"     : 119,
        "Inputs"            : 8, # FIXME: check this number is right!!!
        "LHoodFile"         : "models/bsmm-all.lhood" ,
        "ModelFile"         : "models/tester.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "MinChi2"           : 0,
#        "MaxChi2"           : 1e9,
        "MaxChi2"           : 45.,
        "MinContrib"        : 0,
     }
def nuhm1_bsmm2012_histo() :
    return [MCFile(nuhm1_bsmm2012_histo_dict() )]

def nuhm1_pre_lhc_histo_dict() :
    return {
        "FileName"          : "%s/nuhm1_pre_lhc_including_cmssm.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 12,
        "SpectrumIndex"     : 126,
        "Inputs"            : 8, # FIXME: check this number is right!!!
#        "LHoodFile"         : "models/mc7.lhood" ,
        "ModelFile"         : "models/mc7.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "MinChi2"           : 0,
#        "MaxChi2"           : 1e9,
        "MaxChi2"           : 45.,
        "MinContrib"        : 0,
     }
def nuhm1_pre_lhc_histo() :
    return [MCFile(nuhm1_pre_lhc_histo_dict() )]

def nuhm1_SuFla_no_bug_selected_histo_dict() :
    return {
        "FileName"          : "%s/nuhm1_SuFla_no_bug_selected.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 12,
        "SpectrumIndex"     : 119,
        "Inputs"            : 8, # FIXME: check this number is right!!!
        "ModelFile"         : "models/mc7.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "SelectSuFlaNoneBugPoints" : True,
        "MinChi2"           : 0,
        "MaxChi2"           : 1e9,
        "MinContrib"        : 0,
     }
def nuhm1_SuFla_no_bug_selected_histo() :
    return [MCFile(nuhm1_SuFla_no_bug_selected_histo_dict() )]

def nuhm1_SuFla_lowtanb_histo_dict() :
    return {
        "FileName"          : "%s/nuhm1_SuFla_lowtanb.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 12,
        "SpectrumIndex"     : 119,
        "Inputs"            : 8, # FIXME: check this number is right!!!
        "ModelFile"         : "models/mc7.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "SelectSuFlaNUHM1LowTanbPoints": True,
        "MinChi2"           : 0,
        "MaxChi2"           : 1e9,
        "MinContrib"        : 0,
     }
def nuhm1_SuFla_lowtanb_histo() :
    return [MCFile(nuhm1_SuFla_lowtanb_histo_dict() )]

def nuhm1_SuFla_selected_histo_dict() :
    return {
        "FileName"          : "%s/nuhm1_SuFla_selected.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 12,
        "SpectrumIndex"     : 119,
        "Inputs"            : 8, # FIXME: check this number is right!!!
        "ModelFile"         : "models/mc7.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "SelectSuFlaBugPoints": True,
        "MinChi2"           : 0,
        "MaxChi2"           : 1e9,
        "MinContrib"        : 0,
     }
def nuhm1_SuFla_selected_histo() :
    return [MCFile(nuhm1_SuFla_selected_histo_dict() )]

def nuhm1_mcmh_mc7_histo_dict() :
    return {
        "FileName"          : "%s/nuhm1_mcmh_mc7.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 12,
        "SpectrumIndex"     : 119,
        "Inputs"            : 8, # FIXME: check this number is right!!!
        "LHoodFile"         : "models/mc7.lhood" ,
        "ModelFile"         : "models/mc7.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "MinChi2"           : 26.97     ,
        "MaxChi2"           : 45.,
        "MinContrib"        : 0,
     }
def nuhm1_mcmh_mc7_histo() :
    return [MCFile(nuhm1_mcmh_mc7_histo_dict() )]


#####################################################################################
def cmssm_mc8_all_stop_nlsp_input() :
    # output / global options
    gd = cmssm_mc8_all_stop_nlsp_histo_dict()
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 5000

    # input files: 1 dict per file
    fd = {
             "FileName"          : "%s/cmssm_mc8_all_stop_nlsp_input.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)

def cmssm_mc8_all_stop_nlsp_histo_dict() :
    return {
        "FileName"          : "%s/cmssm_mc8_all_stop_nlsp.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 10,
        "SpectrumIndex"     : 117,
        "Inputs"            : 7, # FIXME: check this number is right!!!
        "LHoodFile"         : "models/mc8-all.lhood" ,
        "ModelFile"         : "models/mc8.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "MinChi2"           : 0,
        "MaxChi2"           : 45, 
        "MinContrib"        : 0,
#        "LongLivedStuaTanbCut": True,
    #    "MaxMADiff"         : 0.4,
        'CharginoNLSPCut'   : True, 
     }
def cmssm_mc8_all_stop_nlsp_histo() :
    return [MCFile(cmssm_mc8_all_stop_nlsp_histo_dict() )]


#####################################################################################

def nuhm1_mc8_all_stop_nlsp_input() :
    gd = nuhm1_mc8_all_stop_nlsp_histo_dict()
#    gd["StartEntry"] = 0      
#    gd["EndEntry"]   = 20000 
    fd = {
             "FileName"          : "%s/nuhm1_combine_sampling.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)

def nuhm1_mc8_all_stop_nlsp_histo_dict() :
    return {
        "FileName"          : "%s/nuhm1_mc8_all_stop_nlsp.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 12,
        "SpectrumIndex"     : 119,
#        "SpectrumIndex"     : 126,
        "Inputs"            : 8, # FIXME: check this number is right!!!
        "LHoodFile"         : "models/mc8-all.lhood" ,
        "ModelFile"         : "models/mc8.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "MinChi2"           : 0,
#        "MaxChi2"           : 1e9,
#        "MaxChi2"           : 45.,
        "MinContrib"        : 0,
        "MaxMADiff"         : 0.45,
        'CharginoNLSPCut'   : True, 
     }
def nuhm1_mc8_all_stop_nlsp_histo() :
    return [MCFile(nuhm1_mc8_all_stop_nlsp_histo_dict() )]

#####################################################################################
def cmssm_pre_lhc_drop_mh_input() :
    # output / global options
    gd = cmssm_pre_lhc_drop_mh_histo_dict()
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 50000

    # input files: 1 dict per file
    fd = {
#             "FileName"          : "%s/cmssm_combine_sampling.root" % base_directory(),
             "FileName"          : "%s/cmssm_pre_lhc_temp_in.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)


def cmssm_pre_lhc_drop_mh_histo_dict() :
    return {
        "FileName"          : "%s/cmssm_pre_lhc_drop_mh.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 10,
#        "SpectrumIndex"     : 117,
        "SpectrumIndex"     : 124,
        "Inputs"            : 7, # FIXME: check this number is right!!!
        "ModelFile"         : "models/mc7_drop_mh.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "MinChi2"           : 0,
        "MaxChi2"           : 1e9,
        "MaxChi2"           : 45.,
        "MinContrib"        : 0,
     }
def cmssm_pre_lhc_drop_mh_histo() :
    return [MCFile(cmssm_pre_lhc_drop_mh_histo_dict() )]
#####################################################################################
def nuhm1_pre_lhc_drop_mh_input() :
    # output / global options
    gd = nuhm1_pre_lhc_drop_mh_histo_dict()
#    gd["StartEntry"] = 0
#    gd["EndEntry"]   = 50000

    # input files: 1 dict per file
    fd = {
#             "FileName"          : "%s/nuhm1_combine_sampling.root" % base_directory(),
             "FileName"          : "%s/nuhm1_pre_lhc_including_cmssm_no_KO.root" % base_directory(),
             "Chi2TreeName"      : "tree",
         }
    mcf = MCFile( fd, warn = False ) # dont warn us on missing attributes as they're handled by MCFC
    return MCFileCollection( [ mcf ], gd, warn = False)


def nuhm1_pre_lhc_drop_mh_histo_dict() :
    return {
        "FileName"          : "%s/nuhm1_pre_lhc_drop_mh.root" % base_directory(),
        "Chi2TreeName"      : "tree",
        "Chi2BranchName"    : "vars",
        "ContribTreeName"   : "contribtree",
        "ContribBranchName" : "vars",
        "LHoodTreeName"     : "lhoodtree",
        "LHoodBranchName"   : "vars",
        "BestFitEntryName"  : "BestFitEntry",
        "PredictionIndex"   : 12,
        "SpectrumIndex"     : 119,
#        "SpectrumIndex"     : 126,
        "Inputs"            : 7, # FIXME: check this number is right!!!
        "ModelFile"         : "models/mc7_drop_mh.model" ,
        "EntryDirectory"    : "entry_histograms",
        "DataDirectory"     : "data_histograms",
        "SmoothDirectory"   : "smooth_histograms",
        "MinChi2"           : 0,
        "MaxChi2"           : 1e9,
        "MaxChi2"           : 45.,
        "MinContrib"        : 0,
     }
def nuhm1_pre_lhc_drop_mh_histo() :
    return [MCFile(nuhm1_pre_lhc_drop_mh_histo_dict() )]
