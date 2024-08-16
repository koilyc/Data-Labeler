import os
import tkinter as tk

from controller.data_controller import DataController
from controller.settings_controller import SettingsController
from view.main_frame.image_editor.image_editor import ImageEditor


class ImageFolder:
    def __init__(
        self,
        parent: tk.Frame,
        image_editor: ImageEditor,
        data_controller: DataController,
        settings_controller: SettingsController,
    ) -> None:
        self.parent_frame = parent
        self.image_editor = image_editor
        self.data_controller = data_controller
        self.settings_controller = settings_controller

        self.folder_path_stringvar = tk.StringVar()

        self._folder_path = ""
        self._image_list = []
        self.current_image_index = 0

        self.setup_ui()
        self.reload_image_folder()

    def setup_ui(self) -> None:
        self.frame = tk.Frame(self.parent_frame, relief="groove", border=1)
        self.folder_path_label = tk.Label(
            self.frame, textvariable=self.folder_path_stringvar, anchor="w"
        )
        self.folder_path_label.pack(fill=tk.X)
        self.listbox = tk.Listbox(self.frame)
        self.listbox.pack(fill=tk.BOTH, expand=True)
        self.listbox.bind("<<ListboxSelect>>", self.on_image_select)

    @property
    def image_list(self) -> list:
        return self._image_list

    @image_list.setter
    def image_list(self, new_list: list) -> None:
        self._image_list = new_list
        self.update_listbox()

    @property
    def folder_path(self) -> str:
        return self._folder_path

    @folder_path.setter
    def folder_path(self, new_folder_path) -> None:
        self._folder_path = new_folder_path
        self.image_list = self.load_jpg_files_in_folder(new_folder_path)
        self.update_folder_name()
        self.settings_controller.update_image_folder_path(new_folder_path)

    def reload_image_folder(self):
        self.folder_path = str(self.settings_controller.image_folder_path)
        self.image_list = self.data_controller.load_jpg_files_in_folder(
            self.folder_path
        )

    def update_folder_name(self):
        folder_basename = os.path.basename(os.path.normpath(self.folder_path))
        self.folder_path_stringvar.set(folder_basename)

    def on_image_select(self, event) -> None:
        if self.listbox.size() > 0 and self.listbox.curselection():
            self.current_image_index = self.listbox.curselection()[0]
            select_image = self.image_list[self.current_image_index]
            self.image_editor.current_image_path = select_image

    def update_listbox(self) -> None:
        jpg_file_names = [os.path.basename(path) for path in self.image_list]
        self.listbox.delete(0, tk.END)
        self.listbox.insert(tk.END, *jpg_file_names)
        self.current_image_index = 0

    def load_jpg_files_in_folder(self, folder_path):
        return self.data_controller.load_jpg_files_in_folder(folder_path)
