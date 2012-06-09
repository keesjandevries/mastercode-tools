#include "CartesianLikelihoodFunctions.h"
#include "FileConstants.h"
#include <TMath.h>
#include <cmath>
#include <string>

double getChi2_Chi2(Coords& c, double val)
{
  // get the X^2 directly !!!!
  return c.getYVal(val);
}

double getChi2_CL(Coords& c, double val)
{
  double chi2 = 0;
  double CL = c.getYVal(val);
  double erfterm = TMath::ErfInverse(2*CL-1);
  chi2 = 2*(erfterm*erfterm);
  return chi2;
}

double getChi2_PDF(Coords& c, double val)
{
  double chi2 = 0; 
  double PDF = c.getZVal(val);
  chi2 = -1.*log(PDF/c.getMaxZ());
  return chi2;
}

double getGaussChi2Simple(double x, double mu, double sigma)
{
  double chi = (x-mu)/sigma;
  double chi2 = chi*chi;
  return chi2;
}

double getGaussChi2(double x, double mu, double sigma, int ndof)
{
  double Earg = fabs(x-mu)/(sqrt(2*sigma*sigma));
  double cdf = 0.5*(1+erf(Earg));
  double pval = cdf*2.-1.;
  double chi2=0;
  if(pval<1.) chi2 = TMath::ChisquareQuantile(pval,ndof);
  else if (pval==1) chi2 = 1e9;
  return chi2;
}

void CartesianLikelihoodFunctions::add_supplementary(std::vector<std::string>& files)
{
    c_.resize( files.size() ); 
    std::vector<std::string>::iterator f_it;
    std::vector<Coords>::iterator c_it;
    for( f_it = files.begin(),c_it = c_.begin(); 
        f_it != files.end() && c_it != c_.end(); f_it++, c_it++ )
    {
       c_it->doPopulate(*f_it);
    }
}

void CartesianLikelihoodFunctions::set_values(double mu, double sigma, int ndof)
{
    mu_=mu;
    sigma_=sigma;
    ndof_=ndof;
}

double CartesianLikelihoodFunctions::Gauss( double P, double Q, Coords &c )
{
    return getGaussChi2(P,mu_,sigma_,ndof_);
}

double CartesianLikelihoodFunctions::PDF( double P, double Q, Coords &c )
{
    return getChi2_PDF( c, P );
}

double CartesianLikelihoodFunctions::CHI2( double P, double Q, Coords &c )
{
    return getChi2_Chi2( c, P );
}

double CartesianLikelihoodFunctions::CL( double P, double Q, Coords &c )
{
    return getChi2_CL( c, P );
}

double CartesianLikelihoodFunctions::XenonMC6( double P, double Q, Coords &c )
{
    double chi2 = 0;
    /* for Xenon implementation */
    double yval = c.getYVal(P);
    double r = Q/yval;
    double x0 = 6.0548;
    double R = x0*r;
    chi2 = getGaussChi2(R,mu_,sigma_,ndof_);
    return chi2;
}

double CartesianLikelihoodFunctions::BsmmMC6( double P, double Q, Coords &c )
{
    double chi2 = 0;
    /* bsmm way */
    if( P < 20.e-9 ) {
      chi2 = getChi2_PDF(c, P);
    } else {
      chi2 = getChi2_CL(c, P); 
    } 
    return chi2;
}

double CartesianLikelihoodFunctions::MAcmssmMC6( double P, double Q, Coords &c )
{
    double chi2 = 0;
    // MA stuff
    /* tan^b scaling mA implementation */
    double tb_P = Q;
    double MA_P = P;
    if( MA_P > 100 && MA_P < 350 ) {
        double tb_95 = c.getYVal(MA_P);
        double sBR_95 = c_[1].getYVal(MA_P);
        double sBR_p = sBR_95 * tb_P * tb_P / (tb_95 * tb_95);
        double phi = (log(3)-log(2))/(log(c_[2].getYVal(MA_P))-log(c_[1].getYVal(MA_P)));
        double f = c_[2].getYVal(MA_P) / c_[0].getYVal(MA_P);
        double A = 3*pow(f,-1.*phi);
        double sigma_sig = A*pow(sBR_p/c_[0].getYVal(MA_P),phi);
        // 1d gaussian
        chi2 = getGaussChi2(sigma_sig,mu_,sigma_,ndof_); // 1d implementation
    } else {
        chi2 = 0 ;
    }
    return chi2;
}

double CartesianLikelihoodFunctions::MAnuhm1MC6( double P, double Q, Coords &c )
{
    double chi2 = 0;
    /* mA nuhm1 sigma*BR calc */
    double tb = Q;
    double MA = P;
    if( MA>100 && MA<350 ) {
        double SigmaBR_p = (90.71578072195604 - 0.9713370357798988*MA + 
            0.002876970690206135*MA*MA + 3.2885816607005684e-6*MA*MA*MA - 
            2.9070887742926235e-8*MA*MA*MA*MA + 3.66236435276743e-11*MA*MA*MA*MA*MA ) * 
            2 * tb*tb / 1000.;
        double phi = (log(3)-log(2))/(log(c_[2].getYVal(MA))-log(c_[1].getYVal(MA)));
        double f = c_[2].getYVal(MA) / c_[0].getYVal(MA);
        double A = 3*pow(f,-1.*phi);
        double sigma_sig = A*pow(SigmaBR_p/c_[0].getYVal(MA),phi);
        // 1d gaussian
        chi2 = getGaussChi2(sigma_sig,0,1,1);
    } else {
        chi2 = 0;
    } 
    return chi2;
}

double CartesianLikelihoodFunctions::CDF2011( double P, double Q, Coords &c )
{
    double chi2 = 0;
    if( P < 1.8e-8 ) {
        chi2 = getGaussChi2(P,1.8e-8,0.9e-8,1);
    } else {
        chi2 = getGaussChi2(P,1.8e-8,1.1e-8,1);
    }
    return chi2;
}

double CartesianLikelihoodFunctions::HAttStd( double P, double Q, Coords &c )
{
    double chi2 = 0;
    double MA = P;
    double tanB = Q;
    if( MA <= 90 )
    {
        MA = 91.;
    }
    if( MA < 473 )
    {
        double tb_contour = c.getYVal(MA); // tanb on contour for this MA
        double r = (tanB * tanB) / (tb_contour * tb_contour);
        chi2 = r * 4.00; //1D 2sigma
    }
    return chi2;
}
