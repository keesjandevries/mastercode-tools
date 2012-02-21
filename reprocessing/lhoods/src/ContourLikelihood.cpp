#include "FileConstants.h"
#include "ContourLikelihood.h"

#include <new>

double ContourLikelihood::getChi2(double x, double y)
{
    double theta = atan(y/x);
    double X2 = 0; //
    if( params && lhood )
    {
        if( theta > min_theta_ && theta < max_theta_   ) 
        {
            std::vector<double> fPara = get_segment_params(theta);
            X2 = (*lhood)(x,y,fPara); 
        }
    }
    else
    {
        std::cerr << "*** Attempted to use badly configured ContourLikelihood" << std::endl;
    }
    return X2;
}

void ContourLikelihood::configure(int function, std::string filename,
        double chival, double Achiinf)
{
    // clear out previous versions
    delete lhood;

    // by default use whole range
    // account for someone not knowing cmath ranges
    max_theta_ = 2.*M_PI;
    min_theta_ = -2.*M_PI;

    std::vector<std::string> cont_files;
    std::vector<double> chi_vals;
    double chiinf;
    double rnum(0), rdenom(0);
    switch(function)
    {
        /*
         * Contour file names and chi2 values stored in FileConstants.h
         */
        case 1: // CMS new ME_t search (march 2011 - alex tapper talk)
        {
            std::cout << "CMS ME_t 03/2011" << std::endl;
            cont_files.push_back(cms_new_at);
            chi_vals.push_back(chisq_95percent_2d);
            chiinf = 0;
            lhood = new LikelihoodFunctor<LikelihoodFunctions> 
                (&lfuncs,&LikelihoodFunctions::likelihood_simple);
            params = new ParamsFunctor<LikelihoodFunctions> 
                (&lfuncs,&LikelihoodFunctions::params_simple);
            break;
        }
        case 2: // ATLAS combined 1l and 0l contour
        {
            std::cout << "ATLAS 1l + 0l 35pb^-1 " << std::endl;
            cont_files.push_back(atlas_combined);
            chi_vals.push_back(chisq_95percent_2d);
            chiinf = 0;
            lhood = new LikelihoodFunctor<LikelihoodFunctions> 
                (&lfuncs,&LikelihoodFunctions::likelihood_simple);
            params = new ParamsFunctor<LikelihoodFunctions> 
                (&lfuncs,&LikelihoodFunctions::params_simple);
            break;
        }
        case 3: // 1.1 Alpha t analysis
        {
            std::cout << "CMS Alpha_t 1.1fb^-1" << std::endl;
            cont_files.push_back(cmsATeps);
            chi_vals.push_back(chisq_95percent_2d);
            chiinf = 0;
            lhood = new LikelihoodFunctor<LikelihoodFunctions> 
                (&lfuncs,&LikelihoodFunctions::likelihood_simple);
            params = new ParamsFunctor<LikelihoodFunctions> 
                (&lfuncs,&LikelihoodFunctions::params_simple);
            break;
        }
        case 4: // ATLAS 1.04 0l analysis
        {
            std::cout << "ATLAS 0l 1.04fb^-1" << std::endl;
            cont_files.push_back(atlas0leps);
            chi_vals.push_back(chisq_95percent_2d);
            chiinf = 0;
            lhood = new LikelihoodFunctor<LikelihoodFunctions> 
                (&lfuncs,&LikelihoodFunctions::likelihood_simple);
            params = new ParamsFunctor<LikelihoodFunctions> 
                (&lfuncs,&LikelihoodFunctions::params_simple);
            break;
        }
        default:
        {
            chi_vals.push_back(chival);
            chiinf = Achiinf;
            std::cerr << "Specified unknown/non-default Likelihood " << 
                function << std::endl << "\t - Assuming standard R^-4 " <<
                "scaling law and chi^2 = 0 @ infinity" << std::endl 
                << "\t - Taking file + vals from argument" << std::endl;
            if( filename != "" )
            {
                lhood = new LikelihoodFunctor<LikelihoodFunctions> 
                    (&lfuncs,&LikelihoodFunctions::likelihood_simple);
                params = new ParamsFunctor<LikelihoodFunctions> 
                    (&lfuncs,&LikelihoodFunctions::params_simple);
                cont_files.push_back(filename);
            }
            else
            {
                std::cout<< "Failed to provide contour for lookup" << std::endl;
            }
            break;
        }
    }
    if(cont_files.size() != chi_vals.size()) {
        lhood = NULL; params = NULL;
        std::cerr
            << "Wrong number of boundary conditions for number of contours provided"
            << std::endl;
        return;
    }

    for(int i = 0; i<(int)cont_files.size(); ++i)
    {
        contours.push_back( Contour(cont_files[i]) );
    }

    lfuncs.set_values(chi_vals,chiinf,rnum,rdenom);
    SegmentRange cRange = contours[0].getData();
    // populate the data so we don't have to calcualte every point
    for( std::vector<Segment>::const_iterator it = cRange.begin; it!=cRange.end; ++it)
    {
        // pair of segments is sorted by theta, so second of pair has highest theta
        double theta_upper = it->end.theta;
        double theta_lower = it->begin.theta;
        double theta = theta_lower + (theta_upper-theta_lower)/2.;
        std::vector<double> pvec;
        (*params)(theta,contours,&pvec);
        theta_max.push_back(theta);
        functionParameters.push_back(pvec);
    }
}

std::vector<double> ContourLikelihood::get_segment_params(double theta)
{

    std::vector<std::vector<double> >::iterator it = functionParameters.begin();
    int pos = contours[0].getSegmentIndex(theta);
    return functionParameters[pos];
}
