from PIL import Image
from customtkinter import *

from gui_methods import *
from gui_variables import gui_variables

root = CTk()
gui_variables.update_root(root)
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
    textvariable=gui_variables.activation_key_var,
    state='readonly',
    text_color='grey'
)
activation_key_entry.place(relx=0.3, rely=0.1, anchor='w')
gui_variables.activation_key_entry = activation_key_entry

quit_key_var = StringVar(value=constants.quit_key)
quit_key_var.trace("w", update_quit_key)
quit_key_label = CTkLabel(root, text="Quit Key:")
quit_key_label.place(relx=0.04, rely=0.2, anchor='w')
quit_key_entry = CTkEntry(
    root,
    corner_radius=64,
    textvariable=gui_variables.quit_key_var,
    state='readonly',
    text_color='grey'
)
quit_key_entry.place(relx=0.3, rely=0.2, anchor='w')
gui_variables.quit_key_entry = quit_key_entry

change_activation_key = CTkButton(
    root,
    text="Change",
    width=120,
    corner_radius=64,
    hover_color="#C850C0",
    command=activation_key_change
)
change_activation_key.place(anchor='e', relx=0.98, rely=0.1)

change_quit_key = CTkButton(
    root,
    text="Change",
    width=120,
    corner_radius=64,
    hover_color="#C850C0",
    command=quit_key_change
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
    variable=gui_variables.activation_mode_var,
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
    variable=gui_variables.activation_mode_var,
    command=update_activation_mode
)
toggle_radio.place(relx=0.45, rely=0.3, anchor='w')
gui_variables.activation_mode_var = activation_mode_var

cps_var = IntVar(value=constants.clicks_per_second)
cps_var.trace("w", update_cps)
gui_variables.cps_var = cps_var

cps_label = CTkLabel(root, text="CPS:")
cps_label.place(relx=0.04, rely=0.4, anchor='w')

cps_slider = CTkSlider(
    root,
    width=200,
    from_=1,
    to=100,
    number_of_steps=100,
    button_hover_color="#C850C0",
    variable=gui_variables.cps_var,
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
    hover_color="#C850C0",
    variable=gui_variables.cps_randomize_var,
    command=update_cps_randomize
)
cps_randomize_checkbox.place(relx=0.2, rely=0.5, anchor='w')
gui_variables.cps_randomize_var = cps_randomize_var

jitter_click_movement_var = BooleanVar(value=constants.jitter_click_movement)
jitter_click_movement_var.trace("w", update_jitter_click_movement)
jitter_click_movement_checkbox = CTkCheckBox(
    root,
    checkbox_width=20,
    checkbox_height=20,
    text="Jitter",
    hover_color="#C850C0",
    variable=gui_variables.jitter_click_movement_var,
    command=update_jitter_click_movement
)
jitter_click_movement_checkbox.place(relx=0.48, rely=0.5, anchor='w')
gui_variables.jitter_click_movement_var = jitter_click_movement_var

img = Image.open("assets/logo_3.png")
img = img.resize((64, 64), Image.LANCZOS)
logo_image = CTkImage(img, size=[64, 64])
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
