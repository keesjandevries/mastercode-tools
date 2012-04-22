class MCFile( obj ) :
    def __init__( self, d ) :
        attrlist = [ "FileName", "Chi2TreeName", "Chi2BranchName", 
                     "ContribTreeName", "ContribBranchName", "PredictionIndex",
                     "SpectrumIndex", "Inputs" ]
        for key in attrlist :  
            val = d.get(key,None)
            if val is None : 
                print "MCFile Object: %s has not been initialized" % key
            setattr( self,key, d.get(key,None) )

class MCFileCollection( obj ) :
    def __init__( self, mcfs, d ) :
        for fpos in range(1, len(self.files) ) :
            for prop in [ "Chi2BranchName", "ContribBranchName", 
                          "PredictionIndex", "SpectrumIndex" ] :
                assert mcfs[fpos].prop == mcfs[0].prop,
                    "%s does not match across all files in collection" % prop
        self.files = mcfs
        print "%d files added to MCFileCollection" % len(self.files)
