#filename="LHC_CDF.dat"
filename="LHCb_large.dat"

with open(filename, 'rb') as f:
    for line in f :
        words=line.split()
        out=[  "%se-9" % words[0] , words[3],words[4]]
        print ' '.join(( '%*s' % (20,i) for i in out    )  )

