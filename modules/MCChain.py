#! /usr/bin/env python

import ROOT as r
from array import array
from collections import defaultdict

from modules.MCFile import MCFileCollection

#-- Tree Classes
#---------------

class treeData( object ) :
    def __init__(self, content, treeName, branchName) :
        self.content  = content
        self.treeName = treeName
        self.branchName = branchName

class treeFile( object ) :
    def __init__(self, fileName, tData = [] )
        self.fileName = fileName
        self.treeData = tData
        self.state = checkState()

    def checkState( self ) :
        tf = r.TFile( self.fileName )
        state = True
        for tData in self.treeData :
            if tf.Get(tData.treeName) is None : state = False
        return state

#-- Chain Classes
#----------------

class MCChain( object ) :
    def __init__(self, mcfc) :
        if mcfc.__class__.__name__ == "MCFile" :
            mcfc = MCFileCollection([mcfc])
        if not hasattr(self, "treeFiles") : setattr( self, "treeFiles", [] )
        initializeChains()

    def initializeChains( self ) :
        for tFile in self.treeFiles :
            if tFile.state :
                for tData in tFile.treeData :

class MCRecalcChain( object, MCChain ) :
    def __init__(self, mcfc) :
        self.treeFiles = [
            treeFile( mcf.FileName, [treeData("predictions", mcf.Chi2TreeName, mcf.Chi2BranchName)] ) for mcf in mcfc.files
        ]
        super(MCRecalcChain,self).__init__(mcfc)

class MCAnalysisChain( object, MCChain ) :
    def __init__(self, mcf) : #no need for a collection here
        tData = [ 
            treeData( "predictions", mcf.Chi2TreeName,    mcf.Chi2BranchName    ),
            treeData( "contributions", mcf.ContribTreeName, mcf.ContribBranchName ),
            treeData( "lhoods", mcf.LHoodTreeName,   mcf.LHoodBranchName   ),
        ]

        self.treeFiles = [
            treeFile( mcf.FileName, tData )
        ]

        super(MCRecalcChain,self).__init__(mcf)



class MCChain( object ) :
    def __init__( self, mcfc ) :
        if mcfc.__class__.__name__ == "MCFile" :
            mcfc = MCFileCollection([mcfc])
        self.branch_name         = mcfc.Chi2BranchName
        self.contrib_branch_name = mcfc.ContribBranchName
        self.lhood_branch_name   = mcfc.LHoodBranchName
        chi2_states, contrib_states, lhood_states = check_files( mcfc )
        self.chi2chain    = r.TChain()
        self.contribchain = r.TChain()
        self.lhoodchain   = r.TChain()
        self.init_chains( mcfc, chi2_states, contrib_states, lhood_states )
        self.setup_branches()

    def initializeChains( self, collection, c2states, cbstates, lhstates ) :
        for pos, f in enumerate(collection.files) :
            if c2states[pos]:
                self.AddFile( f.FileName, f.Chi2TreeName, f.ContribTreeName, f.LHoodTreeName )
            self.chi2chain.SetCacheSize(0)
            self.contribchain.SetCacheSize(0)
            self.lhoodchain.SetCacheSize(0)

    def AddFile( self, fname, chi2treename, contribtreename ) :
        c2s, cbs, lhs = check_file( fname, chi2treename, contribtreename )

        if c2s and cbs and lhs :
            print " --> Adding file %s" % fname
            self.chi2chain.AddFile(fname,-1,chi2treename)
            self.contribchain.AddFile(fname,-1,contribtreename)
            self.lhoodchain.AddFile(fname,-1,lhoodtreename)

        self.nentries = self.chi2chain.GetEntries()
        return c2s, cbs, lhs

    def init_chains( self, collection, c2states, cbstates, lhstates ) :
        for pos, f in enumerate(collection.files) :
            if c2states[pos]:
                self.AddFile( f.FileName, f.Chi2TreeName, f.ContribTreeName, f.LHoodTreeName )
            self.chi2chain.SetCacheSize(0)
            self.contribchain.SetCacheSize(0)
            self.lhoodchain.SetCacheSize(0)

    def setup_branches( self ) :
        self.nentries = self.chi2chain.GetEntries()
        self.chi2chain.AddFriend(self.contribchain)
        self.chi2chain.AddFriend(self.lhoodchain)
        self.nTotVars = self.chi2chain.GetLeaf(self.branch_name).GetLen()
        self.chi2vars = array('d',[0]*self.nTotVars)
        self.chi2chain.SetBranchAddress(self.branch_name,self.chi2vars)
        self.contribvars = array('d',[0]*self.nTotVars)
        self.contribchain.SetBranchAddress(self.contrib_branch_name,self.contribvars)
        self.lhoodvars = array('d',[0]*self.nTotVars)
        self.lhoodchain.SetBranchAddress(self.lhood_branch_name,self.lhoodvars)


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
