import modules.Variables as v

indices  = [ 10 ]
min_vals = [ 0 ]
max_vals = [ 1000 ]
nbins    = [ 100 ]
names    = [ "test" ]
log      = [ False ]

x = v.pSpace( indices, min_vals, max_vals, nbins, names, log )

print repr(x)
