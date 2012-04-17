#ifndef H_MultiAB
#define H_MultiAB

#include <string>
#include <numeric>

#include "LHood.h"
#include "RadialLikelihood.h"
#include "CartesianLikelihood.h"

struct FileInfo {
    int spec_index, pred_index;
    TString tree_name, branch_name;
};

struct LHdata {
    LHood* lhood;
    std::string name;
    int varX,varY;
    int group;
};

std::vector<double> getAllChi2( double* vars, std::vector<LHdata>& lhoods, int verbose )
{
    std::vector<double> chi2;
    std::vector< std::vector<LHdata>::iterator > its;
    for( std::vector<LHdata>::iterator it = lhoods.begin(); it!=lhoods.end();
        ++it )
    {
        double chi2_lh = it->lhood->getChi2( vars[it->varX],vars[it->varY] );
        if( it->group > (int)chi2.size() ) 
        {
            chi2.resize(it->group);
            its.resize(it->group);
        }
        if( verbose > 5 )  // 
        {
            std::cout << "PREDICT " << vars[it->varX] <<"," << vars[it->varY] <<
                " " << chi2_lh << " " << it->group << " 1 " << " 0 0 " << 
                it->group << " " << it->name << std::endl;
        }
        if( chi2_lh >= chi2[it->group-1] ) 
        {
            chi2[it->group-1] = chi2_lh;
            its[it->group-1] = it;
        }
    }
    double total_chi2 = std::accumulate( chi2.begin(), chi2.end(), 0. );
    chi2.insert(chi2.begin(),total_chi2);
    its.insert( its.begin(), lhoods.begin() );
    if( verbose > 1 ) 
    {
        for( int i = 1; i < chi2.size(); ++i )
        {
            std::vector<LHdata>::iterator it = its[i];
            double chi2_lh = chi2[i];
            std::cout << "PREDICT  " << vars[it->varX] <<"," << vars[it->varY] <<
                " " << chi2_lh << " " << it->group << " 1 " << " 0 0 " << 
                it->group << " " << it->name << std::endl;
        }
    }
    return chi2;
}

double getAllChi2( double* vars, std::vector<LHdata>& lhoods )
{
    std::vector<double> chi2 = getAllChi2( vars, lhoods, 0 );
    return chi2[0];
}

#endif    /* H_MultiAB */
