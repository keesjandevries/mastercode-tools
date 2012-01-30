#ifndef H_Likelihood1D
#define H_Likelihood1D

#include "LHood.h"
#include "LikelihoodFunctions1D.h"
#include "Coords.h"

#include <vector>

class Likelihood1D : public LHood
{
  private:
    //  parameters corresponding to each segment of the first contour (primary
    //  contour)
    LikelihoodFunctions1D lfuncs;

    TLikelihood_functor1D *lhood;
    
    Coords valindex;

    std::vector<Coords> alt_lookups;

    // do not allow copying -> should add some constructors but for now this
    // removes double free errors
    Likelihood1D(const Likelihood1D&); 
    Likelihood1D& operator=( Likelihood1D& );
    
  public:
    Likelihood1D(int function = 0, double mu=0, double sigma=0, int ndf=1,
        std::string filename = "") : lhood(0)// NULL
    { this->configure(function,mu,sigma,ndf,filename); }

    ~Likelihood1D()
    { delete lhood; }

    void configure(int function = 0, double mu=0, double sigma=0, int ndf=1,
        std::string filename = "" );

    virtual void printData()
    { valindex.print(); }

    virtual double getChi2(double x, double y);

};
#endif    /* H_Likelihood1D */
