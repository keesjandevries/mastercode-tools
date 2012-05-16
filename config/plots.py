#! /usr/bin/env python
def plots_to_make() :
    d = {
            # spaces
            ("m0", "m12")    : [ [0,2500], [0,2500]     ],
            ("tanb", "m12")  : [ [0,60],   [0,2500]     ],
            ("MA", "tanb")   : [ [0,1500], [0,60]       ],
            ("mneu1", "ssi") : [ [0,1000], [1-48,1e-40] ],
            # splines
            ("mstau1")       : [ [0,2500]  ],
            ("mg")           : [ [0,5000]  ],
            ("msqr")         : [ [0,3000]  ],
            ("bsmm")         : [ [0,10e-9] ],
        }
    return d

def contributions_to_make() :
    l = []
#    l = [ "g-2", "Oh2" ]
    return l
