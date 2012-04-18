#! /usr/bin/env python

import ROOT as r
import Variables as v 
import MCchain as MCC
from progress_bar import ProgressBar
from sys import stdout
from array import array
from operator import mul

def histo_call_count() :
    c = 0
    while True:
        c += 1
        yield c

def entry_histo_prefix() :
    return "iHist"
def chi2_histo_prefix() :
    return "cHist"
def histo_name( vl = [], f = entry_histo_prefix ) :
    format_string = "%s"
    for v in vl : format_string += "_%d"
    return format_string % ( tuple([f()] + vl) )
# assume histogram naming as above: PREFIX_d1_d2_d3....
def get_histogram_dimension_from_name( name, delim = "_" ) :
    x = name.split(delim)
    return len(x)-1

def get_histogram_dimension( h ):
    return int( h.Class()[2] )

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

# these two can be combined (1d and 2d init functions) using blot
def initialize_1d_histo( line ) :
    xmin, xmax = line.min_val, line.max_val
    nxbins = int( line.bins )

    xbins = array('d',[0.0] * nxbins)

    logx = line.log if hasattr(line,"log") else False

    if logx :
        logxmin = r.TMath.Log10(xmin)
        logxmax = r.TMath.Log10(xmax)
        xbinwidth = (logxmax - logxmin ) / nxbins
        for i, xb in enumerate(xbins) :
            xb = r.TMath.Power(10,logxmin*i*xbinwidth)

    title = ";%s" % ( line.name )
    hname = histo_name( [line.index], entry_histo_prefix )
    cname = histo_name( [line.index], chi2_histo_prefix )

    if logx :
        histo   = r.TH1I( hname, title, nxbins, xbins )
        c2histo = r.TH1D( cname, title, nxbins, xbins )
    else :
        histo   = r.TH1I( hname, title, nxbins, xmin, xmax )
        c2histo = r.TH1D( cname, title, nxbins, xmin, xmax )

    # set our chi2 histogram to some ridiculous values
    content = r.Long(1e9)
    econtent = -1
    nbins = histo.GetNbinsX()
    for i in range(0,nbins+1) :
        if not histo.IsBinUnderflow(i) and not histo.IsBinOverflow(i) :
           c2histo.SetBinContent(i,content)
           histo.SetBinContent(i,econtent)

    return histo, c2histo

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

    hname = histo_name( [space.xaxis.index, space.yaxis.index], entry_histo_prefix )
    cname = histo_name( [space.xaxis.index, space.yaxis.index], chi2_histo_prefix )

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


def calculate_entry_histograms( spaces, lines, chain ) :
    ##assert canvas is not None, "Canvas must be specified in calculate_histograms"
    # setup our 2d histos
    histos = []
    chi2histos = []
    for s in spaces :
        entryhisto, chi2histo = initialize_2d_histo( s )
        histos.append(entryhisto)
        chi2histos.append(chi2histo)
    for l in lines :
        entryhisto, chi2histo = initialize_1d_histo( l )
        histos.append(entryhisto)
        chi2histos.append(chi2histo)

    s_n_l = spaces + lines

    nentries = chain.GetEntries()
    prog = ProgressBar(0, nentries+1, 77, mode='fixed', char='#')
    for entry in range(0,nentries+1) :
        prog.increment_amount()
        print prog,'\r',
        stdout.flush()
        chain.GetEntry(entry) 
        for h, c, plot in zip( histos, chi2histos, s_n_l ) :
            indices = plot.get_indices()
            vals = [ chain.chi2vars[ index ] for index in indices ]
            nbins = plot.bins
            ibin = h.FindBin(*vals)
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

def fill_bins( toFill, bin, chain, d ) : 
    for mode in toFill.keys() :
        fill = False
        curr_content = toFill[mode][-1].GetBinContent(bin)
        content = 0.
        if mode == "chi2" or mode == "dchi" :  
            # for dchi offset is done later
            content = chain.chi2vars[0]
            fill = ( content < curr_content )
        if mode == "pval" :
            if chain.contrib_state :
                ndof = count_ndof( chain.contribvars, d["MinContrib"], d["Inputs"] )
                chi2 = chain.chi2vars[0]
                content = r.TMath.Prob( chi2, ndof )
                fill = ( content > curr_content )
        if fill : toFill[mode][-1].SetBinContent(bin,content)

# attempt to have dimension independant filling
def fill_all_data_hists( rfile, rfileopts, hlist, toFill) :
    axes = [ "X", "Y", "Z" ]
    chain = MCC.MCchain( rfile, rfileopts )
    nentries = chain.GetEntries()

    for h in hlist :
        h_dim = int(h.ClassName()[2])
        dim_range = range(h_dim)
        
        axis_nbins = []
        axis_mins = []
        axis_maxs = []
        axis_bins = []
        axis_titles = []

        th_arg_list  = []

        user_notify_format = ""
        user_notify = []

        title_format = "%s"
        title_items = [ h.GetTitle() ]
        for axis in dim_range :
            axis_nbins.append( eval( "h.GetNbins%s()" % axes[axis] ) )
            axis_mins.append( eval( "h.Get%saxis().GetXmin()" % axes[axis] ) )
            axis_maxs.append( eval( "h.Get%saxis().GetXmax()" % axes[axis] ) )
            axis_bins.append( eval( "h.Get%saxis().GetXbins().GetArray()" % axes[axis] ) )
            axis_titles.append( eval( "h.Get%saxis().GetTitle()" % axes[axis] ) )

            th_arg_list.append( axis_nbins[-1] )
            th_arg_list.append( axis_mins[-1] )
            th_arg_list.append( axis_maxs[-1] )

            user_notify_format += ": [ %f, %f ] :"
            user_notify.append( axis_mins[-1] )
            user_notify.append( axis_maxs[-1] )

            title_format += ";%s"
            title_items.append( axis_titles[-1] )

        print user_notify_format % tuple(user_notify)

        title = title_format % tuple(title_items)
        nbins = reduce(mul, axis_nbins)

        firstbin = h.FindBin( *axis_mins )
        lastbin = h.FindBin( *axis_maxs )
        for mode in toFill.keys() :
            toFill[mode].append( eval( 'r.TH%dD( h.GetName() + "_" + mode, title, *th_arg_list )' % h_dim ) )
            base_val = 1e9
            if mode == "pval" :
                base_val = 0.0
            for bin in range( firstbin, lastbin + 1 ) :
                toFill[mode][-1].SetBinContent( bin, base_val )

        prog = ProgressBar(0, nbins+1, 77, mode='fixed', char='#')
        for i in range( 0, nbins + 1 ) :
            prog.increment_amount()
            print prog,'\r',
            stdout.flush()
            entry = int( h.GetBinContent(i) )
            if entry > 0 :
                chain.GetEntry(entry)
                fill_bins( toFill, i, chain, rfileopts )
        print
    perform_zero_offset( toFill["dchi"] )

def get_entry_hist_list( rfile, d, plots ) :
    hl = []
    entry_hist_dict = d["EntryDirectory"]
    hnames = []
    for plot in plots :
        hist_name =  histo_name( plot.get_indices(), entry_histo_prefix )
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
    axes = ["X", "Y", "Z"]
    for h in hl :
        h_dim = int(h.ClassName()[2])
        axes_nbins = []
        for axis in range(h_dim) :
            axes_nbins.append( eval(" h.GetNbins%s()" % axes[axis] ) )
        nbins = reduce(mul, axes_nbins)
        min_val = 1e9
        for bin in range(nbins+1) :
            c = h.GetBinContent(bin)
            if c < min_val and c > 0 : min_val = c
        for bin in range(nbins+1) :
            content = h.GetBinContent(bin)
            h.SetBinContent( bin, content - min_val )
