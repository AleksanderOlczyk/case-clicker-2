import threading

import keyboard

from clicking import click
from constants import constants
from detection import detect_2x_booster, detect_money_bag, detect_4x_booster, detect_7x_booster
from utils import is_earn_menu_active, on_press


def main():
    """Main function to start and join threads."""
    keyboard.on_press_key(constants.key_stop, on_press)
    keyboard.on_press_key(constants.key_LMB, on_press)

    # Create threads
    is_earn_menu_active_thread = threading.Thread(target=is_earn_menu_active)
    click_thread = threading.Thread(target=click, args=(constants.clicks_per_second, constants.cps_randomization))
    money_bag_thread = threading.Thread(target=detect_money_bag)
    detect_2x_booster_thread = threading.Thread(target=detect_2x_booster)
    detect_4x_booster_thread = threading.Thread(target=detect_4x_booster)
    detect_7x_booster_thread = threading.Thread(target=detect_7x_booster)

    # Start threads
    is_earn_menu_active_thread.start()
    click_thread.start()
    money_bag_thread.start()
    detect_2x_booster_thread.start()
    detect_4x_booster_thread.start()
    detect_7x_booster_thread.start()

    # Join threads
    is_earn_menu_active_thread.join()
    click_thread.join()
    money_bag_thread.join()
    detect_2x_booster_thread.join()
    detect_4x_booster_thread.join()
    detect_7x_booster_thread.join()


if __name__ == "__main__":
    main()
