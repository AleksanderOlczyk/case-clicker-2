import random
import threading
import time
import math
from constants import constants
from pynput.mouse import Controller


class SmoothCursor:
    move_lock = threading.Lock()
    mouse_controller = Controller()

    @staticmethod
    def sinusoidal_interpolation(start, end, t):  # not bad but not smooth enough
        return start + (end - start) * (1 - math.cos(t * math.pi)) / 2

    @staticmethod
    def exponential_interpolation(start, end, t, tau=0.1):
        return start + (end - start) * (1 - math.exp(-t / tau))

    @staticmethod
    def move_mouse(x, y):
        SmoothCursor.mouse_controller.position = (x, y)

    @staticmethod
    def smooth_move_to(x2, y2):
        with SmoothCursor.move_lock:
            constants.jitter_click_movement = False
            x1, y1 = SmoothCursor.mouse_controller.position
            distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

            optimal_duration = max(0.5, min(1, distance / constants.move_speed))
            start_time = time.time()
            end_time = start_time + optimal_duration

            while time.time() < end_time:
                t = (time.time() - start_time) / optimal_duration
                x = SmoothCursor.exponential_interpolation(x1, x2, t)
                y = SmoothCursor.exponential_interpolation(y1, y2, t)
                SmoothCursor.move_mouse(x, y)
                time.sleep(0.01)
            constants.jitter_click_movement = True
