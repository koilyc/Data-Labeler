import os


class DataManager:
    def __init__(self) -> None:
        self._jpg_files: list[str] = []

    @property
    def jpg_files(self) -> list:
        return self._jpg_files

    def load_jpg_files_in_folder(self, folder_path) -> None:
        if not os.path.isdir(folder_path):
            raise ValueError(f"Path {folder_path} is not a valid directory.")

        self._jpg_files = [
            os.path.join(folder_path, file)
            for file in os.listdir(folder_path)
            if file.lower().endswith(".jpg")
        ]
