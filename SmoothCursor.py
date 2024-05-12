import time
import pyautogui


class SmoothCursor:
    @staticmethod
    def lerp(start, end, t):
        return start * (1 - t) + end * t

    @staticmethod
    def smooth_move_to(x2, y2, duration):
        x1, y1 = pyautogui.position()
        start_time = time.time()
        end_time = start_time + duration
        while time.time() < end_time:
            t = (time.time() - start_time) / duration
            x = SmoothCursor.lerp(x1, x2, t)
            y = SmoothCursor.lerp(y1, y2, t)
            pyautogui.moveTo(x, y)
            time.sleep(0.01)
