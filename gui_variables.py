from customtkinter import StringVar, IntVar, BooleanVar, CTkLabel
from constants import constants


class GuiVariables:
    def __init__(self):
        self.root = None
        self.activation_key_var = None
        self.quit_key_var = None
        self.activation_mode_var = None
        self.cps_var = None
        self.cps_randomize_var = None
        self.jitter_click_movement_var = None
        self.cps_display_label = None

    def update_root(self, root):
        self.root = root
        self.activation_key_var = StringVar(value=constants.activation_key, master=root)
        self.quit_key_var = StringVar(value=constants.quit_key, master=root)
        self.activation_mode_var = StringVar(value="hold" if constants.activation_mode else "toggle", master=root)
        self.cps_var = IntVar(value=constants.clicks_per_second, master=root)
        self.cps_randomize_var = BooleanVar(value=constants.cps_randomize, master=root)
        self.jitter_click_movement_var = BooleanVar(value=constants.jitter_click_movement, master=root)
        self.cps_display_label = CTkLabel(root, text=str(constants.clicks_per_second))


gui_variables = GuiVariables()
