import cv2
from multi_screen import MultiScreen

# Declare the input sources for webcameras, and the windows' output dimensions
multiscreen = MultiScreen([0, 2], [(160, 120), (160, 120)])
multiscreen.start_all()

while True:
    # Capture a still image from each webcam
    # The return value will be a list of numpy matrices containing image info
    frames = multiscreen.get_frames()
    multiscreen.set_frames(frames)

    # Exit the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

multiscreen.stop()
