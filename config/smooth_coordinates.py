from modules.file_dicts import base_directory


def get_smooth_coordinates_dict():
    d={ "%s/recalc_out.root" % base_directory() : 
            {"stau_1":
                [
                    [1000. , 2000. ,50],
                ]        
            },
############################################################
        "%s/nuhm1_mc8_drop_mh.root" % base_directory():
            {"m_h^0":
                [
                    [108.3  ,   127. , 200  ],
#                    [117.8  ,   123. ,  50  ],
#                   [114.0  ,   127. , 50   ],
#                   [129.0  ,   123. , 100  ],
                ]        
            },
############################################################
        "%s/cmssm_mc8_drop_mh.root" % base_directory():
            {"m_h^0":
                [
                    [108.3  ,   127. , 200 ],
#                    [108.3  ,   112. ,100 ],
#                    [124.0  ,   126. , 50 ],
                 #   [114.0  ,   127. , 10   ],
                 #   [119.0  ,   125. , 100  ],
                ]        
            },
############################################################
#        "%s/nuhm1_mcmh_mh125.root" % base_directory():
        "%s/nuhm1_mcmh_mh125_ssi.root" % base_directory():
            {
                "stau_1":
                [
                    [463  ,   3800 , 10 ],
                    [900  ,   3800 , 40 ],
                ],
                "stop1":
                [
                    [1000 ,   4800 ,  5 ],
                    [3000 ,   4700 , 10 ],
                ],
                "gluino":
                [
                    [1400 ,   6000 ,  5 ],
                    [3000 ,   6000 , 25 ],
                    [4000 ,   5500 , 25 ],
                ],
                "squark_r":
                [
                    [1200 ,   5600 , 10 ],
                    [3000 ,   5400 , 10 ],
                ],
                "BsmumuRatio" :
                [
                    [0.6  ,   0.85 ,  5 ],
                    [1.   ,   1.63 ,  2 ],
                    [1.63 ,   3.   ,  2 ],
                    [1.25 ,   1.63 , 10 ],
                    [1.63 ,   3.   , 10 ],
                    [1.55 ,   3.   , 50 ],
                ],
            },
############################################################
        "%s/nuhm1_mc8_all.root" % base_directory():
            {
                "stau_1":
                [
                    [463  ,   2500 , 10 ],
                    [900  ,   2500 , 10 ],
                    [1800 ,   2500 , 10 ],
                    [2400 ,   2900 , 10 ],
                    [3000 ,   4000 , 40 ],
                ],
                "stop1":
                [
                    [ 900 ,   1686 ,  5 ],
                    [1686 ,   4800 ,  5 ],
                    [3000 ,   4700 , 10 ],
                ],
                "gluino":
                [
#                    [1400 ,   2132 ,  5 ],
#                    [2132 ,   6000 ,  5 ],
                    [1400 ,   6000 ,  5 ],
                    [3000 ,   6000 , 25 ],
                    [4000 ,   5500 , 25 ],
                ],
                "squark_r":
                [
                    [1200 ,   5600 , 10 ],
                    [3000 ,   5400 , 10 ],
                ],
                "BsmumuRatio" :
                [
                    [0.5  ,   0.95 , 20 ],
                    [1.   ,  1.1   ,  2 ],
                    [1.1  ,  2.5   ,  2 ],
                ],
            },
############################################################
        "%s/cmssm_mcmh_mh125_ssi.root" % base_directory():
            {
                "stau_1":
                [
                    [300. , 1000.   ,  5 ],
                    [750. , 1500.   ,  5 ],
                    [1000., 3960.   , 25 ],
                ],
                "stop1":
                [
                    [ 800 ,   4190 ,  5 ],
                ],
                "gluino":
                [
                    [ 700 ,   5240 ,  5 ],
                    [ 700 ,   1100 , 25 ],
                    [5240 ,   5700 , 25 ],
                ],
                "squark_r":
                [
                    [ 950 ,   5540 ,  5 ],
                    [4500 ,   5200 ,  5 ],
                ],
                "BsmumuRatio" :
                [
                    [0.6  ,   0.95 ,  5 ],
                    [0.95 ,  3.0   ,  1 ],
                    [1.   ,  3.0   , 50 ],
#                    [0.95 ,  3.0   ,  2 ],
                ],
            },
############################################################
        "%s/cmssm_mc8_all.root" % base_directory():
            {
                "stau_1":
                [
                    [190. , 3900.   ,  5 ],
#                    [300. , 1000.   ,  5 ],
#                    [750. , 1500.   ,  5 ],
#                    [1000., 3960.   , 25 ],
                ],
                "stop1":
                [
#                    [ 800 ,   1278 ,  10],
#                    [1278 ,   4190 ,  10],
                    [ 800 ,   4190 ,  10],
                ],
                "gluino":
                [
                    [ 700 ,   5240 ,  5 ],
                    [ 700 ,   1100 , 25 ],
                    [5240 ,   5700 , 25 ],
                ],
                "squark_r":
                [
                    [ 950 ,   5540 ,  5 ],
                    [4500 ,   5200 ,  5 ],
                ],
                "BsmumuRatio" :
                [
                    [0.6  ,   0.95 ,  5 ],
                    [0.95 ,  2.2   ,  1 ],
                    [1.   ,  2.2   , 5  ],
#                    [0.95 ,  3.0   ,  2 ],
                ],
                "Dm_stau1_neu1":
                [
                    [0.,   0.43    ,10],        
                    [0.43,  20.    ,10],        
                ],
            },
############################################################
        "%s/cmssm_mc8_all_tanb_cut.root" % base_directory():
            {
                "Dm_stau1_neu1":
                [
                    [0., 0.43,  20],        
                    [0., 0.53,   5],        
                    [0.43,9.,   10],        
                ],
            },
############################################################
        "%s/nuhm1_mc8_region_c_char_nlsp.root" % base_directory():
            {
#                "Dm_nslp_lsp":   # for stau_slp
#                [
#                    [0., 24.2,20],        
#                    [20., 24.2,20],        
#                    [24.5, 25.5,10],        
#                ],
                "Dm_nslp_lsp":
                [
                    [6.4, 25.,20],        
                    [10., 20.,200],        
                    [ 9., 21.,2],        
                ],
            },
############################################################
        "%s/cmssm_mc8_Nov12_bsmm.root" % base_directory():
            {
                "BsmumuRatio":
                [
                ],
            },
############################################################
        "%s/nuhm1_mc8_Nov12_bsmm.root" % base_directory():
            {
                "BsmumuRatio":
                [
                ],
            },
############################################################
        "%s/cmssm_mc8_HCP12_bsmm.root" % base_directory():
            {
                "gluino":
                [
                    [1150 ,   5240 ,  5 ],
#                   [1150 ,   1100 , 25 ],
                    [5240 ,   5700 , 25 ],
                ],
                "BsmumuRatio" :
                [
                    [0.6  ,   0.95 ,  5 ],
                    [0.95 ,  2.2   ,  1 ],
                    [1.   ,  2.5   , 5  ],
#                    [0.95 ,  3.0   ,  2 ],
                ],
            },
############################################################
        "%s/nuhm1_mc8_HCP12_bsmm.root" % base_directory():
            {
                "gluino":
                [
                    [1400 ,   6000 ,  5 ],
                    [3000 ,   6000 , 25 ],
                    [4000 ,   5500 , 25 ],
                ],
                "BsmumuRatio" :
                [
                    [0.5  ,   0.95 , 20 ],
                    [1.   ,  1.1   ,  2 ],
                    [1.1  ,  2.5   ,  2 ],
                ],
            },
############################################################
        "%s/cmssm_pre_lhc.root" % base_directory():
            {
                    "stau_1":
                    [
                        [1000, 3000, 10],
                        ],
                    "stop1":
                    [
                        [200, 500, 1],
                        [2000, 3500, 10],
                        ],
                    "gluino":
                    [
                        [300, 500, 1],
                        [2500, 4500, 10],
                        ],
                    "squark_r":
                    [
                        [2500,4000,1],
                        ],
                    "BsmumuRatio" :
                    [
                        [0.95,3.0,10],
                        ],
                    "m_h^0" :
                    [
                        #[],
                        ],
                    },
############################################################
        "%s/nuhm1_pre_lhc_including_cmssm.root" % base_directory():
            {
                    "stau_1":
                    [
                        [300., 1400., 5],
                        [1300., 2100, 100],
                        ],
                    "stop1":
                    [
                        [200, 500, 1],
                        [300, 600, 1],
                        [2000, 3500, 100],
                        [600, 2000, 5],
                        ],
                    "gluino":
                    [
                        [450, 700, 1],
                        [700, 3000, 5],
                        ],
                    "squark_r":
                    [
                        [400, 600, 1],
                        [600, 2500, 5],
                        [2500,3000,1000],
                        ],
                    "BsmumuRatio" :
                    [
                        [0.95,1.13,10],
                        [1.11,3.0,20]
                        ],
#                    "m_h^0" :
#                    [
#                        #[],
#                        ],
                    },

      }
    return d
