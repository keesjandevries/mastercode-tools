#ifndef H_LikelihoodFunctions1D
#define H_LikelihoodFunctions1D

#include "Coords.h"

class LikelihoodFunctions1D
{
  private:
    double mu_,sigma_;
    int ndof_;
    std::vector<Coords> c_;
  public:
    LikelihoodFunctions1D() {};
    void set_values(double, double, int);
    void add_supplementary(std::vector<std::string>& files);

    // likelihood functions
    double Gauss(double,double,Coords&);
    double PDF(double,double,Coords&); 
    double CL(double,double,Coords&);
    double XenonMC6(double,double,Coords&);
    double BsmmMC6(double,double,Coords&);
    double MAcmssmMC6(double,double,Coords&);
    double MAcmssmMC6_old(double,double,Coords&);
    double MAnuhm1MC6(double,double,Coords&);
    double CDF2011(double,double,Coords&);
    double HAttStd(double,double,Coords&);
};

class TLikelihood_functor1D
{
  public:
    virtual double operator()(double,double,Coords&)=0;
};

template <class TClass> class LikelihoodFunctor1D : public TLikelihood_functor1D
{
  private:
    double (TClass::*fpt)(double,double,Coords&);
    TClass* pt2Object;

  public:
    LikelihoodFunctor1D() {};

    LikelihoodFunctor1D(TClass* _pt2Object,
      double(TClass::*_fpt)(double,double,Coords&))
       { pt2Object = _pt2Object; fpt=_fpt; };
    
    virtual double operator()(double v1,double v2, Coords& c)
      {  return (*pt2Object.*fpt)(v1,v2,c); };
};

#endif /* H_LikelihoodFunctions1D */
