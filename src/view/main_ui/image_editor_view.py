import tkinter as tk
import utilities.constants as Constants

from PIL import Image, ImageTk


class ImageEditorView:
    def __init__(
        self,
        parent_frame: tk.Frame,
    ) -> None:
        self.parent_frame = parent_frame

        self.frame = tk.Frame(self.parent_frame, relief="groove", border=1, padx=5, pady=5)
        self.image_canvas = tk.Canvas(
            self.frame,
            width=Constants.CANVAS_BORDER_LENGTH,
            height=Constants.CANVAS_BORDER_LENGTH,
        )
        self.image_canvas.pack(expand=True)

        self._image_path = ""

    def display_image(self, image: Image.Image, new_width, new_height) -> None:
        self.image_canvas.delete("all")

        self.draw_image(image, new_width, new_height)

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
