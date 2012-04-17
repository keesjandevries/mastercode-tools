#include "RadialLikelihoodFunctions.h"

#include <string>
#include <iostream>

/* PARAMETER CALCULATORS */

bool range_check(int e1=0, int e2=0, int p1=0, int p2=0)
{
    bool range_state = ( p1<=e1 || p2<=e2 );
    /*std::cout << "-------" <<"-" << "------------" <<"-" << std::endl;
      std::cout << "given: " << p1 << ", expected: " << e1 << std::endl;
      std::cout << "given: " << p2 << ", expected: " << e2 << std::endl;
      std::cout << "-------" <<"-" << "------------" <<"-" << std::endl;*/
    if(!range_state) std::cerr << "Range check failed" << std::endl;
    return range_state;
}

void RadialLikelihoodFunctions::set_values(std::vector<double>& chivals,
        double chiinf,double rnum, double rdenom)
{
    rescale_num = rnum;
    rescale_denom = rdenom;
    chi_inf = chiinf;

    chi_vals.clear();
    chi_vals.reserve(chivals.size());
    for( std::vector<double>::iterator it=chivals.begin();it!=chivals.end();++it)
    {
        chi_vals.push_back(*it);
    }
}

void RadialLikelihoodFunctions::params_simple(double theta, std::vector<Contour>& c, std::vector<double>* params)
{
    int expected_contours = 1;
    int expected_boundaries = 1;
    bool state=range_check(expected_contours,expected_boundaries,c.size(),chi_vals.size());

    if(state) {
        double MC = c.begin()->get_R(theta);
        double M = MC*pow(chi_vals[0],0.25);

        params->clear();
        params->push_back(M);
        params->push_back(4.);
    }
    return;
}

void RadialLikelihoodFunctions::params_asymptote(double theta, std::vector<Contour>& c, std::vector<double>* params)
{
    int expected_contours = 2;
    int expected_boundaries = 2;
    bool state=range_check(expected_contours,expected_boundaries,c.size(),chi_vals.size());

    if( state )
    {
        double M_C_max = 1500;
        double step = 0.01;

        double LHS_exponent = log(chi_vals[0]/chi_inf)/log(chi_vals[1]/chi_inf);
        std::vector<double> solutions;
        double delta = 0;
        double R_1 = c[0].get_R(theta), R_2 = c[1].get_R(theta);

        for( double M_C = 0; M_C<M_C_max; M_C+=step )
        {
            double delta_old = delta;
            double RHS = fabs(M_C/R_1 - 1.);
            double LHS = pow(fabs(M_C/R_2 - 1.), LHS_exponent);
            delta = (RHS - LHS)/RHS;
            if( (delta_old>0 && delta<0) || (delta_old<0 && delta>0) )
            {
                solutions.push_back(M_C-step);
            }
        }
        double M_good, P_good;
        int good_func(0);
        for(std::vector<double>::iterator it = solutions.begin();
                it!= solutions.end(); ++it )
        {
            double M_C = *it;
            double P = log(chi_vals[0]/chi_inf)/log(fabs((M_C/R_1) - 1.));
            if( P>0 )
            {
                M_good = M_C;
                P_good = P;
                good_func++;
            }
        }
        params->clear();
        if( good_func>1 )
        {
            std::cerr << "Found multiple good function" << std::endl;
            M_good = 0;
            P_good = 0;
        }

        params->push_back(M_good);
        params->push_back(P_good);
    }

    return;
}

void RadialLikelihoodFunctions::params_cutoff(double theta, std::vector<Contour>& c, std::vector<double>* params)
{
    int expected_contours = 2;
    int expected_boundaries = 2;
    bool state=range_check(expected_contours,expected_boundaries,c.size(),chi_vals.size());
    // std::cout<< "c.size: " << c.size() << ", chi_vals.size: " << chi_vals.size() << std::endl;

    if( state )
    {
        double R_21 = c[1].get_R(theta)/c[0].get_R(theta);
        double P = log(chi_vals[0]/chi_vals[1])/log(R_21);
        double M_C = c[0].get_R(theta)*pow(chi_vals[0],(1./P));

        params->clear();
        params->push_back(M_C);
        params->push_back(P);
    }
    return;
}

void RadialLikelihoodFunctions::params_ATLAS(double theta, std::vector<Contour>& c, std::vector<double>* params )
{
    int expected_contours = 2;
    int expected_boundaries = 2;
    bool state=range_check(expected_contours,expected_boundaries,c.size(),chi_vals.size());
    /*
     * chi^2 = chi_inf + (M_A/M)^P
     * - phi is defined for convenience
     */
    //std::cout<<" Getting params for " << theta << std::endl;
    if( state )
    {
        double M_1 = c[0].get_R(theta);
        double M_2 = c[1].get_R(theta);
        double phi = log(chi_vals[0]-chi_inf)/log(chi_vals[1]-chi_inf);
        double M_21 = M_2/M_1;
        double M_exp = 1./(phi-1);
        double M_A = M_2*pow(M_21,M_exp);
        double P = ((phi-1)/phi)*(log(chi_vals[0]-chi_inf)/(log(M_2)-log(M_1)));
        params->clear();
        params->push_back(M_A);
        params->push_back(P);
    }
    return;
}

void RadialLikelihoodFunctions::params_ATLAS_exp(double theta, std::vector<Contour>& c, std::vector<double>* params)
{
    int expected_contours = 2;
    int expected_boundaries = 2;
    bool state=range_check(expected_contours,expected_boundaries,c.size(),chi_vals.size());

    if( state )
    {
        double M_1 = c[0].get_R(theta);
        double M_2 = c[1].get_R(theta);
        double phi = log((chi_vals[0]-chi_inf)/(chi_vals[1]-chi_inf));
        double M_A = ((M_2*M_1)/(M_1-M_2))*phi;
        double C = (chi_vals[0]-chi_inf)*exp(M_A/M_1);

        params->clear();
        params->push_back(M_A);
        params->push_back(C);
    }
    return;
}

void RadialLikelihoodFunctions::params_ATLAS_scale(double theta, std::vector<Contour>& c, std::vector<double>* params)
{
    int expected_contours = 1;
    int expected_boundaries = 2;
    bool state=range_check(expected_contours,expected_boundaries,c.size(),chi_vals.size());

    if( state )
    {
        double R_A = c[0].get_R(theta);
        double P = ( log(chi_vals[1] - chi_inf)-log(chi_vals[0]-chi_inf) ) / ( log(rescale_denom) - log(rescale_num) );
        double M_A = R_A * pow(chi_vals[0] - chi_inf,1./P);

        params->clear();
        params->push_back(M_A);
        params->push_back(P);
    }
    return;
}

/* LIKELIHOOD FUNCTIONS */

double RadialLikelihoodFunctions::likelihood_simple(double m0, double m12, std::vector<double>& fParas)
{
    double X2 = 0;
    int expected_params = 1;
    bool state = range_check(expected_params,0,fParas.size(),0);
    if( state )
    {
        double M = sqrt(m0*m0 + m12*m12);
        X2 = (fParas[0]/M);
        X2*=X2; X2*=X2; // square then ^4
    }
    return X2;
}

double RadialLikelihoodFunctions::likelihood_asymptote(double m0, double m12, std::vector<double>& fParas)
{
    double X2 = 0;
    int expected_params = 2;
    bool state = range_check(expected_params,0,fParas.size(),0);
    if( state )
    {
        double M = sqrt(m0*m0 + m12*m12);
        X2 = chi_inf*pow(fabs(fParas[0]/M - 1.),fParas[1]);
    }
    return X2;
}

double RadialLikelihoodFunctions::likelihood_cutoff(double m0,double m12, std::vector<double>& fParas)
{
    double X2 = 0;
    int expected_params = 2;
    bool state = range_check(expected_params,0,fParas.size(),0);
    if( state )
    {
        double M = sqrt(m0*m0 + m12*m12);
        X2 = pow(fParas[0]/M,fParas[1]);
        X2 = (X2>chi_inf)?X2:chi_inf;
    }
    return X2;
}

double RadialLikelihoodFunctions::likelihood_ATLAS(double m0, double m12, 
    std::vector<double>& fParas)
{
    double X2 = 0;
    int expected_params = 2;
    bool state = range_check(expected_params,0,fParas.size(),0);
    if( state )
    {
        //std::cout << "Getting X2 for " << m0 << "," << m12 << "," << 
        //    fPara.M_C <<"," << fPara.P << "," << fPara.theta_max 
        //    << std::endl;
        //double theta = atan(m12/m0);
        double M = sqrt(m0*m0 + m12*m12);
        X2 = chi_inf + pow(fParas[0]/M,fParas[1]);
    }
    return X2;
}

double RadialLikelihoodFunctions::likelihood_ATLAS_exp(double m0, double m12,
    std::vector<double>& fParas )
{
    double X2 = 0;
    int expected_params = 2;
    bool state = range_check(expected_params,0,fParas.size(),0);
    if( state )
    {
        //double theta = atan(m12/m0);
        double M = sqrt(m0*m0 + m12*m12);
        X2 = chi_inf + fParas[1]*(exp(-1*fParas[0]/M));
    }
    return X2;
}
