#! /usr/bin/env python
from modules.Variables import Space
import sys

def get_plots( pindex, sindex, nbins = 100 ) :
    return standard_plots(pindex, sindex, nbins )

def standard_plots( pindex, sindex, nbins ) :
    v = standard_variables( pindex, sindex, nbins )
    l = [ 
            [ v["m0"], v["m12"] ],
            [ v["m0"], v["tanb"] ],
            [ v["tanb"], v["m12"] ],
            [ v["mneu1"] ],
            [ v["mh"] ],
        ]
    spaces = map( make_space, l )
    return spaces

def make_space( l ) :
    args = [ [],[],[],[],[],[] ]
    for v in l :
        for o,a in zip(v,args) :
            a.append(o)
    s = Space( *args )
    print repr(s)
    return s

def standard_variables( pindex, sindex, nbins ) :
    sv = { 
            #shortname     index,    min,   max, nbins,                                  title,   log
            "m0"    : [         1,     0,  2500, nbins,                    "m_{0} [GeV/c^{2}]", False ],
            "m12"   : [         2,     0,  2500, nbins,                  "m_{1/2} [GeV/c^{2}]", False ],
            "a0"    : [         3, -5000,  5000, nbins,                          "A_{0} [GeV]", False ],
            "tanb"  : [         4,     0,    60, nbins,                           "tan(#beta)", False ],
            "h0"    : [ pindex+20,    85,   140, nbins,                "m_{h^{0}} [GeV/c^{2}]", False ],
            "ssi"   : [ pindex+64, 1e-48, 1e-40, nbins,            "#sigma_{p}^{SI} [cm^{-2}]", False ],
            "mneu1" : [  sindex+2,    10,  1000, nbins, "m_{#tilde{#chi}^{0}_{1}} [GeV/c^{2}]", False ],
            "mh"    : [ pindex+18,    85,   140, nbins,                 "m_{h^{0}} [GeV/c^{2}", False ],
         }
    return sv
