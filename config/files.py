###############
# input files #
###############
def cmssm_test_input_file( base_dir ) :
    fd = {
             "FileName"          : "%s/cmssm_test.root" % base_dir,
             "Chi2TreeName"      : "tree",
             "Chi2BranchName"    : "vars",
             "ContribTreeName"   : "contribtree",
             "ContribBranchName" : "vars" ,
             "PredictionIndex"   : 10,
             "SpectrumIndex"     : 117,
             "Inputs"            : 10,
         }
    return fd

################
# output files #
################
def cmssm_test_output_files( base_dir ) :
    fd = {
             "FileName"          : "%s/recalc_out.root" % base_dir
             "Chi2TreeName"      : "tree",
             "Chi2BranchName"    : "vars",
             "ContribTreeName"   : "contribtree",
             "ContribBranchName" : "vars",
             "PredictionIndex"   : 10,
             "SpectrumIndex"     : 117,
             "Inputs"            : 10,
             "EntryDirectory"    : "entry_histograms",
             "DataDirectory"     : "data_histograms",
         }
    return fd
