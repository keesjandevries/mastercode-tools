class MCFile() :

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

''' Stores MCFile objects for recalculation that have the same global
    properties required for recalculation  '''
class MCFileCollection() :

    def __init__( self, mcfs, collection_options ) :
        for fpos in range(1, len(mcfs) ) :
            for prop in [ "Chi2BranchName", "ContribBranchName", 
                          "PredictionIndex", "SpectrumIndex", "Inputs" ] :
                mcf_attr = getattr(mcfs[fpos],prop,None)
                if mcf_attr is not None and mcf_attr != collection_options[prop] :
                    print "%s in %s overriden by collection" % ( prop, mcfs[fpos].filename )
                    print "\t%s --> %s" % ( mcfs[fpos].prop, collection_options[prop] )

        self.files = mcfs
        for key,value in collection_options.iteritems() :
            setattr( self, key, value )
        print "%d files added to MCFileCollection" % len(self.files)
