def ParseVar(arg):
    s=arg.split("=")
    var=s[0].replace(' ','')
    val=float(s[1])
    return var, val


def GetVars(argv):
    # will output something like  {"m0" : 500, "m12" : 1000}
    vars={}
    for arg in argv:
        var,val=  ParseVar(arg)  
        vars[var]=val
    return vars
                        
def GetEntry(vars,mcf):
    print vars
    return 1000

def PrintInfo(n,mcf):
    print "hello", n, mcf.FileName


