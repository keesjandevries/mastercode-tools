#! /usr/bin/env python
def plots_to_make() :
    d = {
#            # spaces
#           ("m0", "m12")               : { "ranges" : [ (0,4000), (0, 3000) ],   "nbins" : [100,100] },
#           ("stau_1","Dm_stau1_neu1")  : { "ranges" : [(0,1500), (0,50) ],       "nbins" : [100,100] },
#           ("m0", "tanb")              : { "ranges" : [ (0,4000), (0, 60)   ],   "nbins" : [100,100] },
#           ("tanb", "m12")             : { "ranges" : [ (0,60),   (0,3000)  ],   "nbins" : [100,100] },
#           ("mA0", "tanb")             : { "ranges" : [ (0,3000), (0,60)    ],   "nbins" : [100,100] },
#           ("Dm_stau1_neu1", "m_h^0")  : { "ranges" : [ (0,20), (120, 130) ],    "nbins" : [100,100] },
#           ("Dm_stau1_neu1", "tanb")   : { "ranges" : [ (0,20), (0,60) ],        "nbins" : [100,100] },
#        ("neu1", "sigma_pp^SI")  : { "ranges" : [ (10,1000), (1E-12,1E-4) ], "nbins" : [100,100],"logaxes": [True,True],"KOhack":True },
#        ("neu1", "sigma_pp^SI_cm-2")  : { "ranges" : [ (10,1000), (1E-48,1E-40) ], "nbins" : [100,100],"logaxes": [True,True],
#                                          "KOhack" : True, },
#        ("neu1", "sigma_pp^SI_cm-2")  : { "ranges" : [ (10,1000), (1E-48,1E-40) ], "nbins" : [100,100],"logaxes": [True,True],
#                                          "KOhack" : True,"xenon_lhood":"Xenon2011" },
#        ("neu1", "sigma_pp^SI_cm-2")  : { "ranges" : [ (10,1000), (1E-48,1E-40) ], "nbins" : [100,100],"logaxes": [True,True],
#                                          "KOhack" : True,"xenon_lhood":"Xenon2012" },
#        ("neu1", "sigma_pp^SI_cm-2")  : { "ranges" : [ (10,1000), (1E-48,1E-40) ], "nbins" : [100,100],"logaxes": [True,True],
#                                          "KOhack" : True,"xenon_lhood":"Xenon2012LogUnc" },
#        ("neu1", "sigma_pp^SI")       : { "ranges" : [ (1,1000), (1E-12,1E-4) ], "nbins" : [100,100],"logaxes": [True,True] },
#        ("neu1", "sigma_pp^SI_cm-2")  : { "ranges" : [ (1,1000), (1E-48,1E-40) ],"nbins" : [100,100],"logaxes": [True,True] },
          # splines
#            ("neu1",)     : { "ranges" : [ (1,1000) ],  "nbins" : [100],"logaxes" : [True] },
#            ("neu1",)     : { "ranges" : [ (1,1000) ],  "nbins" : [100],"logaxes" : [True] },
#            ("neu1",)     : { "ranges" : [ (1,1000) ],  "nbins" : [100] },
#            ("m_h^0",)    : { "ranges" : [ (105,130) ],  "nbins" : [100] },
#            ("stau_1",)   : { "ranges" : [ (0,5000) ],  "nbins" : [100] },
#            ("Dm_stau1_neu1",)   : { "ranges" : [ (0,10) ],  "nbins" : [100] },
#            ("stop1"  ,) : { "ranges" : [ (0,6000) ],  "nbins" : [100] },
#            ("gluino",)   : { "ranges" : [ (0,6000) ],  "nbins" : [100] },
#            ("squark_r",) : { "ranges" : [ (0,6000) ],  "nbins" : [100] },
#            ("BsmumuRatio",)   : { "ranges" : [ (0,3) ], "nbins" : [100] },
#            ("Bsmumu",)   : { "ranges" : [ (0,10.38E-9) ], "nbins" : [100] },
     }
    return d

def contributions_to_make() :
    l = []
#    l = ["m_h^0"]
    return l

def predictions_to_make() :
    l = []
#    l =[ "mA0","tamb"]
#    l = ["Dm_stau1_neu1"]
    return l
