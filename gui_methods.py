from constants import constants
from gui_variables import gui_variables
from key_reader import KeyReader


# Fix error in the code below
# In each of the functions below, is error with applying the new value to the gui_variable.py file

def update_activation_key():
    constants.activation_key = gui_variables.activation_key_var.get()
    print("Activation key updated:", constants.activation_key)


def update_quit_key():
    constants.quit_key = gui_variables.quit_key_var.get()
    print("Quit key updated:", constants.quit_key)


def update_activation_mode():
    constants.activation_mode = gui_variables.activation_mode_var.get()
    print("Activation mode updated:", constants.activation_mode)


def quit_key_change():
    gui_variables.quit_key_entry.configure(text_color='white')
    key_reader = KeyReader(gui_variables.root)
    gui_variables.root.wait_window(key_reader)
    if key_reader.key_pressed:
        gui_variables.quit_key_var.set(key_reader.key_pressed)
    gui_variables.quit_key_entry.configure(text_color='grey')


def activation_key_change():
    gui_variables.activation_key_entry.configure(state='normal', text_color='white')
    key_reader = KeyReader(gui_variables.root)
    gui_variables.root.wait_window(key_reader)
    if key_reader.key_pressed:
        gui_variables.activation_key_var.set(key_reader.key_pressed)
    gui_variables.activation_key_entry.configure(text_color='grey')


def update_cps():
    constants.clicks_per_second = gui_variables.cps_var.get()
    gui_variables.cps_display_label.configure(text=str(gui_variables.cps_var.get()))
    gui_variables.root.update_idletasks()
    print("CPS updated:", constants.clicks_per_second)
    print("CPS updated2:", gui_variables.cps_var.get())


def update_cps_randomize():
    constants.cps_randomize = gui_variables.cps_randomize_var.get()
    print("CPS Randomize updated:", constants.cps_randomize)


def update_jitter_click_movement():
    constants.jitter_click_movement = gui_variables.jitter_click_movement_var.get()
    print("Jitter Click Movement updated:", constants.jitter_click_movement)


def quit_application():
    constants.running = False
    gui_variables.root.destroy()
