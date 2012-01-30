/*
    Samuel Rogerson: 10/2010
      Class to store connected 2-D contours.  Initialised from file of (x,y)
      coordinates progressing around the contour.
      Linearly interpolates for line segments.  
      Given a point (theta,r) can determine if this lies within the contour.
      By adding multiple contours can include both multiple disconnected
      contours and holes.
*/

#ifndef H_Contour
#define H_Contour

#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <sstream>
#include <string>
#include <utility>
#include <algorithm>
#include <limits>
#include <cmath>

#define _USE_MATHS_DEFINES

struct PolCoord
{
  double r;
  double theta;
  PolCoord(double r_=0, double theta_=0) : r(r_), theta(theta_) {};
};

struct Segment
{
  PolCoord begin, end;
  Segment(PolCoord p1, PolCoord p2)
  {
    begin = (p1.theta<p2.theta)?p1:p2;
    end = (p1.theta>p2.theta)?p1:p2;
  }
};

struct SegmentRange
{
  std::vector<Segment>::const_iterator begin, end;
  SegmentRange(std::vector<Segment>::const_iterator b,
    std::vector<Segment>::const_iterator e) : begin(b), end(e) {};
};

struct SegmentAscendingSort
{
  bool operator()( const Segment& sStart, const Segment& sEnd )
  {
    return sStart.begin.theta < sEnd.begin.theta;
  }
};

struct SegmentLessThan
{
  bool operator()( Segment& left, const PolCoord& right )
  {
    return left.begin.theta < right.theta;
  }
};

class Contour
{
  private:
    std::vector<Segment> segment_data;
    double max_r, min_r, max_theta, min_theta;
    // by default it is assumed the contour doesn't overlap the origin
    bool include_origin;

  public:
    // constructor
    Contour() : include_origin(true) {};
    Contour(std::string filename, bool origin = true) : include_origin(origin)
    { populate_contour(filename); }

    // data filling
    bool populate_contour(std::string filename="");
    
    // calculation methods
    bool in_contour(double,double);
    double min_distance(double,double);
    double point_to_segment(double,double,Segment&);
    double point_to_segment(double,double,double,double,double,double);
    double get_R(double); // returns R for a particular theta
    double get_Theta(double); // returns theta for a given X-value
    int getSegmentIndex(double); // for a given theta returns the index of the segment that it lies in

    // display and print
    bool print();

    SegmentRange getData() {
      SegmentRange r1(segment_data.begin(),segment_data.end());
      return r1;
    }
};

#endif    /* H_Contour */
