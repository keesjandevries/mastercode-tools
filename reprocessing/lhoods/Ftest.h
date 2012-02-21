#ifndef H_Ftest
#define H_Ftest

#include "../includes/SMvals.h"

double get_Fchi( double Xm, double Xmr, int Nm, int r )
{
    double Fchi = (Xm - Xmr) / ( Xmr/(Nm - r) );
    return Fchi;
}

double get_Fchi_SM( double chi2, int model_ndof, bool g2 = true )
{
    int sm_ndof = getSMNDOF( g2 );
    double sm_chi2 = 0.;
    int r = sm_ndof - model_ndof;

    if( g2 ) sm_chi2 = getSMValue( SMvals::MINCHI2 );
    else sm_chi2 = getSMValue( SMvals::MINCHI2_NOG2 );

    double Fchi = get_Fchi( sm_chi2, chi2, sm_ndof, r );
    return Fchi;
}

#endif    /* H_Ftest */
