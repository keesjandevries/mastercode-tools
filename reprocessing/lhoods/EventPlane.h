#ifndef H_EventPlane
#define H_EventPlane

#include <fstream>
#include <iostream>
#include <vector>
#include <cmath>

#include "EventRegion.h"

class EventPlane
{
  private:
    std::vector<EventRegion> grid_;
  public:
    EventPlane() {}
    EventPlane(std::string filename)
    {
      if(filename=="") return; // allows for empty
      std::ifstream file_in(filename.c_str());
      if (!file_in) 
      {
        std::cout << "Error while trying to open file `" << filename 
                  << "`, file not found" << std::endl;
        return; 
      }
      std::cout << "Opened " << filename << std::endl;

      double xmin, xmax, ymin, ymax, nevents;
      while( file_in >> nevents >> xmin >> xmax >> ymin >> ymax )
      {
       // std::cout << xmin << "," << xmax << "," << ymin << "," << ymax << ","
        //       << nevents << std::endl;
        // more efficient to check #lines first? push_back not exactly the best
        // method, but don't think we have enough lines to worry about it
        EventRegion _er(xmin,xmax,ymin,ymax,nevents);
        grid_.push_back(_er);
      }
    }


    void configure(std::string filename)
      { *this = EventPlane(filename); }

    bool isInPlane(double x, double y);
    std::vector<EventRegion>::iterator getEnd() { return grid_.end(); }
    bool isEnd(std::vector<EventRegion>::iterator it) // provide method for checking validity
      { return it==grid_.end(); }
    std::vector<EventRegion>::iterator getRegion(double, double);
    std::pair<std::vector<EventRegion>::iterator, std::vector<EventRegion>::iterator> 
      getNeighbours(double,double,std::vector<EventRegion>::iterator);
    std::vector<std::vector<EventRegion>::iterator> getIntersects(double,double);

    void printAllDistances(double,double);
};
#endif    /* H_EventPlane */
