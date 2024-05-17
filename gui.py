from customtkinter import *
from PIL import *


def switch_event():
    print("switch toggled, current value:", switch_var.get())


root = CTk()
set_default_color_theme("dark-blue")
root.iconbitmap("assets/logo.ico")

root.title("Case Clicker 2 Automation Tool")
root.geometry("400x300")

button_start = CTkButton(
    root,
    text="Start",
    corner_radius=64,
    hover_color="#C850C0"
)
button_start.place(anchor='se', relx=0.98, rely=0.88)

button_apply = CTkButton(
    root,
    text="Apply",
    corner_radius=64,
    hover_color="#C850C0"
)
button_apply.place(anchor='se', relx=0.98, rely=0.98)

switch_var = StringVar(value="on")
switch = CTkSwitch(root,
                   text="jitter click",
                   command=switch_event,
                   variable=switch_var,
                   onvalue="on",
                   offvalue="off"
)
switch.place(relx=0.5, rely=0.4, anchor='center')

root.mainloop()
