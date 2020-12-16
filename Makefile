CC = gcc
CFLAG = 
SRC = main.c
SRC += gesture_src/platform_basic_func.c gesture_src/platform_basic_func.h  gesture_src/Seeed_3D_touch_mgc3030.c gesture_src/Seeed_3D_touch_mgc3030.h
LIB = -lwiringPi -lcurses

EXEC_NAME = mgc3130

all: 
	$(CC) $(CFLAG) $(SRC) $(LIB) -o $(EXEC_NAME)
clean:
	rm -f $(EXEC_NAME)
