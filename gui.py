# gui.py
from customtkinter import *

from constants import constants


def update_activation_mode(*args):
    constants.activation_mode = activation_mode_var.get()
    print("Activation mode updated:", constants.activation_mode)


def update_activation_key(*args):
    constants.activation_key = activation_key_var.get()
    print("Activation key updated:", constants.activation_key)


def update_quit_key(*args):
    constants.quit_key = quit_key_var.get()
    print("Quit key updated:", constants.quit_key)


root = CTk()
set_default_color_theme("dark-blue")
root.iconbitmap("assets/logo.ico")

root.title("Case Clicker 2 Automation Tool")
root.geometry("400x300")
root.resizable(False, False)

activation_key_var = StringVar()
activation_key_var.trace("w", update_activation_key)
activation_key_label = CTkLabel(root, text="Activation Key:")
activation_key_label.place(relx=0.1, rely=0.1, anchor='w')
activation_key_entry = CTkEntry(root, textvariable=activation_key_var)
activation_key_entry.place(relx=0.4, rely=0.1, anchor='w')

quit_key_var = StringVar()
quit_key_var.trace("w", update_quit_key)
quit_key_label = CTkLabel(root, text="Quit Key:")
quit_key_label.place(relx=0.1, rely=0.2, anchor='w')
quit_key_entry = CTkEntry(root, textvariable=quit_key_var)
quit_key_entry.place(relx=0.4, rely=0.2, anchor='w')

activation_mode_var = StringVar(value="hold")
activation_mode_label = CTkLabel(root, text="Activation Mode:")
activation_mode_label.place(relx=0.1, rely=0.3, anchor='w')
hold_radio = CTkRadioButton(
    root,
    text="Hold",
    variable=activation_mode_var,
    value="hold",
    command=update_activation_mode
)
hold_radio.place(relx=0.4, rely=0.3, anchor='w')
toggle_radio = CTkRadioButton(
    root,
    text="Toggle",
    variable=activation_mode_var,
    value="toggle",
    command=update_activation_mode
)
toggle_radio.place(relx=0.55, rely=0.3, anchor='w')

# button_start = CTkButton(
#     root,
#     text="Start",
#     corner_radius=64,
#     hover_color="#C850C0"
# )
# button_start.place(anchor='se', relx=0.98, rely=0.88)

button_quit = CTkButton(
    root,
    text="Quit",
    corner_radius=64,
    hover_color="#C850C0"
)
button_quit.place(anchor='se', relx=0.98, rely=0.98)

root.mainloop()
