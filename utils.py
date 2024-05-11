import pyautogui

from constants import key_stop, key_LMB


def is_earn_menu_active():
    """Check if earn menu is active and update the global variable earn_menu_active."""
    while running:
        try:
            earn_menu_pos = pyautogui.locateCenterOnScreen('assets/menu/active_earn_menu.png', grayscale=True,
                                                           confidence=0.8)
            earn_menu_active = earn_menu_pos is not None
        except pyautogui.ImageNotFoundException:
            earn_menu_active = False


def on_press(key):
    """Handle key press events."""
    global running, mouse_click
    if key.name == key_stop:
        running = not running
        SystemExit(0)
    elif key.name == key_LMB:
        mouse_click = not mouse_click
        print("Mouse click:", mouse_click)
