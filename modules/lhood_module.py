#! /usr/bin/env python

from ctypes import cdll
from ctypes import byref
from ctypes import c_double
from ctypes import c_int

def makeLHLib() :
    import os
    build_dir = "reprocessing"
    cwd = os.getcwd() # get current directory
    try:
        os.chdir(build_dir)
        os.system("make")
    finally:
        os.chdir(cwd)


lhlib_path = './reprocessing/libs/libLH.so'
try:
    open(lhlib_path)
except:
    makeLHLib()
finally:
    lhoodLib = cdll.LoadLibrary('./reprocessing/libs/libLH.so')

contour_base_dir = '../reprocessing/lhoods/contour_lookups/'
lh1d_base_dir = '../reprocessing/lhoods/1d_lookups/'

# should update to have get_chi2 inherited from base LHood
# can abstract the constructor as well and have a function as a member of the class (i.e. LH1D just sets. self.lhood = RadialLikelihood_new

class RadialLikelihood( object ):
    def __init__(self, filename="", chi2 = 5.99, chi2_inf = 0.0) :
        chi2_c     = c_double( chi2 )
        chi2_inf_c = c_double( chi2_inf )
        self.obj = lhoodLib.RadialLikelihood_new( str(filename), byref(chi2_c),
                                                  byref(chi2_inf_c) )
    def get_chi2( self, x, y ) :
        x_c = c_double(x)
        y_c = c_double(y)
        c2_c = c_double()
        lhoodLib.get_chi2( self.obj, byref(x_c), byref(y_c), byref(c2_c))
        return c2_c.value

class CartesianLikelihood( object ) :
    def __init__(self, filename="", function = 6, mu = 0., sigma = 0., ndof = 1 ) :
        function_c = c_int( function )
        mu_c = c_double( mu )
        sigma_c = c_double( sigma )
        ndof_c = c_int( ndof )
        self.obj = lhoodLib.CartesianLikelihood_new( byref(function_c), byref(mu_c),
                                                     byref(sigma_c), byref(ndof_c),
                                                     str(filename) )
    def get_chi2( self, x, y = 0. ) :
        x_c = c_double(x)
        y_c = c_double(y)
        c2_c = c_double()
        lhoodLib.get_chi2( self.obj, byref(x_c), byref(y_c), byref(c2_c))
        return c2_c.value

class LHood( object ) :
    def __init__( self, var_pos, lhd ) :
        self.var_pos = var_pos # i.e. [1,2] for m0,m12
        lh_type = lhd["lhtype"]
        self.name = lhd["name"]
        if lh_type == "Radial" :
            self.LH = RadialLikelihood( *lhd["c_args"] )
        if lh_type == "Cartesian" :
            self.LH = CartesianLikelihood( *lhd["c_args"] )

    def __str__(self ):
        return self.name

    def __repr__(self):
        return self.name

    def get_chi2( self, vals ) :
        args = [ vals[x] for x in self.var_pos ]
        chi2 = self.LH.getChi2( *args  )
        return chi2

    def test_chi2( self, vals ) :
        chi2 = self.LH.getChi2( *vals )
        return chi2
