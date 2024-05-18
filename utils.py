import sys
import time
import pyautogui
from constants import constants


def is_earn_menu_active():
    """Check if earn menu is active and update the global variable earn_menu_active."""
    while constants.running:
        try:
            location = pyautogui.locateOnScreen('assets/menu/dollar_sign.png', confidence=0.80)
            constants.earn_menu_active = location is not None
        except pyautogui.ImageNotFoundException:
            constants.earn_menu_active = False

        time.sleep(0.1)
    else:
        sys.exit(0)


def on_press(key):
    """Handle key press events."""
    if key.name == constants.quit_key:
        constants.running = not constants.running
    elif key.name == constants.activation_key:
        if constants.activation_mode:  # hold mode
            constants.mouse_click = True
        else:  # toggle mode
            constants.mouse_click = not constants.mouse_click


def on_release(key):
    """Handle key release events."""
    if constants.activation_mode and key.name == constants.activation_key:  # hold mode
        constants.mouse_click = False
