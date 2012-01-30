#ifndef  H_MCVars
#define H_MCVars

#include <map>
#include <string>
#include <vector>
#include <fstream>
#include <iostream>

#include "../includes/SMvals.h"

struct MCConstraint 
{
    int n;
    std::vector<int> mode;
    std::vector<double> value;
    std::vector<double> error;
    std::map<int,std::string> name;

    void resize( int n ) 
    {
        mode.resize(n);
        value.resize(n);
        error.resize(n);
    }

    void print( int i, bool end_line = true)
    {
        std::cout << i << " " << mode[i] << " " << value[i] << " " << 
            error[i] << " " <<  name[i] << std::flush;
        if( end_line ) std::cout << std::endl;
    }
};

namespace MCVars
{
    MCConstraint c;
    
    void add_specials()
    {
        c.name[666] = "nonUniMeasureD";
        c.name[667] = "nonUniMeasureU";
        c.name[701] = "sqRgldiff";
        c.name[702] = "glsqLdiff";
        c.name[703] = "glsqRdiff";
        c.name[704] = "stauchi0diff";
        c.name[705] = "MT2";
        c.name[706] = "mAdiff";
        c.name[801] = "stauthresh";
        c.name[802] = "higgsthresh";
        c.name[803] = "neu1thresh";
        c.name[804] = "chathresh";
        c.name[805] = "seLseRthresh"; 
        c.name[806] = "neu12thresh";
        c.name[807] = "squthresh";
        c.name[808] = "seLseLthresh";
        c.name[809] = "seRseRthresh";
        c.name[999] = "A0/m0";
        c.name[998] = "A0-/m0";
        c.name[997] = "BsmumuSM";
        c.name[996] = "MA/tb";
    }

    double get_var_value(double* vars, int index, int spec_index, 
        int pred_index, bool do_checks = true )
    {
        double var = 0.;
        if( index ==  666)
        {
            var = (vars[1]*vars[1])/vars[6];
        }
        else if( index ==  667)
        {
            var = (vars[1]*vars[1])/vars[7];
        }
        else if( index ==  701)
        {
            var = vars[spec_index+15]-vars[spec_index+21];
        }
        else if( index ==  702)
        {
            var = vars[spec_index+21]-vars[spec_index+16];
        }
        else if( index ==  703)
        {
            var = vars[spec_index+21]-vars[spec_index+15];
        }
        else if( index ==  704)
        {
            var = vars[spec_index+12]-vars[spec_index+2];
        }
        else if( index ==  706)
        {
            var = (sqrt(vars[pred_index+35])-
                vars[spec_index+24])/
                vars[spec_index+24];
        }
        else if( index ==  801)
        {
            var = 2*vars[spec_index+12];
            if(!do_checks) var = 2*vars[12];
        }
        else if( index ==  802)
        {
            var = vars[spec_index+23] + vars[spec_index+24];
            if(!do_checks) var = vars[17] + vars[17];
        }
        else if( index ==  803)
        {
            var = vars[spec_index+2] + vars[spec_index+2];
            if(!do_checks) var = 2*vars[8];
        }
        else if( index ==  804)
        {
            var = vars[spec_index] + vars[spec_index+1];
            if(!do_checks) var = vars[6] + vars[7];
        }
        else if( index ==  805)
        {
            var = vars[spec_index+6] + vars[spec_index+7];
            if(!do_checks) var = vars[10] + vars[11];
        }
        else if( index ==  806)
        {
            var = vars[spec_index+2] + vars[spec_index+3];
            if(!do_checks) var = vars[8] + vars[9];
        }
        else if( index ==  807)
        {
            double x1 = vars[spec_index+15];
            double x2 = vars[spec_index+16];
            var =2*std::min(x1,x2);
            if(!do_checks) 
                var = 2*(vars[13]<vars[14]?vars[13]:vars[14]);
        }
        else if( index ==  808)
        {
            var = vars[spec_index+7] + vars[spec_index+7];
            if(!do_checks) var = 2*vars[11]; 
        }
        else if( index == 809)
        {
            var = vars[spec_index+6] + vars[spec_index+6];
        }
        else if( index ==  996)
        {
            var = vars[spec_index+24]/vars[4]; 
        }
        else if( index ==  997)
        {
            var = vars[pred_index+2]/getSMValue(SMvals::BSMM);
            if(!do_checks) 
                var = vars[pred_index]/getSMValue(SMvals::BSMM);
        }
        else if( index ==  998)
        {
            var = -1.*(vars[3]/vars[1]);
        }
        else if( index ==  999)
        {
            var = vars[3]/vars[1];
        }
        else if( index ==  spec_index+4)
        {
            var = fabs(vars[index]);
        }
        else if( index ==  pred_index+34)
        {
            var = std::pow(sin(atan(vars[4])-vars[index]),2);
        }
        else 
        {
            var = vars[index];
        }
        return var;
    }

    double read_model_file( std::string filename )
    {

        ifstream Card(filename.c_str());
        if( !Card || !Card.is_open() ) 
        {
            std::cerr << "Couldn't open file \"" << filename << "\"" << std::endl;
            return(0);
        }

        // Strip out header
        char buffer[256];
        Card.getline(buffer,256);

        // Get number of c and minimum chi2 (global variable!)
        int n = 0;
        Card >> n;
        c.n = n;
        double minC2;
        Card >> minC2;
        Card.getline(buffer,256); // Read end of line
        std::cout << "Number of c from " << filename << ": " << 
            c.n << " - min chi^2: " << 
            minC2 << std::endl;

        // Strip out comments
        Card.getline(buffer,256);

        double eexp, etheo;
        int ivar = 0;

        c.resize(n); 
        while ( !Card.eof() && Card.good() && ivar<c.n) 
        {
            Card >> c.mode[ivar] >> c.value[ivar] >> 
                eexp >> etheo;
            c.error[ivar] = sqrt( eexp*eexp + etheo*etheo );
            Card.getline(buffer,256,'!');
            Card.getline(buffer,256);
            c.name[ivar] =  buffer ;
            ivar++;
        }

        return minC2;
    }

}


#endif  /*H_MCVars*/
