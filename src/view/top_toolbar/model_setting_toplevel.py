import tkinter as tk

from tkinter import filedialog
from controller.view_controller.main_ui_controller import MainUIController


class ModelSettingToplevel:
    def __init__(self, parent_Tk: tk.Tk, main_ui_controller: MainUIController) -> None:
        self.parent_Tk = parent_Tk
        self.main_ui_controller = main_ui_controller
        self.current_lang = ""
        self.current_det_model = None
        self.current_rec_model = None
        self.lang_options = ["en", "ch", "chinese_cht"]

    def show_toplevel(self):
        self.top_level = tk.Toplevel(self.parent_Tk)
        self.top_level.title("Model Setting")
        self.top_level.geometry("300x400")
        self.top_level.resizable(False, False)
        self.top_level.focus_set()

        text_font = ("Arial", 10)

        model_lang_frame = tk.Frame(self.top_level)
        model_lang_frame.pack(padx=5, pady=5, fill=tk.X)
        model_lang_label = tk.Label(model_lang_frame, text="Language")
        model_lang_label.pack(anchor="w")
        self.selected_option = tk.StringVar(value=self.lang_options[0])
        self.current_lang = self.selected_option.get()
        self.model_lang_option_menu = tk.OptionMenu(
            model_lang_frame, self.selected_option, *self.lang_options
        )
        self.model_lang_option_menu.pack(fill=tk.X)

        det_model_frame = tk.Frame(self.top_level)
        det_model_frame.pack(padx=5, pady=5, fill=tk.X)
        det_model_label = tk.Label(det_model_frame, text="Detection Model")
        det_model_label.pack(anchor="w")
        self.det_model_text = tk.Text(det_model_frame, height=1, font=text_font)
        self.det_model_text.pack(fill=tk.X)
        self.det_model_button = tk.Button(
            det_model_frame, text="Browse", command=self.choose_det_model_folder_path
        )
        self.det_model_button.pack(anchor="e")

        rec_model_frame = tk.Frame(self.top_level)
        rec_model_frame.pack(padx=5, pady=5, fill=tk.X)
        rec_model_label = tk.Label(rec_model_frame, text="Recognition Model")
        rec_model_label.pack(anchor="w")
        self.rec_model_text = tk.Text(rec_model_frame, height=1, font=text_font)
        self.rec_model_text.pack(fill=tk.X)
        self.rec_model_button = tk.Button(
            rec_model_frame, text="Browse", command=self.choose_rec_model_folder_path
        )
        self.rec_model_button.pack(anchor="e")

        self.button_frame = tk.Frame(self.top_level)
        self.button_frame.pack(padx=5, pady=5, anchor='e')
        confirm_button = tk.Button(self.button_frame, text="Confirm", command=self.confirm)
        confirm_button.grid(padx=2, column=0, row=0)
        cancel_button = tk.Button(self.button_frame, text="Cancel", command=self.cancel)
        cancel_button.grid(padx=2, column=1, row=0)

    def choose_det_model_folder_path(self):
        folder_path = filedialog.askdirectory()
        self.top_level.focus_set()
        if folder_path:
            self.det_model_text.delete("1.0", tk.END)
            self.det_model_text.insert(tk.END, folder_path)
            self.current_det_model = folder_path

    def choose_rec_model_folder_path(self):
        folder_path = filedialog.askdirectory()
        self.top_level.focus_set()
        if folder_path:
            self.rec_model_text.delete("1.0", tk.END)
            self.rec_model_text.insert(tk.END, folder_path)
            self.current_rec_model = folder_path

    def confirm(self):
        selected_model = {'det': self.current_det_model, 'rec': self.current_rec_model}
        self.main_ui_controller.ocr_controller.change_model(self.current_lang, selected_model)
        self.main_ui_controller.settings_controller.update_det_model_path(self.current_det_model)
        self.main_ui_controller.settings_controller.update_rec_model_path(self.current_rec_model)
        self.top_level.destroy()

    def cancel(self):
        self.current_det_model = None
        self.current_rec_model = None
        self.top_level.destroy()
