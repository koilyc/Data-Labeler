import tkinter as tk

from controller.view_controller.image_editor_controller import ImageEditorController
from controller.model_controller.data_controller import DataController
from controller.model_controller.ocr_controller import OCRController
from controller.model_controller.settings_controller import SettingsController
from view.main_frame.main_frame import MainFrame
from view.main_frame.image_folder import ImageFolder
from view.main_frame.image_editor.image_editor import ImageEditor
from view.main_frame.image_info import ImageInfo


class MainFrameController:
    def __init__(self, parent: tk.Tk) -> None:
        self.main_frame = MainFrame(parent)

        self.image_editor_controller = ImageEditorController()
        self.data_controller = DataController()
        self.ocr_controller = OCRController()
        self.settings_controller = SettingsController()

        self.image_info = ImageInfo(self.main_frame.frame, self.ocr_controller)
        self.image_editor = ImageEditor(self.main_frame.frame, self.image_info, self.image_editor_controller)
        self.image_folder = ImageFolder(
            self.main_frame.frame,
            self.image_editor,
            self.data_controller,
            self.settings_controller,
        )

        self.image_folder.frame.grid(row=0, column=0, sticky="nsew")
        self.image_editor.frame.grid(row=0, column=1, sticky="nsew")
        self.image_info.frame.grid(row=0, column=2, sticky="nsew")
