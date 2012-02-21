#ifndef H_Coords
#define H_Coords

#include <iostream>
#include <fstream>
#include <vector>

struct Coord {
  double x,y,z;
  void print() { std::cout << "(" << x << "," << y << "," << z << ")"; }
};

class Coords {
  private:
    std::vector<Coord> cindex;
    Coord max_vals;
    Coord min_vals;
    std::vector<Coord>::iterator getPos(double val)
    {
      std::vector<Coord>::iterator pos = cindex.end();
      for( std::vector<Coord>::iterator it = cindex.begin(); it!=
           cindex.end(); ++it )
      {
        if(val<=it->x) {
        // relies on the vector being sorted in increasing x
          pos = it;
          break; // eugh - sorry
        }
      }
      if(pos==cindex.end()){ pos--; }
      if(val < cindex.begin()->x ){ pos = cindex.begin(); }
      return pos;
    }
  public:
    Coords(std::string file="");
    void doPopulate(std::string file="");
    void print();



    std::vector<Coord>::const_iterator getItBegin() { return cindex.begin(); }
    std::vector<Coord>::const_iterator getItEnd() { return cindex.end(); }
    const Coord operator[] (const int& i) const { return cindex[i]; }
    double getMaxX(){ return max_vals.x; }
    double getMaxY(){ return max_vals.y; }
    double getMaxZ(){ return max_vals.z; }
    double getMinX(){ return min_vals.x; }
    double getMinY(){ return min_vals.y; }
    double getMinZ(){ return min_vals.z; }
    std::vector<Coord>::size_type size(){ return cindex.size(); }

    double getYVal(double x);
    double getZVal(double x);
};

#endif    /* H_Coords */
