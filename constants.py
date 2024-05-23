"""
This module contains the Constants class, which stores global variables used throughout the project.

Class Constants:
    A class that stores global variables.

    Attributes:
        quit_key (str): The key that stops the tool's operation.
        activation_key (str): The key that activates and deactivates mouse clicking.
        clicks_per_second (int): The number of mouse clicks per second.
        jitter_click_movement (bool): Determines whether mouse movements should be random during clicking.
        activation_mode (bool): Determines the activation mode. True for "hold" mode, False for "toggle" mode.
        cps_randomize (bool): Determines whether the number of clicks per second should be randomized.

        cps_randomization (int): The range of randomness for the number of clicks per second.
        earn_menu_active (bool): Determines whether the earn menu is active.
        detect_boosters (bool): Determines whether the tool should detect boosters.
        mouse_moving (bool): Determines whether the mouse is currently moving.
        mouse_click (bool): Determines whether the tool should simulate mouse clicks.
        move_speed (int): The speed of mouse movement.
        running (bool): Determines whether the tool is currently running.
"""


class Constants:
    # Game variables
    quit_key: str = 'delete'
    activation_key: str = 'p'
    clicks_per_second: int = 20
    jitter_click_movement: bool = True
    activation_mode: bool = False  # True for hold, False for toggle
    detect_boosters: bool = True
    cps_randomize: bool = True

    # System variables
    cps_randomization: int = 4
    earn_menu_active: bool = False
    mouse_moving: bool = False
    mouse_click: bool = False
    move_speed: int = 400
    running: bool = True


constants = Constants()
