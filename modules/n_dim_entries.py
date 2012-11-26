#! /usr/bin/env python
import ROOT as r
from modules.mcchain import MCAnalysisChain

def init_interv_dict_list(space_dict):
    rdl=[]
    for space in space_dict:
        dl={}    
        intervs=space_dict[space]["ranges"]
        nbins=space_dict[space]["nbins"]
        interv_list  = add_intervs_recursively([[]],0,intervs,nbins)
        for interv in interv_list:
            dl[interv]=(-1 , 1.0e9) # will evenually be filled with bin number and X^2
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
#    chain = MCAnalysisChain(mcf)
    print space_dict
    interv_dict_list = init_interv_dict_list(space_dict)
    print interv_dict_list
    
    return interv_dict_list
