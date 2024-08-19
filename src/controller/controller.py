import tkinter as tk

from controller.model_controller.data_controller import DataController
from controller.model_controller.ocr_controller import OCRController
from controller.model_controller.settings_controller import SettingsController

from controller.view_controller.main_ui_controller import MainUIController
from controller.view_controller.top_toolbar_controller import (
    TopToolbarController,
)
from view.view import View


class Controller:
    def __init__(self) -> None:
        self.view = View()

        self.data_controller = DataController()
        self.ocr_controller = OCRController()
        self.settings_controller = SettingsController()

        self.main_ui_controller = MainUIController(
            self.view.main_window,
            self.data_controller,
            self.ocr_controller,
            self.settings_controller,
        )
        self.top_toolbar_controller = TopToolbarController(
            self.view.main_window, self.main_ui_controller
        )

        self.top_toolbar_controller.view.frame.pack(side=tk.TOP, fill=tk.X)
        self.main_ui_controller.view.frame.pack(fill=tk.BOTH, expand=True)

    def update(self):
        self.view.update()
