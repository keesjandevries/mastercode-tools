#ifndef H_ThreePointPlane
#define H_ThreePointPlane

#include <iostream>
#include <ostream>
#include <cmath>

#include "ThreeVector.h"


class ThreePointPlane
{
  private:
    ThreeVector I_;
    ThreeVector J_;
    ThreeVector K_;
  public:
    ThreePointPlane() {}
    ThreePointPlane(ThreeVector I, ThreeVector J, ThreeVector K)
      : I_(I),J_(J),K_(K) {}

    ThreePointPlane(double i1, double i2, double i3,
                    double j1, double j2, double j3,
                    double k1, double k2, double k3)
    {
      I_ = ThreeVector(i1,i2,i3);
      J_ = ThreeVector(j1,j2,j3);
      K_ = ThreeVector(k1,k2,k3);
    }
    
    bool isCollinear_ij(double colTol = 100.) {
      return areCollinear(I_,J_,K_, colTol);
    }

    void normalise()
      { I_.normalise(); J_.normalise(); K_.normalise(); }

    double getMissingComponent(ThreeVector&);
    double getMissingComponentCollinear(ThreeVector&);
    double getWeightedContribution(ThreeVector&);

    std::pair<double,double> getLinearIntercept(double,double);
    
};

// some useful non-member functions
double minDistance_ij(ThreeVector&,ThreeVector&);
double minDistance_ij(ThreeVector&,double,double);
bool areCollinear(ThreeVector& I,ThreeVector& J, ThreeVector& K, double colTol);

#endif    /* H_ThreePointPlane */
