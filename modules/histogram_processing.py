#! /usr/bin/env python
import ROOT as r
import mcspace as s
from modules.mcchain import MCAnalysisChain
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
    for v in vl : format_string += "_%s"
    return format_string % ( tuple([f()] + [str(v) for v in vl]) )

def entry_histo_full_path(vl,mcf):
    entry_hist_dict = mcf.EntryDirectory
    hist_name =  histo_name(vl)
    full_name =  "%s/%s" % ( entry_hist_dict, hist_name )
    return full_name


# assume histogram naming as above: PREFIX_d1_d2_d3....
def get_histogram_dimension_from_name( name, delim = "_" ) :
    x = name.split(delim)
    return len(x)-1

def get_histogram_dimension( h ):
    return int( h.Class()[2] )

def save_hdict_to_root_file( hdict, filename, directory = None ) :
    f = r.TFile( filename, "UPDATE" )
    f.cd()
    if directory is not None :
        if not f.cd( directory ) :
            f.mkdir( directory ).cd()
            f.cd( directory )
    print "Saving to %s..." % filename,
    for h in hdict.values() :
        h.Write("",r.TObject.kOverwrite)
    f.Close()
    print "Done"

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

def initialize_histo( obj ) :
    dim = obj.dimension

    bins = [ array('d',[0.0] * (abins+1)) for abins in obj.nbins ]
#    print "***"
#    for index, min_val, max_val, nbins, name, log in zip( obj.indices,
#            obj.min_vals, obj.max_vals, obj.nbins, obj.names,
#            obj.log ) :
#        print index, min_val, max_val, nbins, name, log
#    print "***"

    for i,log in enumerate(obj.log) :
        if log :
            logmin = r.TMath.Log10( obj.min_vals[i] )
            logmax = r.TMath.Log10( obj.max_vals[i] )
            binwidth = (logmax - logmin) / float(obj.nbins[i])
            for c, b in enumerate( bins[i] ) :
                b = r.TMath.Power(10, logmin*c*binwidth)
        else :
            bmin = obj.min_vals[i]
            bmax = obj.max_vals[i]
            binwidth = float(bmax-bmin) / float(obj.nbins[i])
            for c in range(len( bins[i] )) :
                bins[i][c] = bmin + binwidth*c

    title_f = ";%s" * dim
    title = title_f % tuple( obj.names )


    hname = histo_name( obj.short_names, entry_histo_prefix )
    cname = histo_name( obj.short_names, chi2_histo_prefix )

    args = []
    [ args.extend( [ nb, b ] ) for nb, b in zip( obj.nbins, bins )  ]

    histo = eval( "r.TH%dI( hname, title, *args )" % dim )
    c2histo = eval( "r.TH%dD( cname, title, *args )" % dim )

    content = r.Long(1e9)
    econtent = -1

    up_bin = [ abin + 1 for abin in obj.nbins ]
    nbins = reduce(mul, up_bin)
    for i in range(0,nbins) :
        if not histo.IsBinUnderflow(i) and not histo.IsBinOverflow(i) :
            c2histo.SetBinContent(i,content)
            histo.SetBinContent(i,econtent)

    return histo,c2histo

def calculate_entry_histograms( plots, chain ) :
    ##assert canvas is not None, "Canvas must be specified in calculate_histograms"
    # setup our 2d histos
    histos = []
    chi2histos = []
    for p in plots :
        entryhisto, chi2histo = initialize_histo( p )
        histos.append(entryhisto)
        chi2histos.append(chi2histo)

    nentries = chain.GetEntries()
    prog = ProgressBar(0, nentries+1, 77, mode='fixed', char='#')
    for entry in range(0,nentries+1) :
        prog.increment_amount()
        print prog,'\r',
        stdout.flush()
        chain.GetEntry(entry)
        for h, c, plot in zip( histos, chi2histos, plots ) :
            indices = plot.get_indices()
            vals = [ chain.treeVars["predictions"][ index ] for index in indices ]
            nbins = plot.bins
            ibin = h.FindBin(*vals)
            if ibin != 0 and ibin < nbins+1 :
                chi2 = chain.treeVars["predictions"][0]
                if chi2 < c.GetBinContent(ibin) :
                    c.SetBinContent(ibin, chi2)
                    h.SetBinContent(ibin, entry)

    print
    return histos

def count_ndof( c, min_contrib, inputs ) :
    count = 0
    for x in c[1:] :
        if x > min_contrib :
            count += 1
    count -= inputs
    return count

def check_chi_mode(mode):
    if mode == "chi2" or mode == "dchi":
        return 0

    # If one specifies dchi_i , then the dX^2 contibution of constraint i is given!
    m=mode.split("_")
    if len(m) == 2 and m[0]=="dchi":
        i= int(m[1])
        return i

    else:
        return -1


def fill_bins( histo_cont, contrib_cont, contribs, bin, chain, mcf ) :
    for mode in histo_cont.keys() :
        fill = False
        curr_content = histo_cont[mode].GetBinContent(bin)
        content = 0.
        if mode == "chi2" or mode == "dchi" :
        #if check_chi_mode(mode) >= 0:
            # for dchi offset is done later
            #ichi= check_chi_mode(mode)
            content = chain.treeVars["contributions"][0]
            fill = ( content < curr_content )
        if mode == "pval" :
            ndof = count_ndof( chain.treeVars["contributions"], getattr( mcf, "MinContrib", 0 ), getattr( mcf, "Inputs", 0 ) )
            chi2 = chain.treeVars["predictions"][0]
            content = r.TMath.Prob( chi2, ndof )
            fill = ( content > curr_content )
        if fill :
            histo_cont[mode].SetBinContent(bin,content)
            if mode == "chi2" : # want to also fill values for the contrib
                for contrib in contribs :
                    contib_cont[contrib.short_name].SetBinContent(bin, chain.treeVars["contributions"][contrib.index] ) #!!!

#def fill_all_data_hists( mcf, hlist, contribs, toFill, toFillContrib) :
def fill_and_save_data_hists( mcf, modes, hlist, contribs ) :
    axes = [ "X", "Y", "Z" ]
    chain = MCAnalysisChain( mcf )
    nentries = chain.GetEntries()

    for h in hlist :
        histo_cont = {}
        contrib_cont = {}

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

            user_notify_format += ": [ %.2e, %.2e ] :"
            user_notify.append( axis_mins[-1] )
            user_notify.append( axis_maxs[-1] )

            title_format += ";%s"
            title_items.append( axis_titles[-1] )

        print user_notify_format % tuple(user_notify)

        title = title_format % tuple(title_items)
        up_bin = [ abin + 1 for abin in axis_nbins ]
        nbins = reduce(mul, up_bin)

        firstbin = h.FindBin( *axis_mins )
        lastbin = h.FindBin( *axis_maxs )
        for mode in modes :
            # here need to add in check on contrib and make one for each contribution
            histo_cont[mode] = eval( 'r.TH%dD( h.GetName() + "_" + mode, title, *th_arg_list )' % h_dim )
            base_val = 1e9
            if mode == "pval" :
                base_val = 0.0
            for bin in range( firstbin, lastbin + 1 ) :
                histo_cont[mode].SetBinContent( bin, base_val )
        for c in contribs : # contribs is a list of Contribution objects
            contrib_cont[c.short_name] = eval( 'r.TH%dD( h.GetName() + "_" + c.short_name, title, *th_arg_list )' % h_dim )
            for bin in range( firstbin, lastbin + 1 ) :
                contib_cont[c.short_name].SetBinContent( bin, 0.0 )

        prog = ProgressBar(0, nbins+1, 77, mode='fixed', char='#')
        for i in range( 0, nbins + 1 ) :
            prog.increment_amount()
            print prog,'\r',
            stdout.flush()
            entry = int( h.GetBinContent(i) )
            if entry > 0 :
                chain.GetEntry(entry)
                fill_bins( histo_cont, contrib_cont, contribs, i, chain, mcf )
        perform_zero_offset( histo_cont["dchi"] )
        print
        save_hdict_to_root_file( histo_cont,  mcf.FileName, mcf.DataDirectory)
        save_hdict_to_root_file( contrib_cont, mcf.FileName, mcf.DataDirectory)

def get_entry_hist_list( mcf, plots ) :
    hl = []
    entry_hist_dict = mcf.EntryDirectory
    hnames = []
    for plot in plots :
        hist_name =  histo_name( plot.short_names, entry_histo_prefix )
        hnames.append( "%s/%s" % ( entry_hist_dict, hist_name ) )
    f = r.TFile.Open( mcf.FileName )
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

def perform_zero_offset( h ) :
    axes = ["X", "Y", "Z"]
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