import os

from model.ocr_model import OCRModel


class OCRController:
    def __init__(self) -> None:
        self.model = OCRModel()
        self._current_model_lang = "en"
        self._current_model_dir = {"det": None, "rec": None}

    @property
    def current_model_lang(self) -> str:
        return self._current_model_lang

    @current_model_lang.setter
    def current_model_lang(self, new_lang) -> None:
        self._current_model_lang = new_lang
        self.change_model(new_lang, self.current_model_dir)

    @property
    def current_model_dir(self) -> dict:
        return self._current_model_dir

    @current_model_dir.setter
    def current_model_dir(self, new_dir: dict):
        self._current_model_dir = new_dir
        self.change_model(self.current_model_lang, new_dir)

    def change_model(self, lang="en", model_dir={"det": None, "rec": None}):
        self.model.setup_model(lang, model_dir)

    def run_model(self, image_path) -> dict:
        if not os.path.isfile(image_path):
            return {}
        try:
            self.model.run(image_path)
            return {
                "boxes": self.model.recognition_boxes,
                "texts": self.model.recognition_texts,
                "scores": self.model.recognition_scores,
            }
        except Exception as e:
            print(f"Error loading files: {e}")
            return {}
