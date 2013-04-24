#! /usr/bin/env python
import modules.file_dicts as files
import modules.multinest_files as mn_files
import modules.celmov_files as celmov_files
import modules.nuhm2_old as nuhm2_old
import modules.test_cmssm as test_cmssm
import modules.test_mcpp_cmssm as test_mcpp_cmssm

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
#    d = test_cmssm.cmssm_test_vs_cpp_input()
# NUHM1
#    d = files.nuhm1_mcmh_mc7_input()
#    d = files.nuhm1_pre_lhc_input()
#    d = files.nuhm1_pre_lhc_drop_mh_input()
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
#    d = files.nuhm1_mc8_all_stop_nlsp_input()
#    d = files.nuhm1_mc8_all_input()
#CMSSM
#    d = files.cmssm_pre_lhc_input()
#    d = files.cmssm_pre_lhc_drop_mh_input()
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
#    d = files.cmssm_mc8_all_stop_nlsp_input()
#MULTINEST FILES
#    d = mn_files.cmssm_multinest_first_input()
#    d = mn_files.cmssm_multinest_iters_input(10)
#    d = mn_files.cmssm_mn_boxes_combined_input()
#    d = mn_files.cmssm_mn_boxes_N_combined_input(1)
#    d = mn_files.cmssm_mn_boxes_N_combined_input(2)
#    d = mn_files.cmssm_mn_boxes_N_combined_input(3)
#    d = mn_files.cmssm_multinest_all_sessions_comb_input()
#    d = mn_files.nuhm2_mn_boxes_combined_input()
#    d = mn_files.nuhm2_mn_xmas_combined_input()
#    d = mn_files.nuhm2_mn_ndn_combined_input()
# CELMOV
#    d = celmov_files.cmssm_mc8_all_stable_stau_input()
#OLD NUHM2
#    d = nuhm2_old.nuhm2_old_combined_input()
#    d = nuhm2_old.nuhm2_all_old_combined_input()
#    d = nuhm2_old.nuhm2_jad_old_combined_input()
# mcpp testing
#    d = test_mcpp_cmssm.mcpp_cmssm_test_input()
#    d = test_mcpp_cmssm.mcpp_cmssm_mc8_m0_m12_old_input()
#    d = test_mcpp_cmssm.mcpp_cmssm_mc8_m0_m12_new_input()
    d = test_mcpp_cmssm.mcpp_cmssm_combined_input()
    return d

def recalc_file_list():
#    d = [mn_files.cmssm_multinest_iters_input(i) for i in range(1,11) ]
#    d = [ mn_files.cmssm_mn_boxes_input(i) for i in range(0,1)]
#    d = [ mn_files.cmssm_mn_boxes_N_input(i,1) for i in range(0,43)]
#    d = [ mn_files.cmssm_mn_boxes_N_input(i,2) for i in range(0,43)]
#    d = [ mn_files.cmssm_mn_boxes_N_input(i,3) for i in range(0,43)]
#    d = [ mn_files.nuhm2_mn_boxes_input(i) for i in range(0,32)]
#    d = [mn_files.nuhm2_mn_xmas_box_steps_input(i,1, 8) for i in range(0,64)  ]
#    d = [mn_files.nuhm2_mn_xmas_box_all_steps_input(i) for i in range(0,64)  ]
#    d = [mn_files.nuhm2_mn_ndn_box_all_steps_input(i) for i in range(0,192)  ]
    d=[test_mcpp_cmssm.mcpp_cmssm_dir_all_steps_input(i) for i in range(1,2 )]
    return d

def histo_files() :
# TEST
#    d = files.cmssm_test_file_histo()
#    d = files.nuhm1_test_file_histo()
##    d = files.nuhm1_test_histo()
# NUHM1
    d = files.nuhm1_pre_lhc_histo()
#    d = files.nuhm1_pre_lhc_drop_mh_histo()
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
#    d = files.cmssm_pre_lhc_drop_mh_histo()
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
#    d = mn_files.cmssm_mn_boxes_combined_histo()
#    d = mn_files.cmssm_mn_boxes_N_combined_histo(1)
#    d = mn_files.cmssm_mn_boxes_N_combined_histo(2)
#    d = mn_files.cmssm_mn_boxes_N_combined_histo(3)
#    d = mn_files.cmssm_multinest_all_sessions_comb_histo()
#    d = mn_files.nuhm2_mn_boxes_combined_histo()
#    d = mn_files.nuhm2_mn_xmas_combined_histo()
#    d = mn_files.nuhm2_mn_ndn_combined_histo()
#OLD MASTERCODE
#    d = nuhm2_old.nuhm2_old_combined_histo()
#    d = nuhm2_old.nuhm2_all_old_combined_histo()
#    d = nuhm2_old.nuhm2_jad_old_combined_histo()
# CELMOV
#    d = celmov_files.cmssm_mc8_all_stable_stau_histo()
#    d = files.cmssm_mc8_all_tanb_cut_histo()
# MCPP
#    d = test_mcpp_cmssm.mcpp_cmssm_combined_histo()
#    d = test_mcpp_cmssm.mcpp_cmssm_mc8_m0_m12_old_histo()
#    d = test_mcpp_cmssm.mcpp_cmssm_mc8_m0_m12_new_histo()
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
    d = files.nuhm1_mc8_all_histo()
#    d = files.nuhm1_mc8_all_stop_nlsp_histo()
#    d = files.nuhm1_mc8_Nov12_bsmm_histo()
#    d = files.nuhm1_mc8_HCP12_bsmm_histo()
#    d = files.nuhm1_mc8_region_c_histo()
#    d = files.nuhm1_mc8_region_c_char_nlsp_histo()
#    d = files.nuhm1_mc8_drop_mh_histo()
#    d = files.nuhm1_mc8_drop_atlas_histo()
#    d = files.nuhm1_mc8_drop_bsmm_histo()
#    d = files.nuhm1_mc8_drop_Xenon2012_histo()
# CMSSM
#    d = files.cmssm_pre_lhc_histo()
#    d = files.cmssm_pre_lhc_drop_mh_histo()
#    d = files.cmssm_mcmh_mc7_histo()
#    d = files.cmssm_mcmh_mh125_histo()
#    d = files.cmssm_mc8_all_histo()
#    d = files.cmssm_mc8_all_stop_nlsp_histo()
#    d = files.cmssm_mc8_Nov12_bsmm_histo()
#    d = files.cmssm_mc8_HCP12_bsmm_histo()
#    d = files.cmssm_mc8_drop_mh_histo()
#    d = files.cmssm_mc8_drop_atlas_histo()
#    d = files.cmssm_mc8_drop_bsmm_histo()
#    d = files.cmssm_mc8_drop_Xenon2012_histo()
# MULTINEST
#    d = mn_files.cmssm_multinest_first_histo()
#    d = mn_files.cmssm_mn_boxes_histo(0)
#    d = mn_files.cmssm_mn_boxes_histo_range(0,81)
#    d = mn_files.cmssm_mn_boxes_combined_histo()
#    d = mn_files.cmssm_mn_boxes_N_combined_histo(1)
#    d = mn_files.cmssm_mn_boxes_N_combined_histo(2)
#    d = mn_files.cmssm_mn_boxes_N_combined_histo(3)
#    d = mn_files.nuhm2_mn_boxes_histo_range(0,32)
#    d = mn_files.nuhm2_mn_boxes_combined_histo()
#    d = mn_files.nuhm2_mn_xmas_combined_histo()
#    d = mn_files.nuhm2_mn_ndn_combined_histo()
# CELMOV
#    d = celmov_files.cmssm_mc8_all_stable_stau_histo()
#    d = nuhm2_old.nuhm2_old_combined_histo()
#OLD MASTERCODE
#    d = nuhm2_old.nuhm2_jad_old_combined_histo()
# mcpp test file
#    d = test_mcpp_cmssm.mcpp_cmssm_test_histo()
#    d = test_mcpp_cmssm.mcpp_cmssm_combined_histo()
    return d

