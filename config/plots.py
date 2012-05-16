#! /usr/bin/env python
def plots_to_make() :
    d = {
            # spaces
            ("m0", "m12")    : { "ranges" : [ (0,2500), (0, 2500) ],    "nbins" : [100,100] },
            ("tanb", "m12")  : { "ranges" : [ (0,60),   (0,2500) ],     "nbins" : [100,100] },
            ("MA", "tanb")   : { "ranges" : [ (0,1500), (0,60) ],       "nbins" : [100,100] },
            ("mneu1", "ssi") : { "ranges" : [ (0,1000), (1-48,1e-40) ], "nbins" : [100,100] },
            # splines
            ("mstau1")       : { "ranges" : [ (0,2500) ],  "nbins" : [100] },
            ("mg")           : { "ranges" : [ (0,5000) ],  "nbins" : [100] },
            ("msqr")         : { "ranges" : [ (0,3000) ],  "nbins" : [100] },
            ("bsmm")         : { "ranges" : [ (0,10e-9) ], "nbins" : [100] },
        }
    return d

def contributions_to_make() :
    l = []
#    l = [ "g-2", "Oh2" ]
    return l
