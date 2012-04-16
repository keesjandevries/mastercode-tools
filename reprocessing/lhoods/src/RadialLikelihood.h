#ifndef H_RadialLikelihood
#define H_RadialLikelihood

#include <iostream>
#include <string>
#include <cmath>

#include "LHood.h"
#include "RadialLikelihoodFunctions.h"
#include "FileConstants.h"
#include "Contour.h"

#define _USE_MATHS_DEFINES

class RadialLikelihood : public LHood
{
    private:
        // parameters corresponding to each segment of the first contour (primary
        // contour)
        std::vector<std::vector<double> > functionParameters;
        std::vector<double> theta_max;

        std::vector<Contour> contours;

        double max_theta_;
        double min_theta_;

        RadialLikelihoodFunctions lfuncs;

        TLikelihood_functor* lhood;
        TParams_functor* params;

        // do not allow copying -> should add some constructors but for now this
        // removes double free errors
        RadialLikelihood(const RadialLikelihood&);
        RadialLikelihood& operator=( RadialLikelihood& );

    public:
        RadialLikelihood(int function = 0) : lhood(0),params(0) // NULL
        { this->configure(function); }
        RadialLikelihood(std::string onefile, double chicont = 5.99, 
            double continf = 0) : lhood(0),params(0)
        { this->configure(-1,onefile,chicont,continf); }

        ~RadialLikelihood()
        { delete lhood; delete params; }

        void set_max_theta_(double theta) { max_theta_ = theta; }
        void set_min_theta_(double theta) { min_theta_ = theta; }
        void set_range(double x1, double x2) 
        {
            max_theta_ = contours[0].get_Theta(x1);
            min_theta_ = contours[0].get_Theta(x2);
        }


        void configure(int function = 0, std::string filename = "",
                double chival = 0, double Achiinf = 0);

        std::vector<double> get_segment_params(double);

        virtual void printData()
        {
            for( std::vector<Contour>::iterator it = contours.begin();
                it!=contours.end(); ++it)
            {
                it->print();
            }
        }
        virtual double getChi2(double, double);
};
#endif    /* H_RadialLikelihood */
