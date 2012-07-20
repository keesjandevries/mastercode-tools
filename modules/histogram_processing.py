#! /usr/bin/env python
import ROOT as r
import mcspace as s
from modules.mcchain import MCAnalysisChain
from progress_bar import ProgressBar
from sys import stdout
from array import array
from operator import mul

from modules import variables as v
from modules import lhood_dict 
from modules.lhood_module import LHood

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
    return int( h.ClassName()[2] )

def get_histogram_bin_range(h, minimums = None, maximums = None):
    dim = get_histogram_dimension(h)
    axes = ["X", "Y", "Z"]

    if maximums is None:
        maximums = []
        for axis in axes[0:dim]:
            axis_nbins = eval("h.Get{axis}axis().GetNbins()".format(axis=axis))
            maximums.append(eval("h.Get{axis}axis().GetBinUpEdge({abin})".format(axis=axis,abin=axis_nbins)))
    if minimums is None:
        minimums = [0]*len(maximums)
    first_bin = h.FindBin(*minimums)
    last_bin = h.FindBin(*maximums)
    return first_bin, last_bin

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

def initialize_histo( space,hname,entry=False, data=False,chi2=False ) :
    dim = space.dimension

    #initialise bins
    bins = [ array('d',[0.0] * (abins+1)) for abins in space.nbins ]
    # bins wil  be filled with begin_value, ..... , end_value [total nbins+1 values], they mark the bin edges.

#    print "***"
#    for index, min_val, max_val, nbins, name, log in zip( obj.indices,
#            obj.min_vals, obj.max_vals, obj.nbins, obj.names,
#            obj.log ) :
#        print index, min_val, max_val, nbins, name, log
#    print "***"

    for i,log in enumerate(space.log) :
        if log :
            logmin = r.TMath.Log10( space.min_vals[i] )
            logmax = r.TMath.Log10( space.max_vals[i] )
            binwidth = (logmax - logmin) / float(space.nbins[i])
            for c, b in enumerate( bins[i] ) :
                bins[i][c] = r.TMath.Power( 10, logmin+c*binwidth)
        else :
            bmin = space.min_vals[i]
            bmax = space.max_vals[i]
            binwidth = float(bmax-bmin) / float(space.nbins[i])
            for c in range(len( bins[i] )) :
                bins[i][c] = bmin + binwidth*c

    title_f = ";%s" * dim
    title = title_f % tuple( space.names )

    args = []
    [ args.extend( [ nb, b ] ) for nb, b in zip( space.nbins, bins ) ]

    if entry:
        histo = eval( "r.TH%dI( hname, title, *args )" % dim )
        content = -1
    elif chi2:
        histo = eval( "r.TH%dD( hname, title, *args )" % dim )
        content = r.Long(1e9)
    elif data:
        histo = eval( "r.TH%dD( hname, title, *args )" % dim )
        content = r.Long(1e9)
    else:
        histo = None
        content = None


    up_bin = [ abin + 1 for abin in space.nbins ]

    first_bin, last_bin = get_histogram_bin_range(histo)
    for i in range(first_bin,last_bin+1) :
        if not histo.IsBinUnderflow(i) and not histo.IsBinOverflow(i) :
            histo.SetBinContent(i,content)

    return histo


def get_modified_data_chi2(chain,KOhack):
    if  KOhack.get_hack_applied(): chi2 = KOhack.get_bin_KO_chi2(chain) 
    else  : chi2= chain.treeVars["contributions"][0]
    return chi2 

def get_values_from_chain(chain,plot,vars,s,KOhack):
    values=[]
    for var_name in plot.get_short_names():
       var = vars[var_name]
       if (var.__class__.__name__ == "MCVariable") and not KOhack.get_hack_applied():
           index = var.get_index(plot.mcf)
           values.append( chain.treeVars["predictions"][ index ] )
       elif (var.__class__.__name__ == "DerivedMCVariable") and not KOhack.get_hack_applied() :
           input_vars_sns = var.get_input_vars()
           input_mcvs = [vars[mcvsn] for mcvsn in input_vars_sns  ]
           input_args = [chain.treeVars["predictions"][ mcv.get_index(plot.mcf)] for mcv in input_mcvs   ]
           values.append(var.function(input_args) )
       elif   KOhack.get_hack_applied():
           mneu1=chain.treeVars["predictions"][KOhack.mneu1_index]
           KO_ssi=KOhack.df*chain.treeVars["predictions"][s+KOhack.KOssi_first_index ] 
           values=[mneu1,KO_ssi]
    return values

def get_dimension_factor(plot):
    df=1
    for n in plot.get_short_names():
        if "cm" in n: 
            df=1.e-36
    return df

def check_entry_KO_hack(plot):
    hack=plot.KOhack
    return hack

def calculate_entry_histograms( plots, chain ) :
    ##assert canvas is not None, "Canvas must be specified in calculate_histograms"
    # setup our 2d histos
    vars = v.mc_variables()
    # KOhack class gets initiated, because it has to be checked "if KOhack is applied"
    KOhack=KOhack_class(plots[0].mcf)
    histos = []
    chi2histos = []
    for p in plots :
        hname = histo_name( p.short_names, entry_histo_prefix )
        cname = histo_name( p.short_names, chi2_histo_prefix )

        entryhisto = initialize_histo( p,hname,entry=True )
        chi2histo  = initialize_histo( p,cname,chi2 =True )

        histos.append(entryhisto)
        chi2histos.append(chi2histo)

        if check_entry_KO_hack(p):
            KOhack.init_hack()
            KOhack.noxenon2011=p.noxenon2011
            KOhack.df=get_dimension_factor(p)

    nentries = chain.GetEntries()
    prog = ProgressBar(0, nentries+1, 77, mode='fixed', char='#')
    for entry in range(0,nentries+1) :
        prog.increment_amount()
        print prog,'\r',
        stdout.flush()
        chain.GetEntry(entry)
        for h, c, plot in zip( histos, chi2histos, plots ) :
            steps = 1
            if KOhack.get_hack_applied() and check_entry_KO_hack(plot):
                steps = 21
            for s in range(0,steps):
                vals = get_values_from_chain(chain,plot,vars,s,KOhack) 
                nbins = plot.bins
                ibin = h.FindBin(*vals)
                max_bin = h.FindBin(*plot.max_vals)
                if ibin != 0 and ibin < max_bin :
                    chi2 = get_modified_entry_chi2(vals,chain,KOhack,s)
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

#def check_chi_mode(mode):
#    if mode == "chi2" or mode == "dchi":
#        return 0
#
#    # If one specifies dchi_i , then the dX^2 contibution of constraint i is given!
#    m=mode.split("_")
#    if len(m) == 2 and m[0]=="dchi":
#        i= int(m[1])
#        return i
#
#    else:
#        return -1




def fill_bins( histo_cont, contrib_cont,predict_cont, contribs,predicts  , bin , chain, mcf, KOhack ):
    for mode in histo_cont.keys() :
        fill = False
        curr_content = histo_cont[mode].GetBinContent(bin)
        content = 0.
        if mode == "chi2" or mode == "dchi" :
            # for dchi offset is done later
            content = get_modified_data_chi2(chain,KOhack) 
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
                    contrib_cont[contrib.short_name].SetBinContent(bin, chain.treeVars["contributions"][contrib.index] ) #!!!
                for predict in predicts :
                    predict_cont[predict.short_name].SetBinContent(bin, chain.treeVars["predictions"][predict.index] ) #!!!

#This class contains the full hack for making the ssi-plots. In principle we could make the scan for each plot but this is costly.
class KOhack_class(object):
    def __init__(self,mcf):
        self.mcf            = mcf
        self.hack_applied   = False
        self.noxenon2011    = False
        self.df             = 1 #dimention factor, to go to cm-2 df=10^-36
        # the rest only gets initiated upon calling init_hack 
        self.mneu1_index=None
        self.KOssi_first_index=None
        self.bin_range=None
        self.ssi_bin_range= None
        self.lhood = None
        self.KOssi_histo_index = None
        self.ssi_axis = None
        self.xenon_ssi_sn = None
        self.xenon_ssi_index = None

    def init_hack(self):
        self.ssi_axis = 'Y' # FIXME:this is now hard coded!!!
        self.hack_applied=True
        self.init_xenon2012_lhood() 
        self.init_var_indices()

    def init_xenon2012_lhood(self):
        from modules.lhood_dict import get_lhood_dict
        from modules.lhood_module import LHood
        xenon2011_dict=get_lhood_dict()["Xenon2011"]
        self.lhood = LHood(None,xenon2011_dict)
        self.xenon_ssi_sn = xenon2011_dict["vars"][1]
        print self.xenon_ssi_sn

    def init_var_indices(self):
        vars = v.mc_variables()
        # one will need indices: first   of KO's (to find the other 21); m_neutralino; ssi with whith the normal X^2 was calculated
        self.KOssi_first_index=vars["KOsigma_pp^SI"].get_index(self.mcf)
        self.mneu1_index = vars["neu1"].get_index(self.mcf)
        self.xenon_ssi_index = vars[self.xenon_ssi_sn].get_index(self.mcf)
        print self.KOssi_first_index, self.mneu1_index, self.xenon_ssi_index
         

################## Genaral    - functions #########################
    def get_lh_chi2(self,mneu1,ssi):
        return self.lhood.test_chi2([mneu1,ssi])

    def set_axis(self, axis):
        self.ssi_axis= axis

    def get_hack_applied(self):
        return self.hack_applied

################## DataHistos - functions #########################
    def set_ssi_bin_range(self,histo, i_bin):
        assert self.ssi_axis is not None
        nX,nY,nZ=r.Long(0),r.Long(0),r.Long(0)
        histo.GetBinXYZ(i_bin,nX,nY,nZ)
        low_ssi=eval("histo.Get%saxis().GetBinLowEdge(n%s)" % (self.ssi_axis,self.ssi_axis) )
        up_ssi =eval("histo.Get%saxis().GetBinUpEdge(n%s)" % (self.ssi_axis,self.ssi_axis) )
        self.bin_range= [low_ssi,up_ssi]

    def get_KO_chi2(self,chain  , ssi_i):
        # USE [pb] AS UNIT !!!
        mneu1       = chain.treeVars["predictions"][self.mneu1_index]
        xenon_ssi   = chain.treeVars["predictions"][self.xenon_ssi_index]
        old_tot_chi2= chain.treeVars["contributions"][0]
        KO_ssi      = chain.treeVars["predictions"][ssi_i+self.KOssi_first_index ]

#        ZSigPiNs=[0,0, 0.2,-0.,2, 0.4,-0.4, 0.6,-0.6, 0.8,-0.8, 1.0,-1.0,
#               1.33,-1.33, 1.66,-1.66, 2.0,-2.0, 2.5,-2.5, 3.0,-3.0]
        Zs=[ 0.2, 0.4, 0.6, 0.8, 1.0,  1.33, 1.66, 2.0, 2.5, 3.0]
        ZSigPiNs=[0.]+Zs+[-Z for Z in Zs]
        if self.noxenon2011:
            chi2=ZSigPiNs[ssi_i]**2 + old_tot_chi2
        else:
            chi2=  ZSigPiNs[ssi_i]**2 +self.get_lh_chi2(mneu1,KO_ssi) + (old_tot_chi2 - self.get_lh_chi2(mneu1,xenon_ssi)) 
        return chi2

    def get_bin_KO_chi2(self,chain):
        # USE UNIT OF PLOT. if [cm^-2] then df=1e-36
        KO_ssis  = [self.df*chain.treeVars["predictions"][i+self.KOssi_first_index ]  for i in range(0,20)]

        #work out which of these lie in the bin
        ssi_i_s_in_bin=[]
        for i, ssi in enumerate(KO_ssis):
            if ssi > self.bin_range[0] and ssi < self.bin_range[1]:
                ssi_i_s_in_bin.append(i)

        # calculate their X^2. The minimum gets assigned to this bin
        X2s_in_bin= [self.get_KO_chi2(chain, ssi_i)  for ssi_i in ssi_i_s_in_bin ]
        if len(X2s_in_bin)==0:
            chi2=1e9
        else:
            chi2=min(X2s_in_bin)
        return chi2


def get_modified_entry_chi2(values,chain,KOhack,s):
    if  KOhack.get_hack_applied(): 
        chi2 = KOhack.get_KO_chi2(chain, s) 
    else  : chi2= chain.treeVars["contributions"][0]
    return chi2 
        

def fill_and_save_data_hists( mcf, plots,entry_hists, modes, contribs,predicts ) :
    axes = [ "X", "Y", "Z" ]
    chain = MCAnalysisChain( mcf )
    nentries = chain.GetEntries()
    
    KOhack=KOhack_class(mcf)
    for p , h in zip(plots,entry_hists) :
#############################################
        if check_entry_KO_hack(p):
            KOhack.init_hack()
            KOhack.noxenon2011=p.noxenon2011
            KOhack.df=get_dimension_factor(p)
#############################################
            
        histo_cont = {}
        contrib_cont = {}
        predict_cont = {}

        print p.short_names
        firstbin, lastbin = get_histogram_bin_range(h)
        for mode in modes :
            # here need to add in check on contrib and make one for each contribution
            hname = histo_name( p.short_names, entry_histo_prefix )+ "_" + mode
            histo_cont[mode] =initialize_histo( p,hname,data =True ) 
            base_val = 1e9
            if mode == "pval" :
                base_val = 0.0
            for bin in range( firstbin, lastbin + 1 ) :
                histo_cont[mode].SetBinContent( bin, base_val )
        for c in contribs : # contribs is a list of Contribution objects
            contrib_cont[c.short_name] = eval( 'r.TH%dD( h.GetName() + "_dX_" + c.short_name, title, *th_arg_list )' % h_dim )#fixme initialisation for modes
            for bin in range( firstbin, lastbin + 1 ) :
                contrib_cont[c.short_name].SetBinContent( bin, 0.0 )
        for p in predicts : # predicts is a list of Contribution objects
            predict_cont[p.short_name] = eval( 'r.TH%dD( h.GetName() + "_pred_" + p.short_name, title, *th_arg_list )' % h_dim )#fixme initialisation for modes
            for bin in range( firstbin, lastbin + 1 ) :
                predict_cont[p.short_name].SetBinContent( bin, 0.0 )

        prog = ProgressBar(0, (lastbin-firstbin)+1, 77, mode='fixed', char='#')
        for i in range( firstbin, lastbin+1 ) :
            prog.increment_amount()
            print prog,'\r',
            stdout.flush()
            entry = int( h.GetBinContent(i) )
            if entry > 0 :
                chain.GetEntry(entry)
#############################################
                if KOhack.get_hack_applied(): 
                     KOhack.set_ssi_bin_range(h,i)
#############################################
                fill_bins( histo_cont, contrib_cont,predict_cont, contribs,predicts  , i, chain, mcf, KOhack )
        perform_zero_offset( histo_cont["dchi"],firstbin,lastbin )
        print
        save_hdict_to_root_file( histo_cont,  mcf.FileName, mcf.DataDirectory)
        save_hdict_to_root_file( contrib_cont, mcf.FileName, mcf.DataDirectory)
        save_hdict_to_root_file( predict_cont, mcf.FileName, mcf.DataDirectory)

def get_entry_hists( mcf, plots ) :
    hl = []
    entry_hist_dict = mcf.EntryDirectory
    hnames = []
    for plot in plots :
        hist_name =  histo_name( plot.short_names, entry_histo_prefix )
        hnames.append( "%s/%s" % ( entry_hist_dict, hist_name ) )
    f = r.TFile.Open( mcf.FileName )
    r.gROOT.cd()
    for hn in hnames :
        assert f.Get(hn), hn + " was not found"
        hl.append( f.Get( hn ).Clone()) 
    f.Close()
    return hl

def get_hist_minimum_values( hl ) :
    mins = []
    for h in hl :
        nbins = h.GetNbinsX()*h.GetNbinsY()
        min_val = 1e9
        first_bin, last_bin = get_histogram_bin_range(h)
        for bin in range(first_bin,last_bin+1):
            c = h.GetBinContent(bin)
            if c < min_val and c > 0 : min_val = c
        mins.append(min_val)
    return mins

def perform_zero_offset( h,firstbin,lastbin ) :
    axes = ["X", "Y", "Z"]
    h_dim = get_histogram_dimension(h)
    axes_nbins = []
    for axis in range(h_dim) :
        axes_nbins.append( eval(" h.GetNbins%s()" % axes[axis] ) )
    first_bin, last_bin = get_histogram_bin_range(h)
    min_val = 1e9
    for bin in range(first_bin, last_bin+1) :
        c = h.GetBinContent(bin)
        if c < min_val and c > 0 : min_val = c
    for bin in range(first_bin, last_bin+1) :
        content = h.GetBinContent(bin)
        h.SetBinContent( bin, content - min_val )
