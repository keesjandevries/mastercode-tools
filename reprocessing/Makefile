ROOTCFLAGS = $(shell root-config --cflags)
#ROOTFLAGS = $(shell root-config --cflags --ldflags --libs)
#ROOTXFLAGS = $(shell root-config --cflags --libs)

CPP          =	g++ 
CPPFLAGS     =	-c -fPIC 
LINKER       =	g++ 
LINKERFLAGS  =	-shared -Wl,-soname,$@ -o
RM           =	rm -f 
MAKE         =	make 
OBJDIR		 =	lhoods/obj
SRCDIR	     =	lhoods/src
OBJS         =	$(OBJDIR)/Contour.o \
				$(OBJDIR)/ContourLikelihood.o \
				$(OBJDIR)/LikelihoodFunctions.o \
				$(OBJDIR)/Coords.o \
				$(OBJDIR)/Likelihood1D.o \
			    $(OBJDIR)/LikelihoodFunctions1D.o
TARGET       =	libLH.so

.IGNORE: 
.SILENT: 
.SUFFIXES: .o .cpp

$(TARGET): $(OBJS) 
		$(LINKER) $(LINKERFLAGS) libs/$@ $(OBJS) 

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
