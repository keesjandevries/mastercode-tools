ROOTCFLAGS = $(shell root-config --cflags)
ROOTFLAGS = $(shell root-config --cflags --ldflags --libs)
ROOTXFLAGS = $(shell root-config --cflags --libs)

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
				$(OBJDIR)/RadialLikelihood.o \
				$(OBJDIR)/RadialLikelihoodFunctions.o \
				$(OBJDIR)/Coords.o \
				$(OBJDIR)/CartesianLikelihood.o \
				$(OBJDIR)/CartesianLikelihoodFunctions.o
APIFILE		=	$(LHDIR)/lhood.cc
APIOBJ		=   $(LHDIR)/lhood.o
TARGET      =	libLH.so

OUT_DIR		=	$(OBJDIR) $(SRCDIR) libs

.IGNORE: 

.SUFFIXES: .o .cpp

.PHONY: directories

all: directories $(TARGET)

directories: ${OUT_DIR}

${OUT_DIR}:
		${MKDIR_P} ${OUT_DIR}

$(TARGET): $(APIOBJ) $(OBJS)
		$(LINKER) $(LINKERFLAGS) libs/$@ $(APIOBJ) $(OBJS) $(ROOTFLAGS)

$(APIOBJ): $(OBJS)
		$(CPP) $(CPPFLAGS) -o $@ $(APIFILE) $(ROOTFLAGS)

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

MKDIR_P = mkdir -p
