import os

from model.data_manager import DataManager


class DataController:
    def __init__(self) -> None:
        self.data_manager = DataManager()

    def load_jpg_files_in_folder(self, folder_path: str) -> list:
        if os.path.isdir(folder_path):
            self.data_manager.load_jpg_files_in_folder(folder_path)
            return self.data_manager.jpg_files
        else:
            return []
