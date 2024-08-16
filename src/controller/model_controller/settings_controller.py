from model.setting_manager import SettingManager


class SettingsController:
    def __init__(self) -> None:
        self.model = SettingManager()

    @property
    def image_folder_path(self):
        return self.get_settings("image-folder-path")

    def get_settings(self, key: str):
        return self.model.get(key)

    def update_image_folder_path(self, image_folder_path):
        self.model.update_image_folder_path(image_folder_path)
