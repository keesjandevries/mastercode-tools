#include "CartesianLikelihood.h"
#include "FileConstants.h"

#include <cmath>

double CartesianLikelihood::getChi2(double x, double y)
{
    double X2 = 0;
    if( lhood )
    {
        X2 = (*lhood)(x,y,valindex);
    }
    else 
    {
        std::cerr << "*** Attempted to use badly configured CartesianLikelihood" << 
            std::endl;
    }
    return X2;
}

void CartesianLikelihood::configure(int function, double mu, double sigma, int ndf,
    std::string filename)
{
    // clear out previous versions
    delete lhood;
    switch(function)
    {
        case 1: //Xenon MC6 
        {
            std::cout << "Using CartesianLikelihood default Xenon MC6" << std::endl;
            lfuncs.set_values(mu,sigma,ndf);
            lhood = new LikelihoodFunctor1D<CartesianLikelihoodFunctions> 
                (&lfuncs,&CartesianLikelihoodFunctions::XenonMC6);
            valindex.doPopulate(filename);
            break;
        }
        case 2:  // Bsmm MC6
        {
            std::cout << "Using CartesianLikelihood default Bsmm MC6" << std::endl;
            lfuncs.set_values(0,13e-9,1);
            lhood = new LikelihoodFunctor1D<CartesianLikelihoodFunctions> 
                (&lfuncs,&CartesianLikelihoodFunctions::BsmmMC6);
            valindex.doPopulate(Bsmumu_file);
            break;
        }
        case 3:  // MA cmssm MC6
        {
            std::cout << "Using CartesianLikelihood default MA cmssm MC6" << std::endl;
            std::vector<std::string> suppl;
            suppl.resize(3);
            suppl[0]=HA_sigbr68_file;
            suppl[1]=HA_sigbr95_file;
            suppl[2]=HA_sigbr997_file;
            lfuncs.add_supplementary(suppl);
            lfuncs.set_values(0,1,1);
            lhood = new LikelihoodFunctor1D<CartesianLikelihoodFunctions> 
                (&lfuncs,&CartesianLikelihoodFunctions::MAcmssmMC6);
            valindex.doPopulate(HAtautau_file);
            break;
        }
        case 4: // MA nuhm1 MC6
        {
            std::cout << "Using CartesianLikelihood default MA nuhm1 MC6" << std::endl;
            std::vector<std::string> suppl;
            suppl.resize(3);
            suppl[0]=HA_sigbr68_file;
            suppl[1]=HA_sigbr95_file;
            suppl[2]=HA_sigbr997_file;
            lfuncs.add_supplementary(suppl);
            lfuncs.set_values(0,1,1);
            lhood = new LikelihoodFunctor1D<CartesianLikelihoodFunctions> 
                (&lfuncs,&CartesianLikelihoodFunctions::MAnuhm1MC6);
            valindex.doPopulate(HAtautau_file);
            break;
        }
        case 5: // Bsmm CDF 2011
        {
            std::cout << "Using CartesianLikelihood default Bsmumu CDF 2011" << std::endl;
            lfuncs.set_values(0,0,1);
            lhood = new LikelihoodFunctor1D<CartesianLikelihoodFunctions> 
                (&lfuncs,&CartesianLikelihoodFunctions::CDF2011);
            break;
        }
        case 6:
        {
            std::cout << "Using CartesianLikelihood pseudo chi2 from CL" << std::endl;
            lhood = new LikelihoodFunctor1D<CartesianLikelihoodFunctions> 
                (&lfuncs,&CartesianLikelihoodFunctions::CL);
            valindex.doPopulate(filename);
            break;

        }
        case 7:
        {
            std::cout << "Using CartesianLikelihood pseudo chi2 from PDF" << std::endl;
            lhood = new LikelihoodFunctor1D<CartesianLikelihoodFunctions> 
                (&lfuncs,&CartesianLikelihoodFunctions::PDF);
            valindex.doPopulate(filename);
            break;

        }
        case 8: // HAtautau 2011
        {
            std::cout << "Using CartesianLikelihood default HA->tautau EPS 2011" << 
                std::endl;
            lhood = new LikelihoodFunctor1D<CartesianLikelihoodFunctions>
                (&lfuncs,&CartesianLikelihoodFunctions::HAttStd);
            valindex.doPopulate(HAtautauEPS_file);
            break;
        }
        case 9: // HAtautau 2011
        {
            std::cout << "Using CartesianLikelihood default HA->tautau 08/2011 1.6fb^-1" << 
                std::endl;
            lhood = new LikelihoodFunctor1D<CartesianLikelihoodFunctions>
                (&lfuncs,&CartesianLikelihoodFunctions::HAttStd);
            valindex.doPopulate(filename);
            break;
        }
        case 10:
        {
            std::cout << "Using CartesianLikelihood X^2 directly from lookup (MC8)" << std::endl;
            lhood = new LikelihoodFunctor1D<CartesianLikelihoodFunctions> 
                (&lfuncs,&CartesianLikelihoodFunctions::CHI2);
            valindex.doPopulate(filename);
            break;

        }
        default: // Gaussian
        {
            lfuncs.set_values(mu,sigma,ndf);
            lhood = new LikelihoodFunctor1D<CartesianLikelihoodFunctions> 
                (&lfuncs,&CartesianLikelihoodFunctions::Gauss);
            if( filename != "" ) valindex.doPopulate(filename);
            break;
        }
    }
}

