import tkinter as tk

from controller.model_controller.data_controller import DataController
from controller.model_controller.ocr_controller import OCRController
from controller.model_controller.settings_controller import SettingsController

from controller.view_controller.image_editor_controller import (
    ImageEditorController,
)
from controller.view_controller.image_folder_controller import (
    ImageFolderController,
)
from controller.view_controller.image_info_controller import ImageInfoController
from view.main_ui.main_ui_view import MainUIView


class MainUIController:
    def __init__(
        self,
        parent_Tk: tk.Tk,
    ) -> None:
        self.view = MainUIView(parent_Tk)

        self.data_controller = DataController()
        self.ocr_controller = OCRController()
        self.settings_controller = SettingsController()

        self.image_info_controller = ImageInfoController(
            self.view.frame, self.ocr_controller
        )
        self.image_editor_controller = ImageEditorController(
            self.view.frame, self.image_info_controller
        )
        self.image_folder_controller = ImageFolderController(
            self.view.frame,
            self.data_controller,
            self.settings_controller,
            self.image_editor_controller,
        )

        self.image_folder_controller.view.frame.grid(row=0, column=0, sticky="nsew")
        self.image_editor_controller.view.frame.grid(row=0, column=1, sticky="nsew")
        self.image_info_controller.view.frame.grid(row=0, column=2, sticky="nsew")
