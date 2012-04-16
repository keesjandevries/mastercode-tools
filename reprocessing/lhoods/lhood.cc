#include "src/LHood.h"
#include "src/RadialLikelihood.h"
#include "src/CartesianLikelihood.h"

#include <string>

extern "C" 
{
    RadialLikelihood* RadialLikelihood_new(const char* filename, double* chi2,
                                             double* chiinf)
    { 
        std::string f(filename); 
        return new RadialLikelihood(f, *chi2, *chiinf); 
    }
    CartesianLikelihood* CartesianLikelihood_new(int *function, double *mu, double *sigma, 
                                   int *ndf, const char *filename)
    {
        std::string f(filename);
        return new CartesianLikelihood( *function, *mu, *sigma, *ndf, f );
    }
    void getChi2( LHood *lh, double *x, double *y, double* chi2 )
    {
        *chi2 = lh->getChi2(*x,*y);
    }
    
}
