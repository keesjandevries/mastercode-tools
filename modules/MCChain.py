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
    def __init__(self, fileName, tData = None )
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
        setupBranches()

    def initializeChains( self ) :
        self.chains = {}
        self.brachNames = {}
        for tFile in self.treeFiles :
            if tFile.state :
                for tData in tFile.treeData :
                    if self.chains.get( tData.content, None ) is None :
                        self.chains[ tData.content ] = r.TChain()
                        self.branchNames[ tData.content ] = tData.branchName
                    self.chains[ tData.content ].Add( tFile.fileName, -1, tData.treeName )
        for chain in self.chains.values :
            chain.SetCacheSize(0)
        ## we dont use this
        #self.nentries = self.chain.values()[-1].GetEntries()
        self.contentKeys = sorted(self.chain.keys())
        self.baseKey = self.contentKeys[0]

    def setupBranches( self ) :
        for contentKey in self.contentKeys :
            if contentKey is not self.baseKey :
                self.chains[self.baseChainKey].AddFriend( self.chains[contentKey] )
            self.nTotVars[contentKey] = self.chains[contentKey].GetLeaf( self.branchNames[contentKey] ).GetLen()
            self.treeVars[contentKey] = array('d', [0].self.nTotVars[contentKey])
            self.chains[contentKey].SetBranchAddress( self.branchNames[contentKey], self.treeVars[contentKey] )

    # ROOT access functions
    def GetEntry( self, entry ) :
        read = 0
        read = self.chains[self.baseChainKey].GetEntry(entry)
        return read

    def GetEntries( self ) :
        n_entries = -1
        n_entries = self.chains[self.baseChainKey].GetEntries()
        return n_entries

    def GetBranchLength( self ) :
        return self.nTotVars

    def GetTreeNumber( self ) :
        return self.chains[self.baseChainKey].GetTreeNumber()


class MCRecalcChain( object, MCChain ) :
    def __init__(self, mcfc) :
        self.branchNames["predictions"] = mcfc.files[0].Chi2BranchName
        for mcf in mcfc.files[1:] :
            assert mcf.Chi2BranchName == self.branchName, "Can only reprocess trees with the same branch name"

        self.treeFiles = [
            treeFile( mcf.FileName, [treeData("predictions", mcf.Chi2TreeName, self.branchName)] ) for mcf in mcfc.files
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
