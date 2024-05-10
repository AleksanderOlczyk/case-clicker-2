import random
import time

import keyboard
import pyautogui
import win32api
import win32con


def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(1 / (cps + random.randint(0, cps_randomization)))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def jitter_move():
    dx = random.randint(-2, 2)
    dy = random.randint(-2, 2)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy)


def on_press(key):
    global running, mouse_click
    if key.name == key_stop:
        running = not running
    elif key.name == key_LMB:
        mouse_click = not mouse_click
        print("Mouse click:", mouse_click)


key_stop = 'o'
key_LMB = 'p'

cps = 20
cps_randomization = 4

keyboard.on_press_key(key_stop, on_press)
keyboard.on_press_key(key_LMB, on_press)
game_map_pos = pyautogui.locateOnScreen('assets/game_map.png', grayscale=True, confidence=0.75)

running = True
mouse_click = False
while running:
    if mouse_click:
        click()
        jitter_move()

        try:
            if game_map_pos is not None:
                booster_pos = pyautogui.locateCenterOnScreen('assets/2x_booster.png', region=game_map_pos,
                                                             grayscale=True, confidence=0.8)
                if booster_pos is not None:
                    win32api.SetCursorPos(booster_pos)
        except pyautogui.ImageNotFoundException:
            continue
