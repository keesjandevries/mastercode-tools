#! /usr/bin/env python
import ROOT as r
from modules.mcchain import MCAnalysisChain
from modules import variables 

def fill_n_dim_hisogram(chain,n_dim_histo_list,space_dict,mcf):
    
    mc_vars = variables.mc_variables() # this gets all mc-variabls
    space_vars = [  [mc_vars[sn] for sn in short_names  ] for short_names in space_dict  ]

    begin   = 0
#    end     = chain.GetEntries()
    end     = 10000 
    prog = ProgressBar(begin, end, 77, mode='fixed', char='#')
    for entry in xrange(begin,end) :
        chi2 = get_chi2(chain,mcf)
        for histo, vars  in zip(n_dim_histo_list, space_vars )  :
            coord=get_and_coordinates(vars,chain,mcf)
            fill_histo(entry,chi2,coord)


           
        

def init_interv_dict_list(space_dict):
    rdl=[]
    for space in space_dict:
        dl={}    
        intervs=space_dict[space]["ranges"]
        nbins=space_dict[space]["nbins"]
        interv_list  = add_intervs_recursively([[]],0,intervs,nbins)
        for interv in interv_list:
            dl[tuple(interv)]=(-1 , 1.0e9) # will evenually be filled with bin number and X^2
        rdl.append(dl)
    return rdl

#        for interv, nbins  in zip( space_dict[space]["ranges"], space_dict[space]["nbins"] ) :

def add_intervs_recursively(l_old, step, intervs, nbins):
    # safety first !!
    if len(intervs) is not len(nbins): 
        print "Number of intervals does not equal number of bins"
        return None
    #alrogrithm starts here
    if step < len(intervs):
        min=intervs[step][0]
        max=intervs[step][1]
        n_bins=nbins[step]
        l_new=[]
        l_count=0
        for j,int in enumerate(l_old):
            for i in range(n_bins):
                l_new.append(int + [(  (min+(i)*(max-min)/n_bins) , (min+(i+1)*(max-min)/n_bins)  )]    )
        l_old =add_intervs_recursively(l_new, step+1, intervs, nbins)
    if len(l_old[0]) == len(intervs):
        return l_old

def go(mcf,space_dict):
#   the space dict looks like this:
#   { ("m0", "m12","A0","tanb") : { "ranges" : [ (0,4000), (0, 4000), (-5000,5000),(2,68) ],   "nbins" : [3,3,3,3] },... }
    chain = MCAnalysisChain(mcf)
    print space_dict
    interv_dict_list = init_interv_dict_list(space_dict)
    fill_n_dim_hisogram(chain,interv_dict_list,space_dict,mcf)
    
    return interv_dict_list
