import cv2
from multi_screen import MultiScreen

multiscreen = MultiScreen([0, 2], [(160, 120), (160, 120)])
multiscreen.start_all()

while True:
    frames = multiscreen.get_frames()
    multiscreen.set_frames(frames)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

multiscreen.stop()
