#! /usr/bin/env python
def plots_to_make() :
    d = {
            # spaces
            ("m0", "m12")            : { "ranges" : [ (0,2500), (0, 2500) ],    "nbins" : [100,100] },
            ("tanb", "m12")          : { "ranges" : [ (0,60),   (0,2500) ],     "nbins" : [100,100] },
            ("A0", "tanb")           : { "ranges" : [ (0,1500), (0,60) ],       "nbins" : [100,100] },
            #("neu1", "sigma_pp^SI")  : { "ranges" : [ (0,1000), (1E-48,1E-40) ], "nbins" : [100,100] },
            # splines
            ("stau_1",)   : { "ranges" : [ (0,2500) ],  "nbins" : [100] },
            ("gluino",)   : { "ranges" : [ (0,5000) ],  "nbins" : [100] },
            ("squark_r",) : { "ranges" : [ (0,3000) ],  "nbins" : [100] },
            ("Bsmumu",)   : { "ranges" : [ (0,10E-9) ], "nbins" : [100] },
        }
    return d

def contributions_to_make() :
    l = []
    #l = ["Oh^2"]
    return l
