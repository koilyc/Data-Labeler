import tkinter as tk


class ImageInfoView:
    def __init__(self, parent: tk.Frame) -> None:
        self.parent_frame = parent

        self.frame = tk.Frame(self.parent_frame, relief="groove", border=1)
        self.texts_name_label = tk.Label(self.frame, anchor="w", text="Texts")
        self.texts_name_label.pack(fill=tk.X)
        self.texts_listbox = tk.Listbox(self.frame)
        self.texts_listbox.pack(fill=tk.BOTH, expand=True)
        self.boxes_name_label = tk.Label(self.frame, anchor="w", text="Boxes")
        self.boxes_name_label.pack(fill=tk.X)
        self.boxes_listbox = tk.Listbox(self.frame)
        self.boxes_listbox.pack(fill=tk.BOTH, expand=True)

    def update_texts_listbox(self, texts: list) -> None:
        self.texts_listbox.delete(0, tk.END)
        self.texts_listbox.insert(tk.END, *texts)

    def update_boxes_listbox(self, boxes: list) -> None:
        self.boxes_listbox.delete(0, tk.END)
        self.boxes_listbox.insert(tk.END, *boxes)
