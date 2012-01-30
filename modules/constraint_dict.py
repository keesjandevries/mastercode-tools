#!/usr/bin/env python

def get_constraint_dict() :
    c_type = [ "GAUSS", "UL", "LL" ]
    GAUSS = c_type[0]
    UL    = c_type[1]
    LL    = c_type[2]

    d = { 
          "mtop"              : [ 173.2   , [0.9    , 0.     ], GAUSS, "m_{top}"                            ],
          "MZ"                : [ 91.1875 , [0.0021 , 0.     ], GAUSS, "M_{Z}"                              ],
          "Gamma_Z_in"        : [ 2.4952  , [0.0023 , 0.     ], GAUSS, "#Gamma_{Z}"                         ],
          "DeltaAlphaHad"     : [ 0.027490, [0.00010, 0.     ], GAUSS, "#Delta#alpha_{had}"                 ],
          "R(b->sg)"          : [ 1.117   , [0.12   , 0.0    ], GAUSS, "R(b#rightarrow s#gamma"             ],
          "R(Delta_ms)"       : [ 0.97    , [0.01   , 0.27   ], GAUSS, "R(#Delta_{ms}"                      ],
          "BR(Bs->mumu)"      : [ 4.7E-8  , [0.1E-9 , 0.2E-9 ], UL   , "BR(B_{s}#rightarrow #mu^{+}#mu^{-}" ],
          "R(B->taunu)"       : [ 1.43    , [0.43   , 0.0    ], GAUSS, "R(B#rightarrow#tau#nu)"             ],
          "R(B->Xsll)"        : [ 0.99    , [0.32   , 0.00   ], GAUSS, "R(B#rightarrow X_{s}#ell#ell"       ],
          "R(K->lnu)"         : [ 1.008   , [0.014  , 0.000  ], GAUSS, "R(K#rightarrow#ell#nu)"             ],
          "Delta(g-2)"        : [ 30.2E-10, [8.8E-10, 2.0E-10], GAUSS, "#Delta(g-2)"                        ],
          "MW"                : [ 80.399  , [0.023  , 0.010  ], GAUSS, "M_{W} [GeV/c^{2}]"                  ],
          "sintheta_eff(Qfb)" : [ 0.2324  , [0.0012 , 0.     ], GAUSS, "sin(#theta_{eff}) (Q_{fb})"         ],
          "Gamma_Z"           : [ 2495.2  , [2.3    , 1.0    ], GAUSS, "#Gamma_{Z}"                         ],
          "Rl"                : [ 20.767  , [0.025  , 0.     ], GAUSS, "R_{#ell}"                           ],
          "Rb"                : [ 0.21629 , [0.00066, 0.     ], GAUSS, "R_{b}"                              ],
          "Rc"                : [ 0.1721  , [0.003  , 0.     ], GAUSS, "R_{c}"                              ],
          "Afb(b)"            : [ 0.0992  , [0.0016 , 0.     ], GAUSS, "A_{fb}(b)"                          ],
          "Afb(c)"            : [ 0.0707  , [0.0035 , 0.     ], GAUSS, "A_{fb}(c)"                          ],
          "Ab16"              : [ 0.923   , [0.020  , 0.     ], GAUSS, "A_{b}"                              ],
          "Ac17"              : [ 0.670   , [0.027  , 0.     ], GAUSS, "A_{c}"                              ],
          "Al(SLD)"           : [ 0.1513  , [0.0021 , 0.     ], GAUSS, "A_{#ell} (SLD)"                     ],
          "m_h^0"             : [ 115.0   , [1.1    , 1.5    ], LL   , "M_{h^{0}} [GeV/c^{2}]"              ],
          "Omegah^2"          : [ 0.1109  , [0.0056 , 0.012  ], GAUSS, "#Omega h^{2}"                       ],
          "Al(P_tau)"         : [ 0.1465  , [0.0032 , 0.     ], GAUSS, "A#ell (P_{#tau})"                   ],
          "Al_fb"             : [ 0.01714 , [0.00095, 0.     ], GAUSS, "A#ell FB"                           ],
          "sigma_had^0"       : [ 41.540  , [0.037  , 0.     ], GAUSS, "#sigma_{had}^{0} (nb)"              ],
          "R(Delta_md)"       : [ 1.05    , [0.01   , 0.34   ], GAUSS, "R(#Delta_{md})"                     ],
          "R(Delta_mk)"       : [ 1.08    , [0.00   , 0.14   ], GAUSS, "R(#Delta_{mk})"                     ],
          "R(Kp->pinn)"       : [ 4.5     , [0.01   , 0.0    ], UL   , "R(K#pi#rightarrow#pi nn)"           ],
          "BR(Bd->ll)"        : [ 2.3E-8  , [0.0    , 0.2E-9 ], UL   , "BR(B_{d}#rightarrow#ell#ell"        ],
          "R(Dms)/R(Dmd)"     : [ 1.00    , [0.01   , 0.13   ], GAUSS, "R(#Delta_{ms})/R(#Delta_{md})"      ],
          "Delta_0(K*gamma)"  : [ 0.028   , [0.023  , 0.024  ], GAUSS, "#Delta_{0}(K^{*}#gamma"             ],
          "BR(b->sg)"         : [ 1.117   , [0.12   , 0.0    ], GAUSS, "BR(b#rightarrow s#gamma)"           ],
          "sigma_pp^SI"       : [ 0.00    , [0.00   , 0.0    ], GAUSS, "#sigma_{p}^{SI}"                    ]
        }                                                               
    return d
