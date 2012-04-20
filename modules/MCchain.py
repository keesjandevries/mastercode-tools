#! /usr/bin/env python

import ROOT as r
from array import array

def check_files( fd ) :
    nfiles = len(fd["InputFiles"])
    chi2_states = [None]*nfiles
    contrib_states = [None]*nfiles
    for pos in range(nfiles) :
        chi2_states[pos], contrib_states[pos] = \
            check_file( fd["InputFile"][pos], fd["Chi2TreeNames"][pos], 
                        fd["ContribTreeNames"][pos] )

def check_file( filename, chi2treename, contribtreename ) :
    tf = r.TFile( fd["InputFiles"] )

    chi2tree  = tf.Get(chi2treename)
    conttree  = tf.Get(contribtreename)

    contrib_state = conttree  is not None
    chi2_state    = chi2tree  is not None

    return chi2_state,contrib_state


class MCchain( object ) :
    def __init__( self, fd ) :
        self.tree_names           = fd["Chi2TreeNames"]
        self.branch_name         = fd["Chi2BranchName"]
        self.contrib_names        = fd["ContribTreeNames"] 
        self.contrib_branch_name = fd["ContribBranchName"]
        chi2_states, contrib_states = check_files( fd )
        self.init_chains( fd, chi2_states, contrib_states )
        self.setup_branches()

    def AddFile( self, fname, chi2treename, contribtreename ) :
        c2s, cbs = check_file( fname, chi2treename, contribtreename )

        if c2s and c2b :
            self.chi2chain.AddFile(fname,-1,chi2treename)
            self.contribchain.AddFile(fname,-1,contribtreename)

        self.nentries = self.chi2chain.GetEntries()
        return c2s, cbs

    def init_chains( self, fd, c2states, cbstates ) :
        for filename, c2name, cbname, c2state, cbstate in zip( fd["InputFiles"],\
                fd["Chi2TreeNames"], fd["ContribTreeNAmes"], c2sates, cbstates ) :
            if not hasattr(self,"chi2chain") :
                self.chi2chain =  r.TChain()
            if not hasattr(self, "contribchain") :
                self.contribchian = r.TChain()
            if c2state: 
                self.AddFile( filename, c2name, cbname )  
            self.chi2chain.SetCacheSize(0)    
            self.contrib2chain.SetCacheSize(0)    

    def setup_branches( self ) :
        self.nentries = self.chi2chain.GetEntries()
        if hasattr(self,"contribchain") :
            self.chi2chain.AddFriend(self.contribchain)
        self.nTotVars = self.chi2chain.GetLeaf(self.branch_name).GetLen()
        self.chi2vars = array('d',[0]*self.nTotVars)
        self.chi2chain.SetBranchAddress(self.branch_name,self.chi2vars)
        if self.contrib_state :
            self.contribvars = array('d',[0]*self.nTotVars)
            self.contribchain.SetBranchAddress(self.contrib_branch_name,self.contribvars)


    def GetEntry( self, entry ) :
        read = 0
        if self.chi2_state :
            read = self.chi2chain.GetEntry(entry)
        else :
            print "No main tree available to source entries"
        return read

    def GetEntries( self ) :
        n_entries = -1
        if self.chi2_state :
            n_entries = self.chi2chain.GetEntries()
        else :
            "No valid entries"
        return n_entries

    def GetBranchLength( self ) :
        return self.nTotVars

    def GetTreeNumber( self ) :
        return self.chi2chain.GetTreeNumber()
