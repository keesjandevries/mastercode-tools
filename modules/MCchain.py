#! /usr/bin/env python

import ROOT as r
from array import array

def check_files( collection ) :
    nfiles = len(collection.files)
    chi2_states = [None]*nfiles
    contrib_states = [None]*nfiles
    for pos, f in enumerate( collection.files ) :
        chi2_states[pos], contrib_states[pos] = \
        check_file( f.FileName, f.Chi2TreeName, f.ContribTreeName )
    return chi2_states, contrib_states

def check_file( filename, chi2treename, contribtreename ) :
    tf = r.TFile( filename )

    chi2tree  = tf.Get(chi2treename)
    conttree  = tf.Get(contribtreename)

    contrib_state = conttree  is not None
    chi2_state    = chi2tree  is not None

    return chi2_state,contrib_state


class MCchain( object ) :
    def __init__( self, mcfc ) :
        self.branch_name         = mcfc.Chi2BranchName
        self.contrib_branch_name = mcfc.ContribBranchName
        chi2_states, contrib_states = check_files( mcfc )
        self.chi2chain =  r.TChain()
        self.contribchain = r.TChain()
        self.init_chains( mcfc, chi2_states, contrib_states )
        self.setup_branches()

    def AddFile( self, fname, chi2treename, contribtreename ) :
        c2s, cbs = check_file( fname, chi2treename, contribtreename )

        if c2s and cbs :
            self.chi2chain.AddFile(fname,-1,chi2treename)
            self.contribchain.AddFile(fname,-1,contribtreename)

        self.nentries = self.chi2chain.GetEntries()
        return c2s, cbs

    def init_chains( self, collection, c2states, cbstates ) :
        for pos, f in enumerate(collection.files) :
            if c2states[pos]:
                self.AddFile( f.FileName, f.Chi2TreeName, f.ContribTreeName )
            self.chi2chain.SetCacheSize(0)
            self.contribchain.SetCacheSize(0)

    def setup_branches( self ) :
        self.nentries = self.chi2chain.GetEntries()
        self.chi2chain.AddFriend(self.contribchain)
        self.nTotVars = self.chi2chain.GetLeaf(self.branch_name).GetLen()
        self.chi2vars = array('d',[0]*self.nTotVars)
        self.chi2chain.SetBranchAddress(self.branch_name,self.chi2vars)
        self.contribvars = array('d',[0]*self.nTotVars)
        self.contribchain.SetBranchAddress(self.contrib_branch_name,self.contribvars)


    def GetEntry( self, entry ) :
        read = 0
        read = self.chi2chain.GetEntry(entry)
        return read

    def GetEntries( self ) :
        n_entries = -1
        n_entries = self.chi2chain.GetEntries()
        return n_entries

    def GetBranchLength( self ) :
        return self.nTotVars

    def GetTreeNumber( self ) :
        return self.chi2chain.GetTreeNumber()
