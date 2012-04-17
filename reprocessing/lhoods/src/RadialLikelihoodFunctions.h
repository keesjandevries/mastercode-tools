#ifndef H_RadialLikelihoodFunctions
#define H_RadialLikelihoodFunctions

#include <utility>
#include <vector>
#include <cmath>

#include "Contour.h"

// next time need to look at function params;
// why not just have a std::vector - then check std::vector.size() for each of the
// functions, rather than rely on this crass labelling


class RadialLikelihoodFunctions
{
  private:
    std::vector<double> chi_vals;
    double chi_inf;
    double rescale_num, rescale_denom;

  public:
    RadialLikelihoodFunctions() {};
    void set_values(std::vector<double>&, double, double, double);

    // likelihood functions
    double likelihood_simple(double,double,std::vector<double>&);
    double likelihood_asymptote(double,double,std::vector<double>&);
    double likelihood_cutoff(double,double,std::vector<double>&);
    double likelihood_ATLAS(double,double,std::vector<double>&);
    double likelihood_ATLAS_exp(double,double,std::vector<double>&);
    // parameters calculations
    // IDEALLY: these are voids - take pointers to the std::vector and fill it
    // f(theta, contours, parameters)
    void params_simple(double,std::vector<Contour>&,std::vector<double>*);
    void params_asymptote(double,std::vector<Contour>&,std::vector<double>*);
    void params_cutoff(double,std::vector<Contour>&,std::vector<double>*);
    void params_ATLAS(double,std::vector<Contour>&,std::vector<double>*);
    void params_ATLAS_exp(double,std::vector<Contour>&,std::vector<double>*);
    void params_ATLAS_scale(double,std::vector<Contour>&,std::vector<double>*);
};

class TLikelihood_functor
{
  public:
    virtual double operator()(double,double,std::vector<double>&)=0;
};

template <class TClass> class LikelihoodFunctor : public TLikelihood_functor
{
  private:
    double (TClass::*fpt)(double,double,std::vector<double>&);
    TClass* pt2Object;

  public:
    LikelihoodFunctor() {};

    LikelihoodFunctor(TClass* _pt2Object,
      double(TClass::*_fpt)(double,double,std::vector<double>&))
       { pt2Object = _pt2Object; fpt=_fpt; };
    
    virtual double operator()(double v1,double v2,std::vector<double>& fParas)
      { return (*pt2Object.*fpt)(v1,v2,fParas); };
};

class TParams_functor
{
  public:
    virtual void operator()(double,std::vector<Contour>&,std::vector<double>*)=0;
};

template <class TClass> class ParamsFunctor : public TParams_functor
{
  private:
    void (TClass::*fpt)(double,std::vector<Contour>&,std::vector<double>*);
    TClass* pt2Object;

  public:
    ParamsFunctor() {};

    ParamsFunctor(TClass* _pt2Object,
      void(TClass::*_fpt)(double,std::vector<Contour>&,std::vector<double>*))
        { pt2Object = _pt2Object; fpt=_fpt; };
    
    virtual void operator()(double t, std::vector<Contour>& c,
      std::vector<double>* p)
       { (*pt2Object.*fpt)(t,c,p); };

};

#endif    /* H_RadialLikelihoodFunctions */
