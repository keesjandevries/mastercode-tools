#! /usr/bin/env python
import modules.file_dicts as files
import modules.multinest_files as mn_files

def recalc_files() :
# COMBINATION OF ALL SAMPLING, APPLYING X^2 CUT
#    d = files.cmssm_combine_sampling_input()
#    d = files.nuhm1_combine_sampling_input()
# RESAMPLING 
#    d = files.cmssm_SuFla_selected_input()
#    d = files.cmssm_SuFla_triangle_input()
#    d = files.cmssm_SuFla_no_bug_selected_input()
#    d = files.nuhm1_SuFla_selected_input()
#    d = files.nuhm1_SuFla_lowtanb_input()
#    d = files.nuhm1_SuFla_no_bug_selected_input()
# TEST
#    d = files.cmssm_test_input_files()
#    d = files.nuhm1_test_input()
#    d = files.nuhm1_test_input_files()
# NUHM1
#    d = files.nuhm1_mcmh_mc7_input()
#    d = files.nuhm1_mcmh_mh125_input()
#    d = files.nuhm1_mc8_drop_atlas_input()
#    d = files.nuhm1_mc8_drop_bsmm_input()
#    d = files.nuhm1_mc8_drop_mh_input()
#    d = files.nuhm1_mc8_all_Xenon2012LogUnc_input()
#    d = files.nuhm1_mc8_region_c_input()
#    d = files.nuhm1_mc8_region_c_char_nlsp_input()
#    d = files.nuhm1_mc8_Nov12_bsmm_no_g2_input()
#    d = files.nuhm1_mc8_Nov12_bsmm_input()
#    d = files.nuhm1_mc8_HCP12_bsmm_input()
#    d = files.nuhm1_mc8_all_input()
#CMSSM
#    d = files.cmssm_pre_lhc_input()
#    d = files.cmssm_mcmh_mc7_input()
#    d = files.cmssm_mcmh_mh125_input()
#    d = files.cmssm_mc8_drop_atlas_input()
#    d = files.cmssm_mc8_drop_bsmm_input()
#    d = files.cmssm_mc8_drop_mh_input()
#    d = files.cmssm_mc8_all_Xenon2012LogUnc_input()
#    d = files.cmssm_mc8_Nov12_bsmm_no_g2_input()
#    d = files.cmssm_mc8_Nov12_bsmm_input()
#    d = files.cmssm_mc8_HCP12_bsmm_input()
#    d = files.cmssm_mc8_all_input()
#MULTINEST FILES
#    d = mn_files.cmssm_multinest_first_input()
#    d = mn_files.cmssm_multinest_iters_input(10)
    return d

def recalc_file_list():
#    d = [mn_files.cmssm_multinest_iters_input(i) for i in range(1,11) ]
    d = [mn_files.cmssm_mn_boxes_input(i) for i in range(0,3)]
    return d

def histo_files() :
# TEST
#    d = files.cmssm_test_file_histo()
#    d = files.nuhm1_test_file_histo()
##    d = files.nuhm1_test_histo()
# NUHM1
#    d = files.nuhm1_pre_lhc_histo()
#    d = files.nuhm1_mcmh_mc7_histo()
#    d = files.nuhm1_mcmh_mh125_histo()
#    d = files.nuhm1_mc8_all_histo()
#    d = files.nuhm1_mc8_Nov12_bsmm_histo()
#    d = files.nuhm1_mc8_HCP12_bsmm_histo()
#    d = files.nuhm1_mc8_Nov12_bsmm_no_g2_histo()
#    d = files.nuhm1_mc8_region_c_histo()
#    d = files.nuhm1_mc8_region_c_char_nlsp_histo()
#    d = files.nuhm1_mc8_all_Xenon2012LogUnc_histo()
#    d = files.nuhm1_mc8_drop_mh_histo()
#    d = files.nuhm1_mc8_drop_atlas_histo()
#    d = files.nuhm1_mc8_drop_bsmm_histo()
#    d = files.nuhm1_mc8_drop_Xenon2012_histo()
#CMSSM
#    d = files.cmssm_pre_lhc_histo()
#    d = files.cmssm_mcmh_mc7_histo()
#    d = files.cmssm_mcmh_mh125_histo()
#    d = files.cmssm_mc8_all_histo()
#    d = files.cmssm_mc8_Nov12_bsmm_histo()
#    d = files.cmssm_mc8_HCP12_bsmm_histo()
#    d = files.cmssm_mc8_Nov12_bsmm_no_g2_histo()
#    d = files.cmssm_mc8_all_Xenon2012LogUnc_histo()
#    d = files.cmssm_mc8_drop_mh_histo()
#    d = files.cmssm_mc8_drop_atlas_histo()
#    d = files.cmssm_mc8_drop_bsmm_histo()
#    d = files.cmssm_mc8_drop_Xenon2012_histo()
#MULTINEST FILES 
#    d= mn_files.cmssm_multinest_first_histo()
#    d = mn_files.cmssm_multinest_iters_histo(10)
    d = mn_files.cmssm_multinest_all_iters_histo_list()
    return d


def point_files() :
# TEST
#    d = files.cmssm_test_file_histo()
#    d = files.nuhm1_test_file_histo()
#    d = files.nuhm1_test_histo()
# NUHM1
#    d = files.nuhm1_pre_lhc_histo()
#    d = files.nuhm1_mcmh_mc7_histo()
#    d = files.nuhm1_mcmh_mh125_histo()
#    d = files.nuhm1_mc8_all_histo()
#    d = files.nuhm1_mc8_Nov12_bsmm_histo()
#    d = files.nuhm1_mc8_HCP12_bsmm_histo()
#    d = files.nuhm1_mc8_region_c_histo()
#    d = files.nuhm1_mc8_region_c_char_nlsp_histo()
#    d = files.nuhm1_mc8_drop_mh_histo()
#    d = files.nuhm1_mc8_drop_atlas_histo()
#    d = files.nuhm1_mc8_drop_bsmm_histo()
#    d = files.nuhm1_mc8_drop_Xenon2012_histo()
#CMSSM
#    d = files.cmssm_pre_lhc_histo()
#    d = files.cmssm_mcmh_mc7_histo()
#    d = files.cmssm_mcmh_mh125_histo()
#    d = files.cmssm_mc8_all_histo()
#    d = files.cmssm_mc8_Nov12_bsmm_histo()
#    d = files.cmssm_mc8_HCP12_bsmm_histo()
#    d = files.cmssm_mc8_drop_mh_histo()
#    d = files.cmssm_mc8_drop_atlas_histo()
#    d = files.cmssm_mc8_drop_bsmm_histo()
#    d = files.cmssm_mc8_drop_Xenon2012_histo()
#    d= mn_files.cmssm_multinest_first_histo()
#    d= mn_files.cmssm_mn_boxes_histo(0)
    d= mn_files.cmssm_mn_boxes_histo_range(0,2)
    return d

