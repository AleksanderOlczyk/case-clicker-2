"""
This module contains utility functions.

Functions:
    is_earn_menu_active(): Checks if the earn menu is active and updates the global variable earn_menu_active.
    on_press(key): Handles key press events.
    on_release(key): Handles key release events.
"""

import sys
import time
import pyautogui
from constants import constants


def is_earn_menu_active():
    """
    This function continuously checks if the earn menu is active by looking for the dollar sign image on the screen.
    If the image is found, it sets the earn_menu_active flag to True, otherwise it sets it to False.
    """
    while constants.running:
        dollar_sign_path = 'assets/menu/dollar_sign.png'
        try:
            location = pyautogui.locateOnScreen(
                dollar_sign_path,
                grayscale=True,
                confidence=0.80
            )
            constants.earn_menu_active = location is not None
        except pyautogui.ImageNotFoundException:
            constants.earn_menu_active = False

        time.sleep(0.1)
    else:
        sys.exit(0)


def on_press(key):
    """
    This function checks if the pressed key is the quit key or the activation key. If the quit key is pressed,
    it toggles the running flag. If the activation key is pressed, it either activates or deactivates mouse clicking
    based on the activation mode (hold or toggle).
    """
    if key.name == constants.quit_key:
        constants.running = not constants.running
    elif key.name == constants.activation_key:
        if constants.activation_mode:  # hold mode
            constants.mouse_click = True
            print("Mouse click activated.")
        else:  # toggle mode
            constants.mouse_click = not constants.mouse_click
            print("Mouse click:", "activated." if constants.mouse_click else "deactivated.")


def on_release(key):
    """
    This function checks if the released key is the activation key and the activation mode is hold. If so,
    it deactivates mouse clicking.
    """
    if constants.activation_mode and key.name == constants.activation_key:  # hold mode
        constants.mouse_click = False
        print("Mouse click deactivated.")
