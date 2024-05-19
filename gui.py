import keyboard
from PIL import Image, ImageTk
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


def on_key_press(e):
    quit_key_var.set(e.name)
    quit_key_entry.configure(state='readonly', text_color='grey')


def change_key():
    quit_key_entry.configure(state='normal', text_color='white')
    keyboard.on_press(on_key_press)


def update_cps(*args):
    constants.clicks_per_second = cps_var.get()
    cps_display_label.configure(text=str(constants.clicks_per_second))
    print("CPS updated:", constants.clicks_per_second)


def update_cps_randomize(*args):
    constants.cps_randomize = cps_randomize_var.get()
    print("CPS Randomize updated:", constants.cps_randomize)


def update_jitter_click_movement(*args):
    constants.jitter_click_movement = jitter_click_movement_var.get()
    print("Jitter Click Movement updated:", constants.jitter_click_movement)


def quit_application():
    constants.running = False
    root.destroy()


root = CTk()
set_default_color_theme("dark-blue")
root.iconbitmap("assets/logo.ico")

root.title("Case Clicker 2 Automation Tool")
root.geometry("400x300")
root.resizable(False, False)

activation_key_var = StringVar(value=constants.activation_key)
activation_key_var.trace("w", update_activation_key)
activation_key_label = CTkLabel(root, text="Activation Key:")
activation_key_label.place(relx=0.04, rely=0.1, anchor='w')
activation_key_entry = CTkEntry(
    root,
    corner_radius=64,
    textvariable=activation_key_var,
    state='readonly',
    text_color='grey'
)
activation_key_entry.place(relx=0.3, rely=0.1, anchor='w')

quit_key_var = StringVar(value=constants.quit_key)
quit_key_var.trace("w", update_quit_key)
quit_key_label = CTkLabel(root, text="Quit Key:")
quit_key_label.place(relx=0.04, rely=0.2, anchor='w')
quit_key_entry = CTkEntry(
    root,
    corner_radius=64,
    textvariable=quit_key_var,
    state='readonly',
    text_color='grey'
)
quit_key_entry.place(relx=0.3, rely=0.2, anchor='w')

change_activation_key = CTkButton(
    root,
    text="Change",
    width=120,
    corner_radius=64,
    hover_color="#C850C0",
    command=change_key
)
change_activation_key.place(anchor='e', relx=0.98, rely=0.1)

change_quit_key = CTkButton(
    root,
    text="Change",
    width=120,
    corner_radius=64,
    hover_color="#C850C0",
    command=change_key
)
change_quit_key.place(anchor='e', relx=0.98, rely=0.2)

activation_mode_var = StringVar(value="hold" if constants.activation_mode else "toggle")
activation_mode_label = CTkLabel(root, text="Activation Mode:")
activation_mode_label.place(relx=0.04, rely=0.3, anchor='w')
hold_radio = CTkRadioButton(
    root,
    radiobutton_width=20,
    radiobutton_height=20,
    text="Hold",
    value="hold",
    hover_color="#C850C0",
    variable=activation_mode_var,
    command=update_activation_mode
)
hold_radio.place(relx=0.3, rely=0.3, anchor='w')
toggle_radio = CTkRadioButton(
    root,
    radiobutton_width=20,
    radiobutton_height=20,
    text="Toggle",
    value="toggle",
    hover_color="#C850C0",
    variable=activation_mode_var,
    command=update_activation_mode
)
toggle_radio.place(relx=0.45, rely=0.3, anchor='w')

cps_var = IntVar(value=constants.clicks_per_second)
cps_var.trace("w", update_cps)

cps_label = CTkLabel(root, text="CPS:")
cps_label.place(relx=0.04, rely=0.4, anchor='w')

cps_slider = CTkSlider(
    root,
    width=200,
    from_=1,
    to=100,
    number_of_steps=100,
    button_hover_color="#C850C0",
    variable=cps_var,
    command=update_cps
)
cps_slider.place(relx=0.15, rely=0.4, anchor='w')
cps_display_label = CTkLabel(root, text=str(constants.clicks_per_second))
cps_display_label.place(relx=0.65, rely=0.4, anchor='w')

cps_randomize_var = BooleanVar(value=constants.cps_randomize)
cps_randomize_var.trace("w", update_cps_randomize)
cps_randomize_checkbox = CTkCheckBox(
    root,
    checkbox_width=20,
    checkbox_height=20,
    text="Randomize",
    variable=cps_randomize_var,
    command=update_cps_randomize
)
cps_randomize_checkbox.place(relx=0.2, rely=0.5, anchor='w')

jitter_click_movement_var = BooleanVar(value=constants.jitter_click_movement)
jitter_click_movement_var.trace("w", update_jitter_click_movement)
jitter_click_movement_checkbox = CTkCheckBox(
    root,
    checkbox_width=20,
    checkbox_height=20,
    text="Jitter",
    variable=jitter_click_movement_var,
    command=update_jitter_click_movement
)
jitter_click_movement_checkbox.place(relx=0.48, rely=0.5, anchor='w')

img = Image.open("assets/logo.png")
img = img.resize((64, 64), Image.LANCZOS)
logo_image = ImageTk.PhotoImage(img)
logo_label = CTkLabel(root, image=logo_image, text="")
logo_label.place(anchor='sw', relx=0.02, rely=0.98)


button_apply = CTkButton(
    root,
    text="Apply",
    corner_radius=64,
    hover_color="#C850C0"
)
button_apply.place(anchor='se', relx=0.98, rely=0.88)

button_quit = CTkButton(
    root,
    text="Quit",
    corner_radius=64,
    hover_color="#C850C0",
    command=quit_application
)
button_quit.place(anchor='se', relx=0.98, rely=0.98)

root.mainloop()
