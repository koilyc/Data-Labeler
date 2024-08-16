import tkinter as tk


class MainFrame:
    def __init__(self, parent: tk.Tk) -> None:
        self.parent_frame = parent

        self.frame = tk.Frame(
            self.parent_frame,
        )

        self.configure_grid()

    def configure_grid(self) -> None:
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=2)
        self.frame.grid_columnconfigure(2, weight=1)

        self.frame.grid_rowconfigure(0, weight=1)
