import random
import threading
import time
import pyautogui
from constants import constants


class SmoothCursor:
    move_lock = threading.Lock()

    @staticmethod
    def linear_interpolation(start, end, t):
        return start * (1 - t) + end * t

    @staticmethod
    def smooth_move_to(x2, y2):
        with SmoothCursor.move_lock:
            constants.jitter_move = False
            x1, y1 = pyautogui.position()
            distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            optimal_duration = max(0.5, min(1, distance / constants.cursor_speed))
            start_time = time.time()
            end_time = start_time + optimal_duration

            humanization = 3
            while time.time() < end_time:
                t = (time.time() - start_time) / optimal_duration
                x = SmoothCursor.linear_interpolation(x1, x2, t) + random.uniform(-humanization, humanization)
                y = SmoothCursor.linear_interpolation(y1, y2, t) + random.uniform(-humanization, humanization)
                pyautogui.moveTo(x, y)
                time.sleep(0.01)
            constants.jitter_move = True
