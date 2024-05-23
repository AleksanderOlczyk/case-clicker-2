import re
import cv2
import pyautogui
import pytesseract
import numpy as np


def process_image(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Adaptive thresholding
    binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY_INV, 11, 2)

    # Dilate and erode to remove noise
    kernel = np.ones((1, 1), np.uint8)
    binary = cv2.dilate(binary, kernel, iterations=1)
    binary = cv2.erode(binary, kernel, iterations=1)

    # Further blur to smooth the image
    blurred = cv2.GaussianBlur(binary, (3, 3), 0)

    # OCR configuration
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(blurred, config=custom_config)

    # Extract numbers
    numbers = re.findall(r'x(\d+\.\d+)', text)
    float_numbers = [float(num) for num in numbers]
    return float_numbers


def capture_screen():
    crash_menu = 'assets/menu/crash/crash_menu.png'
    try:
        location = pyautogui.locateOnScreen(
            crash_menu,
            grayscale=True,
            confidence=0.80
        )
        if location is not None:
            x, y, width, height = location
            center_x = int(x + width // 2)
            y = int(y)
            screenshot = pyautogui.screenshot(region=(center_x - 400, y + 180, 760, 30))
            screenshot.save('screenshot.png')
            return process_image('screenshot.png')
    except pyautogui.ImageNotFoundException:
        pass


print(capture_screen())