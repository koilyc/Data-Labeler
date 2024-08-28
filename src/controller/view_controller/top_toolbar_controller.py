import tkinter as tk

from tkinter import filedialog

from controller.view_controller.main_ui_controller import MainUIController
from controller.view_controller.model_setting_controller import ModelSettingController
from view.top_toolbar.top_toolbar_view import TopToolbarView


class TopToolbarController:
    def __init__(self, parent_Tk: tk.Tk, main_ui_controller: MainUIController) -> None:
        self.parent_Tk = parent_Tk
        self.main_ui_controller = main_ui_controller
        self.view = TopToolbarView(parent_Tk)
        self.model_setting_controller = ModelSettingController(parent_Tk, main_ui_controller)

        self.setup_menu_command()

    def setup_menu_command(self) -> None:
        self.view.file_menu.add_command(label="Open Folder", command=self.open_folder)
        # self.view.file_menu.add_command(label="儲存標記點")

        self.view.model_menu.add_command(
            label="OCR Current (Ctrl + O)", command=self.ocr_current_image
        )
        self.view.model_menu.add_command(label="OCR All", command=self.ocr_all_images)
        self.view.model_menu.add_command(label="Model Setting", command=self.model_setting)

    # File command
    def open_folder(self) -> None:
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.main_ui_controller.current_folder_path = folder_path

    # Model command
    def ocr_current_image(self) -> None:
        self.main_ui_controller.ocr_current_image()

    def ocr_all_images(self) -> None:
        self.main_ui_controller.show_ocr_progress()
    
    def model_setting(self) -> None:
        self.model_setting_controller.show_setting_model()

    # Shortcuts
    def ocr_current_image_shortcut(self, event) -> None:
        self.ocr_current_image()
