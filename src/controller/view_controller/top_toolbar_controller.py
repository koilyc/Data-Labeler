import tkinter as tk

from tkinter import filedialog

from controller.view_controller.main_ui_controller import MainUIController
from view.top_toolbar.model_setting_toplevel import ModelSettingToplevel
from view.top_toolbar.top_toolbar_view import TopToolbarView


class TopToolbarController:
    def __init__(self, parent_Tk: tk.Tk, main_ui_controller: MainUIController) -> None:
        self.parent_Tk = parent_Tk
        self.main_ui_controller = main_ui_controller
        self.view = TopToolbarView(parent_Tk)
        self.model_setting_toplevel = ModelSettingToplevel(
            parent_Tk, self.main_ui_controller
        )

        self.setup_menu_command()
        self.bind_shortcuts()

    def open_folder(self) -> None:
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.main_ui_controller.current_folder_path = folder_path

    def setup_menu_command(self) -> None:
        self.view.file_menu.add_command(label="Open Folder", command=self.open_folder)
        # self.view.file_menu.add_command(label="儲存標記點")

        self.view.model_menu.add_command(
            label="OCR Current (Ctrl + O)", command=self.ocr_current_image
        )
        self.view.model_menu.add_command(label="OCR All", command=self.ocr_all_images)
        self.view.model_menu.add_command(
            label="Model Setting", command=self.show_setting_model
        )

    def ocr_current_image(self) -> None:
        self.main_ui_controller.ocr_current_image()

    def ocr_all_images(self) -> None:
        self.main_ui_controller.show_ocr_progress()

    def bind_shortcuts(self) -> None:
        # 快捷鍵需綁定在主窗口 (tk.Tk) 上，因為快捷鍵僅在當前焦點窗口中有效
        self.parent_Tk.bind("<Control-o>", self.handle_ocr_shortcut)

    def handle_ocr_shortcut(self, event) -> None:
        self.ocr_current_image()

    def show_setting_model(self) -> None:
        self.model_setting_toplevel.show_toplevel()
