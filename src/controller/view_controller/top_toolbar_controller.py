import tkinter as tk

from tkinter import filedialog

from controller.view_controller.main_ui_controller import MainUIController
from view.top_toolbar.top_toolbar_view import TopToolbarView


class TopToolbarController:
    def __init__(self, parent_Tk: tk.Tk, main_ui_controller: MainUIController) -> None:
        self.parent_Tk = parent_Tk
        self.main_ui_controller = main_ui_controller
        self.view = TopToolbarView(parent_Tk)

        self.setup_command()
        self.bind_shortcuts()

    def open_folder(self) -> None:
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.main_ui_controller.current_folder_path = folder_path

    def setup_command(self) -> None:
        self.view.file_menu.add_command(label="開啟資料夾", command=self.open_folder)
        self.view.file_menu.add_command(label="儲存標記點")

        self.view.edit_menu.add_command(label="OCR檢測", command=self.ocr_current_image)

    def ocr_current_image(self) -> None:
        self.main_ui_controller.ocr_current_image()

    def bind_shortcuts(self) -> None:
        # 快捷鍵需綁定在主窗口 (tk.Tk) 上，因為快捷鍵僅在當前焦點窗口中有效
        self.parent_Tk.bind("<Control-o>", self.handle_ocr_shortcut)

    def handle_ocr_shortcut(self, event) -> None:
        self.ocr_current_image()
