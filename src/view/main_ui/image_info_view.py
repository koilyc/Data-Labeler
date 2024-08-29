import tkinter as tk


class ImageInfoView:
    def __init__(self, parent: tk.Frame) -> None:
        self.parent_frame = parent
        self.frame = tk.Frame(self.parent_frame, relief="groove", border=1)

        self.setup_texts_info()
        self.setup_boxes_info()
        self.setup_result_info()
        self.pack_components()

    def setup_texts_info(self):
        self.texts_name_label = tk.Label(self.frame, anchor="w", text="Texts")
        self.texts_listbox = tk.Listbox(self.frame)

    def setup_boxes_info(self):
        self.boxes_name_label = tk.Label(self.frame, anchor="w", text="Boxes")
        self.boxes_listbox = tk.Listbox(self.frame)

    def setup_result_info(self):
        self.result_eval_label = tk.Label(self.frame, anchor="w", text="Result")
        self.result_eval_frame = tk.Frame(self.frame)

    def pack_components(self):
        self.texts_name_label.pack(fill=tk.X)
        self.texts_listbox.pack(fill=tk.BOTH, expand=True)
        self.boxes_name_label.pack(fill=tk.X)
        self.boxes_listbox.pack(fill=tk.BOTH, expand=True)
        self.result_eval_label.pack(fill=tk.X)
        self.result_eval_frame.pack(fill=tk.BOTH)
