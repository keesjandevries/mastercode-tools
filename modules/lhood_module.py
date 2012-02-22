#! /usr/bin/env python

from ctypes import cdll
from ctypes import byref
from ctypes import c_double
from ctypes import c_int
lhoodLib = cdll.LoadLibrary('./reprocessing/libs/libLH.so')

contour_base_dir = '../reprocessing/lhoods/contour_lookups/'
lh1d_base_dir = '../reprocessing/lhoods/1d_lookups/'

# should update to have getChi2 inherited from base LHood
# can abstract the constructor as well and have a function as a member of the class (i.e. LH1D just sets. self.lhood = ContourLikelihood_new

class ContourLikelihood( object ):
    def __init__(self, filename="", chi2 = 5.99, chi2_inf = 0.0) :
        chi2_c     = c_double( chi2 )
        chi2_inf_c = c_double( chi2_inf )
        self.obj = lhoodLib.ContourLikelihood_new( str(filename), byref(chi2_c),
                                                   byref(chi2_inf_c) )
    def getChi2( self, x, y ) :
        x_c = c_double(x)
        y_c = c_double(y)
        c2_c = c_double()
        lhoodLib.getChi2( self.obj, byref(x_c), byref(y_c), byref(c2_c))
        return c2_c.value

class Likelihood1D( object ) :
    def __init__(self, filename="", function = 6, mu = 0., sigma = 0., ndof = 1 ) :
        function_c = c_int( function )
        mu_c = c_double( mu )
        sigma_c = c_double( sigma )
        ndof_c = c_int( ndof )
        self.obj = lhoodLib.Likelihood1D_new( byref(function_c), byref(mu_c),
                                              byref(sigma_c), byref(ndof_c),
                                              str(filename) )
    def getChi2( self, x, y = 0. ) :
        x_c = c_double(x)
        y_c = c_double(y)
        c2_c = c_double()
        lhoodLib.getChi2( self.obj, byref(x_c), byref(y_c), byref(c2_c))
        return c2_c.value
