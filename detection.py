"""
This module contains functions to detect various boosters and money bags in the game.

Functions:
    detect_booster(booster_image): Detects a booster on the screen using the provided image.
    detect_2x_booster(): Detects the 2x booster on the screen.
    detect_4x_booster(): Detects the 4x booster on the screen.
    detect_7x_booster(): Detects the 7x booster on the screen.
    detect_money_bag(): Detects the money bag on the screen.
    reset_cursor(): Resets the cursor to the center of the dollar sign image with a random offset.
"""

import random
import sys
import time
import pyautogui

from smooth_cursor import SmoothCursor
from constants import constants


def detect_booster(booster_image):
    """Detect booster if mouse_click and earn_menu_active are True."""
    booster_detected: bool = False
    booster_previously_detected: bool = False
    last_detection_time: int = 0
    detection_delay: int = 1
    moving_to_booster: bool = False
    booster_pos: tuple = None

    while True:
        while constants.running:
            if constants.mouse_click and constants.earn_menu_active and constants.detect_boosters:
                try:
                    booster_pos = pyautogui.locateCenterOnScreen(booster_image, grayscale=True, confidence=0.8)
                    if booster_pos is not None:
                        booster_detected = True
                        last_detection_time = time.time()
                        time.sleep(random.uniform(0.1, 0.3))
                        SmoothCursor.smooth_move_to(booster_pos[0], booster_pos[1])
                    else:
                        booster_detected = False
                except pyautogui.ImageNotFoundException:
                    booster_detected = False

            if (booster_previously_detected and not booster_detected
                    and time.time() - last_detection_time > detection_delay):
                if not moving_to_booster and constants.running:
                    reset_cursor()
            booster_previously_detected = booster_detected

            current_pos = pyautogui.position()
            if booster_pos is not None and abs(current_pos[0] - booster_pos[0]) < 5 and abs(
                    current_pos[1] - booster_pos[1]) < 5:
                moving_to_booster = False
        else:
            sys.exit(0)


def detect_2x_booster():
    return detect_booster('assets/boosters/2x_booster.png')


def detect_4x_booster():
    return detect_booster('assets/boosters/4x_booster.png')


def detect_7x_booster():
    return detect_booster('assets/boosters/7x_booster.png')


def detect_money_bag():
    return detect_booster('assets/boosters/money_bag.png')


def reset_cursor():
    """Reset cursor to the center of the dollar_sign.png image with a random offset of 200 pixels."""
    try:
        center_pos = pyautogui.locateCenterOnScreen(
            'assets/menu/dollar_sign.png',
            grayscale=True,
            confidence=0.8
        )
        if center_pos is not None:
            current_pos = pyautogui.position()
            if abs(current_pos[0] - center_pos[0]) > 250 or abs(current_pos[1] - center_pos[1]) > 250:
                offset_x = random.randint(-200, 200)
                offset_y = random.randint(-200, 200)
                time.sleep(random.uniform(0.1, 0.5))
                SmoothCursor.smooth_move_to(center_pos[0] + offset_x, center_pos[1] + offset_y)
    except pyautogui.ImageNotFoundException:
        pass
