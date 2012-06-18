from config import plots as pc
from modules.mcspace import MCSpace
from modules.mcspace import MCContribution
from modules.variables import mc_variables
from modules.variables import base_variables

def get_plots(mcf) :
    # plots from now on based on Variables, so that it can accomodate for MCVariables and DerivedMCVariables
    v = base_variables()   
    plots = pc.plots_to_make()
    for plane, opts in plots.iteritems() :
        assert len(plane) == len( opts["ranges"] ) == len( opts["nbins"] ), \
            "Wrong option numbers for plots (dimensionality doesnt match ranges and/or bins"
    d = {}
    for plot_vars, options in plots.iteritems() :
        d[tuple([ v[var] for var in plot_vars])] = options

    spaces = [ MCSpace( mcf, Var, opts ) for (Var, opts) in d.iteritems() ]
    return spaces

def get_contribs( mcf ) :
    v = mc_variables()
    c = pc.contributions_to_make()
    contribs = []
    for contrib in c :
        opts = v[contrib]
        contribs.append( MCContribution( mcf, v[contrib] ) )
    return contribs

def get_predicts( mcf ) :
    v = mc_variables()
    p = pc.predictions_to_make()
    predicts = []
    for predict in p :
        opts = v[predict]
        predicts.append( MCContribution( mcf, v[predict] ) )
    return predicts
