import os

from model.ocr_model import OCRModel


class OCRController:
    def __init__(self) -> None:
        self.model = OCRModel()

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
