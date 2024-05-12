import random
import time
import pyautogui
from constants import constants


class SmoothCursor:
    @staticmethod
    def linear_interpolation(start, end, t):
        return start * (1 - t) + end * t

    @staticmethod
    def cubic_interpolation(start, end, t):
        t = t * t * (3 - 2 * t)
        return start * (1 - t) + end * t

    @staticmethod
    def smooth_move_to(x2, y2):
        # x2 += random.randint(-4, 4)
        # y2 += random.randint(-4, 4)

        x1, y1 = pyautogui.position()
        start_time = time.time()
        end_time = start_time + constants.move_duration
        while time.time() < end_time:
            t = (time.time() - start_time) / constants.move_duration
            x = SmoothCursor.cubic_interpolation(x1, x2, t)  # Use cubic interpolation
            y = SmoothCursor.cubic_interpolation(y1, y2, t)  # Use cubic interpolation
            pyautogui.moveTo(x, y)
            time.sleep(0.01)
