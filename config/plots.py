#! /usr/bin/env python
def plots_to_make() :
    d = {
#            # spaces
#           ("m0", "m12","A0","tanb")               : { "ranges" : [ (0,4000), (0, 4000), (-5000,5000),(2,68) ],   "nbins" : [3,3,3,3] },
#           ("m0", "m12")               : { "ranges" : [ (0,2000), (500,2500 ) ],   "nbins" : [100,100] },
#           ("mhd2","mhu2")             : { "ranges" : [ (-10000000,10000000),(-10000000,10000000)],  "nbins" : [100,100] },
#           ("m0", "m12")               : { "ranges" : [ (-600,4000), (0, 4000) ],   "nbins" : [100,100] },
#           ("m0", "tanb")              : { "ranges" : [ (-600,4000), (0, 60)   ],   "nbins" : [100,100] },
#           ("tanb", "m12")             : { "ranges" : [ (0,60),   (0,4000)  ],   "nbins" : [100,100] },
#           ("A0" , "tanb")             : { "ranges" : [ (-5000,5000), (0,60)],   "nbins" : [100,100] },
#           ("mA0", "tanb")             : { "ranges" : [ (0,4000), (0,60)    ],   "nbins" : [100,100] },
#           ("Dm_stau1_neu1", "m_h^0")  : { "ranges" : [ (0,20), (120, 130) ],    "nbins" : [100,100] },
#           ("stau_1","Dm_stau1_neu1")  : { "ranges" : [(0,1500), (0,30) ],       "nbins" : [100,100] },
#           ("Dm_stau1_neu1", "tanb")   : { "ranges" : [ (0,30), (0,60) ],        "nbins" : [100,100] },
#        ("neu1", "sigma_pp^SI")  : { "ranges" : [ (10,1000), (1E-12,1E-4) ], "nbins" : [100,100],"logaxes": [True,True],"KOhack":True },
#        ("neu1", "sigma_pp^SI_cm-2")  : { "ranges" : [ (10,1000), (1E-48,1E-40) ], "nbins" : [100,100],"logaxes": [True,True],
#                                          "KOhack" : True, },
#        ("neu1", "sigma_pp^SI_cm-2")  : { "ranges" : [ (10,1000), (1E-48,1E-40) ], "nbins" : [100,100],"logaxes": [True,True],
#                                          "KOhack" : True,"xenon_lhood":"Xenon2011" },
#        ("neu1", "sigma_pp^SI_cm-2")  : { "ranges" : [ (10,1000), (1E-48,1E-40) ], "nbins" : [100,100],"logaxes": [True,True],
#                                          "KOhack" : True,"xenon_lhood":"Xenon2012" },
#        ("neu1", "sigma_pp^SI_cm-2")  : { "ranges" : [ (10,1000), (1E-48,1E-40) ], "nbins" : [100,100],"logaxes": [True,True],
#                                          "KOhack" : True,"xenon_lhood":"Xenon2012LogUnc" },
#        ("neu1", "sigma_pp^SI")       : { "ranges" : [ (1,1000), (1E-12,1E-4) ], "nbins" : [100,100],"logaxes": [True,True] },
#        ("neu1", "sigma_pp^SI_cm-2")  : { "ranges" : [ (1,1000), (1E-48,1E-40) ],"nbins" : [100,100],"logaxes": [True,True] },
          # splines
#            ("neu1",)     : { "ranges" : [ (1,1000) ],  "nbins" : [100],"logaxes" : [True] },
#            ("neu1",)     : { "ranges" : [ (1,1000) ],  "nbins" : [100],"logaxes" : [True] },
#            ("neu1",)     : { "ranges" : [ (1,1000) ],  "nbins" : [100] },
#            ("m_h^0",)    : { "ranges" : [ (105,130) ],  "nbins" : [100] },
#           ("Dm_stau1_neu1",)   : { "ranges" : [ (0,10) ],  "nbins" : [100] },
            ("Dm_stau1_neu1",)   : { "ranges" : [ (0,20) ],  "nbins" : [100] },
#            ("Dm_nslp_lsp",)   : { "ranges" : [ (0,30) ],  "nbins" : [100] },
#            ("Bsmumu",)   : { "ranges" : [ (0,10.38E-9) ], "nbins" : [100] },
#            ("stau_1",)   : { "ranges" : [ (0,5000) ],  "nbins" : [100] },
#            ("stop1"  ,) : { "ranges" : [ (0,6000) ],  "nbins" : [100] },
#            ("gluino",)   : { "ranges" : [ (0,6000) ],  "nbins" : [100] },
#            ("squark_r",) : { "ranges" : [ (0,6000) ],  "nbins" : [100] },
#            ("BsmumuRatio",)   : { "ranges" : [ (0,3) ], "nbins" : [100] },
    }
    return d

def multi_dim_histos_dict():
    d = {
           ("m0", "m12","A0","tanb")               : { "ranges" : [ (0.,3999.), (0., 3999.), (-5000.,4999.),(2.,68.) ],   "nbins" : [3,3,3,3] },
#           ("m0", "m12",)               : { "ranges" : [ (0,100), (0, 1.0),],   "nbins" : [2,2,] },
        }
    return d

def contributions_to_make() :
    l = []
#    l = ["m_h^0"]
    return l

def predictions_to_make() :
#    l=["tanb","A0"]
    l=["Bsmumu"]
#    l = [
#"R(b->sg)"    
#,"R(D_ms)"     
#,"Bsmumu"      
#,"R(B->taunu)" 
#,"R(B->Xsll)"  
#,"R(K->lnu)"   
#,"Delta(g-2)"  
#,"MW"          
#,"sintheta_eff"
#,"Gamma_Z"     
#,"Rl"          
#,"Rb"          
#,"Rc"          
#,"Afb(b)"      
#,"Afb(c)"      
#,"Ab16"        
#,"Ac17"        
#,"Al(SLD)"     
#,"m_h^0"       
#,"Al(P_tau)"   
#,"Al_fb"       
#,"sigma_had^0" 
#,"R(Delta_md)" 
#,"R(Delta_mk)" 
#,"R(Kp->pinn)" 
#,"BR(Bd->ll)"  
#,"R(Dms)/R(Dmd)"
#,"D_0(K*g)"    
#,"BR(b->sg)"   
#,"sigma_pp^SI" ]
#    l =[ "mA0","tamb"]
#    l = ["Dm_stau1_neu1"]
    return l
