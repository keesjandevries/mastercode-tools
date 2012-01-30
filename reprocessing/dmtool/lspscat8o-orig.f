      PROGRAM LSPSCAT
c
c  calculates the ratio of the spin dependent and independend part of 
c  scattering cross section as a function of the phase angle in mu
c
      REAL*8 pi, MZ, M2, thw, mslr, msll, msnl, msul, msur, msdl,
     &      M1, thmu, tbeta, absm, beta, msdr, msbl, msbr, mstr,
     &      xmin, mlsp, eta, mnucl, yu, yd, t3u, mstl, mu,
     &      t3d, g1, g2, alpha, Mw,deltup,deltdp,deltsp, 
     &      deltun, deltdn, deltsn, mh1, mh2, mbot, mchrm,
     &      eu, ed, sigma2, sigma3, mup, mdown, mstrn, mtop,
     &      mstaur, mstaul, m0, evals(4), evecs(4,4),sinb, 
     &      alph2u, alph2d, alph2s, gf, mr,lambda,spin,
     &      alph3u, alph3d, alph3s, alph3c, alph3t, alph3b, 
     &      sp, sn, ap, an, fp, fn, ftgn, ftup, ftdp, ftsp, mprot, 
     &      mneut, ftun, ftdn, ftsn, ftgp, m0min, m0max, 
     &      sigma, sigrat, alphs, etat(2,2), etab(2,2), etau(2,2), 
     &        etad(2,2), etac(2,2), etas(2,2), M(4,4), compo
     &      sig, At, Ab, Ag, M2x, absmx, sb, Ma, Mo, Mt, Mb,
     &      thmixt, thmixb,ratio,sigmacdms,sigbr2,
     $      msur1,msul1,msdr1,msdl1
      REAL*8  andy1, andy2,y,sig,zf,bdbu,mumd,msmd,r,
     $        mubu,mdbd,msbs,sigy,ftup0,ftdp0,ftsp0,
     $        sigsig,sig0,sigsig0,sigmumd,sigmsmd,sigftup,
     $        sigftdp,sigftsp,sigftun,sigftdn,sigftsn,
     $        sigftgn,sigftgp,sigfn,sigfp,sigsigma3,
     $        a3,a8,siga3,siga8,sigdeltup,sigdeltun,sigdeltdp,
     $        sigdeltdn,sigdeltsp,sigdeltsn,sigan,sigap,
     $        siglambda,sigsigma2
      INTEGER i, j, thuint, numpro, numneu, m0num, nummu,
     &        muint, m2int, sigpow, numth, k, m12, lspi,
     &        l, lspcomp, ij, nstop, nsbot
      COMPLEX*16  z(4), switch, aup, adown, dup, ddown, 
     &        cup, cdown, z321, z421,
     &        mcom, check, lsp(4)
      PARAMETER(pi = 3.141592654d0, MZ = 91.187d0, 
     &           yu = 1.0d0/3.0d0,
     &          t3u = 1.0d0/2.0d0, eu = 2.0d0/3.0d0, 
     &          ed = -1.0d0/3.0d0, g2 = 0.6293d0, 
     &          g1 = 0.3454d0, gf = 1.16639D-05, 
     &       mneut = 0.93956, mprot = 0.93827)
c
      thw = DASIN(DSQRT(0.2315d0))
      yd = yu
      t3d = -t3u
      Mw = Mz*DCOS(thw)

      OPEN(UNIT=10,FILE='scat.dat',status='unknown')
c      OPEN(UNIT=81,FILE='scatadd.dat',status='unknown')

c

ccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
cc  matn.dat contains the 4 neutralino eigenmasses.
cc  There should be 1 negative eigenvalue. These are
cc  followed by the diagonization matrix. Care should be taken
cc to use proper form (not transpose):
cc (Trans(evecs).M.evecs = diag. 
cc                   --> evecs = Transpose(N) in G&H notation)
cc  Here is an example for m12 = 400 and tb = 10 (m0 = 100 A0 = 0)
cc  and mu > 0:  matn.dat
cc
cc       164.920443688    313.806429320    548.423908106   -533.369204875
cc      0.993882051      0.053472729     -0.087677149     -0.040643002
cc     -0.025419833      0.960701854      0.269709565      0.060518844
cc      0.099872004     -0.228883864      0.667234488      0.701737770
cc     -0.039722584      0.147664458     -0.688743498      0.708695787

cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
cc Higgs.dat needs to have the light Higgs mass, heavy scalar mass, and 
cc the mixing angle alpha
cc example    114.70800000000000        594.49530000000004     
cc             -0.10454769999999999  

cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
cc cres.in contains the sin beta in the 3rd spot (1st two can be 0 
cc         or anything)
cc  followed by two more 0's, followed by input values of mtop and mbot.
cc example: 0   0  0.99503719020998915  0   0   173.1   4.2 

ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
cc fort.98 contains 3 0's followed by the squares of the uL, dL, uR, and dR
cc masses.  These should be physical (not soft) masses
cc  example:  0 0 0 685500.97109808691        691777.20326883392       
cc             641764.24896795058        638049.32167516614

ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
cc fort.99 should contain the squares of the masses of  bottom squarks 
cc (lightest first) and top squarks (lightest first) followed by
cc  the stop mixing angle and then the sbottom mixing anle
cc  example:
cc           587346.51113831170        638907.41174951592        
cc           395630.47406983603        674689.69984674465        
cc            1.0709444223091809       0.29069297900170998 

cccccccccccccccccccccccccccccccccccccccccccccccc


      OPEN(UNIT = 33,FILE='matn.dat',status='old')
      OPEN(UNIT = 43,FILE='higgs.dat',STATUS='old')
      OPEN(UNIT=44,file='cres.in',status='old')
 
      READ(33,*) evals(1),evals(2),evals(3),evals(4)
      READ(33,*) evecs(1,1),evecs(1,2),evecs(1,3),evecs(1,4)
      READ(33,*) evecs(2,1),evecs(2,2),evecs(2,3),evecs(2,4)
      READ(33,*) evecs(3,1),evecs(3,2),evecs(3,3),evecs(3,4)
      READ(33,*) evecs(4,1),evecs(4,2),evecs(4,3),evecs(4,4)
      READ(44,*)x,x,sinb,x,x,mtop,mbot
      READ(43,*) mh2, mh1, alpha
      READ(98,*) x,x,x,msul, msdl, msur, msdr 
      Read(99,*) msbr, msbl, mstr, mstl, thmixt, thmixb


ccccccccccccccccccccccccccccccccccccccccccccccccccccc
cc programs reads in sigma_piN  and its error.
cc  This could be hard wired in as sig = 64 and sigsig = 8

ccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      write(6,*)'sigmapiN and its error:'
      read(5,*)sig,sigsig
c      OPEN(UNIT=91,file='sinputs.dat',status='old')
c      READ(91,*)sig,sigsig


 

      mnucl = 0.93827
      spin = 0.5
      sp = 0.5
      sn = 0
      numneu = 0
      numpro = 1
      

c
      beta = dasin(sinb)


c the sfermion diagonalizing matrix

         if(msul.le.msur) then
          etau(1,1) = 1
          etau(1,2) = 0
          etau(2,1) = 0
          etau(2,2) = 1 
        else
          etau(1,1) = 0
          etau(1,2) = -1
          etau(2,1) = 1
          etau(2,2) = 0
        endif
c        etac = etau

        if(msdl.le.msdr) then
          etad(1,1) = 1
          etad(1,2) = 0
          etad(2,1) = 0
          etad(2,2) = 1
        else
          etad(1,1) = 0
          etad(1,2) = -1
          etad(2,1) = 1
          etad(2,2) = 0
        end if
c        etas = etad

         DO 210 i = 1,2
            DO 220 j = 1,2
             etac(j,i)=etau(j,i)
             etas(j,i)=etad(j,i)
 220        CONTINUE
 210     CONTINUE
     


        msul1=msul
        msur1=msur
        msdl1=msdl
        msdr1=msdr

        msur=dmin1(msur1,msul1)
        msul=dmax1(msur1,msul1)
        msdr=dmin1(msdr1,msdl1)
        msdl=dmax1(msdr1,msdl1)

         mssr = msdr
         mssl = msdl
         mscr = msur
         mscl = msul


         etab(1,1) = cos(thmixb)
         etab(2,2) = cos(thmixb)
         etab(1,2) = - sin(thmixb)
         etab(2,1) = sin(thmixb)
         etat(1,1) = cos(thmixt)
         etat(2,2) = cos(thmixt)
         etat(1,2) = - sin(thmixt)
         etat(2,1) = sin(thmixt)


c     the eta's used in the program are not directly the same eta's in my
c     formula;  the correspondence is that conjg(eta11) becomes eta11
c     conjg(eta22) becomes eta22, conjg(eta21) becomes eta12, and
c     conjg(eta12) becomes eta21.         




c
c     create neutralino mass matrix in order to find the
c     extra phase and make the diagonalized matrix real
c
         
c
c    find the LSP
c
        DO 22 i =1,4
           IF (i.EQ.1) THEN
              mlsp = DABS(evals(i))
              lspi = i
           ELSE
              IF (mlsp.GT.DABS(evals(i))) THEN
                 mlsp = DABS(evals(i))
                 lspi = i
              ENDIF
           ENDIF
 22     CONTINUE

        DO 30 i = 1,4
           z(i) = DCMPLX(evecs(i,lspi), 0d0)
 30     CONTINUE

c
c   make correction if the mass of the LSP is negative
c
        mcom = evals(lspi)

c  Put all of the phase from mcom into the coefficients
c
         IF (REAL(mcom).GT.0.0) THEN
            eta =  DATAN(DIMAG(mcom)/REAL(mcom))
         ELSE
            eta =  pi + DATAN(DIMAG(mcom)/REAL(mcom))
         ENDIF
c         PRINT*, 'The value of eta: ', eta
c         PRINT*, 'The value of mcom: ', mcom
         DO 130 I = 1,4
            z(I) = z(I)*DCMPLX(DCOS(-eta/2.0d0),  DSIN(-eta/2.0d0))
 130     CONTINUE




c
c  Calculate the values of the scalar and spin-dependent
c  terms.  Note that there is a slight difference between my notes
c and what the program calculates.  
c the way that the neutralino matrix is diagnolized for the purpose 
c of the program is transpose(z) M z.  However, I used Gunion and Haber's
c notation when calculating the cross section.  They diagnolize as 
c  Conjg(z) M z^{-1}.  So the z's in this program are the conjugate of
c  what we need in the formula.
c
c
c
        mup = 0.004
        mdown = 0.007
        mstrn = 0.15
        mchrm = 1.5
        mdown = 0.005
        mup = 0.553*mdown
        mstrn = 18.9*mdown
        mchrm = 1.25
        aup = g2*DCONJG(z(4))/(2*Mw*DSIN(beta))
        cup = yu*g1*DCONJG(z(1))/2 + g2*t3u*DCONJG(z(2))
        dup = eu*g1*DCONJG(z(1))
        adown = g2*DCONJG(z(3))/(2*Mw*DCOS(beta))
        cdown = yd*g1*DCONJG(z(1))/2 + g2*t3d*DCONJG(z(2))
        ddown = ed*g1*DCONJG(z(1))
c
c   these next z's do not need to be conjugated since we take real part
c
        z321 = REAL(z(3)*(g2*z(2) - g1*z(1)))
        z421 = REAL(z(4)*(g2*z(2) - g1*z(1)))
c   
c     the eta's used here are not directly the same eta's in my
c     formula the correspondence is that conjg(eta11) becomes eta11
c     conjg(eta22) becomes eta22, conjg(eta21) becomes eta12, and
c     conjg(eta12) becomes eta21.
c
c        PRINT*, 'calculating alpha2'
c
        alph2u = 
     &   ( (CDABS(etau(1,1)*cup + etau(2,1)*aup*mup))**2 +
     &   (CDABS(etau(1,1)*DCONJG(aup)*mup - etau(2,1)*DCONJG(dup)))**2)/
     &   (4*(msur - mlsp**2))  +
     &   ( (CDABS(etau(2,2)*aup*mup + etau(1,2)*cup))**2 +
     &   (CDABS(etau(1,2)*DCONJG(aup)*mup - etau(2,2)*DCONJG(dup)))**2)/
     &   (4*(msul - mlsp**2))  -
     &   g2**2*( (CDABS(z(3)))**2 - (CDABS(z(4)))**2)*t3u/(8*Mw**2)
c
c  this is for diagnostics
        andy1 = 
     &   ( (CDABS(etau(1,1)*cup + etau(2,1)*aup*mup))**2 +
     &   (CDABS(etau(1,1)*DCONJG(aup)*mup - etau(2,1)*DCONJG(dup)))**2)/
     &   (4*(msur - mlsp**2))  +
     &   ( (CDABS(etau(2,2)*aup*mup + etau(1,2)*cup))**2 +
     &   (CDABS(etau(1,2)*DCONJG(aup)*mup - etau(2,2)*DCONJG(dup)))**2)/
     &   (4*(msul - mlsp**2))  
        andy2 =
     &    -  g2**2*( (CDABS(z(3)))**2 - (CDABS(z(4)))**2)*t3u/(8*Mw**2)

c  end diagnostics
c
        alph2d = 
     &   ( (CDABS(etad(1,1)*cdown + etad(2,1)*adown*mdown))**2 +
     &   (CDABS(etad(1,1)*DCONJG(adown)*mdown - etad(2,1)*DCONJG(ddown))
     &   )**2)/(4*(msdr - mlsp**2))  +
     &   ( (CDABS(etad(2,2)*adown*mdown + etad(1,2)*cdown))**2 +
     &   (CDABS(etad(1,2)*DCONJG(adown)*mdown - etad(2,2)*DCONJG(ddown))
     &   )**2)/(4*(msdl - mlsp**2))  -
     &   g2**2*( (CDABS(z(3)))**2 - (CDABS(z(4)))**2)*t3d/(8*Mw**2)
        alph2s = 
     &   ( (CDABS(etas(1,1)*cdown + etas(2,1)*adown*mstrn))**2 +
     &   (CDABS(etas(1,1)*DCONJG(adown)*mstrn - etas(2,1)*DCONJG(ddown))
     &   )**2)/(4*(mssr - mlsp**2))  +
     &   ( (CDABS(etas(2,2)*adown*mstrn + etas(1,2)*cdown))**2 +
     &   (CDABS(etas(1,2)*DCONJG(adown)*mstrn - etas(2,2)*DCONJG(ddown))
     &   )**2)/(4*(mssl - mlsp**2))  -
     &   g2**2*( (CDABS(z(3)))**2 - (CDABS(z(4)))**2)*t3d/(8*Mw**2)
c       
c  Spin independent
c        PRINT*,'calculating alpha3'
c
        alph3u = - REAL( (etau(1,1)*DCONJG(aup)*mup - etau(2,1)
     &    *DCONJG(dup))*DCONJG(etau(1,1)*cup + etau(2,1)*mup*aup))/
     &    (2*(msur - mlsp**2)) 
     &    - REAL( (etau(1,2)*mup*DCONJG(aup) -
     &    etau(2,2)*DCONJG(dup) )*DCONJG(etau(1,2)*cup + etau(2,2)*
     &    aup*mup))/(2*(msul - mlsp**2))  
     &    - g2*mup/(4*Mw*DSIN(beta))*(z321*DCOS(alpha)*DSIN(alpha)*
     &    (1/mh2**2 - 1/mh1**2) + z421*( (DCOS(alpha))**2/mh2**2 +
     &    (DSIN(alpha))**2/mh1**2 ))
        alph3c = - REAL( (etac(1,1)*DCONJG(aup)*mchrm - etac(2,1)
     &    *DCONJG(dup))*DCONJG(etac(1,1)*cup + etac(2,1)*mchrm
     &    *aup))/(2*(mscr - mlsp**2)) 
     &    - REAL( (etac(1,2)*mchrm*DCONJG(aup) -
     &    etac(2,2)*DCONJG(dup) )*DCONJG(etac(1,2)*cup + etac(2,2)*
     &    aup*mchrm))/(2*(mscl - mlsp**2))  
     &    - g2*mchrm/(4*Mw*DSIN(beta))*(z321*DCOS(alpha)*DSIN(alpha)*
     &    (1/mh2**2 - 1/mh1**2) + z421*( (DCOS(alpha))**2/mh2**2 +
     &    (DSIN(alpha))**2/mh1**2 ))
        alph3t = - REAL( (etat(1,1)*DCONJG(aup)*mtop - etat(2,1)
     &    *DCONJG(dup))*DCONJG(etat(1,1)*cup + etat(2,1)*mtop
     &    *aup))/(2*(mstr - mlsp**2)) 
     &    - REAL( (etat(1,2)*mtop*DCONJG(aup) -
     &    etat(2,2)*DCONJG(dup) )*DCONJG(etat(1,2)*cup + etat(2,2)*
     &    aup*mtop))/(2*(mstl - mlsp**2))  
     &    - g2*mtop/(4*Mw*DSIN(beta))*(z321*DCOS(alpha)*DSIN(alpha)*
     &    (1/mh2**2 - 1/mh1**2) + z421*( (DCOS(alpha))**2/mh2**2 +
     &    (DSIN(alpha))**2/mh1**2 ))
        alph3d = - REAL( (etad(1,1)*DCONJG(adown)*mdown - etad(2,1)
     &    *DCONJG(ddown))*DCONJG(etad(1,1)*cdown + etad(2,1)*mdown*
     &    adown))/(2*(msdr - mlsp**2)) 
     &    - REAL( (etad(1,2)*mdown*DCONJG(adown) -
     &    etad(2,2)*DCONJG(ddown) )*DCONJG(etad(1,2)*cdown + 
     &    etad(2,2)*adown*mdown))/(2*(msdl - mlsp**2))  
     &    - g2*mdown/(4*Mw*DCOS(beta))*(z421*DCOS(alpha)*DSIN(alpha)*
     &    (1/mh1**2 - 1/mh2**2) - z321*( (DCOS(alpha))**2/mh1**2 +
     &    (DSIN(alpha))**2/mh2**2 ))
        alph3s = - REAL( (etas(1,1)*DCONJG(adown)*mstrn - etas(2,1)
     &    *DCONJG(ddown))*DCONJG(etas(1,1)*cdown + etas(2,1)*mstrn*
     &    adown))/(2*(mssr - mlsp**2)) 
     &    - REAL( (etas(1,2)*mstrn*DCONJG(adown) -
     &    etas(2,2)*DCONJG(ddown) )*DCONJG(etas(1,2)*cdown + 
     &    etas(2,2)*adown*mstrn))/(2*(mssl - mlsp**2))  
     &    - g2*mstrn/(4*Mw*DCOS(beta))*(z421*DCOS(alpha)*DSIN(alpha)*
     &    (1/mh1**2 - 1/mh2**2) - z321*( (DCOS(alpha))**2/mh1**2 +
     &    (DSIN(alpha))**2/mh2**2 ))
        alph3b = - REAL( (etab(1,1)*DCONJG(adown)*mbot - etab(2,1)
     &    *DCONJG(ddown))*DCONJG(etab(1,1)*cdown + etab(2,1)*mbot*
     &    adown))/(2*(msbr - mlsp**2)) 
     &    - REAL( (etab(1,2)*mbot*DCONJG(adown) -
     &    etab(2,2)*DCONJG(ddown) )*DCONJG(etab(1,2)*cdown + 
     &    etab(2,2)*adown*mbot))/(2*(msbl - mlsp**2))  
     &    - g2*mbot/(4*Mw*DCOS(beta))*(z421*DCOS(alpha)*DSIN(alpha)*
     &    (1/mh1**2 - 1/mh2**2) - z321*( (DCOS(alpha))**2/mh1**2 +
     &    (DSIN(alpha))**2/mh2**2 ))
c
c
c     compute scalar and spin dependent cross sections
c
        deltsp = -0.09 
        sigdeltsp = 0.03
        a3=1.2695
        siga3=0.0029
        a8=0.585
        siga8=0.025
        deltup = 0.5d0*(a3 + a8) + deltsp    ! 0.83725
        deltdp = 0.5d0*(a8 - a3) + deltsp    ! -0.43225
        deltsn = deltsp
        deltdn = deltup
        deltun = deltdp
        ap = (alph2u*deltup + alph2d*deltdp + alph2s*deltsp)/
     &              (gf*SQRT(2.0))
        an = (alph2u*deltun + alph2d*deltdn + alph2s*deltsn)/
     &              (gf*SQRT(2.0))
        mr = mnucl*mlsp/(mnucl + mlsp)
        lambda = (ap*sp + an*sn)/spin
        sigma2 = 32.0*gf**2*mr**2*lambda**2*spin*(spin + 1)/pi

c        print*,'checkSD:alpha2u,d,s,ap',alph2u,alph2d,alph2s,ap

c
c these values are corrected versions from the wrong review
c article
c
c

       sig0=36.0
       sigsig0=7.0
       y = 1.0 - sig0/sig
       if (y.lt.0.0) y=0.0
       zf = 1.49
       mumd=0.553
       sigmumd=0.043
       msmd=18.9
       sigmsmd=0.8
       r=2.0*msmd/(1.0+mumd)
       bdbu=(2.0+(zf-1.0)*y)/(2.0*zf-(zf-1.0)*y)
       mubu=2.0*sig/(1.0+1.0/mumd)/(1.0+bdbu)
       mdbd=2.0*sig/(1.0+mumd)/(1.0+1.0/bdbu)
       msbs=r*y*sig/2.0       
       ftup = mubu/938.27
       ftdp = mdbd/938.27
       ftsp = msbs/938.27
       
        ftsn = msbs/939.4
        ftun = mumd*mdbd/939.4
        ftdn = mubu/939.4/mumd

        ftgn = 1. - (ftun + ftdn + ftsn)
        ftgp = 1. - (ftup + ftdp + ftsp)
        fp = mprot*(ftup*alph3u/mup + ftdp*alph3d/mdown +
     &          ftsp*alph3s/mstrn + 2.*ftgp*(alph3c/mchrm +
     &          alph3b/mbot + alph3t/mtop)/27.)
        fn = mneut*(ftun*alph3u/mup + ftdn*alph3d/mdown +
     &          ftsn*alph3s/mstrn + 2.*ftgn*(alph3c/mchrm +
     &          alph3b/mbot + alph3t/mtop)/27.)
        sigma3 = 4.*mr**2.*(numpro*fp + (numneu)*fn)**2./pi
c
c
c what is the LSP?  guagino,...
c      
        compo = CDABS(z(1))**2 + CDABS(z(2))**2
        IF (compo.LT.0.1) THEN
           lspcomp = 34
        ELSEIF (compo.GT.0.9) THEN
           lspcomp = 12
        ELSE
           lspcomp = 1234
        ENDIF

c      sigmacdms=1.3e-7*10**(1.814e-3*mlsp)
c      ratio=sigma3*.38937932e9/sigmacdms



c
c     compute uncertainties in scalar and spin dependent cross sections
c
        sigdeltup=(siga3**2/4.+siga8**2/4.+sigdeltsp**2)**(1./2.)
        sigdeltdp=sigdeltup
        sigdeltsn = sigdeltsp
        sigdeltdn = sigdeltup
        sigdeltun = sigdeltdp
        sigap = (alph2u**2*sigdeltup**2 + alph2d**2*sigdeltdp**2 
     &         + alph2s**2*sigdeltsp**2)**(1./2.)/(gf*SQRT(2.0))
        sigan = (alph2u**2*sigdeltun**2 + alph2d**2*sigdeltdn**2  
     &         + alph2s**2*sigdeltsn**2)**(1./2.)/(gf*SQRT(2.0))
        mr = mnucl*mlsp/(mnucl + mlsp)
        siglambda = (sigap**2*sp**2 + sigan**2*sn**2)**(1./2.)/spin
        sigsigma2 = 2.*sigma2*siglambda/dabs(lambda)
c
c
c
         sigy = (1. - y)*((sigsig/sig)**2. + 
     $       (sigsig0/sig0)**2.)**(1./2.)
         sigbr2=(zf-1.0)**2*sigy**2*(1.+bdbu**2)/
     $      (2.0*zf-(zf-1.0)*y)**2
         sigftup = ftup*((sigsig/sig)**2 + 
     $           (sigmumd/mumd/(1.+mumd))**2 + 
     $                 sigbr2/(1.+bdbu)**2)**(1./2.)
         sigftdp = ftdp*((sigsig/sig)**2 + 
     $          (sigmumd/(1.+mumd))**2. + 
     $                sigbr2/(bdbu*(1+bdbu))**2)**(1./2.)
         if (y.eq.0.0) then
         sigftsp = 0
         else
         sigftsp = ftsp*((sigsig/sig)**2 +  
     $                 (sigy/y)**2 + (sigmsmd/msmd)**2 +
     $           (sigmumd/(1.+mumd))**2)**(1./2.)
         endif
c         if(ftsp.le.0.0) ftsp = 0.0


         sigftdn = ftdn*((sigsig/sig)**2 + 
     $     (sigmumd/(1.+mumd))**2 +
     $                 sigbr2/(1+bdbu)**2)**(1./2.)
         sigftun = ftun*((sigsig/sig)**2 + 
     $        (sigmumd/mumd/(1.+mumd))**2. +
     $                 sigbr2/(bdbu*(1+bdbu))**2)**(1./2.)
         if (y.eq.0.0) then
         sigftsn = 0
         else
         sigftsn = ftsn*((sigsig/sig)**2 +           
     $                 (sigy/y)**2 + (sigmsmd/msmd)**2 +
     $           (sigmumd/(1.+mumd))**2)**(1./2.)
         endif
c         if(ftsn.le.0.0) ftsn = 0.0

        sigftgn = (sigftun**2 + sigftdn**2 + sigftsn**2)**(1./2.)
        sigftgp = (sigftup**2 + sigftdp**2 + sigftsp**2)**(1./2.)
        sigfp = mprot*(sigftup**2*(alph3u/mup)**2 + 
     &           sigftdp**2*(alph3d/mdown)**2 +
     &          sigftsp**2*(alph3s/mstrn)**2 + 
     &          4.*sigftgp**2*(alph3c/mchrm +
     &          alph3b/mbot + alph3t/mtop)**2/729.)**(1./2.)
        sigfn = mneut*(sigftun**2*(alph3u/mup)**2 + 
     &           sigftdn**2*(alph3d/mdown)**2 +
     &          sigftsn**2*(alph3s/mstrn)**2 + 
     &          4.*sigftgn**2*(alph3c/mchrm +
     &          alph3b/mbot + alph3t/mtop)**2/729.)**(1./2.)

        sigsigma3 = 2.*sigma3*((numpro*sigfp)**2 + 
     $      (numneu*fn)**2)**(1./2.)/dabs(numpro*fp + (numneu)*fn)
c



ccccccccccccccccccc
cc  writes out spin dependent cross section (in pb) and its error
cc   followed by spin independent cross section (in pb) and its error
cc   example
cc     1.10684785613924660E-006  1.34684172167397274E-007  
cc      2.66824078085800265E-009  1.27597278306118913E-009

ccccccccccccccccccccccccccccccc

        WRITE(10,*) sigma2*0.38937932E9, sigsigma2*0.38937932E9, 
     $        sigma3*0.38937932E9, sigsigma3*0.38937932E9    
c        Print*,'sig,y,r,bdbu,ftp,ftd,fts',sig,y,r,
c     $          bdbu,ftup,ftdp,ftsp
        Print*,'spin dependent cross section (in pb) =',
     &     sigma2*0.38937932E9, '+/-', sigsigma2*0.38937932E9
        Print*,'scalar cross section (in pb) =',
     &     sigma3*0.38937932E9, '+/-', sigsigma3*0.38937932E9


c        WRITE(81,*) sigma2, sigma3, sigsigma3, y, mlsp
c





c 200  CONTINUE  
c 201  CONTINUE

      END
