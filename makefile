CC = gcc
CFLAGS=	-g -Wall -std=c99

kk: 
	$(CC) $(CFLAGS) -o kk kk.c -lm

clean:
	rm kk