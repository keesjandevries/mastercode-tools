#ifndef H_EventRegion
#define H_EventRegion

#include <vector>
#include <string>

#include <cmath>

#include "ThreePointPlane.h"

class EventRegion 
{
  private:
    double xmin_,xmax_,ymin_,ymax_;
    double nevents_;
  public:
    EventRegion(double xmin=0, double xmax=0, double ymin=0, 
                double ymax=0, double nevents=0)
      :xmin_(xmin),xmax_(xmax),ymin_(ymin),ymax_(ymax),nevents_(nevents) {}

    double getXmin() const { return xmin_; }
    double getYmin() const { return ymin_; }
    double getXmax() const { return xmax_; }
    double getYmax() const { return ymax_; }
    double getNEvents() const { return nevents_; }

    bool isInRegion(double x,double y)
      { return (x<=xmax_ && x>=xmin_ && y<=ymax_ && y>=ymin_); }
    
    std::pair<double,double> getMid()
      { return std::make_pair( (xmin_+xmax_)/2., (ymin_+ymax_)/2. ); }

    double distanceToMid(double x, double y)
      { std::pair<double,double> m = getMid(); 
        return sqrt( (m.first-x)*(m.first-x) + (m.second-y)*(m.second-y) ); }

    ThreeVector getThreeVector()
      { return ThreeVector(getMid().first,getMid().second,nevents_); }

    void print()
      { std::cout<<"{"<<nevents_<<","<<xmin_<<","
        <<xmax_<<","<<ymin_<<","<<ymax_<<"}"; }

    void printMid()
      { std::pair<double,double> mid = getMid();
        std::cout<<"{"<<nevents_<<":"<< mid.first << "," << mid.second << "}"; }
};

#endif    /* H_EventRegion */
