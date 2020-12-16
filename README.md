# AR-window-hardware
The main purpose of this codebase is to provide a clean and easy-to-use interface for developers to hack on the Augmented Reality Window. To that end, we hide all the guts of interfacing with hardware components on a Raspberry Pi, and only expose two modules in Python: `multi_screen` and `gesture_interface`.

## Usage
For an example on how to use the `multi_screen` and `gesture_interface` modules, please see `dual_screen_demo.py`.

## Compilation
Before using the gesture module, be sure to first compile the code for interfacing with Python. To do this, simply run the following.
```
make clean && make
```
