import pyautogui
import win32api

from constants import constants


def detect_booster():
    """Detect booster if mouse_click and earn_menu_active are True."""
    while constants.running:
        if constants.mouse_click and constants.earn_menu_active:
            try:
                booster_pos = pyautogui.locateCenterOnScreen('assets/boosters/2x_booster.png', grayscale=True,
                                                             confidence=0.8)
                if booster_pos is not None:
                    win32api.SetCursorPos(booster_pos)
            except pyautogui.ImageNotFoundException:
                continue


def detect_money_bag():
    """Detect money bag if mouse_click and earn_menu_active are True."""
    while constants.running:
        if constants.mouse_click and constants.earn_menu_active:
            try:
                money_bag_pos = pyautogui.locateCenterOnScreen('assets/boosters/money_bag.png', grayscale=True,
                                                               confidence=0.8)
                if money_bag_pos is not None:
                    win32api.SetCursorPos(money_bag_pos)
            except pyautogui.ImageNotFoundException:
                continue
