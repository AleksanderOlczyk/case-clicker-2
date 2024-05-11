import random
import time
import threading
import keyboard
import pyautogui
import win32api
import win32con


def click(cps, cps_randomization):
    while True:
        if mouse_click:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            time.sleep(1 / (cps + random.randint(0, cps_randomization)))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            jitter_move()


def jitter_move():
    dx = random.randint(-2, 2)
    dy = random.randint(-2, 2)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy)


def detect_booster(game_map_pos):
    global running
    while running:
        try:
            if game_map_pos is not None:
                booster_pos = pyautogui.locateCenterOnScreen('assets/2x_booster.png', region=game_map_pos,
                                                             grayscale=True, confidence=0.8)
                if booster_pos is not None:
                    win32api.SetCursorPos(booster_pos)
        except pyautogui.ImageNotFoundException:
            continue


def verify_game_map():
    global game_map_pos
    while mouse_click:
        try:
            if game_map_pos is None:
                game_map_pos = pyautogui.locateOnScreen('assets/game_map.png', grayscale=True, confidence=0.75)
                time.sleep(2)
            else:
                print("Game map position found.")
                time.sleep(30)
        except Exception as e:
            print("An error occurred while verifying game map:", e)
            time.sleep(2)


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
mouse_click = False

keyboard.on_press_key(key_stop, on_press)
keyboard.on_press_key(key_LMB, on_press)
game_map_pos = None
running = True

# Create threads
click_thread = threading.Thread(target=click, args=(cps, cps_randomization))
booster_thread = threading.Thread(target=detect_booster, args=(game_map_pos,))
verify_game_map_thread = threading.Thread(target=verify_game_map)

# Start threads
click_thread.start()
booster_thread.start()
verify_game_map_thread.start()

# Join threads
click_thread.join()
verify_game_map_thread.join()
booster_thread.join()
