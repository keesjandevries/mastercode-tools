behemoth	= behemoth.x
minchi		= minchi.x
cutpoints	= cutpoints.x
extract		= extract_graphs.x
split		= split_file.x
dmtool		= dmtool.x

executables = $(behemoth) $(minchi) $(cutpoints) $(extract) $(split) $(dmtool)

srcdir		= src/
objdir		= obj/
exedir 		= exe/

# for processAll
lhobjects	= Contour.o ContourLikelihood.o LikelihoodFunctions.o \
				Coords.o Likelihood1D.o LikelihoodFunctions1D.o

dmobjects = dmtool/lspscat8o.o

ROOTCFLAGS = $(shell root-config --cflags)
ROOTFLAGS = $(shell root-config --cflags --ldflags --libs)
ROOTXFLAGS = $(shell root-config --cflags --libs)

processAll : $(objects)  processAll.C 
			 g++ -o processAll.x \
				 $(objects) \
			     processAll.C $(ROOTFLAGS)

Contour.o : Contour.cpp Contour.h
	g++ -c Contour.cpp

ContourLikelihood.o : ContourLikelihood.cpp ContourLikelihood.h
	g++ -c ContourLikelihood.cpp

LikelihoodFunctions.o : LikelihoodFunctions.cpp LikelihoodFunctions.h
	g++ -c LikelihoodFunctions.cpp

Coords.o : Coords.cpp Coords.h
	g++ -c Coords.cpp

Likelihood1D.o : Likelihood1D.cpp Likelihood1D.h
	g++ -c Likelihood1D.cpp

dmtool/lspscat8o.o :
	gfortran -o dmtool/lspscat8o.o -c dmtool/lspscat8o.f

LikelihoodFunctions1D.o : LikelihoodFunctions1D.cpp LikelihoodFunctions1D.h
	g++ -c LikelihoodFunctions1D.cpp $(ROOTCFLAGS)

minchi : file_tools/minchi.C
	g++ -o minchi.x file_tools/minchi.C $(ROOTXFLAGS)

removeBad : file_tools/removeBad.C
	g++ -o removeBad.x file_tools/removeBad.C $(ROOTXFLAGS)

saveGraphs : file_tools/saveGraphs.C
	g++ -o saveGraphs.x file_tools/saveGraphs.C $(ROOTXFLAGS)

splitFile : file_tools/splitFile.C
	g++ -o splitFile.x file_tools/splitFile.C $(ROOTXFLAGS)

dmtool : dmtool/lspscat8o.o dmtool/dmtool.cpp
	g++ -o dmtool.x dmtool/dmtool.cpp $(dmobjects) -lgfortran $(ROOTXFLAGS)

.PHONY: all clean processAll splitFile saveGraphs removeBad minchi dmtool
clean :
	-rm -f processAll.x minchi.x removeBad.x saveGraphs.x splitFile.x dmtool.x \
	$(objects) $(dmobjects)
