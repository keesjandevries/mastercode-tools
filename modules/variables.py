from modules import MCVariable as MCV
from modules import Variable as Var

GeVc2 = "[GeV/c^{2}]"
GeV   = "[GeV]"
GeV   = "[MeV]"

def mc_variables() :
    b = base_variables()
    m = {
            "m0"           : MCV( b["m0"], index_offset=1 ),
            "m12"          : MCV( b["m0"],           
            "A0"           : MCV( b["A0"],           
            "tanb"         : MCV( b["tanb"],         
            "mtop"         : MCV( b["mtop"],         
            "MZ"           : MCV( b["MZ"],           
            "GZ_in"        : MCV( b["GZ_in"],        
            "Rb->sg"       : MCV( b["R(b->sg)"],     
            "RD_ms"        : MCV( b["RD_ms"],        
            "Bsmumu"       : MCV( b["Bsmumu"],       
            "R(B->taunu)"  : MCV( b["R(B->taunu)"],  
            "R(B->Xsll)"   : MCV( b["R(B->Xsll)"],   
            "R(K->lnu)"    : MCV( b["R(K->lnu)"],    
            "Delta(g-2)"   : MCV( b["Delta(g-2)"],   
            "MW"           : MCV( b["MW"],           
            "sintheta_eff" : MCV( b["sintheta_eff"],  index_offset=8,  offset_relative_to="PredictionIndex" )
            "GZ_in"        : MCV( b["GZ_in"],        
            "Rl"           : MCV( b["Rl"],           
            "Rb"           : MCV( b["Rb"],           
            "Rc"           : MCV( b["Rc"],           
            "Afb(b)"       : MCV( b["Afb(b)"],       
            "Afb(c)"       : MCV( b["Afb(c)"],       
            "Ab16"         : MCV( b["Ab16"],         
            "Ac17"         : MCV( b["Ac17"],         
            "Al(SLD)"      : MCV( b["Al(SLD)"],      
            "m_h^0"        : MCV( b["m_h^0"],        
            "Oh^2"         : MCV( b["Oh^2"],         
            "Al(P_tau)"    : MCV( b["Al(P_tau)"],    
            "Al_fb"        : MCV( b["Al_fb"],        
            "sigma_had^0"  : MCV( b["sigma_had^0"],  
            "R(Delta_md)"  : MCV( b["R(Delta_md)"],  
            "R(Delta_mk)"  : MCV( b["R(Delta_mk)"],  
            "R(Kp->pinn)"  : MCV( b["R(Kp->pinn)"],  
            "BR(Bd->ll)"   : MCV( b["BR(Bd->ll)"],   
            "R(Dms)/R(Dmd)": MCV( b["R(Dms)/R(Dmd)"], index_offset=27, offset_relative_to="PredictionIndex" )
            "D_0(K*g)"     : MCV( b["D_0(K*g)"],     
            "BR(b->sg)"    : MCV( b["BR(b->sg)"],    
            "sigma_pp^SI"  : MCV( b["sigma_pp^SI"],  
    }
    return m

def base_variables() :
    return {
        "m0"           : Var( "m0",           r"$m_{0} %s$"%GeVc2 )
        "m12"          : Var( "m0",           r"$m_{0} %s$"%GeVc2 )
        "A0"           : Var( "A0",           r"$A_{0} %s$"%GeV )
        "tanb"         : Var( "tanb",         r"$\tan(\beta)$" )
        "mtop"         : Var( "mtop",         r"$m_{t} %s$"%GeVc2,                    "GAUSS", 173.2,    [0.9]  )
        "MZ"           : Var( "MZ",           r"$m_{Z} %s$"%GeVc2,                    "GAUSS", 91.1875,  [0.0021] )
        "GZ_in"        : Var( "GZ_in",        r"$\Gamma_{Z} %s (input)"%GeV,          "GAUSS", 2.4952,   [0.0023] )
        "Rb->sg"       : Var( "R(b->sg)",     r"$R(b\rightarrow s\gamma)$",           "GAUSS", 1.117,    [0.12] )
        "RD_ms"        : Var( "RD_ms",        r"$R(\Delta_{ms}$",                     "GAUSS", 0.97,     [0.01, 0.27] )
        "Bsmumu"       : Var( "Bsmumu",       r"$BR(B_{s}\rightarrow\mu^{+}\mu^{-})", "UL",    4.6E-8,   [0.1E-9, 0.2E-9] )
        "R(B->taunu)"  : Var( "R(B->taunu)",  r"$R(B\rightarrow\tau\nu)$",            "GAUSS", 1.43,     [0.43] )
        "R(B->Xsll)"   : Var( "R(B->Xsll)",   r"$R(B\rightarrow X_{s}\ell\ell$",      "GAUSS", 0.99,     [0.32, 0.00] )
        "R(K->lnu)"    : Var( "R(K->lnu)",    r"$R(K\rightarrow\ell\nu)$",            "GAUSS", 1.008,    [0.014 ] )
        "Delta(g-2)"   : Var( "Delta(g-2)",   r"$\Delta(g-2)_{\mu}$",                 "GAUSS", 30.2E-10, [8.8E-10, 2.0E-10] )
        "MW"           : Var( "MW",           r"$m_{W} %s$"%GeVc2,                    "GAUSS", 80.399,   [0.023, 0.01] )
        "sintheta_eff" : Var( "sintheta_eff", r"$\sin(\theta_{eff}) (Q_{fb})$",       "GAUSS", 0.2324,   [0.0012] )
        "GZ_in"        : Var( "GZ_in",        r"$\Gamma_{Z} %s"%MeV,                  "GAUSS", 2495.2,   [2.3, 1.0] )
        "Rl"           : Var( "Rl",           r"$R_{\ell}$",                          "GAUSS", 20.767,   [0.025] )
        "Rb"           : Var( "Rb",           r"$R_{b}$",                             "GAUSS", 0.21629,  [0.00066] )
        "Rc"           : Var( "Rc",           r"$R_{c}$",                             "GAUSS", 0.1721,   [0.00066] )
        "Afb(b)"       : Var( "Afb(b)",       r"$A_{fb}(b)$",                         "GAUSS", 0.0992,   [0.0016] )
        "Afb(c)"       : Var( "Afb(c)",       r"$A_{fb}(c)$",                         "GAUSS", 0.0707,   [0.0035] )
        "Ab16"         : Var( "Ab16",         r"$A_{b}$",                             "GAUSS", 0.923,    [0.020] )
        "Ac17"         : Var( "Ac17",         r"$A_{c}$",                             "GAUSS", 0.670,    [0.027] )
        "Al(SLD)"      : Var( "Al(SLD)",      r"$A_{\ell} (SLD)$",                    "GAUSS", 0.1513,   [0.0021] )
        "m_h^0"        : Var( "m_h^0",        r"$M_{h^{0}} [GeV/c^{2}]$",             "LL",    115.0,    [1.1, 1.5] )
        "Oh^2"         : Var( "Oh^2",         r"$\Omega h^{2}$",                      "GAUSS", 0.1109,   [0.0056, 0.012] )
        "Al(P_tau)"    : Var( "Al(P_tau)",    r"$A\ell (P_{\tau})$",                  "GAUSS", 0.1465,   [0.0032] )
        "Al_fb"        : Var( "Al_fb",        r"$A\ell FB$",                          "GAUSS", 0.01714,  [0.00095] )
        "sigma_had^0"  : Var( "sigma_had^0",  r"$\sigma_{had}^{0} (nb)$",             "GAUSS", 41.540,   [0.037] )
        "R(Delta_md)"  : Var( "R(Delta_md)",  r"$R(\Delta_{md})$",                    "GAUSS", 1.05,     [0.01, 0.34] )
        "R(Delta_mk)"  : Var( "R(Delta_mk)",  r"$R(\Delta_{mk})$",                    "GAUSS", 1.08,     [0.00, 0.14] )
        "R(Kp->pinn)"  : Var( "R(Kp->pinn)",  r"$R(K\pi\rightarrow\pi nn)$",          "UL",    4.5,      [0.01] )
        "BR(Bd->ll)"   : Var( "BR(Bd->ll)",   r"$BR(B_{d}\rightarrow\ell\ell$",       "UL",    2.3E-8,   [0.0, 0.2E-9] )
        "R(Dms)/R(Dmd)": Var( "R(Dms)/R(Dmd)" r"$R(\Delta_{ms})/R(\Delta_{md})$",     "GAUSS", 1.00,     [0.01, 0.13] )
        "D_0(K*g)"     : Var( "D_0(K*g)",     r"$\Delta_{0}(K^{*}\gamma$",            "GAUSS", 0.028,    [0.023, 0.024] )
        "BR(b->sg)"    : Var( "BR(b->sg)",    r"$BR(b\rightarrow s\gamma)$",          "GAUSS", 1.117,    [0.12] )
        "sigma_pp^SI"  : Var( "sigma_pp^SI",  r"$\sigma_{p}^{SI}$",                   "GAUSS", 0.00,     [0.00] )
    }
