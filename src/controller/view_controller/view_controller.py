import tkinter as tk

from controller.view_controller.main_frame.main_frame_controller import MainFrameController
from view.view import View
from view.top_toolbar.top_toolbar import TopToolbar


class ViewController:
    def __init__(self) -> None:
        self.view = View()

        self.main_frame_controller = MainFrameController(self.view.main_window)
        self.top_toolbar = TopToolbar(self.view.main_window, self.main_frame_controller)
        self.top_toolbar.frame.pack(side=tk.TOP, fill=tk.X)
        self.main_frame_controller.main_frame.frame.pack(fill=tk.BOTH, expand=True)

    def update(self):
        self.view.update()
