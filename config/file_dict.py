#! /usr/bin/env python
import config.files as files

def files( fileset ) :
    base_dir = base_directory( fileset )
    d = files.cmssm_test_output_file( base_dir )
    return d

def recalc_files( fileset ) :
    base_dir = base_directory( fileset )
    d = files.cmssm_test_input_file( base_dir )
    return d


def base_directory( fileset ) :
    d = {
            "hep.ph.ic.ac.uk" : "/vols/cms03/mastercode/test_files/",
            "localdomain" :     "~/Documents/mastercode_data/",
        }
    return d[fileset]
