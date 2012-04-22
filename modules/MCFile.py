class MCFile( obj ) :
    def __init__( d ) :
        attrlist = [ "Filename", "Chi2TreeName", "Chi2BranchName", 
                     "ContribTreeName", "ContribBranchName", "PredictionIndex",
                     "SpectrumIndex", "Inputs", "MinContrib" ]
        for key in attrlist :  
            val = d.get(key,None)
            if val is None : 
                print "MCFile Object: %s has not been initialized" % key
            setattr( self,key, d.get(key,None) )
