import random
import time

import win32api
import win32con

from constants import mouse_click, earn_menu_active


def click(clicks_per_second, cps_randomization):
    """Simulate mouse click if mouse_click and earn_menu_active are True."""
    while True:
        if mouse_click and earn_menu_active:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            time.sleep(1 / (clicks_per_second + random.randint(0, cps_randomization)))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            jitter_move()


def jitter_move():
    """Simulate mouse movement."""
    dx = random.randint(-2, 2)
    dy = random.randint(-2, 2)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy)
