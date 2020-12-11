import cv2
from video_capture import VideoCaptureAsync
#from multi_capture import VideoCaptureAsync


class MultiScreen():
    def __init__(self, sources, screen_dimensions):
        self.n_cameras = len(screen_dimensions)
        self.screen_dimensions = screen_dimensions
        self.video_captures = [
            VideoCaptureAsync(src=idx,
                              width=screen_width,
                              height=screen_height)
            for idx, (screen_width, screen_height)
            in zip(sources, screen_dimensions)]
        self.window_ids = [f'screen{i}'
                           for i in range(self.n_cameras)]

        x_displacement = 0
        for i, window_id in enumerate(self.window_ids):
            cv2.namedWindow(window_id, cv2.WND_PROP_FULLSCREEN)
            cv2.moveWindow(window_id, x_displacement, 0)
            cv2.setWindowProperty(window_id, cv2.WND_PROP_FULLSCREEN, 0)
            x_displacement += self.screen_dimensions[i][0]

    def start_all(self):
        for capture in self.video_captures:
            capture.start()

    def get_frames(self, all_sources=True, src=None):
        if not all_sources:
            return [self.video_captures[i].read()[1]
                    for i in src]
        return [capture.read()[1] for capture in self.video_captures]

    def set_frames(self, data, all_sources=True, src=None):
        # Remember to check that there's enough data sources!
        if not all_sources:
            for frame, idx in zip(data, src):
                cv2.imshow(self.window_ids[idx], frame)
            return
        for frame, window_id in zip(data, self.window_ids):
            cv2.imshow(window_id, frame)

    def stop(self):
        for capture in self.video_captures:
            capture.stop()
        cv2.destroyAllWindows()
