"""
This module contains functions to simulate mouse clicks and movements.

Functions:
    click(): Simulates mouse clicks if certain conditions are met.
    jitter_click_movement(): Simulates small random mouse movements to mimic human behavior.
"""

import random
import time

import win32api
import win32con

from constants import constants


def click():
    """
    This function continuously checks if the tool is running, and if the mouse_click and earn_menu_active
    flags are set to True. If these conditions are met, it simulates a mouse click with optional random
    intervals and jitter movements to mimic human behavior.
    """
    while constants.running:
        if constants.mouse_click and constants.earn_menu_active and not constants.mouse_moving:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            if constants.cps_randomize:
                time.sleep(
                    1 / (constants.clicks_per_second
                         + random.randint(
                                -constants.cps_randomization,
                                constants.cps_randomization)
                         )
                )
            else:
                time.sleep(1 / constants.clicks_per_second)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            if constants.jitter_click_movement:
                jitter_click_movement()


def jitter_click_movement():
    """
    This function generates small random movements in the x and y directions to simulate
    natural jittery movements of a human hand while clicking.
    """
    dx = random.randint(-2, 2)
    dy = random.randint(-2, 2)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy)
