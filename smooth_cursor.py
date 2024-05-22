"""
This module contains the SmoothCursor class, which provides methods for smooth mouse movement.

Classes:
    SmoothCursor: A class that provides methods for smooth mouse movement.

Methods:
    exponential_interpolation(start, end, t, tau=0.1): Interpolates between two points using an exponential function.
    move_mouse(x, y): Moves the mouse to the specified coordinates.
    smooth_move_to(x2, y2): Moves the mouse to the specified coordinates in a smooth manner.

Variables:
    move_lock: A threading.Lock object used to synchronize mouse movement.
    mouse_controller: A pynput.mouse.Controller object used to control the mouse.
"""
import threading
import time
import math
from constants import constants
from pynput.mouse import Controller


class SmoothCursor:
    """
    A class that provides methods for smooth mouse movement.

    Methods:
        exponential_interpolation(start, end, t, tau=0.1): Interpolates between two points using an exponential function.
        move_mouse(x, y): Moves the mouse to the specified coordinates.
        smooth_move_to(x2, y2): Moves the mouse to the specified coordinates in a smooth manner.
    """
    move_lock = threading.Lock()
    mouse_controller = Controller()

    @staticmethod
    def exponential_interpolation(start: float, end: float, t: float, tau: float = 0.1) -> float:
        """
        Interpolates between two points using an exponential function.

        Parameters:
            start (float): The start value.
            end (float): The end value.
            t (float): The interpolation parameter.
            tau (float, optional): The time constant of the exponential function. Default is 0.1.

        Returns:
            float: The interpolated value.
        """
        return start + (end - start) * (1 - math.exp(-t / tau))

    @staticmethod
    def move_mouse(x, y):
        """
        Moves the mouse to the specified coordinates.

        Parameters:
            x (float): The x-coordinate.
            y (float): The y-coordinate.
        """
        SmoothCursor.mouse_controller.position = (x, y)

    @staticmethod
    def smooth_move_to(x2, y2):
        """
        Moves the mouse to the specified coordinates in a smooth manner.

        Parameters:
            x2 (float): The target x-coordinate.
            y2 (float): The target y-coordinate.
        """
        with SmoothCursor.move_lock:
            constants.jitter_click_movement = False
            x1, y1 = SmoothCursor.mouse_controller.position
            distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

            optimal_duration = max(0.5, min(1, distance / constants.move_speed))
            start_time = time.time()
            end_time = start_time + optimal_duration

            while time.time() < end_time:
                t = (time.time() - start_time) / optimal_duration
                x = SmoothCursor.exponential_interpolation(x1, x2, t)
                y = SmoothCursor.exponential_interpolation(y1, y2, t)
                SmoothCursor.move_mouse(x, y)
                time.sleep(0.01)
            constants.jitter_click_movement = True
