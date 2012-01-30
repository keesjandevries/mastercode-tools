#! /usr/bin/env python

class Variable(object) : 
    def __init__(self, index, min_val, max_val, bins = 100, name = "") :
        self.index   = index
        self.min_val = min_val 
        self.max_val = max_val
        self.name    = name
        self.bins    = bins

    def __str__ ( self ) :
        s = ""
        if len(self.name) > 0 :
            s = self.name
        else :
            s = "unnamed"
        return self.name
    
    def __repr__( self ) :
        r = "(%d) %s  [%4.2e, %4.2e]{%d}" % ( self.index, self.name,
            self.min_val, self.max_val, self.bins )
        return r

class Space( object ):
    def __init__( self, v1, v2, logx = False, logy = False ) :
        self.xaxis = v1
        self.yaxis = v2
        self.logx = logx
        self.logy = logy
        self.title = "(%s,%s)" % ( v1.name, v2.name )

    def __str__( self ) :
        return self.title
        
    def __repr__( self ) :
        r = ""
        if not self.logx and not self.logy :
            r = "{%s, %s}" % ( repr(self.xaxis), repr(self.yaxis) )
        if not self.logx and self.logy :
            r = "{%s, %s (LOG)}" % ( repr(self.xaxis), repr(self.yaxis) )
        if self.logx and not self.logy :
            r = "{%s (LOG), %s}" % ( repr(self.xaxis), repr(self.yaxis) )
        else :
            r = "{%s (LOG), %s (LOG)}" % ( repr(self.xaxis), repr(self.yaxis) )
            
        return r

    def get_indices( self ) :
        return [ self.xaxis.index, self.yaxis.index ]

    def get_bins( self ) :
        x = [ self.xaxis.bins, self.yaxis.bins ]
        return x
