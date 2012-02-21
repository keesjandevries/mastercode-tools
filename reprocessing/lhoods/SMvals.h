#ifndef H_SMvals
#define H_SMvals

namespace SMvals
{
    // can just expand this with a list of the values you want
    enum e { MINCHI2, MINCHI2_NOG2, BSMM };

    const int NDOF = 23;
    const int NDOF_NOG2 = 22;
}

double getSMValue( SMvals::e sm )
{
    double val = 0.;
    switch ( sm )
    {   
        case SMvals::MINCHI2:
            val = 33.8867670541;
            break;
        case SMvals::MINCHI2_NOG2:
            val = 21.7813589;
            break;
        case SMvals::BSMM:
            val  = 3.46e-9;     
            break;
        default:
            val = 0;
            break;
    }
    return val;
}

int getSMNDOF( bool incg2 = true )
{
    int ndof = SMvals::NDOF;
    if( !incg2 ) ndof = SMvals::NDOF_NOG2;
    return ndof;
}

#endif    /* H_SMvals */
