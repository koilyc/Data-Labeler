import tkinter as tk

from tkinter import filedialog


class ModelSettingToplevel:
    def __init__(self, parent_Tk: tk.Tk) -> None:
        self.parent_Tk = parent_Tk
        self.lang_options = ["en", "ch", "chinese_cht"]

    def show_toplevel(self):
        self.top_level = tk.Toplevel(self.parent_Tk)
        self.top_level.title("模型設定")
        self.top_level.geometry("300x400")
        self.top_level.resizable(False, False)
        self.top_level.focus_set()

        text_font = ("Arial", 10)

        model_lang_frame = tk.Frame(self.top_level)
        model_lang_frame.pack(padx=5, pady=5, fill=tk.X)
        model_lang_label = tk.Label(model_lang_frame, text="檢測語言")
        model_lang_label.pack(anchor="w")
        self.selected_option = tk.StringVar(value=self.lang_options[0])
        self.model_lang_option_menu = tk.OptionMenu(
            model_lang_frame, self.selected_option, *self.lang_options
        )
        self.model_lang_option_menu.pack(fill=tk.X)

        det_model_frame = tk.Frame(self.top_level)
        det_model_frame.pack(padx=5, pady=5, fill=tk.X)
        det_model_label = tk.Label(det_model_frame, text="檢測模型")
        det_model_label.pack(anchor="w")
        self.det_model_text = tk.Text(det_model_frame, height=1, font=text_font)
        self.det_model_text.pack(fill=tk.X)
        self.det_model_button = tk.Button(
            det_model_frame, text="瀏覽", command=self.choose_det_model_folder_path
        )
        self.det_model_button.pack(anchor="e")

        rec_model_frame = tk.Frame(self.top_level)
        rec_model_frame.pack(padx=5, pady=5, fill=tk.X)
        rec_model_label = tk.Label(rec_model_frame, text="辨識模型")
        rec_model_label.pack(anchor="w")
        self.rec_model_text = tk.Text(rec_model_frame, height=1, font=text_font)
        self.rec_model_text.pack(fill=tk.X)
        self.rec_model_button = tk.Button(
            rec_model_frame, text="瀏覽", command=self.choose_rec_model_folder_path
        )
        self.rec_model_button.pack(anchor="e")

    def choose_det_model_folder_path(self):
        folder_path = filedialog.askdirectory()
        self.top_level.focus_set()
        if folder_path:
            self.det_model_text.delete("1.0", tk.END)
            self.det_model_text.insert(tk.END, folder_path)

    def choose_rec_model_folder_path(self):
        folder_path = filedialog.askdirectory()
        self.top_level.focus_set()
        if folder_path:
            self.rec_model_text.delete("1.0", tk.END)
            self.rec_model_text.insert(tk.END, folder_path)
