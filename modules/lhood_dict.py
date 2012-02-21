#!/usr/bin/env python

def get_lhood_dict() :
    c_type = [ "CONT", "LH1D" ]
    CONT  = c_type[0]
    LH1D  = c_type[1]

    # name; argument to be blotted to constructor, axis title for fun
    d = { 
          "CMSalphaT1.6"  : [ CONT, [ "reprocessing/lhoods/lookups/contour_lookups/mc7/cms_1.1fb_2011.csv", 5.99, 0.0 ], 
                              "CMS #alpha_{T} 1.6fb^{-1}" ],
          "BsmumuLHCbCMS" : [ LH1D, [ "./reprocessing/lhoods/lookups/1d_lookups/mc7/bs_cms_lhcb_s_sb.dat" ],             
                              "BR(B_{s}#rightarrow#mu^{+}#mu^{-}) LHCb+CMS" ],
        }                                                               
    return d
