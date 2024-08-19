import tkinter as tk

from view.main_ui.image_info_view import ImageInfoView


class ImageInfoController:
    def __init__(self, parent_frame: tk.Frame) -> None:
        self.parent_frame = parent_frame
        self.view = ImageInfoView(self.parent_frame)

        self._current_image_path = ""
        self.reset_image_info()

    @property
    def current_image_path(self) -> str:
        return self._current_image_path

    @current_image_path.setter
    def current_image_path(self, new_image_path) -> None:
        self._current_image_path = new_image_path
        self.reset_image_info()
        self.view.update_boxes_listbox(self.current_boxes)
        self.view.update_texts_listbox(self.current_texts)

    @property
    def current_boxes(self):
        return self._current_boxes

    @current_boxes.setter
    def current_boxes(self, new_boxes):
        self._current_boxes = new_boxes
        self.view.update_boxes_listbox(self.current_boxes)

    @property
    def current_texts(self):
        return self._current_texts

    @current_texts.setter
    def current_texts(self, new_texts):
        self._current_texts = new_texts
        self.view.update_texts_listbox(self.current_texts)

    @property
    def current_scores(self):
        return self._current_scores

    @current_scores.setter
    def current_scores(self, new_scores):
        self._current_scores = new_scores

    def reset_image_info(self):
        self._current_boxes = []
        self._current_texts = []
        self._current_scores = []
