# AR-window-hardware
The main purpose of this codebase is to provide a clean and easy-to-use interface for developers to hack on the Augmented Reality Window. To that end, we hide all the guts of interfacing with hardware components on a Raspberry Pi, and only expose two modules in Python: `multi_screen` and `gesture_interface`.

## Usage
For an example on how to use the `multi_screen` and `gesture_interface` modules, please see `dual_screen_demo.py`.

The `MultiScreen` class takes in video sources and output resolutions, and provides the methods to `start_all()` and `stop()` video capture. You can get all webcam information as a array via `get_frames()`, as well as send modified image information to the screens via `set_frames(frames)`.

`GestureCaptureAsync` works in a similar way and asynchronously queues all gesture input until the program is ready to handle them. You can `start()` and `stop()` the gesture capture thread, and at any point you can call `get_inputs()` to get the list of gesture inputs that were detected since the last call of the method. Gesture inputs are saved as a `Direction` object, and calling each object's `get_direction()` method returns one of four strings: `'up', 'down', 'left', 'right'`.
## Compilation
Before using the gesture module, be sure to first compile the code for interfacing with Python. To do this, simply run the following:
```
make clean && make
```
## Notes and Credits
Code for the gesture capture interface was adapted from [Seeed Studio](https://github.com/Seeed-Studio/Seeed_Linux_mgc3x30) under [The MIT License](https://opensource.org/licenses/mit-license.php).
