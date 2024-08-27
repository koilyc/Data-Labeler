import tkinter as tk

from tkinter import filedialog
from controller.view_controller.main_ui_controller import MainUIController
from view.top_toolbar.model_setting_toplevel import ModelSettingToplevel


class ModelSettingController:
    def __init__(self, parent_Tk: tk.Tk, main_ui_controller: MainUIController) -> None:
        self.parent_Tk = parent_Tk
        self.main_ui_controller = main_ui_controller
        
        self.model_setting_toplevel = ModelSettingToplevel(self.parent_Tk)

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