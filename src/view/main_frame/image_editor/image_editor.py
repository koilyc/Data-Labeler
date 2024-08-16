import tkinter as tk

from PIL import Image, ImageTk
from view.main_frame.image_editor.box_drawer import BoxDrawer
from view.main_frame.image_info import ImageInfo

CANVAS_BORDER_LENGTH = 600


class ImageEditor:
    def __init__(self, parent: tk.Frame, image_info: ImageInfo) -> None:
        self.parent_frame = parent
        self.image_info = image_info

        self.frame = tk.Frame(self.parent_frame, relief="groove", border=1)

        self._image_path = ""

        self.image_canvas = tk.Canvas(
            self.frame, width=CANVAS_BORDER_LENGTH, height=CANVAS_BORDER_LENGTH
        )
        self.image_canvas.pack(expand=True)

        self._boxes = []
        self.box_drawer = BoxDrawer(self.image_canvas)

        self._selection_mode = ""

    @property
    def current_image_path(self) -> str:
        return self._image_path

    @current_image_path.setter
    def current_image_path(self, new_image_path) -> None:
        self._image_path = new_image_path
        self.image_info.current_image_path = new_image_path
        self.current_boxes = []

    @property
    def current_boxes(self) -> list:
        return self._boxes

    @current_boxes.setter
    def current_boxes(self, new_boxes) -> None:
        self._boxes = new_boxes
        self.show_image()

    @property
    def selection_mode(self) -> str:
        return self._selection_mode

    @selection_mode.setter
    def selection_mode(self, new_mode: str) -> None:
        self._selection_mode = new_mode

    def show_image(self) -> None:
        self.image_canvas.delete("all")

        image = Image.open(self.current_image_path)

        (
            new_width,
            new_height,
            width_ratio,
            height_ratio,
        ) = self.calculate_image_dimension(image)

        self.draw_image(image, new_width, new_height)
        self.box_drawer.draw(self.current_boxes, width_ratio, height_ratio)

    def calculate_image_dimension(self, image: Image.Image) -> tuple:
        canvas_width = CANVAS_BORDER_LENGTH
        canvas_height = CANVAS_BORDER_LENGTH
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
        self.current_boxes = self.image_info.current_boxes

    # TODO:
    def select_rectangle_area(self):
        pass

    def select_freeform_area(self):
        pass
