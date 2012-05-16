from config import plots
from modules.Space import Space
from modules.Space import Contribution

def standard_plots( pindex, sindex, nbins = 100 ) :
    v = standard_variables( pindex, sindex, nbins )
    plots = plots.plots_to_make()
    l = []
    for p in plots :
        l.append([ v[s]+[s] for s in p])
    spaces = map( make_space, l )

    return spaces

def standard_contribs( pindex, sindex, ) :
    v = standard_variables( pindex, sindex, None )
    c = plots.contributions_to_make()
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
