#! /usr/bin/env python
import config.files as files

def histo_files() :
    d = files.cmssm_test_output_files()
    return d

def recalc_files() :
    d = files.cmssm_test_input_files()
    return d
