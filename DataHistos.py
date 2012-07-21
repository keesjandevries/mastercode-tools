#! /usr/bin/env python
from modules import plots
from config import files as fd
from modules import histogram_processing

def main( argv=None ) :
    files = fd.histo_files()

    for mcf in files :
        print mcf.FileName # FIXME: nicer info 
#        plot_vars = plots.get_plots(mcf)
        spaces = plots.get_plots(mcf)
        contrib_vars = plots.get_contribs(mcf)
        predict_vars = plots.get_predicts(mcf)
        #plot_hist_KOhack_s = histogram_processing.get_entry_hist_KOhack_list(mcf, plot_vars)
        entry_hists = histogram_processing.get_entry_hists(mcf, spaces   )

        plot_modes = [ "pval", "chi2", "dchi" ]
#        histogram_processing.fill_and_save_data_hists( mcf, plot_modes,
#                                                       plot_hist_KOhack_s,
#                                                       contrib_vars, predict_vars)
        histogram_processing.fill_and_save_data_hists( mcf, spaces,entry_hists,
                                                       plot_modes,contrib_vars, predict_vars)

if __name__ == "__main__":
    main()
