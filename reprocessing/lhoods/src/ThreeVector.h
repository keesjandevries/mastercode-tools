#ifndef H_ThreeVector
#define H_ThreeVector

#include <cmath>

class ThreeVector
{
  private:
    double i_,j_,k_;
  public:
    ThreeVector() : i_(0),j_(0),k_(0) {}
    ThreeVector(double i, double j, double k) : i_(i),j_(j),k_(k) {}

    double getVal(int i)
      { if(i==1)return i_; if(i==2)return j_; if(i==3)return k_; return -1.; }

    double getI() const { return i_; };
    double getJ() const { return j_; };
    double getK() const { return k_; };

    double getR_ij() { return i_*i_ + j_*j_; };

    ThreeVector operator*(const ThreeVector &rhs ) 
      { return ThreeVector( this->getJ()*rhs.getK()-this->getK()*rhs.getJ(),
                            -(this->getI()*rhs.getK()-this->getK()*rhs.getI()),
                            this->getI()*rhs.getJ()-this->getJ()*rhs.getI() ); }
    
    ThreeVector crossProduct(ThreeVector V) 
      { return ThreeVector( j_*V.getK()-k_*V.getJ(),
                            -(i_*V.getK()-k_*V.getI()),
                            i_*V.getJ()-j_*V.getI() ); }

    void print()
      { std::cout<<"("<<i_<<","<<j_<<","<<k_<<")"<<std::endl;}

    double getModulus()
      { return sqrt(i_*i_ + j_*j_ + k_*k_); }

    void normalise()
      { double m=getModulus(); i_/=m; j_/=m; k_/=m; }

    friend bool areCollinear(ThreeVector&,ThreeVector&,ThreeVector&,double colTol=100.);
    friend double minDistance_ij(ThreeVector&, ThreeVector&);
    friend double minDistance_ij(ThreeVector&, double, double);
    friend class ThreePointPlane;

};

#endif    /* H_ThreeVector */
