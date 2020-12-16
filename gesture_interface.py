from subprocess import check_output
import threading


class Direction:
    def __init__(self, input_val):
        self.input_str = input_val.decode('utf-8')

    def get_direction(self):
        return self.input_str


class GestureCaptureAsync:
    def __init__(self):
        self.started = False
        self.read_lock = threading.Lock()
        self.thread = None
        self.inputs = []

    def get_inputs(self):
        with self.read_lock:
            return_list = self.inputs
            self.inputs = []
        return return_list

    def start(self):
        if self.started:
            print('Gesture capture already started.')
            return None
        self.started = True
        self.thread = threading.Thread(target=self.load, args=())
        self.thread.start()
        return self

    def load(self):
        while self.started:
            new_input = check_output('./mgc3130', shell=True)
            with self.read_lock:
                self.inputs.append(Direction(new_input))

    def stop(self):
        self.started = False
        self.thread.join()
