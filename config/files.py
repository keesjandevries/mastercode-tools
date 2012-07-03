#! /usr/bin/env python
import modules.file_dicts as files

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
#    d = files.nuhm1_bsmm2012_input()
#    d = files.nuhm1_mc8_drop_atlas_input()
#    d = files.nuhm1_mc8_drop_bsmm_input()
#    d = files.nuhm1_mc8_all_input()
#CMSSM
#    d = files.cmssm_mcmh_mc7_input()
#    d = files.cmssm_mcmh_mh125_input()
#    d = files.cmssm_mc8_drop_atlas_input()
#    d = files.cmssm_mc8_drop_bsmm_input()
#    d = files.cmssm_mc8_all_input()
    return d

def histo_files() :
# TEST
#    d = files.cmssm_test_file_histo()
#    d = files.nuhm1_test_file_histo()
#    d = files.nuhm1_test_histo()
# NUHM1
#    d = files.nuhm1_pre_lhc_histo()
#    d = files.nuhm1_mcmh_mc7_histo()
#    d = files.nuhm1_mcmh_mh125_histo()
#    d = files.nuhm1_mc8_all_histo()
#    d = files.nuhm1_mc8_drop_atlas_histo()
#    d = files.nuhm1_mc8_drop_bsmm_histo()
#CMSSM
#    d = files.cmssm_pre_lhc_histo()
#    d = files.cmssm_mcmh_mc7_histo()
#    d = files.cmssm_mcmh_mh125_histo()
#    d = files.cmssm_mc8_all_histo()
#    d = files.cmssm_mc8_drop_atlas_histo()
#    d = files.cmssm_mc8_drop_bsmm_histo()
    return d


def point_files() :
# TEST
#    d = files.cmssm_test_file_histo()
#    d = files.nuhm1_test_file_histo()
#    d = files.nuhm1_test_histo()
# NUHM1
#    d = files.nuhm1_mcmh_mc7_histo()
#    d = files.nuhm1_mcmh_mh125_histo()
#    d = files.nuhm1_bsmm2012_histo()
#    d = files.nuhm1_mc8_all_histo()
#    d = files.nuhm1_mc8_drop_atlas_histo()
#    d = files.nuhm1_mc8_drop_bsmm_histo()
#CMSSM
#    d = files.cmssm_mcmh_mc7_histo()
#    d = files.cmssm_mcmh_mh125_histo()
#    d = files.cmssm_mc8_all_histo()
#    d = files.cmssm_mc8_drop_atlas_histo()
#    d = files.cmssm_mc8_drop_bsmm_histo()
    return d

