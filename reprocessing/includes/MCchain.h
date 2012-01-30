#ifndef H_MCchain
#define H_MCchain

#include <string>

#include <iostream>

#include <TROOT.h>
#include <TChain.h>
#include <TLeaf.h>
#include <TFile.h>
#include <TTree.h>
#include <TFriendElement.h>
#include <TString.h>

class MCchain  // used when recalculating
{
    private:
        Int_t nentries_;
        Int_t nTotVars_;

        bool do_contrib, do_shorts;
    public:
        TString tree_name;

        TChain *chi2chain;
        TChain *contribchain;
        TChain *chain68;
        TChain *chain95;
        TChain *chain99;
        double *chi2vars;
        double *contribvars;

        MCchain(TString& file,
               TString chi2chainName    = "chi2tree",
               TString contribchainName = "contribtree") :
               tree_name(chi2chainName)
        {
            if( check_file(file,chi2chainName,contribchainName) )
            {
                chi2chain    = new TChain(chi2chainName);
                chi2chain->Add(file);
                chi2chain->SetCacheSize(0);
                if( do_contrib ) 
                {
                    contribchain = new TChain(contribchainName);
                    contribchain->Add(file);
                    contribchain->SetCacheSize(0);
                }
                if( do_shorts ) 
                {
                    chain68      = new TChain("tree68");
                    chain95      = new TChain("tree95");
                    chain99      = new TChain("tree99");
                    chain68->Add(file);
                    chain95->Add(file);
                    chain99->Add(file);
                }

                Init();
            }
            else 
            {
                std::cout << "Failed to find \"" << chi2chainName << 
                    "\" in \"" << file << "\"" << std::endl;
            }
        }

        bool check_file(TString&, TString&, TString&);

        void Add(TString& file)
        {
            chi2chain->Add(file);
            if(do_contrib) {
              contribchain->Add(file);
            }
            if(do_shorts) {
              chain68->Add(file);
              chain95->Add(file);
              chain99->Add(file);
            }

	    //std::cout << "ADD: there are now: " << chi2chain->GetEntries() << std::endl;
	    nentries_ = chi2chain->GetEntries();

            return;
        }

        void Init();
        void Write();

        Int_t GetEntry(Long64_t entry,bool short_trees = false);
        Int_t GetMinEntry(Long64_t entry);
        Long64_t GetEntries(bool short_trees = false);
        Long64_t GetMinEntries();
        Int_t GetBranchLength();

};

void MCchain::Init()
{
    nentries_=chi2chain->GetEntries();

    if( do_contrib ) chi2chain->AddFriend(contribchain); 
    nTotVars_ = chi2chain->GetLeaf("vars")->GetLen();
    chi2vars    = new double[nTotVars_];
    contribvars = new double[nTotVars_];

    chi2chain->SetBranchAddress("vars",chi2vars);
    if( do_contrib ) contribchain->SetBranchAddress("vars",contribvars);
    if( do_shorts )
    { 
        chain68->SetBranchAddress("vars",chi2vars);
        chain95->SetBranchAddress("vars",chi2vars);
        chain99->SetBranchAddress("vars",chi2vars);
    }
}

bool MCchain::check_file(TString& file, TString& c2n, TString& cbn)
{
    do_contrib = false;
    do_shorts = false;
    TFile* rf = TFile::Open(file);
    TTree *myC2Chain = (TTree*) rf->Get(c2n);
    TTree *myContribChain = (TTree*) rf->Get(cbn);
    TTree *myShortChain = (TTree*) rf->Get("tree68");
    
    if( myContribChain ) do_contrib = true;
    if( myShortChain ) do_shorts = true;
    bool ret_val = false;
    if( myC2Chain ) ret_val = true;
    return ret_val;
}

Int_t MCchain::GetEntry( Long64_t entry, bool short_trees )
{
    Int_t read = 0;
    if( !short_trees ) 
        read =  chi2chain->GetEntry(entry);
    else
        read = GetMinEntry(entry);
        if( !read )
            read = chi2chain->GetEntry(entry);
    return read;
}

Int_t MCchain::GetMinEntry( Long64_t entry )
{
    Int_t read = 0;
    read = chain68->GetEntry(entry); 
    if( read == 0 ) 
    {
        entry -= chain68->GetEntries();
        read = chain95->GetEntry(entry);
    }
    if( read == 0 )
    {
        entry -= chain95->GetEntries();
        read = chain99->GetEntry(entry);
    }
    return read;
}

Long64_t MCchain::GetEntries(bool short_trees)
{
    Int_t nentries = nentries_;
    if( short_trees ) nentries = GetMinEntries();
    return nentries_;
}

Long64_t MCchain::GetMinEntries()
{
    return chain68->GetEntries();
}

Int_t MCchain::GetBranchLength()
{
    return nTotVars_;
}   
#endif    /* H_MCchain */
