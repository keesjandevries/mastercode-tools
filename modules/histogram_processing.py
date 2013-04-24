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
from config.smooth_coordinates import get_smooth_coordinates_dict as sm_cor_dic 

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

def get_histogram_bin_range(h, minimums = None, maximums = None,space=None):
    dim = get_histogram_dimension(h)
    axes = ["X", "Y", "Z"]

    if not space is None:
        maximums=[]
        minimums=[]
        bcs = get_bin_centres(space)
        for i in range(dim):
            minimums.append(bcs[i][0])
            maximums.append(bcs[i][-1])

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

def get_bin_edges(space):
    #initialise bins
    bin_edges = [ array('d',[0.0] * (abins+1)) for abins in space.nbins ]

    for i,log in enumerate(space.log) :
        if log :
            logmin = r.TMath.Log10( space.min_vals[i] )
            logmax = r.TMath.Log10( space.max_vals[i] )
            binwidth = (logmax - logmin) / float(space.nbins[i])
            for c, b in enumerate( bin_edges[i] ) :
                bin_edges[i][c] = r.TMath.Power( 10, logmin+c*binwidth)
        else :
            bmin = space.min_vals[i]
            bmax = space.max_vals[i]
            binwidth = float(bmax-bmin) / float(space.nbins[i])
            for c in range(len( bin_edges[i] )) :
                bin_edges[i][c] = bmin + binwidth*c

    return bin_edges

def get_bin_centres(space):
    #initialise bins
    bin_centres = [ array('d',[0.0] * (abins)) for abins in space.nbins ]

    for i,log in enumerate(space.log) :
        if log :
            logmin = r.TMath.Log10( space.min_vals[i] )
            logmax = r.TMath.Log10( space.max_vals[i] )
            binwidth = (logmax - logmin) / float(space.nbins[i])
            for c, b in enumerate( bin_centres[i] ) :
                bin_centres[i][c] = r.TMath.Power( 10, logmin+(c+0.5)*binwidth)
        else :
            bmin = space.min_vals[i]
            bmax = space.max_vals[i]
            binwidth = float(bmax-bmin) / float(space.nbins[i])
            for c in range(len( bin_centres[i] )) :
                bin_centres[i][c] = bmin + binwidth*(c+0.5)

    return bin_centres


def initialize_histo( space,hname,entry=False, data=False,chi2=False ) :
    dim = space.dimension

    #initialise bins
    bins= get_bin_edges(space)

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

    first_bin, last_bin = get_histogram_bin_range(histo,space=space)
#    print "first and last bin", first_bin, last_bin
    for i in range(first_bin,last_bin+1) :
        if not histo.IsBinUnderflow(i) and not histo.IsBinOverflow(i) :
            histo.SetBinContent(i,content)

    return histo


def get_modified_data_chi2(chain,KOhack):
    if  KOhack.get_hack_applied(): chi2 = KOhack.get_KO_chi2(chain,KOhack.bin_centre) 
    else  : chi2= chain.treeVars["contributions"][0]
    return chi2 

def get_values_list_from_chain_and_histo(chain,plot,vars,s,KOhack,histo):
    values_list=[]
    if not check_entry_KO_hack(plot,KOhack):
        values=[]
        for var_name in plot.get_short_names():
            var = vars[var_name]
            if (var.__class__.__name__ == "MCVariable") :
                index = var.get_index(plot.mcf)
                values.append( chain.treeVars["predictions"][ index ] )
            elif (var.__class__.__name__ == "DerivedMCVariable") :
                input_vars_sns = var.get_input_vars()
                input_mcvs = [vars[mcvsn] for mcvsn in input_vars_sns  ]
                input_args = [chain.treeVars["predictions"][ mcv.get_index(plot.mcf)] for mcv in input_mcvs   ]
                values.append(var.function(input_args) )
        values_list.append(values)

    elif  check_entry_KO_hack(plot,KOhack):
        # values from chain
        mneu1=chain.treeVars["predictions"][KOhack.mneu1_index]
        KO_ssi_c=KOhack.df*chain.treeVars["predictions"][KOhack.KOssi_cen50_index ] 
        KO_ssi_u_14 =KOhack.df*chain.treeVars["predictions"][KOhack.KOssi_unc50_14_index ] 
        KO_ssi_u_7  =KOhack.df*chain.treeVars["predictions"][KOhack.KOssi_unc50_7_index ] 
        # values form plot
        bin_centres = KOhack.bin_centres[1]

        # return list of(mneu1, bin centre)'s, with bin centres within 2 (asymmetric) sigma
        for b_c in bin_centres:
            if( (b_c - KO_ssi_c) < 2*KO_ssi_u_14)  and ( (KO_ssi_c - b_c ) < 2* KO_ssi_u_7) :
                values_list.append((mneu1,b_c))
    return values_list


def get_dimension_factor(plot):
    df=1
    for n in plot.get_short_names():
        if "cm" in n: 
            df=1.e-36
    return df

def check_entry_KO_hack(plot,KOhack):
    hack=plot.KOhack
    KOhack.hack_applied=hack
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

        if check_entry_KO_hack(p,KOhack):
            KOhack.init_hack(p)

    nentries = chain.GetEntries()
    prog = ProgressBar(0, nentries+1, 77, mode='fixed', char='#')
    for entry in range(0,nentries+1) :
        prog.increment_amount()
        print prog,'\r',
        stdout.flush()
        chain.GetEntry(entry)
        for h, c, plot in zip( histos, chi2histos, plots ) :
            vals_list = get_values_list_from_chain_and_histo(chain,plot,vars,s,KOhack,h)
            for vals in vals_list:
                nbins = plot.bins
                ibin = h.FindBin(*vals)
                max_bin = h.FindBin(*plot.max_vals)
                if ibin != 0 and ibin < max_bin :
                    chi2 = get_modified_entry_chi2(vals,chain,KOhack)
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
        self.df             = 1 #dimention factor, to go to cm-2 df=10^-36
        # the rest only gets initiated upon calling init_hack 
        self.mneu1_index    = None
        self.lhood          = None
        self.lhood_name     = None
        self.ssi_axis       = None
        self.xenon_ssi_sn   = None
        self.xenon_ssi_index= None
        self.KOssi_cen50_index      = None 
        self.KOssi_unc50_14_index   = None 
        self.KOssi_unc50_7_index    = None 
        self.mneu1_index            = None 

    def init_hack(self,space=None):
        self.ssi_axis = 'Y' # FIXME:this is now hard coded!!!
        self.hack_applied=True
        #if not space == None:
        if space is not None:
            self.init_lhood(space)
            self.init_var_indices()
            self.df=get_dimension_factor(space)
            self.bin_centres=get_bin_centres(space)

    def init_lhood(self,space):
        from modules.lhood_dict import get_lhood_dict
        from modules.lhood_module import LHood
        self.lhood_name= space.xenon_lhood_name
        if self.lhood_name is not None:
            xenon_dict=get_lhood_dict()[self.lhood_name]
            self.lhood = LHood(None,xenon_dict)
            self.xenon_ssi_sn = xenon_dict["vars"][1]
        print self.xenon_ssi_sn

    def init_var_indices(self):
        vars = v.mc_variables()
        # one will need indices: first   of KO's (to find the other 21); m_neutralino; ssi with whith the normal X^2 was calculated
        self.KOssi_cen50_index      = vars["KOsigma_pp^SI_cen50"].get_index(self.mcf)
        self.KOssi_unc50_14_index   = vars["KOsigma_pp^SI_unc50_14"].get_index(self.mcf)
        self.KOssi_unc50_7_index    = vars["KOsigma_pp^SI_unc50_7"].get_index(self.mcf)
        self.mneu1_index            = vars["neu1"].get_index(self.mcf)
        if self.lhood_name is not None:
            self.xenon_ssi_index = vars[self.xenon_ssi_sn].get_index(self.mcf)
        print  self.mneu1_index, self.xenon_ssi_index
         

################## Genaral    - functions #########################
    def get_lh_chi2(self,mneu1,ssi):
        return self.lhood.test_chi2([mneu1,ssi])

    def set_axis(self, axis):
        self.ssi_axis= axis

    def get_hack_applied(self):
        return self.hack_applied

################## DataHistos - functions #########################

    def set_ssi_bin_centre(self,histo, i_bin):
        assert self.ssi_axis is not None
        nX,nY,nZ=r.Long(0),r.Long(0),r.Long(0)
        histo.GetBinXYZ(i_bin,nX,nY,nZ)
        centre_ssi=eval("histo.Get%saxis().GetBinCenter(n%s)" % (self.ssi_axis,self.ssi_axis) )
        self.bin_centre=centre_ssi

    def get_KO_chi2(self,chain,ssi_b_c_plot  ):
        # USE [pb] AS UNIT !!!
        ssi_b_c= (ssi_b_c_plot/self.df)
        mneu1       = chain.treeVars["predictions"][self.mneu1_index]
        old_tot_chi2= chain.treeVars["contributions"][0]
        KO_ssi_c    = chain.treeVars["predictions"][self.KOssi_cen50_index ] 
        KO_ssi_u_14 = chain.treeVars["predictions"][self.KOssi_unc50_14_index ] 
        KO_ssi_u_7  = chain.treeVars["predictions"][self.KOssi_unc50_7_index ] 
        if self.lhood_name is not None:
            xenon_ssi   = chain.treeVars["predictions"][self.xenon_ssi_index]

        if self.lhood_name is None:
            chi2= self.get_asym_gauss_chi2(KO_ssi_c,ssi_b_c,KO_ssi_u_14,KO_ssi_u_7) + old_tot_chi2
        else:
            chi2= self.get_asym_gauss_chi2(KO_ssi_c,ssi_b_c,KO_ssi_u_14,KO_ssi_u_7) + self.get_lh_chi2(mneu1,ssi_b_c) + (old_tot_chi2 - self.get_lh_chi2(mneu1,xenon_ssi)) 
        return chi2
    
    def get_asym_gauss_chi2(self,mu,val,unc_up,unc_down):
        assert unc_up is not 0
        assert unc_down is not 0
        if val >  mu : chi2=((mu-val)/unc_up)**2
        if val <= mu : chi2=((mu-val)/unc_down)**2
        return chi2

    def get_gauss_chi2(self,cent,meas,unc):
        assert unc is not 0
        return ((cent-meas)/unc)**2



def get_modified_entry_chi2(values,chain,KOhack):
    if  KOhack.get_hack_applied(): 
        b_c = values[1]
        chi2 = KOhack.get_KO_chi2(chain, b_c) 
    else  : chi2= chain.treeVars["contributions"][0]
    return chi2 
        


def plot_and_save_smooth_spline(dchi_histos,mcf,spaces):
    hd={}
    for hist,space in zip(dchi_histos,spaces):
        if len(space.short_names)==1:
            sn=space.short_names[0]
            print sn
            s_hist = hist 
            for coord in sm_cor_dic()[mcf.FileName][sn]:
                xmin, xmax, smooth = coord
                s_hist.GetXaxis().SetRangeUser(xmin,xmax)
                s_hist.Smooth(smooth,"R")
                s_hist.GetXaxis().SetRange(0,0)
            perform_zero_offset(s_hist,space=space)
            hd[sn]=s_hist
    save_hdict_to_root_file( hd, mcf.FileName, mcf.SmoothDirectory ) 

    

def fill_and_save_data_hists( mcf, plots,entry_hists, modes, contribs,predicts ) :
    axes = [ "X", "Y", "Z" ]
    chain = MCAnalysisChain( mcf )
    nentries = chain.GetEntries()
    
    KOhack=KOhack_class(mcf)
    for p , h in zip(plots,entry_hists) :
#############################################
        if check_entry_KO_hack(p,KOhack):
            KOhack.init_hack(p)
#############################################
            
        histo_cont = {}
        contrib_cont = {}
        predict_cont = {}

        print p.short_names
        firstbin, lastbin = get_histogram_bin_range(h,space=p)
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
            hname = histo_name( p.short_names, entry_histo_prefix )+ "_dX_" + c.short_name
            contrib_cont[c.short_name] = initialize_histo( p,hname,data =True )
            for bin in range( firstbin, lastbin + 1 ) :
                contrib_cont[c.short_name].SetBinContent( bin, 0.0 )

        for pred in predicts : # predicts is a list of Contribution objects
            hname = histo_name( p.short_names, entry_histo_prefix )+ "_pred_" + pred.short_name
            predict_cont[pred.short_name] = initialize_histo( p,hname,data =True )
            for bin in range( firstbin, lastbin + 1 ) :
                predict_cont[pred.short_name].SetBinContent( bin, 0.0 )

        prog = ProgressBar(0, (lastbin-firstbin)+1, 77, mode='fixed', char='#')
        for i in range( firstbin, lastbin+1 ) :
            prog.increment_amount()
            print prog,'\r',
            stdout.flush()
            entry = int( h.GetBinContent(i) )
            if entry > 0 :
                chain.GetEntry(entry)
#############################################
                if check_entry_KO_hack(p,KOhack): 
                     KOhack.set_ssi_bin_centre(h,i)
#############################################
                fill_bins( histo_cont, contrib_cont,predict_cont, contribs,predicts  , i, chain, mcf, KOhack )
        perform_zero_offset( histo_cont["dchi"],space=p )
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

def get_dchi_hists( mcf, plots ) :
    hl = []
    dchi_hist_dict = mcf.DataDirectory
    hnames = []
    for plot in plots :
        hist_name =  histo_name( plot.short_names, entry_histo_prefix )+"_dchi"
        hnames.append( "%s/%s" % ( dchi_hist_dict, hist_name ) )
    f = r.TFile.Open( mcf.FileName )
    r.gROOT.cd()
    for hn in hnames :
        assert f.Get(hn), hn + " was not found"
        hl.append( f.Get( hn ).Clone()) 
    f.Close()
    return hl
# this function seems redundant
#def get_hist_minimum_values( hl ) :
#    mins = []
#    for h in hl :
#        nbins = h.GetNbinsX()*h.GetNbinsY()
#        min_val = 1e9
#        first_bin, last_bin = get_histogram_bin_range(h)
#        for bin in range(first_bin,last_bin+1):
#            c = h.GetBinContent(bin)
#            if c < min_val and c > 0 : min_val = c
#        mins.append(min_val)
#    return mins

def perform_zero_offset( h,space=None ) :
    axes = ["X", "Y", "Z"]
    h_dim = get_histogram_dimension(h)
    axes_nbins = []
    for axis in range(h_dim) :
        axes_nbins.append( eval(" h.GetNbins%s()" % axes[axis] ) )
    first_bin, last_bin = get_histogram_bin_range(h,space=space)
    min_val = 1e9
    for bin in range(first_bin, last_bin+1) :
        c = h.GetBinContent(bin)
        if c < min_val and c >= 0 : min_val = c
    for bin in range(first_bin, last_bin+1) :
        content = h.GetBinContent(bin)
        h.SetBinContent( bin, content - min_val )
