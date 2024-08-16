import tkinter as tk


class View:
    def __init__(self) -> None:
        self.main_window = tk.Tk()
        self.main_window.state("zoomed")
        self.main_window.title("Data Labeler")

    def update(self) -> None:
        self.main_window.mainloop()
