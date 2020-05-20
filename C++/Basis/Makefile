#######################################################################
#  Myprogram                                                          #
#######################################################################


OPTIMIZE = -O2

OPTIONS = $(OPTIMIZE) $(OPT)

EXEC = myprogram

OBJS  = example.o

INCL   = const.h example.h Makefile

CPPFLAGS = $(OPTIONS) 

CC = g++

.cc.o:
	$(CC) -c $(CPPFLAGS) -o "$@" "$<"

$(EXEC): $(OBJS)
	$(CC) $(OPTIONS) $(OBJS) -o $(EXEC)

$(OBJS): $(INCL)

clean:
	rm -f $(OBJS)

