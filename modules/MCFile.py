class MCFile( obj ) :
    def __init__( self, d, warn = True ) :
        attrlist = [ "FileName", "Chi2TreeName", "Chi2BranchName", 
                     "ContribTreeName", "ContribBranchName",  ]
        # set import attributes, print warnign if not present
        for key in attrlist :  
            val = d.get(key,None)
            if val is None and warn :
                print "MCFile Object: %s has not been initialized" % key
            setattr( self,key, val )

        # add if available
        opt_attr = [ "PredictionIndex", "SpectrumIndex", "Inputs" ]
        for key in opt_attr :
            setattr( self, key, d.get(key,None) )

class MCFileCollection( obj ) :
''' Stores MCFile objects for recalculation that have the same global
    properties required for recalculation  '''
    def __init__( self, mcfs, d ) :
        for fpos in range(1, len(self.files) ) :
            for prop in [ "Chi2BranchName", "ContribBranchName", 
                          "PredictionIndex", "SpectrumIndex" ] :
                assert mcfs[fpos].prop == mcfs[0].prop,
                    "%s does not match across all files in collection" % prop
        self.files = mcfs
        print "%d files added to MCFileCollection" % len(self.files)
