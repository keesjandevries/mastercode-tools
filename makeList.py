#! /bin/bash
import os

def print_range(xmin=0, xmax=1000, xstep=1, ymin=0, ymax=1000, ystep=1,
                outfile='test.out', overwrite=False):
    if os.path.isfile(outfile) and not overwrite:
        print ("{filename} already exists, run again with "
               "overwrite").format(filename=outfile)
    else:
        f = open(outfile,'w')
        for x in xrange(xmin,xmax,xstep):
            for y in xrange(ymin,ymax,ystep):
                f.write('{x} {y}\n'.format(x=x, y=y))
        f.close()

if __name__=="__main__":
    print_range()
