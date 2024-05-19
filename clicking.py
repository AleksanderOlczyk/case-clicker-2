import random
import time

import win32api
import win32con

from constants import constants


def click(clicks_per_second, cps_randomization):
    """Simulate mouse click if mouse_click and earn_menu_active are True."""
    while constants.running:
        if constants.mouse_click and constants.earn_menu_active and not constants.mouse_moving:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            if constants.cps_randomize:
                time.sleep(1 / (clicks_per_second + random.randint(-cps_randomization, cps_randomization)))
            else:
                time.sleep(1 / clicks_per_second)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            if constants.jitter_click_movement:
                jitter_click_movement()


def jitter_click_movement():
    """Simulate mouse movement."""
    dx = random.randint(-2, 2)
    dy = random.randint(-2, 2)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy)
