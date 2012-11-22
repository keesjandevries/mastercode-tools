#filename="LHC_CDF.dat"
filename="Kees.dat"

with open(filename, 'rb') as f:
    for line in f :
        words=line.split()
        r=float (words[0])
        v=float (words[1])
        print (3.46e-9)*r, v , 0.0
        #out=[  "%se-9" % words[0] , words[3],words[4]]
#        print ' '.join(( '%*s' % (20,i) for i in out    )  )
#        print "{:4.12f }  {:4.4f}   0.0 ".format( r,v   )
