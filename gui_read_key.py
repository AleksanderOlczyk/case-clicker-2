from customtkinter import CTkToplevel


class KeyReader(CTkToplevel):
    window_open = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if KeyReader.window_open:
            self.destroy()
            return
        self.bind('<Key>', self.on_key_press)
        self.key_pressed = None
        KeyReader.window_open = True
        self.attributes('-topmost', True)

    def on_key_press(self, event):
        self.key_pressed = event.keysym
        self.destroy()

    def destroy(self):
        KeyReader.window_open = False
        super().destroy()
