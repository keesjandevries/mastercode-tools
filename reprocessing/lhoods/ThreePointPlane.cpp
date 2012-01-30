#include "ThreePointPlane.h"

//assumes missing component is the third component - could generalise at some
//point
double ThreePointPlane::getMissingComponent(ThreeVector& vec)
{
// call J_ our new origin
  if(isCollinear_ij()) return getMissingComponentCollinear(vec);
  ThreeVector J( J_.i_-I_.i_,J_.j_-I_.j_,J_.k_-I_.k_);
  ThreeVector K( K_.i_-I_.i_,K_.j_-I_.j_,K_.k_-I_.k_);
  ThreeVector vecP(vec.i_-I_.i_,vec.j_-I_.j_,vec.k_-I_.k_);


  // create new basis in which missing component is 0
  ThreeVector A = J*K;
  ThreeVector B = J*A;

  // need unit vectors
  B.normalise(); J.normalise(); A.normalise();

  double num = J.k_*(J.i_*vecP.i_ + J.j_*vecP.j_) +
               B.k_*(vecP.i_*B.i_ + vecP.j_*B.j_);
  double denom = 1. - J.k_*J.k_ - B.k_*B.k_;

  return ((num/denom) + I_.k_);
}

double ThreePointPlane::getMissingComponentCollinear(ThreeVector& vec)
{
  // get the radial distance to each point that defines the plane
  double rI = I_.getR_ij();
  double rJ = J_.getR_ij(); 
  double rK = K_.getR_ij();
  
  // arranges the poinst in order of radial distance furthest > L > M
  ThreeVector *furthest, *L, *M;
  if( rI>rJ) {
    if(rI>rK) {
      furthest = &I_;
      L = &J_; M = &K_;
    } else {
      furthest = &K_;
      L = &I_; M = &J_;
    }
  } else {
    if(rJ>rK) {
      furthest = &J_;
      L = &I_; M = &K_;
    } else {
      furthest = &K_;
      L = &I_; M = &J_;
    }
  }

  // looks for the x-y collinear distance between the radially furtherst point
  // and hte other two; now have a line defined as ---furthest---c1---c2---
  ThreeVector *c1,*c2;
  c1 = (minDistance_ij(*furthest,*L)<minDistance_ij(*furthest,*M))?L:M;
  c2 = (minDistance_ij(*furthest,*L)<minDistance_ij(*furthest,*M))?M:L;
  // now have furthest->c1->c2 progressing along the line


  // gradient of line defined by our 3points (y2-y1)/(x2-x1)
  double mL = (furthest->j_ - L->j_)/(furthest->i_ - L->i_);
  // constant in y = mL*x + cL for our line
  double cL = (L->j_ - mL*L->i_);

  // x-intercept of line a through (vec) perpendicular to our line
  // f->c1->c2;  ( so mVec = -1/mL)
  double xL = ( mL*cL + vec.j_ + (1./mL)*vec.i_ ) / ( mL*mL + 1 );
  // y-intercept must be on our line
  double yL = mL*xL + cL;

  double rp = minDistance_ij(*furthest,xL,yL);
  // distances along our line for each segment
  double r1 = minDistance_ij(*furthest,*c1);
  double r2 = minDistance_ij(*furthest,*c2);
  
  ThreeVector *p1,*p2;
  if(rp<r1) {
    p1 = furthest; p2 = c1;
  } else {
    p1 = c1; p2 = c2;
  }

  double portion = minDistance_ij(*p1,vec)/minDistance_ij(*p1,*p2);
  double kcomponent = (p1->k_ - p2->k_)*portion + p1->k_;

// use min_R{I,J,K} then calc R(min->others), calc R(min->vec) where does it lie
// interp that value; done
  return kcomponent;
}

double ThreePointPlane::getWeightedContribution(ThreeVector& vec)
{
  double rI = minDistance_ij(vec,I_.i_,I_.j_);
  double rJ = minDistance_ij(vec,J_.i_,J_.j_);
  double rK = minDistance_ij(vec,K_.i_,K_.j_);

  double nI(I_.k_),nJ(J_.k_),nK(K_.k_);
  double Rrecip = 1./rI + 1./rJ + 1./rK;
  double nevents = nI/(rI*Rrecip) + nJ/(rJ*Rrecip) + nK/(rK*Rrecip);

  return nevents;
}

std::pair<double,double> ThreePointPlane::getLinearIntercept(double x,double y)
{
  double xint_num = J_.i_*(K_.j_-J_.j_)/(K_.i_-J_.i_);
  double xint_denom = (K_.j_-J_.j_)/(K_.i_-J_.i_) - y/x;
  double xint = xint_num/xint_denom;
  double yint = (y/x)*xint;
  return std::make_pair(xint,yint);
}


/* NON-MEMBER FUNCTION */

double minDistance_ij(ThreeVector& v1, ThreeVector &v2)
{
  double dy = v1.j_ - v2.j_; 
  double dy2 = dy*dy; 
  double dx = v1.i_ - v2.i_;
  double dx2 = dx*dx;
  return sqrt(dx2+dy2);
}

double minDistance_ij(ThreeVector& v1, double i, double j)
{
  ThreeVector v(i,j,0);
  return minDistance_ij(v1,v);
}

bool areCollinear(ThreeVector& I, ThreeVector& J, ThreeVector& K, double colTol)
{
    if(I.j_ == J.j_ && I.j_ == K.j_) {
      return true;
    } else if(I.i_ == J.i_ && I.i_ == K.i_) {
      return true;
    } else return false;
    // for more complicated systems the below a more general way of handling
    // collinearity
    double m1 = (J.j_-I.j_)/(J.i_-I.i_); 
    double m2 = (K.j_-I.j_)/(K.i_-I.i_); 
    if(m1==0. && m2 ==0.) return true;
    return ((m2-m1)<(m2/colTol));
}

