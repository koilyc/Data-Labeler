import tkinter as tk

RECOGNITION_BOXES_WIDTH = 2
RECOGNITION_BOXES_OUTLINE_COLOR = "green"


class BoxDrawer:
    def __init__(self, canvas: tk.Canvas) -> None:
        self.canvas = canvas

    def scale_points(self, points, width_ratio, height_ratio) -> list:
        return [(x * width_ratio, y * height_ratio) for x, y in points]

    def draw(self, boxes, width_ratio=1, height_ratio=1) -> None:
        for points in boxes:
            scaled_points = self.scale_points(points, width_ratio, height_ratio)
            self.draw_polygon(
                self.canvas,
                scaled_points,
                RECOGNITION_BOXES_WIDTH,
                RECOGNITION_BOXES_OUTLINE_COLOR,
            )

    def draw_polygon(
        self, canvas: tk.Canvas, points: list, width: int, outline_color: str
    ) -> None:
        canvas.create_polygon(*points, fill="", width=width, outline=outline_color)
