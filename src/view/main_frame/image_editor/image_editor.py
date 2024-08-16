import tkinter as tk
import utilities.constants as Constants

from PIL import Image, ImageTk
from controller.view_controller.main_frame.image_editor.image_editor_controller import ImageEditorController
from view.main_frame.image_editor.box_drawer import BoxDrawer
from view.main_frame.image_info import ImageInfo


class ImageEditor:
    def __init__(self, parent: tk.Frame, image_info: ImageInfo, image_editor_controller: ImageEditorController) -> None:
        self.parent_frame = parent
        self.image_info = image_info
        self.image_editor_controller = image_editor_controller

        self.frame = tk.Frame(self.parent_frame, relief="groove", border=1)
        self.image_canvas = tk.Canvas(
            self.frame, width=Constants.CANVAS_BORDER_LENGTH, height=Constants.CANVAS_BORDER_LENGTH
        )
        self.image_canvas.pack(expand=True)

        self._image_path = ""
        self.box_drawer = BoxDrawer(self.image_canvas)     

    @property
    def current_image_path(self) -> str:
        return self._image_path

    @current_image_path.setter
    def current_image_path(self, new_image_path) -> None:
        self._image_path = new_image_path
        self.image_info.current_image_path = new_image_path
        self.display_image()

    def display_image(self) -> None:
        self.image_canvas.delete("all")

        image = Image.open(self.current_image_path)

        (
            self.new_width,
            self.new_height,
            self.width_ratio,
            self.height_ratio,
        ) = self.get_image_dimension(image)

        self.draw_image(image, self.new_width, self.new_height)
    
    def get_image_dimension(self, image: Image.Image):
        return self.image_editor_controller.calculate_image_dimension(image)

    def draw_image(self, image, new_width, new_height) -> None:
        self.image_canvas.config(width=new_width, height=new_height)
        resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(resized_image)

        self.image_canvas.delete("all")
        self.frame.update_idletasks()

        self.image_canvas.create_image(
            self.image_canvas.winfo_width() // 2,
            self.image_canvas.winfo_height() // 2,
            anchor="center",
            image=self.photo,
        )

    def ocr_current_image(self) -> None:
        self.image_info.ocr_current_image()
        self.image_editor_controller.current_boxes = self.image_info.current_boxes
        if self.current_image_path:
            self.box_drawer.draw(self.image_editor_controller.current_boxes, self.width_ratio, self.height_ratio)
