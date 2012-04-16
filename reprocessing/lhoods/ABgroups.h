#include "MultiAB.h"
#include "src/LHood.h"
#include "src/RadialLikelihood.h"
#include "src/CartesianLikelihood.h"
#include "src/FileConstants.h"

void mc6_lhoods_cmssm( std::vector<LHdata>&, FileInfo& );
void mc6_lhoods_nuhm1( std::vector<LHdata>&, FileInfo& );
void mc7_lhoods( std::vector<LHdata>&, FileInfo& );
void mc7_simple( std::vector<LHdata>&, FileInfo& );
void mc7_METBMM( std::vector<LHdata>&, FileInfo& );
void mc7_CDFBSMM( std::vector<LHdata>&, FileInfo& );
void mc7_wBMMnHTT( std::vector<LHdata>&, FileInfo& );
void mc7_nBMMwHTT( std::vector<LHdata>&, FileInfo& );
void mc7_nBMMnHTT( std::vector<LHdata>&, FileInfo& );
void mc7_xenonOnly( std::vector<LHdata>&, FileInfo& );

void diego_7pm2( std::vector<LHdata>&, FileInfo& );
void diego_35pm1( std::vector<LHdata>&, FileInfo& );

bool populate_lhoods( std::vector<LHdata>& lhoods, FileInfo& fInfo, int mode )
{
    bool ret_val = true;
    switch ( mode )
    {   
        case 5:
            mc6_lhoods_cmssm(lhoods,fInfo);
            break;
        case 6:
            mc6_lhoods_nuhm1(lhoods,fInfo);
            break;
        case 7:
            mc7_lhoods(lhoods,fInfo);
            break;
        case 777:
            mc7_simple(lhoods,fInfo);
            ret_val=true;
            break;
        case 74:
            mc7_METBMM(lhoods,fInfo);
            break;
        case 75:
            mc7_xenonOnly(lhoods,fInfo);
            break;
        case 76:
            mc7_CDFBSMM(lhoods,fInfo);
            break;
        case 77:
            mc7_wBMMnHTT(lhoods,fInfo);
            break;
        case 78:
            mc7_nBMMwHTT(lhoods,fInfo);
            break;
        case 79:
            mc7_nBMMnHTT(lhoods,fInfo);
            break;
        case 90:
            diego_7pm2(lhoods,fInfo);
            break;
        case 91:
            diego_35pm1(lhoods,fInfo);
            break;
        default:
            ret_val = false;
            std::cerr << "Tried to configure likelihoods" << 
                "with unknown option: " << mode << std::endl;
            break;
    }
    return ret_val;
}

void mc6_lhoods_cmssm( std::vector<LHdata>& lhoods, FileInfo& fInfo )
{
    lhoods.resize(5);    

    lhoods[0].lhood = new RadialLikelihood(1);
    lhoods[0].varX = 1;
    lhoods[0].varY = 2;
    lhoods[0].group = 1;
    lhoods[0].name = "CMS MEt 03/2011";

    lhoods[1].lhood = new RadialLikelihood(2);
    lhoods[1].varX = 1;
    lhoods[1].varY = 2;
    lhoods[1].group = 1;
    lhoods[1].name = "ATLAS 1l+0l 35pb^-1";

    lhoods[2].lhood = new CartesianLikelihood(1);
    lhoods[2].varX = fInfo.spec_index+2;
    lhoods[2].varY = fInfo.pred_index+64;
    lhoods[2].group = 2;
    lhoods[2].name = "Xenon100 2011";

    lhoods[3].lhood = new CartesianLikelihood(2);
    lhoods[3].varX = fInfo.pred_index+2;
    lhoods[3].varY = 0;
    lhoods[3].group = 3;
    lhoods[3].name = "LHCb/CDF/D0 Bsmumu MC6";

    lhoods[4].lhood = new CartesianLikelihood(3);
    lhoods[4].varX = fInfo.spec_index+24;
    lhoods[4].varY = 4;
    lhoods[4].group = 4;
    lhoods[4].name = "Htt CMSSM";
}

void mc6_lhoods_nuhm1( std::vector<LHdata>& lhoods, FileInfo& fInfo )
{
    lhoods.resize(5);    

    lhoods[0].lhood = new RadialLikelihood(1);
    lhoods[0].varX = 1;
    lhoods[0].varY = 2;
    lhoods[0].group = 1;
    lhoods[0].name = "CMS MEt 03/2011";

    lhoods[1].lhood = new RadialLikelihood(2);
    lhoods[1].varX = 1;
    lhoods[1].varY = 2;
    lhoods[1].group = 1;
    lhoods[1].name = "ATLAS 1l+0l 35pb^-1";

    lhoods[2].lhood = new CartesianLikelihood(1);
    lhoods[2].varX = fInfo.spec_index+2;
    lhoods[2].varY = fInfo.pred_index+64;
    lhoods[2].group = 2;
    lhoods[2].name = "Xenon100 2011";

    lhoods[3].lhood = new CartesianLikelihood(2);
    lhoods[3].varX = fInfo.pred_index+2;
    lhoods[3].varY = 0;
    lhoods[3].group = 3;
    lhoods[3].name = "LHCb/CDF/D0 Bsmumu MC6";

    lhoods[4].lhood = new CartesianLikelihood(4);
    lhoods[4].varX = fInfo.spec_index+24;
    lhoods[4].varY = 4;
    lhoods[4].group = 4;
    lhoods[4].name = "Htt NUHM1";
}

void mc7_lhoods( std::vector<LHdata>& lhoods, FileInfo& fInfo )
{
    lhoods.resize(5);
    lhoods[0].lhood = new RadialLikelihood(3);
    lhoods[0].varX = 1;
    lhoods[0].varY = 2;
    lhoods[0].group = 1;
    lhoods[0].name = "CMS Alpha_t 1.1fb^-1";

    lhoods[1].lhood = new RadialLikelihood(4);
    lhoods[1].varX = 1;
    lhoods[1].varY = 2;
    lhoods[1].group = 1;
    lhoods[1].name = "ATLAS 0l 1.04fb^-1";
    
    // Xenon
    lhoods[2].lhood = new CartesianLikelihood(1);
    lhoods[2].varX = fInfo.spec_index+2;
    lhoods[2].varY = fInfo.pred_index+64;
    lhoods[2].group = 2;
    lhoods[2].name = "Xenon100 2011";

    // BSMM LHCb CMS 
    lhoods[3].lhood = new CartesianLikelihood(6,0,0,0,Bsmumu_LHCb_CMS_file);
    lhoods[3].varX = fInfo.pred_index+2;
    lhoods[3].varY = 0;
    lhoods[3].group = 3;
    lhoods[3].name = "LHCb/CMS Bsmum mc7";

    // Just need an HA implementation
    lhoods[4].lhood = new CartesianLikelihood(9);
    lhoods[4].varX = fInfo.spec_index+24;
    lhoods[4].varY = 4;
    lhoods[4].group = 4;
    lhoods[4].name = "HA->tautau EPS";
}

void mc7_simple( std::vector<LHdata>& lhoods, FileInfo& fInfo )
{
    lhoods.resize(3);
    lhoods[0].lhood = new RadialLikelihood(3);
    lhoods[0].varX = 1;
    lhoods[0].varY = 2;
    lhoods[0].group = 1;
    lhoods[0].name = "CMS Alpha_t 1.1fb^-1";

    lhoods[1].lhood = new RadialLikelihood(4);
    lhoods[1].varX = 1;
    lhoods[1].varY = 2;
    lhoods[1].group = 1;
    lhoods[1].name = "ATLAS 0l 1.04fb^-1";
    
    // BSMM LHCb CMS 
    lhoods[2].lhood = new CartesianLikelihood(6,0,0,0,Bsmumu_LHCb_CMS_file);
    lhoods[2].varX = fInfo.pred_index+2;
    lhoods[2].varY = 0;
    lhoods[2].group = 2;
    lhoods[2].name = "LHCb/CMS Bsmumu mc7";

}

void diego_7pm2( std::vector<LHdata>& lhoods, FileInfo& fInfo )
{
    lhoods.resize(1);
    // BSMM LHCb CMS 
    lhoods[0].lhood = new CartesianLikelihood(-1,7e-9,2e-9);
    lhoods[0].varX = fInfo.pred_index+2;
    lhoods[0].varY = 0;
    lhoods[0].group = 1;
    lhoods[0].name = "Bsmumu (7.0 +/- 2.0)e-9";

}

void diego_35pm1( std::vector<LHdata>& lhoods, FileInfo& fInfo )
{
    lhoods.resize(1);
    // BSMM LHCb CMS 
    lhoods[0].lhood = new CartesianLikelihood(-1,3.5e-9,1e-9);
    lhoods[0].varX = fInfo.pred_index+2;
    lhoods[0].varY = 0;
    lhoods[0].group = 1;
    lhoods[0].name = "Bsmumu (3.5 +/- 1.0)e-9";

}

void mc7_METBMM( std::vector<LHdata>& lhoods, FileInfo& fInfo )
{
    lhoods.resize(3);
    lhoods[0].lhood = new RadialLikelihood(3);
    lhoods[0].varX = 1;
    lhoods[0].varY = 2;
    lhoods[0].group = 1;
    lhoods[0].name = "CMS Alpha_t 1.1fb^-1";

    lhoods[1].lhood = new RadialLikelihood(4);
    lhoods[1].varX = 1;
    lhoods[1].varY = 2;
    lhoods[1].group = 1;
    lhoods[1].name = "ATLAS 0l 1.04fb^-1";
    
    // BSMM:LHCb CMS 
    lhoods[2].lhood = new CartesianLikelihood(6,0,0,0,Bsmumu_LHCb_CMS_file);
    lhoods[2].varX = fInfo.pred_index+2;
    lhoods[2].varY = 0;
    lhoods[2].group = 2;
    lhoods[2].name = "LHCb/CMS Bsmum mc7";
}

void mc7_CDFBSMM( std::vector<LHdata>& lhoods, FileInfo& fInfo )
{
    lhoods.resize(5);
    lhoods[0].lhood = new RadialLikelihood(3);
    lhoods[0].varX = 1;
    lhoods[0].varY = 2;
    lhoods[0].group = 1;
    lhoods[0].name = "CMS Alpha_t 1.1fb^-1";

    lhoods[1].lhood = new RadialLikelihood(4);
    lhoods[1].varX = 1;
    lhoods[1].varY = 2;
    lhoods[1].group = 1;
    lhoods[1].name = "ATLAS 0l 1.04fb^-1";
    
    // Xenon
    lhoods[2].lhood = new CartesianLikelihood(1);
    lhoods[2].varX = fInfo.spec_index+2;
    lhoods[2].varY = fInfo.pred_index+64;
    lhoods[2].group = 2;
    lhoods[2].name = "Xenon100 2011";

    // BSMM LHCb CMS 
    lhoods[3].lhood = new CartesianLikelihood(6,0,0,0,Bsmumu_LHCb_CMS_CDF_file);
    lhoods[3].varX = fInfo.pred_index+2;
    lhoods[3].varY = 0;
    lhoods[3].group = 3;
    lhoods[3].name = "LHCb/CMS/CDF Bsmum mc7";

    // Just need an HA implementation
    lhoods[4].lhood = new CartesianLikelihood(8);
    lhoods[4].varX = fInfo.spec_index+24;
    lhoods[4].varY = 4;
    lhoods[4].group = 4;
    lhoods[4].name = "HA->tautau EPS";
}

void mc7_wBMMnHTT( std::vector<LHdata>& lhoods, FileInfo& fInfo )
{
    lhoods.resize(4);
    lhoods[0].lhood = new RadialLikelihood(3);
    lhoods[0].varX = 1;
    lhoods[0].varY = 2;
    lhoods[0].group = 1;
    lhoods[0].name = "CMS Alpha_t 1.1fb^-1";

    lhoods[1].lhood = new RadialLikelihood(4);
    lhoods[1].varX = 1;
    lhoods[1].varY = 2;
    lhoods[1].group = 1;
    lhoods[1].name = "ATLAS 0l 1.04fb^-1";
    
    // Xenon
    lhoods[2].lhood = new CartesianLikelihood(1);
    lhoods[2].varX = fInfo.spec_index+2;
    lhoods[2].varY = fInfo.pred_index+64;
    lhoods[2].group = 2;
    lhoods[2].name = "Xenon100 2011";

    // BSMM LHCb CMS 
    lhoods[3].lhood = new CartesianLikelihood(6,0,0,0,
        "/vols/cms03/samr/MasterCode-Afterburners/MultiAB/LHoods/1d_lookups/mc7/bs_cms_lhcb_s_sb.dat");
    lhoods[3].varX = fInfo.pred_index+2;
    lhoods[3].varY = 0;
    lhoods[3].group = 3;
    lhoods[3].name = "LHCb/CMS Bsmum mc7";

}

void mc7_nBMMnHTT( std::vector<LHdata>& lhoods, FileInfo& fInfo )
{
    lhoods.resize(3);
    lhoods[0].lhood = new RadialLikelihood(3);
    lhoods[0].varX = 1;
    lhoods[0].varY = 2;
    lhoods[0].group = 1;
    lhoods[0].name = "CMS Alpha_t 1.1fb^-1";

    lhoods[1].lhood = new RadialLikelihood(4);
    lhoods[1].varX = 1;
    lhoods[1].varY = 2;
    lhoods[1].group = 1;
    lhoods[1].name = "ATLAS 0l 1.04fb^-1";
    
    // Xenon
    lhoods[2].lhood = new CartesianLikelihood(1);
    lhoods[2].varX = fInfo.spec_index+2;
    lhoods[2].varY = fInfo.pred_index+64;
    lhoods[2].group = 2;
    lhoods[2].name = "Xenon100 2011";

}

void mc7_nBMMwHTT( std::vector<LHdata>& lhoods, FileInfo& fInfo )
{
    lhoods.resize(4);
    lhoods[0].lhood = new RadialLikelihood(3);
    lhoods[0].varX = 1;
    lhoods[0].varY = 2;
    lhoods[0].group = 1;
    lhoods[0].name = "CMS Alpha_t 1.1fb^-1";

    lhoods[1].lhood = new RadialLikelihood(4);
    lhoods[1].varX = 1;
    lhoods[1].varY = 2;
    lhoods[1].group = 1;
    lhoods[1].name = "ATLAS 0l 1.04fb^-1";
    
    // Xenon
    lhoods[2].lhood = new CartesianLikelihood(1);
    lhoods[2].varX = fInfo.spec_index+2;
    lhoods[2].varY = fInfo.pred_index+64;
    lhoods[2].group = 2;
    lhoods[2].name = "Xenon100 2011";

    // Just need an HA implementation
    lhoods[3].lhood = new CartesianLikelihood(8);
    lhoods[3].varX = fInfo.spec_index+24;
    lhoods[3].varY = 4;
    lhoods[3].group = 4;
    lhoods[3].name = "HA->tautau EPS";

}

void mc7_xenonOnly( std::vector<LHdata>& lhoods, FileInfo& fInfo )
{
    lhoods.resize(1);
    // Xenon
    lhoods[0].lhood = new CartesianLikelihood(1);
    lhoods[0].varX = fInfo.spec_index+2;
    lhoods[0].varY = fInfo.pred_index+64;
    lhoods[0].group = 2;
    lhoods[0].name = "Xenon100 2011";
}
