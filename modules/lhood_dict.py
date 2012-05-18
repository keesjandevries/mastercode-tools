#!/usr/bin/env python

def get_lhood_dict() :

    # this needs to be done better than it is; but it's working around a silly implementation of LHoods
    # name; argument to be blotted to constructor, axis title for fun
    d = {
          "ATLAS_0l_4.7fb"  : {
                                  "lhtype" : "Radial",
                                  "c_args" : [ "reprocessing/lhoods/lookups/contour_lookups/mc8/atlas_0l_5fb.csv", 5.99, 0.0 ],
                                  "name"   :  "ATLAS $4.7FB^{-1}$ ATLAS-CONF-2012-033",
                                  "vars"   : [ "m0", "m12" ],
                              },
          "CMSalphaT1.6"  :   {
                                  "lhtype" : "Radial",
                                  "c_args" : [ "reprocessing/lhoods/lookups/contour_lookups/mc7/cms_1.1fb_2011.csv", 5.99, 0.0 ],
                                  "name"   :"CMS #alpha_{T} 1.6fb^{-1}",
                                  "vars"   : [ "m0", "m12" ],
                              },
          "BsmumuLHCbCMS" :   {
                                  "lhtype" : "Cartesian",
                                  "c_args" : [ "reprocessing/lhoods/lookups/1d_lookups/mc7/bs_cms_lhcb_s_sb.dat" ],
                                  "name"   : "BR(B_{s}#rightarrow#mu^{+}#mu^{-}) LHCb+CMS",
                                  "vars"   : [ "Bsmm" ],
                              },
          "Xenon2011"     :   {
                                  "lhtype" : "Cartesian",
                                  "c_args" : [ "reprocessing/lhoods/lookups/1d_lookups/mc6/xenon_contour.csv", 1, 1.2, 3.2, 1 ],
                                  "name"   :"Xenon 2011",
                                  "vars"   : [ "neu1", "sigma_pp^SI" ],
                              },
          "HA->tt2011"    :   {
                                  "lhtype" : "Cartesian",
                                  "c_args" : [ "reprocessing/lhoods/lookups/1d_lookups/mc7/Htt-CMS-1.6fb.csv", 9 ],
                                  "name"   : "CMS H/A #rightarrow#tau#tau 1.6fb^{-1}",
                                  "vars"   : [ "mA0", "tanb" ],
                              },
    }
    return d
