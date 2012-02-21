lhood	= libLHood.so

srcdir		= lhoods/src/
objdir		= obj/
incdir		= includes/

# for processAll
lhobjects	= Contour.o ContourLikelihood.o LikelihoodFunctions.o \
				Coords.o Likelihood1D.o LikelihoodFunctions1D.o

ROOTCFLAGS = $(shell root-config --cflags)
ROOTFLAGS = $(shell root-config --cflags --ldflags --libs)
ROOTXFLAGS = $(shell root-config --cflags --libs)

$(objdir)/Contour.o :
	g++ -c Contour.cpp

$(objdir)/ContourLikelihood.o :
	g++ -c ContourLikelihood.cpp

$(objdir)/LikelihoodFunctions.o :
	g++ -c LikelihoodFunctions.cpp

$(objdir)/Coords.o :
	g++ -c Coords.cpp

$(objdir)/Likelihood1D.o :
	g++ -c Likelihood1D.cpp

$(objdir)/LikelihoodFunctions1D.o :
	g++ -c LikelihoodFunctions1D.cpp $(ROOTCFLAGS)
