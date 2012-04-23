#! /usr/bin/env python
import config.files as files

def files( fileset ) :
    d = files.cmssm_test_output_file()
    return d

def recalc_files( fileset ) :
    d = files.cmssm_test_input_file()
    return [d]
