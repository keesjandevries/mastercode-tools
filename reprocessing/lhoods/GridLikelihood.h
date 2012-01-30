#ifndef H_GridLikelihood
#define H_GridLikelihood

#include "LHood.h"
#include "EventPlane.h"
#include "ThreePointPlane.h"
#include <cmath>
#include <string>

struct VertexIntercept
{
  _v_ER_it region_;
  double xint_,yint_;

  VertexIntercept(_v_ER_it region, double xint, double yint)
    : region_(region),xint_(xint),yint_(yint) {}
};

class GridLikelihood : public LHood
{
  private:
    EventPlane plane_; 
    double mu_,sigma_;
  public:
    GridLikelihood(std::string filename="grid-lookups/1_3.txt",
                    double mu = -0.5, double sigma = 2.2)
      : mu_(mu), sigma_(sigma)
      { plane_ = EventPlane(filename); }

    double getNumberEvents(double,double);
    double getEventsInterpolateGrid(double,double);
    double getEventsWeightedGrid(double,double);
    double get1DChi2(double,double);
    void setPlane(ThreePointPlane&,double,double);
    double getEventsRescaled(double, double);
    VertexIntercept getLastIntercept(double,double);
    double doRescale(double,double,double,double,double);
    double getNSigma(double,double);
    double getNormalCDF(double,double);
    double getPval(double,double);
    void printAllDistances(double x, double y)
      { plane_.printAllDistances(x,y); }

    virtual double getChi2(double,double);
};

#endif    /* H_GridLikelihood */
