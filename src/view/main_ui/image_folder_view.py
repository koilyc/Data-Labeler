import tkinter as tk


class ImageFolderView:
    def __init__(self, parent_frame: tk.Frame) -> None:
        self.parent_frame = parent_frame
        self.folder_path_stringvar = tk.StringVar()
        self.index_stringvar = tk.StringVar()

        self.setup_folder()
        self.pack_components()

    def setup_folder(self) -> None:
        self.frame = tk.Frame(self.parent_frame, relief="groove", border=1)
        self.folder_path_label = tk.Label(
            self.frame, textvariable=self.folder_path_stringvar, anchor="w"
        )
        self.listbox = tk.Listbox(self.frame)
        self.index_label = tk.Label(
            self.frame, textvariable=self.index_stringvar, anchor="e"
        )

    def pack_components(self):
        self.folder_path_label.pack(fill=tk.X)
        self.listbox.pack(fill=tk.BOTH, expand=True)
        self.index_label.pack(fill=tk.X)
