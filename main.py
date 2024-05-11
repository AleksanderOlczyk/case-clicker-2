import threading

import keyboard

from clicking import click
from constants import key_stop, key_LMB, clicks_per_second, cps_randomization
from detection import detect_booster, detect_money_bag
from utils import is_earn_menu_active, on_press


def main():
    """Main function to start and join threads."""
    keyboard.on_press_key(key_stop, on_press)
    keyboard.on_press_key(key_LMB, on_press)

    # Create threads
    click_thread = threading.Thread(target=click, args=(clicks_per_second, cps_randomization))
    booster_thread = threading.Thread(target=detect_booster)
    money_bag_thread = threading.Thread(target=detect_money_bag)
    is_earn_menu_active_thread = threading.Thread(target=is_earn_menu_active)

    # Start threads
    click_thread.start()
    booster_thread.start()
    money_bag_thread.start()
    is_earn_menu_active_thread.start()

    # Join threads
    click_thread.join()
    booster_thread.join()
    money_bag_thread.join()
    is_earn_menu_active_thread.join()


if __name__ == "__main__":
    main()
