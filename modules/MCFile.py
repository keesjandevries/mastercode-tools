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
        opt_attr = [ "PredictionIndex", "SpectrumIndex", "Inputs", 
                     "EntryDirectory", "DataDirectory" ]
        for key in opt_attr :
            setattr( self, key, d.get(key,None) )

''' Stores MCFile objects for recalculation that have the same global
    properties required for recalculation  '''
class MCFileCollection() :

    def __init__( self, mcfs, collection_options = None ) :
        # multiple files
        self.files = mcfs
        if len( mcfs ) > 1 or collection_options is not None :
            for fpos in range(0, len(mcfs) ) :
                for prop in [ "Chi2BranchName", "ContribBranchName", 
                              "PredictionIndex", "SpectrumIndex", "Inputs" ] :
                    mcf_attr = getattr(mcfs[fpos],prop,None)
                    if mcf_attr is not None and mcf_attr != collection_options[prop] :
                        print "%s in %s overriden by collection" % ( prop, mcfs[fpos].filename )
                        print "\t%s --> %s" % ( mcfs[fpos].prop, collection_options[prop] )

            for key,value in collection_options.iteritems() :
                setattr( self, key, value )

            req = [ "Chi2BranchName", "ContribBranchName", "LHoodFile", 
                    "ModelFile", "OutputFile" ]
            for attr in req :
                if collection_options.get(attr,None) is None :
                    print "MCFileCollection not given %s" % attr
            print "%d files added to MCFileCollection" % len(self.files)
        else :
            for attr in dir(mcfs[0]) : # copy all the attributes over
                setattr(self, attr, getattr(mcfs[0],attr) )
