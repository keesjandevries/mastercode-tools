#!/usr/bin/env python

def get_lhood_dict() :

    # this needs to be done better than it is; but it's working around a silly implementation of LHoods
    # name; argument to be blotted to constructor, axis title for fun
    d = {
          "ATLAS_0l_4.7fb"  : {
                                  "lhtype" : "Radial",
                                  "c_args" : [ "reprocessing/lhoods/lookups/contour_lookups/mc8/atlas_0l_5fb.csv", 5.99, 0.0 ],
                                  "name"   :  "ATLAS m0-m12 plane 4.7fb-1 [ATLAS-CONF-2012-033]",
                                  "vars"   : [ "m0", "m12" ],
                              },
          "CMSalphaT1.6"  :   {
                                  "lhtype" : "Radial",
                                  "c_args" : [ "reprocessing/lhoods/lookups/contour_lookups/mc7/cms_1.1fb_2011.csv", 5.99, 0.0 ],
                                  "name"   :"CMS m0-m12 plane, alpha_T, 1.6fb-1 [MC7] ",
                                  "vars"   : [ "m0", "m12" ],
                              },
          "BsmumuMC8lhcb" :   {
                                  "lhtype" : "Cartesian",
                                  "c_args" : [ "reprocessing/lhoods/lookups/1d_lookups/mc8/lhcb_only.dat" ],
                                  "name"   : "BR(B_s->mumu) LHCb [MC8 Diego] ",
                                  "vars"   : [ "Bsmumu" ],
                              },
          "Bsmumu_HCP12_X2" : {
                                  "lhtype" : "Cartesian",
                                  "c_args" : [ "reprocessing/lhoods/lookups/1d_lookups/HCP/HCP_bsmm_2012.dat",10 ],
                                  "name"   : "BR(B_s->mumu) LHCb+CMS+ATLAS+CDF [HCP12 Diego unofficial comb] ",
                                  "vars"   : [ "Bsmumu" ],
                              },
          "BsmumuMC8DiegoX2" :   {
                                  "lhtype" : "Cartesian",
                                  "c_args" : [ "reprocessing/lhoods/lookups/1d_lookups/mc8/bsmm_X2_lookup.dat",10 ],
                                  "name"   : "BR(B_s->mumu) LHCb+CMS+ATLAS+CDF [MC8 Diego unofficial comb] ",
                                  "vars"   : [ "Bsmumu" ],
                              },
          "BsmumuMC8comb" :   {
                                  "lhtype" : "Cartesian",
                                  "c_args" : [ "reprocessing/lhoods/lookups/1d_lookups/mc8/atlas_cms_lhcb_cdf.dat" ],
                                  "name"   : "BR(B_s->mumu) LHCb+CMS+ATLAS+CDF [MC8 Diego unofficial comb] ",
                                  "vars"   : [ "Bsmumu" ],
                              },
          "BsmumuLHCbCMS" :   {
                                  "lhtype" : "Cartesian",
                                  "c_args" : [ "reprocessing/lhoods/lookups/1d_lookups/mc7/bs_cms_lhcb_s_sb.dat" ],
                                  "name"   : "BR(B_s->mumu) LHCb+CMS [MC7]",
                                  "vars"   : [ "Bsmumu" ],
                              },
          "Xenon2012LogUnc"  :   {
                                  "lhtype" : "Cartesian",
                                  "c_args" : [ "reprocessing/lhoods/lookups/1d_lookups/mc8/xenon2012_contour.csv",12, 1.0, 2.7,1 ],
                                  "name"   :"Xenon 2012 [MC8] with log unc on ssi",
                                  "vars"   : [ "neu1", "sigma_pp^SI" ],
                              },
          "Xenon2012"     :   {
                                  "lhtype" : "Cartesian",
                                  "c_args" : [ "reprocessing/lhoods/lookups/1d_lookups/mc8/xenon2012_contour.csv",11, 1.0, 2.7,1 ],
                                  "name"   :"Xenon 2012 [MC8]",
                                  "vars"   : [ "neu1", "sigma_pp^SI" ],
                              },
          "Xenon2011"     :   {
                                  "lhtype" : "Cartesian",
                                  "c_args" : [ "reprocessing/lhoods/lookups/1d_lookups/mc6/xenon_contour.csv", 1, 1.2, 3.2, 1 ],
                                  "name"   :"Xenon 2011 [MC7]",
                                  "vars"   : [ "neu1", "sigma_pp^SI" ],
                              },
          "MAtanb5fb"     :   {
                                  "lhtype" : "Cartesian",
                                  "c_args" : [ "reprocessing/lhoods/lookups/1d_lookups/mc8/CMS-5fb-MA-tanb.csv", 9 ],
                                  "name"   : "CMS, H/A -> tautau, 4.6fb-1 [CMS-HIG-11-029]",
                                  "vars"   : [ "mA0", "tanb" ],
                              },
          "HA->tt2011"    :   {
                                  "lhtype" : "Cartesian",
                                  "c_args" : [ "reprocessing/lhoods/lookups/1d_lookups/mc7/Htt-CMS-1.6fb.csv", 9 ],
                                  "name"   : "CMS, H/A -> tautau, 1.6fb-1 [MC7]",
                                  "vars"   : [ "mA0", "tanb" ],
                              },
    }
    return d
