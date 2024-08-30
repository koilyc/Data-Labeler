import tkinter as tk

TEXT_FONT = ("Arial", 10)


class ModelSettingToplevel:
    def __init__(self, parent_Tk: tk.Tk) -> None:
        self.parent_Tk = parent_Tk
        self.current_lang = ""
        self.top_level: tk.Toplevel

        self.lang_options = ["en", "ch", "chinese_cht"]
        self.current_det_model = ""
        self.current_rec_model = ""

    def show_ui(self):
        self.show_toplevel()

        self.setup_model_lang_frame()
        self.setup_det_model_frame()
        self.setup_rec_model_frame()
        self.setup_button()

        self.pack_components()

    def show_toplevel(self):
        self.top_level = tk.Toplevel(self.parent_Tk)
        self.top_level.title("Model Setting")
        self.top_level.geometry("300x400")
        self.top_level.resizable(False, False)
        self.top_level.focus_set()

    def setup_model_lang_frame(self):
        self.model_lang_frame = tk.Frame(self.top_level)
        self.model_lang_label = tk.Label(self.model_lang_frame, text="Language")
        self.selected_option = tk.StringVar(value=self.lang_options[0])
        self.current_lang = self.selected_option.get()
        self.model_lang_option_menu = tk.OptionMenu(
            self.model_lang_frame, self.selected_option, *self.lang_options
        )

    def setup_det_model_frame(self):
        self.det_model_frame = tk.Frame(self.top_level)
        self.det_model_label = tk.Label(self.det_model_frame, text="Detection Model")
        self.det_model_entry = tk.Entry(self.det_model_frame, font=TEXT_FONT)
        self.det_model_button = tk.Button(self.det_model_frame, text="Browse")

    def setup_rec_model_frame(self):
        self.rec_model_frame = tk.Frame(self.top_level)
        self.rec_model_label = tk.Label(self.rec_model_frame, text="Recognition Model")
        self.rec_model_entry = tk.Entry(self.rec_model_frame, font=TEXT_FONT)
        self.rec_model_button = tk.Button(self.rec_model_frame, text="Browse")

    def setup_button(self):
        self.button_frame = tk.Frame(self.top_level)
        self.confirm_button = tk.Button(self.button_frame, text="Confirm")
        self.cancel_button = tk.Button(self.button_frame, text="Cancel")

    def pack_components(self):
        self.model_lang_frame.pack(padx=5, pady=5, fill=tk.X)
        self.model_lang_label.pack(anchor="w")
        self.model_lang_option_menu.pack(fill=tk.X)

        self.det_model_frame.pack(padx=5, pady=5, fill=tk.X)
        self.det_model_label.pack(anchor="w")
        self.det_model_entry.pack(fill=tk.X)
        self.det_model_button.pack(anchor="e")

        self.rec_model_frame.pack(padx=5, pady=5, fill=tk.X)
        self.rec_model_label.pack(anchor="w")
        self.rec_model_entry.pack(fill=tk.X)
        self.rec_model_button.pack(anchor="e")

        self.button_frame.pack(padx=5, pady=5, anchor="e")
        self.confirm_button.grid(padx=2, column=0, row=0)
        self.cancel_button.grid(padx=2, column=1, row=0)
