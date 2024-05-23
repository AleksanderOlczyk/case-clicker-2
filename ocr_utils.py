import sys
import time
import pyautogui
import pytesseract

from constants import constants


def locate_crash():
    while constants.running:
        crash_menu = 'assets/menu/crash/crash_menu.png'
        try:
            location = pyautogui.locateOnScreen(
                crash_menu,
                grayscale=True,
                confidence=0.80
            )
            if location is not None:
                return location
        except pyautogui.ImageNotFoundException:
            pass

        time.sleep(0.1)
    else:
        sys.exit(0)


def capture_screen():
    crash_menu = 'assets/menu/crash/crash_menu.png'
    try:
        location = pyautogui.locateOnScreen(crash_menu, grayscale=True, confidence=0.80)
        if location is not None:
            x, y, width, height = location
            center_x = int(x + width // 2)
            y = int(y)
            screenshot = pyautogui.screenshot(region=(center_x - 400, y + 180, 760, 30))
            screenshot.save('screenshot.png')
            return pytesseract.image_to_string(screenshot)
    except pyautogui.ImageNotFoundException:
        pass
