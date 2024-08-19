import tkinter as tk


class MainUIView:
    def __init__(self, parent_Tk: tk.Tk) -> None:
        self.parent_Tk = parent_Tk

        self.frame = tk.Frame(
            self.parent_Tk,
        )

        self.configure_grid()

    def configure_grid(self) -> None:
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=2)
        self.frame.grid_columnconfigure(2, weight=1)

        self.frame.grid_rowconfigure(0, weight=1)
