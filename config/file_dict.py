#! /usr/bin/env python
import config.files as files

def histo_files() :
#    d = files.cmssm_test_output_files()
#    d = files.nuhm1_test_output_files()
#    d = files.nuhm1_MCMh_MC7()
    d = files.nuhm1_MC8_ATLAS_test()
    return d

def recalc_files() :
#    d = files.cmssm_test_input_files()
#    d = files.nuhm1_MCMh_MC7_for_recalc()
    d = files.nuhm1_MC8_ATLAS_test_recalc() 
    return d

def point_files() :
#    d = files.cmssm_test_output_files()
#    d = files.nuhm1_test_output_files()
#    d = files.nuhm1_MCMh_MC7()
    d = files.nuhm1_MC8_ATLAS_test()
    return d

