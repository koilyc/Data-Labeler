import tkinter as tk
import utilities.constants as Constants

from PIL import Image

from view.main_ui.image_editor.box_drawer_view import BoxDrawer
from view.main_ui.image_editor_view import ImageEditorView


class ImageEditorController:
    def __init__(self, parent_frame: tk.Frame) -> None:
        self.parent_frame = parent_frame
        self.view = ImageEditorView(self.parent_frame)
        self.box_drawer = BoxDrawer(self.view.image_canvas)

        self._boxes = []
        self._current_image_path = ""

    @property
    def current_boxes(self):
        return self._boxes

    @current_boxes.setter
    def current_boxes(self, new_boxes):
        self._boxes = new_boxes

    @property
    def current_image_path(self):
        return self._current_image_path

    @current_image_path.setter
    def current_image_path(self, new_image_path):
        self._current_image_path = new_image_path
        self.current_image = self.get_image_from_path(new_image_path)
        self.display_new_image()

    def display_new_image(self):
        self.calculate_image_dimension(self.current_image)
        self.view.display_image(self.current_image, self.new_width, self.new_height)

    def get_image_from_path(self, image_path: str) -> Image.Image:
        image = Image.open(image_path)
        return image

    def calculate_image_dimension(self, image: Image.Image):
        canvas_width = Constants.CANVAS_BORDER_LENGTH
        canvas_height = Constants.CANVAS_BORDER_LENGTH
        image_ratio = image.width / image.height
        canvas_ratio = canvas_width / canvas_height

        if image_ratio > canvas_ratio:
            self.new_width = canvas_width
            self.new_height = int(canvas_width / image_ratio)
            self.width_ratio = self.new_width / image.width
            self.height_ratio = self.width_ratio
        else:
            self.new_height = canvas_height
            self.new_width = int(canvas_height * image_ratio)
            self.height_ratio = self.new_height / image.height
            self.width_ratio = self.height_ratio

    def draw_boxes(self):
        self.box_drawer.draw(
            self.current_boxes,
            self.width_ratio,
            self.height_ratio,
        )

    def rotate_image(self, degrees):
        self.current_image = self.current_image.rotate(degrees, expand=True)
        self.display_new_image()
        self.save_image()

    def save_image(self):
        self.current_image.save(self.current_image_path)
