import utilities.constants as Constants

from PIL import Image


class ImageEditorController:
    def __init__(self) -> None:
       self._boxes = []
    
    @property
    def current_boxes(self):
        return self._boxes

    @current_boxes.setter
    def current_boxes(self, new_boxes):
        self._boxes = new_boxes
    
    def calculate_image_dimension(self, image: Image.Image) -> tuple:
        canvas_width = Constants.CANVAS_BORDER_LENGTH
        canvas_height = Constants.CANVAS_BORDER_LENGTH
        image_ratio = image.width / image.height
        canvas_ratio = canvas_width / canvas_height

        if image_ratio > canvas_ratio:
            new_width = canvas_width
            new_height = int(canvas_width / image_ratio)
            width_ratio = new_width / image.width
            height_ratio = width_ratio
        else:
            new_height = canvas_height
            new_width = int(canvas_height * image_ratio)
            height_ratio = new_height / image.height
            width_ratio = height_ratio

        return new_width, new_height, width_ratio, height_ratio