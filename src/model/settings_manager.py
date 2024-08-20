import json
import os


class SettingManager:
    def __init__(self) -> None:
        self.file_path = "./src/configs/settings.json"
        self.settings = self.load_settings()

    def load_settings(self):
        with open(self.file_path, "r") as settings_file:
            return json.load(settings_file)

    def save_settings(self):
        with open(self.file_path, "w") as settings_file:
            json.dump(self.settings, settings_file, indent=4)

    def get(self, key: str, default=None):
        keys = key.split(".")
        value = self.settings
        for k in keys:
            value = value.get(k, default)
        return value

    def update_settings_path(self, id: str, new_path: str) -> None:
        self.settings[id] = new_path
        self.save_settings()

    def get_image_folder_path(self) -> str:
        folder_path = self.get("image-folder-path")
        if os.path.isdir(folder_path):
            return folder_path
        else:
            return ""

    def get_det_model_path(self) -> str:
        model_path = self.get("det-model-path")
        if os.path.isdir(model_path):
            return model_path
        else:
            return ""

    def get_rec_model_path(self) -> str:
        model_path = self.get("rec-model-path")
        if os.path.isdir(model_path):
            return model_path
        else:
            return ""
