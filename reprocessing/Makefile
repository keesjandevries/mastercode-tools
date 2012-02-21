ROOTCFLAGS = $(shell root-config --cflags)
#ROOTFLAGS = $(shell root-config --cflags --ldflags --libs)
#ROOTXFLAGS = $(shell root-config --cflags --libs)

CPP         =	g++ 
CPPFLAGS    =	-c -fPIC 
LINKER      =	g++ 
LINKERFLAGS =	-shared -Wl,-soname,$@ -o
RM          =	rm -f 
MAKE        =	make 
LHDIR		=	lhoods
OBJDIR		=	$(LHDIR)/obj
SRCDIR	    =	$(LHDIR)/src
OBJS        =	$(OBJDIR)/Contour.o \
				$(OBJDIR)/ContourLikelihood.o \
				$(OBJDIR)/LikelihoodFunctions.o \
				$(OBJDIR)/Coords.o \
				$(OBJDIR)/Likelihood1D.o \
				$(OBJDIR)/LikelihoodFunctions1D.o
APIFILE		=	$(LHDIR)/lhood.cc
APIOBJ		=   $(LHDIR)/lhood.o
TARGET      =	libLH.so

.IGNORE: 
.SILENT: 
.SUFFIXES: .o .cpp


$(TARGET): $(APIOBJ) $(OBJS)
		$(LINKER) $(LINKERFLAGS) libs/$@ $(APIOBJ) $(OBJS) 

$(APIOBJ): $(OBJS)
		$(CPP) $(CPPFLAGS) -o $@ $(APIFILE)

$(OBJDIR)/%.o: $(SRCDIR)/%.cpp 
		$(CPP) $(CPPFLAGS) -o $@ $? $(ROOTCFLAGS)

clean: 
		$(RM) *.o 

distclean: 
		$(MAKE) clean 
		$(RM) $(TARGET) 

again: 
		$(MAKE) distclean 
		$(MAKE) $(TARGET)
