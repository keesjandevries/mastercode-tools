from modules.mcvariable import DerivedMCVariable as DMCV
from modules.mcvariable import MCVariable as MCV
from modules.mcvariable import Variable as Var

GeVc2="[GeV/c^{2}]"
GeV  ="[GeV]"
MeV  ="[MeV]"

def mc_variables() :
    b=base_variables()
    f=get_variables_funtions()
    m={
            # inputs
            "m0"           : MCV( b["m0"],            index_offset=1 ),
            "m12"          : MCV( b["m12"],           index_offset=2 ),
            "A0"           : MCV( b["A0"],            index_offset=3 ),
            "tanb"         : MCV( b["tanb"],          index_offset=4 ),
            "mh2"          : MCV( b["mh2" ],          index_offset=6 ),
            "mhd2"         : MCV( b["mhd2"],          index_offset=6 ),
            "mhu2"         : MCV( b["mhu2"],          index_offset=7 ),
            "mtop"         : MCV( b["mtop"],          index_offset=-4, offset_relative_to="PredictionIndex"  ),
            "MZ"           : MCV( b["MZ"],            index_offset=-3, offset_relative_to="PredictionIndex"  ),
            "GZ_in"        : MCV( b["GZ_in"],         index_offset=-2, offset_relative_to="PredictionIndex"  ),
            "DAlpha_had"   : MCV( b["DAlpha_had"],    index_offset=-1, offset_relative_to="PredictionIndex"  ),
            # predictions
            "R(b->sg)"     : MCV( b["R(b->sg)"],      index_offset=0,  offset_relative_to="PredictionIndex" ),
            "R(D_ms)"      : MCV( b["R(D_ms)"],       index_offset=1,  offset_relative_to="PredictionIndex" ),
            "Bsmumu"       : MCV( b["Bsmumu"],        index_offset=2,  offset_relative_to="PredictionIndex" ),
            "R(B->taunu)"  : MCV( b["R(B->taunu)"],   index_offset=3,  offset_relative_to="PredictionIndex" ),
            "R(B->Xsll)"   : MCV( b["R(B->Xsll)"],    index_offset=4,  offset_relative_to="PredictionIndex" ),
            "R(K->lnu)"    : MCV( b["R(K->lnu)"],     index_offset=5,  offset_relative_to="PredictionIndex" ),
            "Delta(g-2)"   : MCV( b["Delta(g-2)"],    index_offset=6,  offset_relative_to="PredictionIndex" ),
            "MW"           : MCV( b["MW"],            index_offset=7,  offset_relative_to="PredictionIndex" ),
            "sintheta_eff" : MCV( b["sintheta_eff"],  index_offset=8,  offset_relative_to="PredictionIndex" ),
            "Gamma_Z"      : MCV( b["Gamma_Z"],       index_offset=9,  offset_relative_to="PredictionIndex" ),
            "Rl"           : MCV( b["Rl"],            index_offset=10, offset_relative_to="PredictionIndex" ),
            "Rb"           : MCV( b["Rb"],            index_offset=11, offset_relative_to="PredictionIndex" ),
            "Rc"           : MCV( b["Rc"],            index_offset=12, offset_relative_to="PredictionIndex" ),
            "Afb(b)"       : MCV( b["Afb(b)"],        index_offset=13, offset_relative_to="PredictionIndex" ),
            "Afb(c)"       : MCV( b["Afb(c)"],        index_offset=14, offset_relative_to="PredictionIndex" ),
            "Ab16"         : MCV( b["Ab16"],          index_offset=15, offset_relative_to="PredictionIndex" ),
            "Ac17"         : MCV( b["Ac17"],          index_offset=16, offset_relative_to="PredictionIndex" ),
            "Al(SLD)"      : MCV( b["Al(SLD)"],       index_offset=17, offset_relative_to="PredictionIndex" ),
            "m_h^0"        : MCV( b["m_h^0"],         index_offset=18, offset_relative_to="PredictionIndex" ),
            "Oh^2"         : MCV( b["Oh^2"],          index_offset=19, offset_relative_to="PredictionIndex" ),
            "Al(P_tau)"    : MCV( b["Al(P_tau)"],     index_offset=20, offset_relative_to="PredictionIndex" ),
            "Al_fb"        : MCV( b["Al_fb"],         index_offset=21, offset_relative_to="PredictionIndex" ),
            "sigma_had^0"  : MCV( b["sigma_had^0"],   index_offset=22, offset_relative_to="PredictionIndex" ),
            "R(Delta_md)"  : MCV( b["R(Delta_md)"],   index_offset=23, offset_relative_to="PredictionIndex" ),
            "R(Delta_mk)"  : MCV( b["R(Delta_mk)"],   index_offset=24, offset_relative_to="PredictionIndex" ),
            "R(Kp->pinn)"  : MCV( b["R(Kp->pinn)"],   index_offset=25, offset_relative_to="PredictionIndex" ),
            "BR(Bd->ll)"   : MCV( b["BR(Bd->ll)"],    index_offset=26, offset_relative_to="PredictionIndex" ),
            "R(Dms)/R(Dmd)": MCV( b["R(Dms)/R(Dmd)"], index_offset=27, offset_relative_to="PredictionIndex" ),
            "D_0(K*g)"     : MCV( b["D_0(K*g)"],      index_offset=28, offset_relative_to="PredictionIndex" ),
            "BR(b->sg)"    : MCV( b["BR(b->sg)"],     index_offset=29, offset_relative_to="PredictionIndex" ),
            "mu"           : MCV( b["mu"       ],     index_offset=32, offset_relative_to="PredictionIndex" ),
            "sigma_pp^SI"  : MCV( b["sigma_pp^SI"],   index_offset=33, offset_relative_to="PredictionIndex" ),
            "KOsigma_pp^SI"  : MCV( b["KOsigma_pp^SI"],   index_offset=64, offset_relative_to="PredictionIndex" ),
            "KOsigma_pp^SI_cen50"  : MCV( b["KOsigma_pp^SI_cen50"],   index_offset=107, offset_relative_to="PredictionIndex" ),
            "KOsigma_pp^SI_unc50_14"  : MCV( b["KOsigma_pp^SI_unc50_14"],   index_offset=108, offset_relative_to="PredictionIndex" ),
            "KOsigma_pp^SI_unc50_7"   : MCV( b["KOsigma_pp^SI_unc50_7"] ,   index_offset=110, offset_relative_to="PredictionIndex" ),
            "mA0^2"        : MCV( b["mA0^2"],         index_offset=35, offset_relative_to="PredictionIndex" ),
            # Spectrum
            "chi1"         : MCV( b["chi1"],          index_offset=0,  offset_relative_to="SpectrumIndex" ),
            "chi2"         : MCV( b["chi2"],          index_offset=1,  offset_relative_to="SpectrumIndex" ),
            "neu1"         : MCV( b["neu1"],          index_offset=2,  offset_relative_to="SpectrumIndex" ),
            "neu2"         : MCV( b["neu2"],          index_offset=3,  offset_relative_to="SpectrumIndex" ),
            "neu3"         : MCV( b["neu3"],          index_offset=4,  offset_relative_to="SpectrumIndex" ),
            "neu4"         : MCV( b["neu4"],          index_offset=5,  offset_relative_to="SpectrumIndex" ),
            "sel_r"        : MCV( b["sel_r"],         index_offset=6,  offset_relative_to="SpectrumIndex" ),
            "sel_l"        : MCV( b["sel_l"],         index_offset=7,  offset_relative_to="SpectrumIndex" ),
            "snu_e"        : MCV( b["snu_e"],         index_offset=8,  offset_relative_to="SpectrumIndex" ),
            "smu_r"        : MCV( b["smu_r"],         index_offset=9,  offset_relative_to="SpectrumIndex" ),
            "smu_l"        : MCV( b["smu_l"],         index_offset=10, offset_relative_to="SpectrumIndex" ),
            "snu_mu"       : MCV( b["snu_mu"],        index_offset=11, offset_relative_to="SpectrumIndex" ),
            "stau_1"       : MCV( b["stau_1"],        index_offset=12, offset_relative_to="SpectrumIndex" ),
            "stau_2"       : MCV( b["stau_2"],        index_offset=13, offset_relative_to="SpectrumIndex" ),
            "snu_tau"      : MCV( b["snu_tau"],       index_offset=14, offset_relative_to="SpectrumIndex" ),
            "squark_r"     : MCV( b["squark_r"],      index_offset=15, offset_relative_to="SpectrumIndex" ),
            "squark_l"     : MCV( b["squark_l"],      index_offset=16, offset_relative_to="SpectrumIndex" ),
            "stop1"        : MCV( b["stop1"],         index_offset=17, offset_relative_to="SpectrumIndex" ),
            "stop2"        : MCV( b["stop2"],         index_offset=18, offset_relative_to="SpectrumIndex" ),
            "sbottom1"     : MCV( b["sbottom1"],      index_offset=19, offset_relative_to="SpectrumIndex" ),
            "sbottom2"     : MCV( b["sbottom2"],      index_offset=20, offset_relative_to="SpectrumIndex" ),
            "gluino"       : MCV( b["gluino"],        index_offset=21, offset_relative_to="SpectrumIndex" ),
            "mh0"          : MCV( b["mh0"],           index_offset=22, offset_relative_to="SpectrumIndex" ),
            "mH0"          : MCV( b["mH0"],           index_offset=23, offset_relative_to="SpectrumIndex" ),
            "mA0"          : MCV( b["mA0"],           index_offset=24, offset_relative_to="SpectrumIndex" ),
            "mH+-"         : MCV( b["mH+-"],          index_offset=25, offset_relative_to="SpectrumIndex" ),
            "ssmh0"        : MCV( b["ssmh0"],         index_offset=30, offset_relative_to="SpectrumIndex" ),
            "ssmH0"        : MCV( b["ssmH0"],         index_offset=31, offset_relative_to="SpectrumIndex" ),
            "ssmA0"        : MCV( b["ssmA0"],         index_offset=32, offset_relative_to="SpectrumIndex" ),
            "ssmH+-"       : MCV( b["ssmH+-"],        index_offset=33, offset_relative_to="SpectrumIndex" ),
            "BsmumuRatio"  : DMCV(b["BsmumuRatio"],     f["BsmumuRatio"] ,  ["Bsmumu"] ),
            "Dm_stau1_neu1": DMCV(b["Dm_stau1_neu1"],   f["Dm_stau1_neu1"] ,["stau_1","neu1"] ),
#            "BsmumuRatio"  : DMCV(b["BsmumuRatio"], ["Bsmumu"] ),
            "sigma_pp^SI_cm-2"  : DMCV(b["sigma_pp^SI_cm-2"], f["sigma_pp^SI_cm-2"],["sigma_pp^SI"]   )
    }
    return m

def base_variables() :
    return {
        "m0"           : Var( "m0",            r"$m_{0} %s$"%GeV ),
        "m12"          : Var( "m12",           r"$m_{1/2} %s$"%GeV ),
        "A0"           : Var( "A0",            r"$A_{0} %s$"%GeV ),
        "tanb"         : Var( "tanb",          r"$\tan(\beta)$" ),
        "mhd2"         : Var( "mhd2",          r"$m_{H_{d}}^{2} %s^{2}$"%GeV       ),                
        "mhu2"         : Var( "mhu2",          r"$m_{H_{u}}^{2} %s^{2}$"%GeV       ),                
        "mh2"          : Var( "mh2" ,          r"$m_{H}^{2} %s^{2}$"%GeV           ),                
        "mtop"         : Var( "mtop",          r"$m_{t} %s$"%GeV                   ),                
        "MZ"           : Var( "MZ",            r"$m_{Z} %s$"%GeV                   ),
        "GZ_in"        : Var( "GZ_in",         r"$\Gamma_{Z} %s (input)"%GeV         ),
        "DAlpha_had"   : Var( "DAlpha_had",    r"$\Delta\alpha_{had}$"               ),
        "R(b->sg)"     : Var( "R(b->sg)",      r"$R(b\rightarrow s\gamma)$"          ),
        "R(D_ms)"      : Var( "R(D_ms)",       r"$R(\Delta_{ms}$"                    ),
        "Bsmumu"       : Var( "Bsmumu",        r"$BR(B_{s}\rightarrow\mu^{+}\mu^{-})$"),
        "BsmumuRatio"  : Var( "BsmumuRatio",   r"$BR(B_{s}\rightarrow\mu^{+}\mu^{-})^{pred} /BR(B_{s}\rightarrow\mu^{+}\mu^{-})^{SM} $"),
        "Dm_stau1_neu1": Var( "Dm_stau1_neu1", r"$m_{\tilde{\tau}_{1}} - m_{\tilde{\chi}^{0}_{1}} %s $"%GeV),
        "R(B->taunu)"  : Var( "R(B->taunu)",   r"$R(B\rightarrow\tau\nu)$"           ),
        "R(B->Xsll)"   : Var( "R(B->Xsll)",    r"$R(B\rightarrow X_{s}\ell\ell$"     ),
        "R(K->lnu)"    : Var( "R(K->lnu)",     r"$R(K\rightarrow\ell\nu)$",          ),
        "Delta(g-2)"   : Var( "Delta(g-2)",    r"$\Delta(g-2)_{\mu}$",               ),
        "MW"           : Var( "MW",            r"$m_{W} %s$"%GeV,                  ),
        "sintheta_eff" : Var( "sintheta_eff",  r"$\sin(\theta_{eff}) (Q_{fb})$",     ),
        "Gamma_Z"      : Var( "Gamma_Z",       r"$\Gamma_{Z} %s"%MeV,                ),
        "Rl"           : Var( "Rl",            r"$R_{\ell}$",                        ),
        "Rb"           : Var( "Rb",            r"$R_{b}$",                           ),
        "Rc"           : Var( "Rc",            r"$R_{c}$",                           ),
        "Afb(b)"       : Var( "Afb(b)",        r"$A_{fb}(b)$",                       ),
        "Afb(c)"       : Var( "Afb(c)",        r"$A_{fb}(c)$",                       ),
        "Ab16"         : Var( "Ab16",          r"$A_{b}$",                           ),
        "Ac17"         : Var( "Ac17",          r"$A_{c}$",                           ),
        "Al(SLD)"      : Var( "Al(SLD)",       r"$A_{\ell} (SLD)$",                  ),
        "m_h^0"        : Var( "m_h^0",         r"$M_{h} [GeV]$",           ),
        "Oh^2"         : Var( "Oh^2",          r"$\Omega h^{2}$",                    ),
        "Al(P_tau)"    : Var( "Al(P_tau)",     r"$A\ell (P_{\tau})$",                ),
        "Al_fb"        : Var( "Al_fb",         r"$A\ell FB$",                        ),
        "sigma_had^0"  : Var( "sigma_had^0",   r"$\sigma_{had}^{0} (nb)$",           ),
        "R(Delta_md)"  : Var( "R(Delta_md)",   r"$R(\Delta_{md})$",                  ),
        "R(Delta_mk)"  : Var( "R(Delta_mk)",   r"$R(\Delta_{mk})$",                  ),
        "R(Kp->pinn)"  : Var( "R(Kp->pinn)",   r"$R(K\pi\rightarrow\pi nn)$",        ),
        "BR(Bd->ll)"   : Var( "BR(Bd->ll)",    r"$BR(B_{d}\rightarrow\ell\ell$",     ),
        "R(Dms)/R(Dmd)": Var( "R(Dms)/R(Dmd)", r"$R(\Delta_{ms})/R(\Delta_{md})$",   ),
        "D_0(K*g)"     : Var( "D_0(K*g)",      r"$\Delta_{0}(K^{*}\gamma$",          ),
        "BR(b->sg)"    : Var( "BR(b->sg)",     r"$BR(b\rightarrow s\gamma)$",        ),
        "sigma_pp^SI"  : Var( "sigma_pp^SI",   r"$\sigma_{p}^{SI}$" ),
        "KOsigma_pp^SI"  : Var( "KOsigma_pp^SI",   r"$\sigma_{p}^{SI}$" ),
        "KOsigma_pp^SI_cen50"  : Var( "KOsigma_pp^SI_cen50",   r"$\sigma_{p}^{SI}$" ),
        "KOsigma_pp^SI_unc50_14"  : Var( "KOsigma_pp^SI_unc50_14",   r"$\sigma_{p}^{SI}$" ),
        "KOsigma_pp^SI_unc50_7"   : Var( "KOsigma_pp^SI_unc50_7",   r"$\sigma_{p}^{SI}$" ),
        "sigma_pp^SI_cm-2"  : Var( "sigma_pp^SI_cm-2",   r"$\sigma_{p}^{SI} [cm^{2}] $" ),
        "mu"           : Var( "mu"   ,         r"$\mu$"                        ),
        "mA0^2"        : Var( "mA0^2",         r"$M_{A}^2 %s^{2} $" %GeV ),
        "chi1"         : Var( "chi1",          r"$m_{\tilde{\chi}^{\pm}_{1}} %s$"%GeV ),
        "chi2"         : Var( "chi2",          r"$m_{\tilde{\chi}^{\pm}_{2}} %s$"%GeV ),
        "neu1"         : Var( "neu1",          r"$m_{\tilde{\chi}^{0}_{1}} %s$"%GeV ),
        "neu2"         : Var( "neu2",          r"$m_{\tilde{\chi}^{0}_{2}} %s$"%GeV ),
        "neu3"         : Var( "neu3",          r"$m_{\tilde{\chi}^{0}_{3}} %s$"%GeV ),
        "neu4"         : Var( "neu4",          r"$m_{\tilde{\chi}^{0}_{4}} %s$"%GeV ),
        "sel_r"        : Var( "sel_r",         r"$m_{\tilde{e}_{r}} %s$"%GeV ),
        "sel_l"        : Var( "sel_l",         r"$m_{\tilde{e}_{l}} %s$"%GeV ),
        "snu_e"        : Var( "snu_e",         r"$m_{\tilde{\nu}_{e}} %s$"%GeV ),
        "smu_r"        : Var( "smu_r",         r"$m_{\tilde{\mu}_{r}} %s$"%GeV ),
        "smu_l"        : Var( "smu_l",         r"$m_{\tilde{\mu}_{l}} %s$"%GeV ),
        "snu_mu"       : Var( "snu_mu",        r"$m_{\tilde{\nu}_{\mu}} %s$"%GeV ),
        "stau_1"       : Var( "stau_1",        r"$m_{\tilde{\tau}_{1}} %s$"%GeV ),
        "stau_2"       : Var( "stau_2",        r"$m_{\tilde{\tau}_{2}} %s$"%GeV ),
        "snu_tau"      : Var( "snu_tau",       r"$m_{\tilde{\nu}_{\tau}} %s$"%GeV ),
#        "squark_r"     : Var( "squark_r",      r"$m_{\tilde{q}_{r}} %s \textrm{(average)}$"%GeV ), FIXME: \textrm is not accepted
        "squark_r"     : Var( "squark_r",      r"$m_{\tilde{q}_{R}} %s}$"%GeV ), 
#        "squark_l"     : Var( "squark_l",      r"$m_{\tilde{q}_{l}} %s \textrm{(average)}$"%GeV ), FIXME: same
        "squark_l"     : Var( "squark_l",      r"$m_{\tilde{q}_{L}} %s}$"%GeV ),
        "stop1"        : Var( "stop1",         r"$m_{\tilde{t}_{1}} %s$"%GeV ),
        "stop2"        : Var( "stop2",         r"$m_{\tilde{t}_{2}} %s$"%GeV ),
        "sbottom1"     : Var( "sbottom1",      r"$m_{\tilde{b}_{1}} %s$"%GeV ),
        "sbottom2"     : Var( "sbottom2",      r"$m_{\tilde{b}_{2}} %s$"%GeV ),
        "gluino"       : Var( "gluino",        r"$m_{\tilde{g}} %s$"%GeV ),
        "mh0"          : Var( "mh0",           r"$m_{h^{0}} %s$"%GeV ),
        "mH0"          : Var( "mH0",           r"$m_{H^{0}} %s$"%GeV ),
        "mA0"          : Var( "mA0",           r"$M_{A} %s$"%GeV ),
        "mH+-"         : Var( "mH+-",          r"$m_{H^{\pm}} %s$"%GeV ),
        "ssmh0"        : Var( "ssmh0",           r"$m_{h^{0}} %s$"%GeV ),
        "ssmH0"        : Var( "ssmH0",           r"$m_{H^{0}} %s$"%GeV ),
        "ssmA0"        : Var( "ssmA0",           r"$m_{A^{0}} %s$"%GeV ),
        "ssmH+-"       : Var( "ssmH+-",          r"$m_{H^{\pm}} %s$"%GeV ),
    }

def get_variables_funtions():
    function_dict= {
       "BsmumuRatio" :  get_bsmumu_ratio,
       "Dm_stau1_neu1" :  get_delta_mstau1_mneu1,
       "sigma_pp^SI_cm-2" : get_sigma_pp_si_cm
    }
    return function_dict

def get_delta_mstau1_mneu1(vals):
    mstau1=vals[0]
    mneu1 =vals[1]
    return mstau1-mneu1

def get_bsmumu_ratio(vals):
    bsmm=vals[0]
    return (bsmm/3.46e-9)


def get_sigma_pp_si_cm(vals):
    ssi=vals[0]
    return (ssi*1e-36)


#def x2_from_ssi_mchi_lhood(mchi,ssi ):
#    return 1
#
#
#def get_sigma_pp_si_cm_KO(vals):
#    mchi=vals[0]
##    ssiMicr=vals[1]
#    ssiKOs=vals[1:21]
#    ZSigPiNs=[0,0, 0.2,-0.,2, 0.4,-0.4, 0.6,-0.6, 0.8,-0.8, 1.0,-1.0,
#               1.33,-1.33, 1.66,-1.66, 2.0,-2.0, 2.5,-2.5, 3.0,-3.0]
#    X2s=[Z**2 + x2_from_ssi_mchi_lhood(mchi,ssi ) for Z,ssi in zip(ZSigPiNs, ssiKOs ) ]
#    ssiKO=ssiKOs[ X2s.index(min(X2s))  ]
#    return (ssiKO*1e-36)
