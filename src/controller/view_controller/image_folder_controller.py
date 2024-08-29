import os
import tkinter as tk

from view.main_ui.image_folder_view import ImageFolderView


class ImageFolderController:
    def __init__(
        self,
        parent_frame: tk.Frame,
    ) -> None:
        self.parent_frame = parent_frame
        self.view = ImageFolderView(self.parent_frame)

        self._folder_path = ""
        self._image_list = []
        self._current_image_index = 0

    @property
    def folder_path(self):
        return self._folder_path

    @folder_path.setter
    def folder_path(self, new_folder_path):
        self._folder_path = new_folder_path
        self.update_folder_name()

    @property
    def image_list(self):
        return self._image_list

    @image_list.setter
    def image_list(self, new_image_list):
        self._image_list = new_image_list
        self.update_listbox()

    @property
    def current_image_index(self):
        return self._current_image_index

    @current_image_index.setter
    def current_image_index(self, new_cur_index):
        self._current_image_index = new_cur_index
        self.update_image_index()

    @property
    def image_count(self):
        return len(self.image_list)

    def update_folder_name(self):
        folder_basename = os.path.basename(os.path.normpath(self.folder_path))
        parent_folder_path = os.path.dirname(os.path.normpath(self.folder_path))
        parent_folder_basename = os.path.basename(parent_folder_path)

        combined_name = os.path.join(parent_folder_basename, folder_basename)
        self.view.folder_path_stringvar.set(combined_name + "\\")

    def update_image_index(self):
        self.view.index_stringvar.set(
            "{}/{}".format(self.current_image_index + 1, self.image_count)
        )

    def update_listbox(self):
        jpg_file_names = [os.path.basename(path) for path in self.image_list]

        self.view.listbox.delete(0, tk.END)
        self.view.listbox.insert(tk.END, *jpg_file_names)
