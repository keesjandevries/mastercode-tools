#include "src/LHood.h"
#include "src/ContourLikelihood.h"
#include "src/Likelihood1D.h"

#include <string>

extern "C" 
{
    ContourLikelihood* ContourLikelihood_new(const char* filename, double* chi2,
                                             double* chiinf)
    { 
        std::string f(filename); 
        return new ContourLikelihood(f, *chi2, *chiinf); 
    }
    Likelihood1D* Likelihood1D_new(int *function, double *mu, double *sigma, 
                                   int *ndf, const char *filename)
    {
        std::string f(filename);
        return new Likelihood1D( *function, *mu, *sigma, *ndf, *filename );
    }
}
