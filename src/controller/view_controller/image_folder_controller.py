import os
import tkinter as tk

from controller.model_controller.data_controller import DataController
from controller.model_controller.settings_controller import SettingsController
from controller.view_controller.image_editor_controller import ImageEditorController
from view.main_ui.image_folder_view import ImageFolderView


class ImageFolderController:
    def __init__(
        self,
        parent_frame: tk.Frame,
        data_controller: DataController,
        settings_controller: SettingsController,
        image_editor_controller: ImageEditorController,
    ) -> None:
        self.parent_frame = parent_frame
        self.view = ImageFolderView(self.parent_frame)

        self.data_controller = data_controller
        self.settings_controller = settings_controller
        self.image_editor_controller = image_editor_controller

        self._folder_path = ""
        self._image_list = []
        self.current_image_index = 0

        self.reload_image_folder()

        self.view.listbox.bind("<<ListboxSelect>>", self.on_image_select)

    @property
    def folder_path(self):
        return self._folder_path

    @folder_path.setter
    def folder_path(self, new_folder_path):
        self._folder_path = new_folder_path
        self.update_folder_name()

        self.image_list = self.load_jpg_files_in_folder(new_folder_path)
        self.settings_controller.update_image_folder_path(new_folder_path)

    @property
    def image_list(self):
        return self._image_list

    @image_list.setter
    def image_list(self, new_image_list):
        self._image_list = new_image_list
        self.update_listbox()

    def on_image_select(self, event) -> None:
        if self.view.listbox.size() > 0 and self.view.listbox.curselection():
            self.current_image_index = self.view.listbox.curselection()[0]
            select_image = self.image_list[self.current_image_index]
            self.image_editor_controller.current_image_path = select_image

    def update_listbox(self):
        jpg_file_names = [os.path.basename(path) for path in self.image_list]
        self.view.update_listbox(jpg_file_names)

    def update_folder_name(self):
        folder_basename = os.path.basename(os.path.normpath(self.folder_path))
        self.view.update_folder_name(folder_basename)

    def load_jpg_files_in_folder(self, folder_path):
        return self.data_controller.load_jpg_files_in_folder(folder_path)

    def reload_image_folder(self):
        self.folder_path = str(self.settings_controller.image_folder_path)
        self.image_list = self.data_controller.load_jpg_files_in_folder(
            self.folder_path
        )
