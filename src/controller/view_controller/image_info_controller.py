import tkinter as tk

from controller.model_controller.ocr_controller import OCRController
from view.main_ui.image_info_view import ImageInfoView


class ImageInfoController:
    def __init__(self, parent_frame: tk.Frame, ocr_controller: OCRController) -> None:
        self.parent_frame = parent_frame
        self.ocr_controller = ocr_controller
        self.view = ImageInfoView(self.parent_frame)

        self._current_image_path = ""
        self._image_info = {"boxes": [], "texts": [], "scores": []}

    @property
    def current_image_path(self) -> str:
        return self._current_image_path

    @current_image_path.setter
    def current_image_path(self, new_image_path) -> None:
        self._current_image_path = new_image_path
        self._image_info = {"boxes": [], "texts": [], "scores": []}
        self.view.update_boxes_listbox(self.current_boxes)
        self.view.update_texts_listbox(self.current_texts)

    @property
    def current_boxes(self):
        return self._image_info["boxes"]

    @current_boxes.setter
    def current_boxes(self, new_boxes):
        self._image_info["boxes"] = new_boxes
        self.view.update_boxes_listbox(self.current_boxes)

    @property
    def current_texts(self):
        return self._image_info["texts"]

    @current_texts.setter
    def current_texts(self, new_texts):
        self._image_info["texts"] = new_texts
        self.view.update_texts_listbox(self.current_texts)

    @property
    def current_scores(self):
        return self._image_info["scores"]

    @current_scores.setter
    def current_scores(self, new_scores):
        self._image_info["scores"] = new_scores

    def ocr_current_image(self) -> None:
        ocr_result = self.ocr_controller.run_model(self.current_image_path)
        if ocr_result:
            self.current_boxes = ocr_result["boxes"]
            self.current_texts = ocr_result["texts"]
            self.current_scores = ocr_result["scores"]
