#! /usr/bin/env python
from modules import plots
from config import files as fd
from modules import histogram_processing

def main( argv=None ) :
    files = fd.histo_files()

    for mcf in files :
        print mcf.FileName # FIXME: nicer info 
        spaces = plots.get_plots(mcf)
#        contrib_vars = plots.get_contribs(mcf)
#        predict_vars = plots.get_predicts(mcf)
#        entry_hists = histogram_processing.get_entry_hists(mcf, spaces   )
        dchi_hists = histogram_processing.get_dchi_hists(mcf, spaces   )
        histogram_processing.plot_and_save_smooth_spline(dchi_hists,mcf,spaces)
#        plot_modes = [ "pval", "chi2", "dchi" ]
#        histogram_processing.fill_and_save_data_hists( mcf, spaces,entry_hists,
#                                                       plot_modes,contrib_vars, predict_vars)

if __name__ == "__main__":
    main()
