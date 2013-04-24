#! /usr/bin/env python
import ROOT as r
from config import files as fd
from config import plots as pd
from config import files

from modules import n_dim_entries 

# This does practically the same as EntryHistos.py, except
# the output is not in the root file, and highter dimensionality is 
# possible

def main():
    mcfile_list = files.histo_files()
    for mcf in mcfile_list :
        print "Processing file: ",mcf.FileName  
        space_dict = pd.multi_dim_histos_dict()
        n_dim_entries.go(mcf,space_dict)

if __name__ == "__main__":
    main()
