import json


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

    def update_image_folder_path(self, new_folder_path):
        self.settings["image-folder-path"] = new_folder_path
        self.save_settings()
