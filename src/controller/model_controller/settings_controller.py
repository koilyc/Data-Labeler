from model.settings_manager import SettingManager


class SettingsController:
    def __init__(self) -> None:
        self.model = SettingManager()

    @property
    def image_folder_path(self):
        return self.model.get_image_folder_path()

    @property
    def det_model_path(self):
        return self.model.get_det_model_path()

    @property
    def rec_model_path(self):
        return self.model.get_rec_model_path()

    def get_settings(self, key: str):
        return self.model.get(key)

    def update_image_folder_path(self, image_folder_path):
        self.model.update_settings_path("image-folder-path", image_folder_path)

    def update_det_model_path(self, det_model_path):
        self.model.update_settings_path("det-model-path", det_model_path)

    def update_rec_model_path(self, rec_model_path):
        self.model.update_settings_path("rec-model-path", rec_model_path)
