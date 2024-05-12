import random
import time
import pyautogui

from SmoothCursor import SmoothCursor
from constants import constants


def detect_2x_booster():
    """Detect booster if mouse_click and earn_menu_active are True."""
    while True:
        while constants.running:
            if constants.mouse_click and constants.earn_menu_active:
                try:
                    booster_pos = pyautogui.locateCenterOnScreen('assets/boosters/2x_booster.png', grayscale=True,
                                                                 confidence=0.8)
                    if booster_pos is not None:
                        time.sleep(random.uniform(0.1, 0.5))
                        SmoothCursor.smooth_move_to(booster_pos[0], booster_pos[1], duration=random.uniform(0.1, 0.3))
                        reset_cursor()
                except pyautogui.ImageNotFoundException:
                    continue


def detect_4x_booster():
    """Detect 4x booster if mouse_click and earn_menu_active are True."""
    while True:
        while constants.running:
            if constants.mouse_click and constants.earn_menu_active:
                try:
                    booster_pos = pyautogui.locateCenterOnScreen('assets/boosters/4x_booster.png', grayscale=True,
                                                                 confidence=0.8)
                    if booster_pos is not None:
                        time.sleep(random.uniform(0.1, 0.5))  # Random delay before moving the cursor
                        SmoothCursor.smooth_move_to(booster_pos[0], booster_pos[1], duration=random.uniform(0.1, 0.3))
                        reset_cursor()
                except pyautogui.ImageNotFoundException:
                    continue


def detect_7x_booster():
    """Detect 7x booster if mouse_click and earn_menu_active are True."""
    while True:
        while constants.running:
            if constants.mouse_click and constants.earn_menu_active:
                try:
                    booster_pos = pyautogui.locateCenterOnScreen('assets/boosters/7x_booster.png', grayscale=True,
                                                                 confidence=0.8)
                    if booster_pos is not None:
                        time.sleep(random.uniform(0.1, 0.5))  # Random delay before moving the cursor
                        SmoothCursor.smooth_move_to(booster_pos[0], booster_pos[1], duration=random.uniform(0.1, 0.3))
                        reset_cursor()
                except pyautogui.ImageNotFoundException:
                    continue


def detect_money_bag():
    """Detect money bag if mouse_click and earn_menu_active are True."""
    while True:
        while constants.running:
            if constants.mouse_click and constants.earn_menu_active:
                try:
                    money_bag_pos = pyautogui.locateCenterOnScreen('assets/boosters/money_bag.png', grayscale=True,
                                                                   confidence=0.8)
                    if money_bag_pos is not None:
                        time.sleep(random.uniform(0.1, 0.5))  # Random delay before moving the cursor
                        SmoothCursor.smooth_move_to(money_bag_pos[0], money_bag_pos[1],
                                                    duration=random.uniform(0.1, 0.3))
                        reset_cursor()
                except pyautogui.ImageNotFoundException:
                    continue


def reset_cursor():
    """Reset cursor to the center of the dollar_sign.png image with a random offset of 200 pixels."""
    try:
        center_pos = pyautogui.locateCenterOnScreen('assets/menu/dollar_sign.png', grayscale=True, confidence=0.8)
        if center_pos is not None:
            offset_x = random.randint(-200, 200)
            offset_y = random.randint(-200, 200)
            time.sleep(random.uniform(0.1, 0.5))  # Random delay before moving the cursor
            SmoothCursor.smooth_move_to(center_pos[0] + offset_x, center_pos[1] + offset_y,
                                        duration=random.uniform(0.1, 0.3))
    except pyautogui.ImageNotFoundException:
        pass
