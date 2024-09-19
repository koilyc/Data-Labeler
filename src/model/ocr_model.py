import os

from paddleocr import PaddleOCR


class OCRModel:
    def __init__(self) -> None:
        self.model = PaddleOCR(use_angle_cls=True, lang="en", show_log=False)

        self._recognition_boxes = []
        self._recognition_texts = []
        self._recognition_scores = []

    @property
    def recognition_boxes(self):
        return self._recognition_boxes

    @property
    def recognition_texts(self):
        return self._recognition_texts

    @property
    def recognition_scores(self):
        return self._recognition_scores

    def setup_model(self, lang, model_dir):
        print("Setup model...")
        self.model = PaddleOCR(
            use_angle_cls=True,
            lang=lang,
            det_model_dir=model_dir["det"],
            rec_model_dir=model_dir["rec"],
        )
        print("Done!")

    def run(self, image_path) -> None:
        if not os.path.isfile(image_path):
            raise ValueError(f"Path {image_path} is not a valid image.")

        recognition_result = self.model.ocr(image_path, cls=True)[0]

        if recognition_result:
            self._recognition_boxes = [line[0] for line in recognition_result]
            self._recognition_texts = [line[1][0] for line in recognition_result]
            self._recognition_scores = [line[1][1] for line in recognition_result]
        else:
            self._recognition_boxes = []
            self._recognition_texts = []
            self._recognition_scores = []
