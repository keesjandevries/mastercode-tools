#ifndef H_CartesianLikelihood
#define H_CartesianLikelihood

#include "LHood.h"
#include "CartesianLikelihoodFunctions.h"
#include "Coords.h"

#include <vector>

class CartesianLikelihood : public LHood
{
  private:
    //  parameters corresponding to each segment of the first contour (primary
    //  contour)
    CartesianLikelihoodFunctions lfuncs;

    TLikelihood_functor1D *lhood;
    
    Coords valindex;

    std::vector<Coords> alt_lookups;

    // do not allow copying -> should add some constructors but for now this
    // removes double free errors
    CartesianLikelihood(const CartesianLikelihood&); 
    CartesianLikelihood& operator=( CartesianLikelihood& );
    
  public:
    CartesianLikelihood(int function = 0, double mu=0, double sigma=0, int ndf=1,
        std::string filename = "") : lhood(0)// NULL
    { this->configure(function,mu,sigma,ndf,filename); }

    ~CartesianLikelihood()
    { delete lhood; }

    void configure(int function = 0, double mu=0, double sigma=0, int ndf=1,
        std::string filename = "" );

    virtual void printData()
    { valindex.print(); }

    virtual double getChi2(double x, double y);

};
#endif    /* H_CartesianLikelihood */
