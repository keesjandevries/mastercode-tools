#! /usr/bin/env python
import modules.file_dicts as files

def histo_files() :
#    d = files.cmssm_test_file_histo()
    d = files.nuhm1_Bsmm2012_histo()
    #d = files.nuhm1_test_file_histo()
    return d

def recalc_files() :
    d = files.cmssm_test_input_files()
#    d = files.nuhm1_MCMh_MC7_input()
#    d = files.nuhm1_Bsmm2012_input()
#    d = files.nuhm1_test_input_files()
    return d

def point_files() :
#    d = files.nuhm1_MCMh_MC7_histo()
    d = files.nuhm1_Bsmm2012_histo()
#    d = files.cmssm_test_output_files()
    return d

