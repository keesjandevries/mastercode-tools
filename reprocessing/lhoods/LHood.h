#ifndef H_LHood
#define H_LHood

class LHood 
{
  public:
    virtual void printData()=0;
    virtual double getChi2(double x = 0, double y = 0)=0;
};

#endif    /* H_LHood */
