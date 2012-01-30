#! /usr/bin/env python

import ROOT as r
import Variables as v 
import MCchain as MCC
from progress_bar import ProgressBar
from sys import stdout
from array import array

def histo_call_count() :
    c = 0
    while True:
        c += 1
        yield c

def entry_histo_prefix() :
    return "iHist"
def entry_histo_name( v1, v2 ) :
    return "%s_%d_%d" % ( entry_histo_prefix(), v1, v2 )

def save_hlist_to_root_file( hlist, filename, directory = None ) :
    f = r.TFile( filename, "UPDATE" )
    f.cd()
    if directory is not None :
        if not f.cd( directory ) :
            f.mkdir( directory ).cd()
            f.cd( directory )
    for h in hlist :
        h.Write("",r.TObject.kOverwrite)
    f.Close()


def initialize_2d_histo ( space ) :
    xmin, xmax = space.xaxis.min_val, space.xaxis.max_val
    ymin, ymax = space.yaxis.min_val, space.yaxis.max_val
    nxbins = int( space.xaxis.bins ) + 1
    nybins = int( space.yaxis.bins ) + 1

    xbins = array('d',[0.0] * nxbins)
    ybins = array('d',[0.0] * nxbins)

    logx = space.logx
    logy = space.logy

    if logx :
        logxmin = r.TMath.Log10(xmin)
        logxmax = r.TMath.Log10(xmax)
        xbinwidth = (logxmax - logxmin ) / nxbins
        for i, xb in enumerate(xbins) :
            xb = r.TMath.Power(10,logxmin*i*xbinwidth)

    if logy :
        logymin = r.TMath.Log10(ymin)
        logymax = r.TMath.Log10(ymax)
        ybinwidth = (logymax - logymin ) / nybins
        for i, yb in enumerate(ybins) :
            yb = r.TMath.Power(10,logymin*i*ybinwidth)

    title = ";%s;%s" % ( space.xaxis.name, space.yaxis.name )

    hname = entry_histo_name( space.xaxis.index, space.yaxis.index )
    cname = "cHist_%d_%d" % ( space.xaxis.index, space.yaxis.index )

    if logx and logy :
        histo   = r.TH2I( hname, title, nxbins, xbins, nybins, ybins )
        c2histo = r.TH2D( cname, title, nxbins, xbins, nybins, ybins )
    elif logx and not logy :
        histo   = r.TH2I( hname, title, nxbins, xbins, nybins, ymin, ymax )
        c2histo = r.TH2D( cname, title, nxbins, xbins, nybins, ymin, ymax )
    elif logy and not logx :
        histo   = r.TH2I( hname, title, nxbins, xmin, xmax, nybins, ybins )
        c2histo = r.TH2D( cname, title, nxbins, xmin, xmax, nybins, ybins )
    else :
        histo   = r.TH2I( hname, title, nxbins, xmin, xmax, nybins, ymin, ymax )
        c2histo = r.TH2D( cname, title, nxbins, xmin, xmax, nybins, ymin, ymax )

    # set our chi2 histogram to some ridiculous values
    content = r.Long(1e9)
    econtent = -1
    nbins = histo.GetNbinsX()*histo.GetNbinsY()
    for i in range(0,nbins+1) :
        if not histo.IsBinUnderflow(i) and not histo.IsBinOverflow(i) :
           c2histo.SetBinContent(i,content)
           histo.SetBinContent(i,econtent)

    return histo, c2histo


def calculate_entry_histograms( spaces, chain ) :
    #assert canvas is not None, "Canvas must be specified in calculate_histograms"
    # setup our 2d histos
    histos = []
    chi2histos = []
    for s in spaces :
        entryhisto, chi2histo = initialize_2d_histo( s )
        histos.append(entryhisto)
        chi2histos.append(chi2histo)

    nentries = chain.GetEntries()
    prog = ProgressBar(0, nentries+1, 77, mode='fixed', char='#')
    for entry in range(0,nentries+1) :
        prog.increment_amount()
        print prog,'\r',
        stdout.flush()
        chain.GetEntry(entry) 
        for h, c, s in zip( histos, chi2histos, spaces ) :
            xindex, yindex = s.get_indices()
            x, y = chain.chi2vars[ xindex ], chain.chi2vars[ yindex ]
            nbins = s.xaxis.bins * s.yaxis.bins
            ibin = h.FindBin(x,y)
            if ibin != 0 and ibin < nbins+1 :
                chi2 = chain.chi2vars[0]
                if chi2 < c.GetBinContent(ibin) :
                    c.SetBinContent(ibin, chi2) 
                    h.SetBinContent(ibin, entry)
    return histos
 
def count_ndof( c, min_contrib, inputs ) :
    count = 0
    for x in c[1:] :    
        if x > min_contrib :
            count += 1
    count -= inputs
    return count

def make_all_data_hists( rfile, d, hlist ) :
    # p_hists[0] = chi2
    # p_hists[1] = pval
    # p_hists[2] = dchi2
    p_hists = [ [],[],[] ]
    chain = MCC.MCchain( rfile, d )
    nentries = chain.GetEntries()
    for h in hlist :
        nbinsx = h.GetNbinsX()
        xmax = h.GetXaxis().GetXmax()
        xmin = h.GetXaxis().GetXmin()
        xbins = h.GetXaxis().GetXbins().GetArray()

        nbinsy = h.GetNbinsY()
        ymax = h.GetYaxis().GetXmax()
        ymin = h.GetYaxis().GetXmin()
        ybins = h.GetYaxis().GetXbins().GetArray()

        # basically our histogram isn't getting fully described
        # it means we have to get:
        #   - binning from original histogram
        #   - can be done with the xbins and ybins arrays above but there's
        #   a buffer indexing error

        print "\n[ %f, %f ] :: [ %f, %f ]" % ( xmin, xmax, ymin, ymax )
        
        title = "%s;%s;%s" % ( h.GetTitle(), h.GetXaxis().GetTitle(),
        h.GetYaxis().GetTitle() )

        p_hists[0].append( r.TH2D( h.GetName() + "_chi2", title, nbinsx,
            xmin, xmax, nbinsy, ymin, ymax ) )
        p_hists[1].append( r.TH2D( h.GetName() + "_pval", title, nbinsx,
            xmin, xmax, nbinsy, ymin, ymax ) )
        p_hists[2].append( r.TH2D( h.GetName() + "_dchi", title, nbinsx,
            xmin, xmax, nbinsy, ymin, ymax ) )

        nbins = nbinsx * nbinsy
        #po.set_hist_properties( p_hists[-1] )

        prog = ProgressBar(0, nbins+1, 77, mode='fixed', char='#')
        for i in range( 0, nbins+1 ) :
            prog.increment_amount()
            print "   ", prog,'\r',
            stdout.flush()
            entry = int( h.GetBinContent(i) )
            content = -1
            if entry > 0 :
                chain.GetEntry(entry)
                content = chain.chi2vars[0]
            p_hists[0][-1].SetBinContent( i, content )
            if content > 0 and chain.contrib_state :
                ndof = count_ndof( chain.contribvars, d["MinContrib"], d["Inputs"] )
                p_hists[1][-1].SetBinContent( i, r.TMath.Prob( content, ndof ) )
            p_hists[2][-1].SetBinContent( i, content )
    perform_zero_offset( p_hists[2] )
    return p_hists


def get_entry_hist_list( rfile, d, spaces ) :
    hl = []
    entry_hist_dict = d["EntryDirectory"]
    hnames = []
    for space in spaces :
        hist_name =  entry_histo_name( space.xaxis.index, space.yaxis.index )
        hnames.append( "%s/%s" % ( d["EntryDirectory"], hist_name ) )
    f = r.TFile.Open( rfile )
    r.gROOT.cd()
    for hn in hnames :
        hl.append( f.Get( hn ).Clone() )
    f.Close()
    return hl

def get_hist_minimum_values( hl ) :
    mins = []
    for h in hl :
        nbins = h.GetNbinsX()*h.GetNbinsY()
        min_val = 1e9
        for bin in range(nbins+1) :
            c = h.GetBinContent(bin)
            if c < min_val and c > 0 : min_val = c
        mins.append(min_val)
    return mins

def perform_zero_offset( hl ) :
    for h in hl :
        nbins = h.GetNbinsX()*h.GetNbinsY()
        min_val = 1e9
        for bin in range(nbins+1) :
            c = h.GetBinContent(bin)
            if c < min_val and c > 0 : min_val = c
        for bin in range(nbins+1) :
            content = h.GetBinContent(bin)
            h.SetBinContent( bin, content - min_val )

def set_hist_properties( mode = "chi2", hl = None ) :
    d = { "dchi" : { "YaxisTitleOffset" : 1.5,
                     "ZaxisTitle"       : "#Delta#chi^{2}",
                     "ZaxisTitleOffset" : 2.5,
                     "Minimum"          : [0.],
                     "Maximum"          : [25.],
                   },
          "pval" : { "YaxisTitleOffset" : 1.5,
                     "ZaxisTitle"       : "P(#chi^{2},N_{DOF})",
                     "ZaxisTitleOffset" : 2.5,
                     "Minimum"          : [0.],
                     "Maximum"          : [1.],
                   },
          "chi2" : { "YaxisTitleOffset" : 1.5,
                     "ZaxisTitle"       : "#chi^{2}",
                     "ZaxisTitleOffset" : 2.0,
                     "Minimum"          : get_hist_minimum_values(hl),
                     "Maximum"          : [25.],
                   }
        }

    e = d[mode]
    for i,h in enumerate(hl) :
        h.GetYaxis().SetTitleOffset( e["YaxisTitleOffset"] )
        h.GetZaxis().SetTitle( e["ZaxisTitle"] )
        h.GetZaxis().SetTitleOffset( e["ZaxisTitleOffset"] )

        if len(e["Minimum"]) > 0 :
            h.SetMinimum( e["Minimum"][i] )
            h.SetMaximum( e["Minimum"][i] + e["Maximum"][0] )
        else :
            h.SetMinimum( e["Minimum"][0] )
            h.SetMaximum( e["Maximum"][0] )
