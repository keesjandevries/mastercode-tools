#! /usr/bin/env python
from modules import plots
from config import files as fd
from modules import histogram_processing

def main( argv=None ) :
    files = fd.histo_files()

    for mcf in files :
        plot_vars = plots.get_plots(mcf)
        contrib_vars = plots.get_contribs(mcf)
        plot_hists = histogram_processing.get_entry_hist_list(mcf, plot_vars)

        plot_modes = [ "pval", "chi2", "dchi" ]
        histogram_processing.fill_and_save_data_hists( mcf, plot_modes,
                                                       plot_hists,
                                                       contrib_vars)

if __name__ == "__main__":
    main()
