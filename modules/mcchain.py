#! /usr/bin/env python

import ROOT as r
from array import array
from collections import defaultdict

from modules.mcfile import MCFileCollection

#-- Tree Classes
#---------------

class treeData( object ) :
    def __init__(self, content, treeName, branchName) :
        self.content  = content
        self.treeName = treeName
        self.branchName = branchName

class treeFile( object ) :
    def __init__(self, fileName, tData = None ) :
        self.fileName = fileName
        self.treeData = tData
        self.state = checkState(fileName, tData)

def checkState( filename, dataToCheck ) :
    tf = r.TFile( filename )
    state = True
    for tData in dataToCheck :
        if not tf.Get(tData.treeName)  : state = False
    return state

#-- Chain Classes
#----------------

class MCChain( object ) :
    def __init__(self, mcfc) :
        self.state=True
        if mcfc.__class__.__name__ == "MCFile" :
            mcfc = MCFileCollection([mcfc])
        if not hasattr(self, "treeFiles") : setattr( self, "treeFiles", [] )

        if self.state: self.initialize_chains()
        if self.state: self.setup_branches()
        if not self.state: print "MCChain has a problem for", mcfc.FileName

    def initialize_chains( self ) :
        self.chains = {}
        self.branchNames = {}
        for tFile in self.treeFiles :
            if tFile.state :
                for tData in tFile.treeData :
                    if self.chains.get( tData.content, None ) is None :
                        self.chains[ tData.content ] = r.TChain()
                        self.branchNames[ tData.content ] = tData.branchName
                    self.chains[ tData.content ].AddFile( tFile.fileName, -1, tData.treeName )
        for chain in self.chains.values() :
            chain.SetCacheSize(0)
        # it can happen that all of the treeFiles are in a "false" state
        if len(self.chains):
            self.contentKeys = sorted(self.chains.keys())
            self.baseKey = self.contentKeys[0]
        else : 
            print "No files made it into the chain"
            self.state = False

    def setup_branches( self ) :
        self.nTotVars = {}
        self.treeVars = {}
        for contentKey in self.contentKeys :
            if contentKey is not self.baseKey :
                self.chains[self.baseKey].AddFriend( self.chains[contentKey] )
            self.nTotVars[contentKey] = self.chains[contentKey].GetLeaf( self.branchNames[contentKey] ).GetLen()
            self.treeVars[contentKey] = array('d', [0]*self.nTotVars[contentKey])
            self.chains[contentKey].SetBranchAddress( self.branchNames[contentKey], self.treeVars[contentKey] )

    # ROOT access functions
    def GetEntry( self, entry ) :
        read = 0
        read = self.chains[self.baseKey].GetEntry(entry)
        return read

    def GetEntries( self ) :
        n_entries = -1
        n_entries = self.chains[self.baseKey].GetEntries()
        return n_entries

    def GetBranchLength( self ) :
        return self.nTotVars

    def GetTreeNumber( self ) :
        return self.chains[self.baseKey].GetTreeNumber()


class MCRecalcChain( MCChain, object ) :
    def __init__(self, mcfc) :
        for mcf in mcfc.files[1:] :
            assert mcf.Chi2BranchName == mcfc.files[0].Chi2BranchName, "Can only reprocess trees with the same branch name"
        self.treeFiles = [
            treeFile( mcf.FileName, [treeData("predictions", mcf.Chi2TreeName, mcf.Chi2BranchName )]) for mcf in mcfc.files
        ]
        super(MCRecalcChain,self).__init__(mcfc)

class MCAnalysisChain( MCChain, object ) :
    def __init__(self, mcf) : #no need for a collection here
        tData = [
            treeData( "predictions", mcf.Chi2TreeName,    mcf.Chi2BranchName    ),
            treeData( "contributions", mcf.ContribTreeName, mcf.ContribBranchName ),
            treeData( "lhoods", mcf.LHoodTreeName,   mcf.LHoodBranchName   ),
        ]
        self.treeFiles = [
            treeFile( mcf.FileName, tData )
        ]
        super(MCAnalysisChain,self).__init__(mcf)
