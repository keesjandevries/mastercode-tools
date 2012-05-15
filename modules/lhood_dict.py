#!/usr/bin/env python

def get_lhood_dict() :
    c_type = [ "CONT", "LH1D" ]
    CONT  = c_type[0]
    LH1D  = c_type[1]

    # this needs to be done better than it is; but it's working around a silly implementation of LHoods
    # name; argument to be blotted to constructor, axis title for fun
    d = {
          "ATLAS_0l_4.7fb"  : [ CONT, [ "reprocessing/lhoods/lookups/contour_lookups/mc8/atlas_0l_5fb.csv", 5.99, 0.0 ],
                              "ATLAS $4.7FB^{-1}$ ATLAS-CONF-2012-033" ],
          "CMSalphaT1.6"  : [ CONT, [ "reprocessing/lhoods/lookups/contour_lookups/mc7/cms_1.1fb_2011.csv", 5.99, 0.0 ],
                              "CMS #alpha_{T} 1.6fb^{-1}" ],
          "BsmumuLHCbCMS" : [ LH1D, [ "reprocessing/lhoods/lookups/1d_lookups/mc7/bs_cms_lhcb_s_sb.dat" ],
                              "BR(B_{s}#rightarrow#mu^{+}#mu^{-}) LHCb+CMS" ],
          "Xenon2011"     : [ LH1D, [ "reprocessing/lhoods/lookups/1d_lookups/mc6/xenon_contour.csv", 1, 1.2, 3.2, 1 ],
                              "Xenon 2011" ],
          "HA->tt2011"    : [ LH1D, [ "reprocessing/lhoods/lookups/1d_lookups/mc7/Htt-CMS-1.6fb.csv", 9 ],
                              "CMS H/A #rightarrow#tau#tau 1.6fb^{-1}" ],
        }
    return d
