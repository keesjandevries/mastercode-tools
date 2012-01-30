#include <iostream>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <cmath>
#include <string>
#include <vector>

#include <TFile.h>
#include <TString.h>
#include <TTree.h>
#include <TLeaf.h>

TString g_TreeName = "tree";
TString g_BranchName = "vars";
int g_specIndex = 74;
int g_paraIndex = 10;

int g_point = -1;

double g_S = 50.;
double g_SS = 14.;

// Def. a structure type to access external Fortran common area... 
typedef struct { double s2out; double ss2out; double s3out; double ss3out; } forcommon;

// List of all modules not written in C/C++ language... 
extern "C" { 
  // YEP this is actually real
  double lspscat_( double&, double&, double&, double&, double&, double&, 
    double&, double&, double&, double&, double&, double&, double&, double&, 
    double&, double&, double&, double&, double&, double&, double&, double&,
    double&, double&, double&, double&, double&, double&, double&, double&,
    double&, double&, double&, double&, double&, double&, double&, double& );
}

void processFile(TString filename, double s = 50., double ss = 14.);
void makeFiles( double* vin );
void runPoint( double* vin, double s, double ss );
void testPoint(TString &filename, int entry);

void usage() {
  std::cout << "./dmwrap [OPTIONS] [FILELIST]" << std::endl
            << "\t-s <int> : starting index of spectrum" << std::endl
            << "\t-p <int> : number of leading parameters in file" << std::endl
            << "\t-b <string> : branch name" << std::endl
            << "\t-t <string> : tree name" << std::endl
            << "\t-X <int> : prepare files for entry X in the file" << std::endl;
}

int main(int argc, char* argv[])
{
  
  char ch;
  while ( ( ch = getopt(argc,argv, "p:s:b:t:S:e:X:") ) != -1 ) {
    switch (ch) {
      case 's': g_specIndex = atoi(optarg); break;
      case 'p': g_paraIndex = atoi(optarg); break;
      case 'b': g_BranchName = TString(optarg); break;
      case 't': g_TreeName = TString(optarg); break;
      case 'X': g_point = atoi(optarg); break;
      case 'S': g_S = atof(optarg); break;
      case 'e': g_SS = atof(optarg); break;
      default: std::cerr << "*** Error: unknown option " << optarg << std::endl;
    }
  }

  // increment for the number of options we have
  argc -= optind;
  argv += optind;
  if(argc<1) { usage(); return 0;}
  for ( int i=0 ; i<argc ; ++i )
  {
     TString file = (TString)argv[i];
     if( g_point >= 0 ) {
       testPoint(file,g_point); 
     } else {
       std::cout<<"Processing " << file << std::endl;
       processFile(file,50.,14.);
     }
  }

  return 0;
}

void processFile(TString filename, double s, double ss)
{
  extern forcommon fcom_;

  int newvars = 43;

  TFile* f = new TFile(filename);
  TFile* output = new TFile(filename,"RECREATE");
  TTree* t = (TTree*)f->Get(g_TreeName);
  TTree* chi2tree = new TTree(g_TreeName,"contains dm data");

  Int_t nTotVars = t->GetLeaf(g_BranchName)->GetLen();

  std::ostringstream varInName, varOutName;
  varOutName << "vars" << "[" << nTotVars+newvars << "]/D";

  double* vin = new double[nTotVars];
  double* varsOut = new double[nTotVars+newvars];

  chi2tree->SetMaxTreeSize(10*chi2tree->GetMaxTreeSize());
  chi2tree->Branch("vars", varsOut, varOutName.str().c_str());

  t->SetBranchAddress(g_BranchName,vin);

  int nEntries = t->GetEntries();
  std::cout<< "Scanning over " << nEntries << " entries." << std::endl;
  std::cout<< "\twith " << nTotVars << " values each" << std::endl;

  int entry = 0;
  int count_in = 0;
  int freq=nEntries/100;
  
  std::cout << "\tProcessing ...   0% " << std::flush;
  double sigma_fracs [11] = { 0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.33, 1.66, 2.0, 2.5, 3.0 };
  while (t->GetEntry(entry++) && entry < nEntries)
  {
    if ( freq>0 && !(entry%freq) )
    {
      std::cout << "\b\b\b\b\b" << std::setprecision(0) << std::setw(3) << std::fixed
                << entry/static_cast<double>(nEntries)*100 << "% " << std::flush;
      std::cout << std::setprecision(4);
    }
    for( int i = 0; i<g_specIndex; ++i ){ varsOut[i]=vin[i]; };
    double s_vals [] = { 50., 64. };
    double ss_vals [] = { 14., 8. };
    for( int j = 0; j<2; ++j )
    {
      g_S = s_vals[j];
      g_SS = ss_vals[j];
      for( int i = 0; i < 11; ++i )
      {
        double S_eff = g_S + g_SS*sigma_fracs[i];
        runPoint(vin,S_eff,g_SS); 
        varsOut[g_specIndex+i+(j*21)] = fcom_.s3out;
        if( sigma_fracs[i] > 0 ) 
        {
          S_eff = g_S - g_SS*sigma_fracs[i];
          runPoint(vin,S_eff,g_SS); 
          varsOut[g_specIndex+i+10+(j*21)] = fcom_.s3out;
        }
      }
    }
    // add spin dependant values on to the end
    runPoint(vin, s_vals[0], ss_vals[0]);
    varsOut[g_specIndex+42] = fcom_.s2out;
   
    // write out the spectrum
    for( int i=g_specIndex; i<nTotVars; ++i ){ varsOut[i+newvars]=vin[i]; };
    chi2tree->Fill();
    double poq;
  }
  std::cout<<std::endl;
  output->cd();
  chi2tree->Write( chi2tree->GetName(), TObject::kOverwrite );

  f->Close();
  output->Close();

  delete [] vin,varsOut;
}

void runPoint( double* vin, double s, double ss ) 
{
  int NMIX = g_paraIndex+36;
  int NMass = g_specIndex+2;
  int QMass = g_paraIndex+52;
  int STOP = g_paraIndex+56;
  int SQMASS = g_specIndex+17;
  int SBOT = g_paraIndex+60;
  int HIGGS = g_specIndex+22;
  int ALPHA = g_paraIndex+34;

  double n1(vin[NMass]), n2(vin[NMass+1]), n3(vin[NMass+3]), n4(vin[NMass+2]);
  double nm11(vin[NMIX]), nm12(vin[NMIX+4]), nm13(vin[NMIX+12]), nm14(vin[NMIX+8]);
  double nm21(vin[NMIX+1]), nm22(vin[NMIX+5]), nm23(vin[NMIX+13]), nm24(vin[NMIX+9]);
  double nm31(vin[NMIX+2]), nm32(vin[NMIX+6]), nm33(vin[NMIX+14]), nm34(vin[NMIX+10]);
  double nm41(vin[NMIX+3]), nm42(vin[NMIX+7]), nm43(vin[NMIX+15]), nm44(vin[NMIX+11]);
  double lhiggs(vin[HIGGS]),shiggs(vin[HIGGS+2]),halpha(vin[ALPHA]);
  double sbeta(sin(atan(vin[4]))), mtin(vin[6]), mbin(4.2);
  double ul = vin[QMass]*vin[QMass];
  double dl = vin[QMass+2]*vin[QMass+2];
  double ur = vin[QMass+1]*vin[QMass+1];
  double dr = vin[QMass+3]*vin[QMass+3];
  double b1 = std::min(vin[SQMASS+2],vin[SQMASS+3]);
  double b2 = std::max(vin[SQMASS+2],vin[SQMASS+3]);
  double t1 = std::min(vin[SQMASS],vin[SQMASS+1]);
  double t2 = std::max(vin[SQMASS],vin[SQMASS+1]);
  double tt(acos(vin[STOP])), tb(acos(vin[SBOT]));

  // want squark mass squared
  b1*=b1;
  b2*=b2;
  t1*=t1;
  t2*=t2;


  lspscat_(s,ss,n1,n2,n3,n4,nm11, nm12, nm13, nm14, nm21, nm22, nm23, nm24, 
    nm31, nm32, nm33, nm34, nm41, nm42, nm43, nm44, lhiggs, shiggs, halpha,
    sbeta, mtin, mbin, ul, ur, dl, dr, b1, b2, t1, t2, tt, tb );
}

void makeFiles( double* vin )
{
  // indices for position of various bits we need
  int prec = 15;

  int NMIX = g_paraIndex+36;
  int NMass = g_specIndex+2;
  int QMass = g_paraIndex+52;
  int STOP = g_paraIndex+56;
  int SQMASS = g_specIndex+17;
  int SBOT = g_paraIndex+60;
  int HIGGS = g_specIndex+22;
  int ALPHA = g_paraIndex+34;

  double n1(vin[NMass]), n2(vin[NMass+1]), n3(vin[NMass+3]), n4(vin[NMass+2]);
  double nm11(vin[NMIX]), nm12(vin[NMIX+4]), nm13(vin[NMIX+12]), nm14(vin[NMIX+8]);
  double nm21(vin[NMIX+1]), nm22(vin[NMIX+5]), nm23(vin[NMIX+13]), nm24(vin[NMIX+9]);
  double nm31(vin[NMIX+2]), nm32(vin[NMIX+6]), nm33(vin[NMIX+14]), nm34(vin[NMIX+10]);
  double nm41(vin[NMIX+3]), nm42(vin[NMIX+7]), nm43(vin[NMIX+15]), nm44(vin[NMIX+11]);
  double lhiggs(vin[HIGGS]),shiggs(vin[HIGGS+2]),halpha(vin[ALPHA]);
  double sbeta(sin(atan(vin[4]))), mtin(vin[6]), mbin(4.2);
  double ul = vin[QMass]*vin[QMass];
  double dl = vin[QMass+2]*vin[QMass+2];
  double ur = vin[QMass+1]*vin[QMass+1];
  double dr = vin[QMass+3]*vin[QMass+3];
  double b1 = std::min(vin[SQMASS+2],vin[SQMASS+3]);
  double b2 = std::max(vin[SQMASS+2],vin[SQMASS+3]);
  double t1 = std::min(vin[SQMASS],vin[SQMASS+1]);
  double t2 = std::max(vin[SQMASS],vin[SQMASS+1]);
  double tt(acos(vin[STOP])), tb(acos(vin[SBOT]));

  b1*=b1;
  b2*=b2;
  t1*=t1;
  t2*=t2;

  std::string b = "    ";
  
  std::ofstream matn("point-files/matn.dat");
  matn.precision(prec);
  matn << n1 << b << n2 << b << n3 << b << n4 << std::endl
       << nm11 << b << nm12 << b << nm13 << b << nm14 << std::endl
       << nm21 << b << nm22 << b << nm23 << b << nm24 << std::endl
       << nm31 << b << nm32 << b << nm33 << b << nm34 << std::endl
       << nm41 << b << nm42 << b << nm43 << b << nm44 << std::endl;
  matn.close();

  std::ofstream higgs("point-files/higgs.dat");
  higgs.precision(prec);
  higgs << lhiggs << b << shiggs << b << halpha << std::endl;
  higgs.close();

  std::ofstream cres("point-files/cres.in");
  cres.precision(prec);
  cres <<0<<b<<0<<b<< sbeta <<b<<0<<b<<0<<b<< mtin << b << mbin << std::endl;
  cres.close();

  std::ofstream fort98("point-files/fort.98");
  fort98.precision(prec);
  fort98 << 0 << b << 0 << b << 0 << b 
         << ul << b << dl << b << ur << b << dr << std::endl; 
  fort98.close();

  std::ofstream fort99("point-files/fort.99");
  fort99.precision(prec);
  fort99 << b1 << b << b2 << b << t1 << b << t2 << b 
         << tt << b << tb << std::endl;
  fort99.close();

}

void testPoint(TString& filename, int entry)
{
  TFile* f = new TFile(filename);
  TTree* t = (TTree*)f->Get(g_TreeName);
  Int_t nTotVars = t->GetLeaf(g_BranchName)->GetLen();
  double* vin = new double[nTotVars];
  t->SetBranchAddress(g_BranchName,vin);
  int nEntries = t->GetEntries();
  if( entry < nEntries )
  {
    extern forcommon fcom_;
    t->GetEntry(entry);
//    std::cout << "point = " << entry << ": " << vin[0] << "," << vin[1] << "," 
//              << vin[2] << "," << vin[3] << "," << vin[4] << std::endl;
    double sigma_fracs [11] = { 0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.33, 1.66, 2.0, 2.5, 3.0 };
    std::cout << std::setw(4) << g_S  << " +/- " << std::setw(4) << g_SS << std::endl;
    std::cout << "-------------" << std::endl;
    for( int i = 0; i < 11; ++i )
    {
      double S_eff = g_S + g_SS*sigma_fracs[i];
      runPoint(vin,S_eff,g_SS); 
      makeFiles(vin);
      std::cout << "[ " << std::setw(5) << S_eff << " ]: " << fcom_.s3out << " (" << fcom_.ss3out << ")" << std::endl; 
      if( sigma_fracs[i] > 0 ) 
      {
        S_eff = g_S - g_SS*sigma_fracs[i];
        runPoint(vin,S_eff,0.); 
        std::cout << "[ " << std::setw(5) << S_eff << " ]: " << fcom_.s3out << " (" << fcom_.ss3out << ")" << std::endl; 
      }
    }
  } else {
    std::cout << "tried to access entry: out of range" << std::endl;
  }
}
