import tkinter as tk

from controller.ocr_controller import OCRController


class ImageInfo:
    def __init__(self, parent: tk.Frame, ocr_controller: OCRController) -> None:
        self.parent_frame = parent
        self.ocr_controller = ocr_controller

        self._image_path = ""
        self._image_info = {"boxes": [], "texts": [], "scores": []}

        self.frame = tk.Frame(self.parent_frame, relief="groove", border=1)
        self.texts_name_label = tk.Label(self.frame, anchor="w", text="Texts")
        self.texts_name_label.pack(fill=tk.X)
        self.texts_listbox = tk.Listbox(self.frame)
        self.texts_listbox.pack(fill=tk.BOTH, expand=True)
        self.boxes_name_label = tk.Label(self.frame, anchor="w", text="Boxes")
        self.boxes_name_label.pack(fill=tk.X)
        self.boxes_listbox = tk.Listbox(self.frame)
        self.boxes_listbox.pack(fill=tk.BOTH, expand=True)

    @property
    def current_image_path(self) -> str:
        return self._image_path

    @current_image_path.setter
    def current_image_path(self, new_image_path) -> None:
        self._image_path = new_image_path
        self._image_info = {"boxes": [], "texts": [], "scores": []}
        self.update_boxes_listbox()
        self.update_texts_listbox()

    @property
    def current_boxes(self):
        return self._image_info["boxes"]

    @current_boxes.setter
    def current_boxes(self, new_boxes):
        self._image_info["boxes"] = new_boxes
        self.update_boxes_listbox()

    @property
    def current_texts(self):
        return self._image_info["texts"]

    @current_texts.setter
    def current_texts(self, new_texts):
        self._image_info["texts"] = new_texts
        self.update_texts_listbox()

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

    def update_texts_listbox(self) -> None:
        self.texts_listbox.delete(0, tk.END)
        self.texts_listbox.insert(tk.END, *self.current_texts)

    def update_boxes_listbox(self) -> None:
        self.boxes_listbox.delete(0, tk.END)
        self.boxes_listbox.insert(tk.END, *self.current_boxes)
