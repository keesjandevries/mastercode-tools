#include "EventPlane.h"

#include <string>

bool EventPlane::isInPlane(double x, double y)
{
   for( std::vector<EventRegion>::iterator it = grid_.begin(); it != grid_.end(); ++it )
   { if( it->isInRegion(x,y) ) return true; }
   return false;
}

std::vector<EventRegion>::iterator EventPlane::getRegion(double x, double y)
{
  for( std::vector<EventRegion>::iterator it = grid_.begin(); it != grid_.end(); ++it )
  { if( it->isInRegion(x,y) ) return it; }
  return grid_.end();
}

std::pair<std::vector<EventRegion>::iterator, std::vector<EventRegion>::iterator> EventPlane::getNeighbours(double x,double y, std::vector<EventRegion>::iterator region)
{
  std::pair<std::vector<EventRegion>::iterator,std::vector<EventRegion>::iterator> pvER_it( grid_.end(), grid_.end() ); 
  for( std::vector<EventRegion>::iterator it = grid_.begin(); it != grid_.end(); ++it )
  {
    if( it==region ) continue;
    if( pvER_it.first==grid_.end() ) {
      pvER_it.first = it;
      continue;
    } else if ( pvER_it.second==grid_.end() ) {
      pvER_it.second = it;
      if( pvER_it.first->distanceToMid(x,y) > 
          pvER_it.second->distanceToMid(x,y) )
      {
        std::vector<EventRegion>::iterator temp = pvER_it.second; 
        pvER_it.second = pvER_it.first;
        pvER_it.first = temp;
      }
      continue;
    } // initialise the pair to the first two regions that aren't the one
      // we're looking for, and sort dist(1)<dist(2)
    double dist = it->distanceToMid(x,y);
    if( dist <= pvER_it.first->distanceToMid(x,y) ) {
      pvER_it.second = pvER_it.first;
      pvER_it.first = it;
    } else if ( dist <= pvER_it.second->distanceToMid(x,y) ) {
      pvER_it.second = it;
    }
  }
  return pvER_it;
}

// return std::vector of regions that a ray to (x,y) intersects with
std::vector<std::vector<EventRegion>::iterator> EventPlane::getIntersects(double x, double y)
{
  double theta = atan(y/x);
  std::vector<std::vector<EventRegion>::iterator> intersects;
  for( std::vector<EventRegion>::iterator it=grid_.begin(); it!=grid_.end(); ++it)
  {
    double tmax = atan(it->getYmax()/it->getXmin());
    double tmin = atan(it->getYmin()/it->getXmax());
    if(theta<tmax && theta>tmin) intersects.push_back(it);
  }
  return intersects;
}

void EventPlane::printAllDistances(double x, double y)
{
  for( std::vector<EventRegion>::iterator it = grid_.begin(); it!=grid_.end(); ++it)
  {
    std::cout<<"["; it->print(); std::cout << ": " << it->distanceToMid(x,y) << "]" 
             << std::endl;
  }
}
