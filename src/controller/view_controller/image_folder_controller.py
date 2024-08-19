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
        self.current_image_index = 0

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

    def update_listbox(self):
        jpg_file_names = [os.path.basename(path) for path in self.image_list]
        self.view.update_listbox(jpg_file_names)

    def update_folder_name(self):
        folder_basename = os.path.basename(os.path.normpath(self.folder_path))
        self.view.update_folder_name(folder_basename)
