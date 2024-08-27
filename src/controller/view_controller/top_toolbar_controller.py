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

    # Model setting面板控制
    # TODO: 寫一個controller專門做這件事0
    def show_setting_model(self) -> None:
        self.model_setting_toplevel.show_toplevel()
        self.setup_model_setting_button()

    def choose_det_model_folder_path(self):
        folder_path = filedialog.askdirectory()
        self.model_setting_toplevel.top_level.focus_set()
        if folder_path:
            self.model_setting_toplevel.det_model_text.delete("1.0", tk.END)
            self.model_setting_toplevel.det_model_text.insert(tk.END, folder_path)
            self.current_det_model = folder_path

    def choose_rec_model_folder_path(self):
        folder_path = filedialog.askdirectory()
        self.model_setting_toplevel.top_level.focus_set()
        if folder_path:
            self.model_setting_toplevel.rec_model_text.delete("1.0", tk.END)
            self.model_setting_toplevel.rec_model_text.insert(tk.END, folder_path)
            self.current_rec_model = folder_path

    def confirm(self):
        selected_model = {"det": self.current_det_model, "rec": self.current_rec_model}
        self.main_ui_controller.ocr_controller.change_model(
            self.model_setting_toplevel.current_lang, selected_model
        )
        self.main_ui_controller.settings_controller.update_det_model_path(
            self.model_setting_toplevel.current_det_model
        )
        self.main_ui_controller.settings_controller.update_rec_model_path(
            self.model_setting_toplevel.current_rec_model
        )
        self.model_setting_toplevel.top_level.destroy()

    def cancel(self):
        self.current_det_model = None
        self.current_rec_model = None
        self.model_setting_toplevel.top_level.destroy()

    def setup_model_setting_button(self):
        self.model_setting_toplevel.det_model_button.config(
            command=self.choose_det_model_folder_path
        )
        self.model_setting_toplevel.rec_model_button.config(
            command=self.choose_rec_model_folder_path
        )
        self.model_setting_toplevel.confirm_button.config(command=self.confirm)
        self.model_setting_toplevel.cancel_button.config(command=self.cancel)
