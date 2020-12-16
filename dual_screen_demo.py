import cv2
from multi_screen import MultiScreen
from gesture_interface import Direction, GestureCaptureAsync

# Declare the input sources for webcameras, 
# and the windows' output dimensions
multiscreen = MultiScreen([0, 2], [(1920, 1080), (1920, 1080)])
gesture_capture = GestureCaptureAsync()
multiscreen.start_all()
gesture_capture.start()

while True:
    # Capture a still image from each webcam and display them
    frames = multiscreen.get_frames()
    multiscreen.set_frames(frames)
    
    # Display all gesture input
    gestures = gesture_capture.get_inputs()
    for gesture in gestures:
        print(gesture.get_direction())

    # Exit the program
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

multiscreen.stop()
gesture_capture.stop()
