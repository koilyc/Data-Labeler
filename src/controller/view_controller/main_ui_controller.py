import tkinter as tk

from controller.model_controller.data_controller import DataController
from controller.model_controller.ocr_controller import OCRController
from controller.model_controller.settings_controller import SettingsController

from controller.view_controller.image_editor_controller import (
    ImageEditorController,
)
from controller.view_controller.image_folder_controller import (
    ImageFolderController,
)
from controller.view_controller.image_info_controller import ImageInfoController
from view.main_ui.main_ui_view import MainUIView


class MainUIController:
    def __init__(
        self,
        parent_Tk: tk.Tk,
        data_controller: DataController,
        ocr_controller: OCRController,
        settings_controller: SettingsController,
    ) -> None:
        self.parent_Tk = parent_Tk
        self.data_controller = data_controller
        self.ocr_controller = ocr_controller
        self.settings_controller = settings_controller

        self.view = MainUIView(parent_Tk)
        self.image_info_controller = ImageInfoController(self.view.frame)
        self.image_editor_controller = ImageEditorController(self.view.frame)
        self.image_folder_controller = ImageFolderController(self.view.frame)

        self.image_folder_controller.view.frame.grid(row=0, column=0, sticky="nsew")
        self.image_editor_controller.view.frame.grid(row=0, column=1, sticky="nsew")
        self.image_info_controller.view.frame.grid(row=0, column=2, sticky="nsew")

        self.current_image_index = 0
        self._current_folder_path = ""
        self._current_image_path = ""
        self.image_folder_controller.view.listbox.bind(
            "<<ListboxSelect>>", self.on_image_select
        )

        self.load_settings()
        self.bind_shortcuts()
        self.update_image_index()

    @property
    def current_folder_path(self):
        return self._current_folder_path

    @current_folder_path.setter
    def current_folder_path(self, new_folder_path):
        self._current_folder_path = new_folder_path
        self.image_folder_controller.folder_path = new_folder_path
        self.image_folder_controller.image_list = self.load_jpg_files_in_folder(
            new_folder_path
        )
        self.settings_controller.update_image_folder_path(new_folder_path)

    @property
    def current_image_path(self):
        return self._current_image_path

    @current_image_path.setter
    def current_image_path(self, new_image_path):
        self._current_image_path = new_image_path
        self.image_editor_controller.current_image_path = new_image_path
        self.image_info_controller.current_image_path = new_image_path

    # 這東西也許可以搬到別的module裡面去，但目前暫時先放這
    def on_image_select(self, event) -> None:
        if (
            self.image_folder_controller.view.listbox.size() > 0
            and self.image_folder_controller.view.listbox.curselection()
        ):
            self.current_image_index = (
                self.image_folder_controller.view.listbox.curselection()[0]
            )
            select_image = self.image_folder_controller.image_list[
                self.current_image_index
            ]
            self.current_image_path = select_image
            self.update_image_index()

    def update_image_index(self):
        self.image_folder_controller.update_image_index(self.current_image_index)

    def ocr_current_image(self):
        ocr_result = self.ocr_controller.run_model(self.current_image_path)
        if ocr_result:
            self.image_editor_controller.current_boxes = ocr_result["boxes"]
            self.image_editor_controller.draw_boxes()
            self.image_info_controller.current_boxes = ocr_result["boxes"]
            self.image_info_controller.current_texts = ocr_result["texts"]
            self.image_info_controller.current_scores = ocr_result["scores"]

    def load_jpg_files_in_folder(self, folder_path):
        return self.data_controller.load_jpg_files_in_folder(folder_path)

    def load_settings(self):
        self.load_image_folder_in_settings()

    def load_image_folder_in_settings(self):
        folder_path = str(self.settings_controller.image_folder_path)
        if folder_path:
            self.image_folder_controller.folder_path = folder_path
            self.image_folder_controller.image_list = (
                self.data_controller.load_jpg_files_in_folder(folder_path)
            )
        else:
            self.settings_controller.update_image_folder_path("")

    def bind_shortcuts(self) -> None:
        # 快捷鍵需綁定在主窗口 (tk.Tk) 上，因為快捷鍵僅在當前焦點窗口中有效
        self.parent_Tk.bind("<q>", self.handle_rotate_left_shortcut)
        self.parent_Tk.bind("<e>", self.handle_rotate_right_shortcut)

    def handle_rotate_left_shortcut(self, event) -> None:
        self.image_editor_controller.rotate_image(90)

    def handle_rotate_right_shortcut(self, event) -> None:
        self.image_editor_controller.rotate_image(270)
