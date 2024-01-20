CC = gcc
CFLAGS = -O2 -fPIC
INCLUDES = -I/usr/include/python3.10 -I../lib -I../../../../../.local/lib/python3.10/site-packages/numpy/core/include
LIBS = -lz
TARGET_D = MPImfp.so
TARGET_S = libMPImfp.a
OBJS = imfp.o rand.o python.o

all:	$(TARGET_D) $(TARGET_S)

$(TARGET_D):	$(OBJS)
		$(CC) -shared -o $@ $(OBJS) $(LIBS)

$(TARGET_S):	$(OBJS)
		ar r $@ $(OBJS)

clean:
		rm $(TARGET_D) $(TARGET_S) $(OBJS)

.c.o:
		$(CC) $(CFLAGS) $(INCLUDES) -c $<

imfp.c:		MPImfp.h
rand.c:		MPImfp.h
python.c:	MPImfp.h

