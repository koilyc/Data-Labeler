import tkinter as tk


class ImageFolderView:
    def __init__(self, parent_frame: tk.Frame) -> None:
        self.parent_frame = parent_frame
        self.folder_path_stringvar = tk.StringVar()

        self.setup_ui()

    def setup_ui(self) -> None:
        self.frame = tk.Frame(self.parent_frame, relief="groove", border=1)
        self.folder_path_label = tk.Label(
            self.frame, textvariable=self.folder_path_stringvar, anchor="w"
        )
        self.folder_path_label.pack(fill=tk.X)
        self.listbox = tk.Listbox(self.frame)
        self.listbox.pack(fill=tk.BOTH, expand=True)

    def update_folder_name(self, folder_basename: str):
        self.folder_path_stringvar.set(folder_basename + "/")

    def update_listbox(self, jpg_file_names: list) -> None:
        self.listbox.delete(0, tk.END)
        self.listbox.insert(tk.END, *jpg_file_names)
        self.current_image_index = 0
