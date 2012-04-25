from histogramProcessing import entry_histo_name as histn


def HistExists(name):
    return name

def ParseVar(arg):
    s=arg.split("=")
    var=s[0].replace(' ','')
    val=float(s[1])
    return var, val

def search_hist_name(vars,mcf):
    vl=[]
    name="_"
    for k in vars.keys():
        vl.append(k)
    if len(vl)==1:
        name=histn(vl,mcf)
        return HistExists(name)

    if len(vl)==2:
        name=histn(vl,mcf)
        if HistExists(name):
            return name
        else:
            vlreverse=[vl[1],vl[0]]
            name=histn(vlreverse,mcf)
            return HistExists(name)

    else:
        return 0


def GetEntryFromHisto(name,mcf):
    return 1000

def GetVars(argv):
    # will output something like  {"m0" : 500, "m12" : 1000}
    vars={}
    for arg in argv:
        var,val=  ParseVar(arg)  
        vars[var]=val
    return vars
                        
def GetEntry(vars,mcf):
    name=search_hist_name(vars,mcf)
    print name
    if name:
        n=GetEntryFromHisto(name,mcf)
    return 1000

def PrintInfo(n,mcf):
    print  n, mcf.FileName


