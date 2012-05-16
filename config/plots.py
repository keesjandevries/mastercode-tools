#! /usr/bin/env python
from modules.Space import Space
from modules.Space import Contribution
import sys

# this is what you edit
def plots_to_make() :
    d = {
            # spaces
            ("m0", "m12")    : [ [0,2500], [0,2500]     ],
            ("tanb", "m12")  : [ [0,60],   [0,2500]     ],
            ("MA", "tanb")   : [ [0,1500], [0,60]       ],
            ("mneu1", "ssi") : [ [0,1000], [1-48,1e-40] ],
            # splines
            ("mstau1")       : [ [0,2500]  ]
            ("mg")           : [ [0,5000]  ]
            ("msqr")         : [ [0,3000]  ]
            ("bsmm")         : [ [0,10e-9] ]
        }
    return d

def contributions_to_make() :
#    l = [ "g-2", "Oh2" ]
    l = [  ]
    return l

###########################################
### Dont edit for run: only development ###
###########################################

def standard_plots( pindex, sindex, nbins = 100 ) :
    v = standard_variables( pindex, sindex, nbins )
    plots = plots_to_make()
    l = []
    for p in plots :
        l.append([ v[s]+[s] for s in p])
    spaces = map( make_space, l )

    return spaces

def standard_contribs( pindex, sindex, ) :
    v = standard_variables( pindex, sindex, None )
    c = contributions_to_make()
    contribs = []
    for contrib in c :
        opts = v[contrib]
        contribs.append( Contribution( opts[0], opts[-2], contrib ) )
    return contribs

def make_space( l ) :
    args = [ [],[],[],[],[],[], [] ]
    for v in l :
        for o,a in zip(v,args) :
            a.append(o)
    s = Space( *args )
    return s
