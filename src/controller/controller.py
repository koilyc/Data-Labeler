import tkinter as tk

from controller.view_controller.main_ui_controller import MainUIController
from controller.view_controller.top_toolbar_controller import (
    TopToolbarController,
)
from view.view import View


class Controller:
    def __init__(self) -> None:
        self.view = View()

        self.main_ui_controller = MainUIController(self.view.main_window)
        self.top_toolbar_controller = TopToolbarController(
            self.view.main_window, self.main_ui_controller
        )

        self.top_toolbar_controller.view.frame.pack(side=tk.TOP, fill=tk.X)
        self.main_ui_controller.view.frame.pack(fill=tk.BOTH, expand=True)

    def update(self):
        self.view.update()
