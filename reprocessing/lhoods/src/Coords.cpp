#include "Coords.h"

Coords::Coords(std::string file)
{
    doPopulate(file);
}

void Coords::doPopulate(std::string file)
{
    if( cindex.size()>0 ) 
    { 
        cindex.clear();
    }

    if( file!="" ) 
    {
        min_vals.x=1e9;min_vals.y=1e9;min_vals.z=1e9;
        std::ifstream infile(file.c_str());
        if( infile.is_open() ) 
        {
            Coord c;
            while( infile >> c.x >> c.y >> c.z )
            { 
                cindex.push_back(c); 
                if(c.x>max_vals.x){ max_vals.x=c.x; }
                if(c.y>max_vals.y){ max_vals.y=c.y; }
                if(c.z>max_vals.z){ max_vals.z=c.z; }
                if(c.x<min_vals.x){ min_vals.x=c.x; }
                if(c.y<min_vals.y){ min_vals.y=c.y; }
                if(c.z<min_vals.z){ min_vals.z=c.z; }
            }
            infile.close();
        } 
        else 
        {
            std::cout << "Failed to open file " << file << std::endl;
            std::cout << "\t- Index has not been filled" << std::endl;
        }
    } 
}

void Coords::print()
{ 
    for(std::vector<Coord>::iterator it = cindex.begin();
        it!=cindex.end(); ++it )
    { 
        it->print(); std::cout << std::endl; 
    }
}

double Coords::getYVal(double x)
{
    if ( x > max_vals.x ) x = max_vals.x;
    if ( x < min_vals.x ) x = min_vals.x;
    std::vector<Coord>::iterator val = getPos(x);
    std::vector<Coord>::iterator prev = val-1;

    double yval = ((val->y - prev->y)/(val->x - prev->x))*(x - prev->x) + prev->y;
    return yval;
}

double Coords::getZVal(double x)
{
    std::vector<Coord>::iterator val = getPos(x);
    std::vector<Coord>::iterator prev = val-1;

    double zval = ((val->z - prev->z)/(val->x - prev->x))*(x - prev->x) + prev->z;
    return zval;
}
