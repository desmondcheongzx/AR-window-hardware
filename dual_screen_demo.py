import cv2
from multi_screen import MultiScreen

multiscreen = MultiScreen([(1280, 720), (1280, 720)])
multiscreen.start_all()

while True:
    frames = multiscreen.get_frames()
    multiscreen.set_frames(frames)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

multiscreen.stop()
