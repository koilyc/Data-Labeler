import os
import threading
import tkinter as tk

from tkinter import ttk
from controller.model_controller.data_controller import DataController
from controller.model_controller.ocr_controller import OCRController
from controller.model_controller.settings_controller import SettingsController
from controller.model_controller.tools_controller import ToolsController
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
        tools_controller: ToolsController,
    ) -> None:
        self.parent_Tk = parent_Tk
        self.data_controller = data_controller
        self.ocr_controller = ocr_controller
        self.settings_controller = settings_controller
        self.tools_controller = tools_controller

        self.view = MainUIView(parent_Tk)
        self.image_info_controller = ImageInfoController(self.view.frame)
        self.image_editor_controller = ImageEditorController(self.view.frame)
        self.image_folder_controller = ImageFolderController(self.view.frame)

        self.image_folder_controller.view.frame.grid(row=0, column=0, sticky="nsew")
        self.image_editor_controller.view.frame.grid(row=0, column=1, sticky="nsew")
        self.image_info_controller.view.frame.grid(row=0, column=2, sticky="nsew")

        self._current_image_index = 0
        self._current_folder_path = ""
        self._current_image_path = ""
        self.image_folder_controller.view.listbox.bind(
            "<<ListboxSelect>>", self.on_image_select
        )

        self.load_settings()
        self.bind_shortcuts()
        self.update_image_index()

    @property
    def current_image_index(self):
        return self._current_image_index

    @current_image_index.setter
    def current_image_index(self, new_index):
        self._current_image_index = new_index
        self.update_image_index()

    @property
    def current_folder_path(self):
        return self._current_folder_path

    @current_folder_path.setter
    def current_folder_path(self, new_folder_path):
        self._current_folder_path = new_folder_path
        self.update_folder_path()

    @property
    def current_image_path(self):
        return self._current_image_path

    @current_image_path.setter
    def current_image_path(self, new_image_path):
        self._current_image_path = new_image_path
        self.update_image_path()

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
            self.show_image_info()

    # 更新路徑和圖片資訊
    def update_image_index(self):
        self.image_folder_controller.current_image_index = self.current_image_index

    def update_folder_path(self):
        self.image_folder_controller.folder_path = self.current_folder_path
        self.image_folder_controller.image_list = (
            self.data_controller.load_jpg_files_in_folder(self.current_folder_path)
        )
        self.all_ocr_results = [
            {"boxes": [], "texts": [], "scores": []}
            for _ in range(len(self.image_folder_controller.image_list))
        ]
        self.settings_controller.update_image_folder_path(self.current_folder_path)

    def update_image_path(self):
        self.image_editor_controller.current_image_path = self.current_image_path
        self.image_info_controller.current_image_path = self.current_image_path

    # 更新圖片資訊
    def show_image_info(self) -> None:
        if self.all_ocr_results[self.current_image_index]["boxes"]:
            # 在editor中畫出外框
            self.image_editor_controller.current_boxes = self.all_ocr_results[
                self.current_image_index
            ]["boxes"]
            self.image_editor_controller.draw_boxes()
            # 更新info中的圖片資訊
            self.image_info_controller.current_boxes = self.all_ocr_results[
                self.current_image_index
            ]["boxes"]
            self.image_info_controller.current_texts = self.all_ocr_results[
                self.current_image_index
            ]["texts"]
            self.image_info_controller.current_scores = self.all_ocr_results[
                self.current_image_index
            ]["scores"]

    # 載入設定檔資訊
    def load_settings(self):
        self.load_image_folder_in_settings()
        self.load_model_in_settings()

    def load_image_folder_in_settings(self):
        folder_path = str(self.settings_controller.image_folder_path)
        if folder_path:
            self.current_folder_path = folder_path
        else:
            self.settings_controller.update_image_folder_path("")

    def load_model_in_settings(self):
        det_model_path = str(self.settings_controller.det_model_path)
        rec_model_path = str(self.settings_controller.rec_model_path)
        if det_model_path and rec_model_path:
            self.ocr_controller.current_model_dir = {
                "det": det_model_path,
                "rec": rec_model_path,
            }
        else:
            self.settings_controller.update_det_model_path("")
            self.settings_controller.update_rec_model_path("")
        
        self.image_info_controller.view.det_model_stringvar.set(f"det: {os.path.basename(det_model_path)}")
        self.image_info_controller.view.rec_model_stringvar.set(f"rec: {os.path.basename(rec_model_path)}")

    # 綁定快捷鍵
    def bind_shortcuts(self) -> None:
        # 快捷鍵需綁定在主窗口 (tk.Tk) 上，因為快捷鍵僅在當前焦點窗口中有效
        self.parent_Tk.bind("<q>", self.handle_rotate_left_shortcut)
        self.parent_Tk.bind("<e>", self.handle_rotate_right_shortcut)
        self.parent_Tk.bind("<p>", self.handle_set_image_pass_shortcut)
        self.parent_Tk.bind("<o>", self.handle_set_image_ng_shortcut)

    def handle_rotate_left_shortcut(self, event) -> None:
        self.image_editor_controller.rotate_image(90)

    def handle_rotate_right_shortcut(self, event) -> None:
        self.image_editor_controller.rotate_image(270)

    def handle_set_image_pass(self) -> None:
        self.image_info_controller.set_image_reuslt("Pass")
        self.current_image_path = self.image_info_controller.current_image_path
        self.update_folder_path()
        self.current_image_index = 0
        self.current_image_path = self.image_folder_controller.image_list[
            self.current_image_index
        ]
        self.show_image_info()

    def handle_set_image_pass_shortcut(self, event) -> None:
        self.handle_set_image_pass()

    def handld_set_image_ng(self) -> None:
        self.image_info_controller.set_image_reuslt("NG")
        self.current_image_path = self.image_info_controller.current_image_path
        self.update_folder_path()
        self.current_image_index = 0
        self.current_image_path = self.image_folder_controller.image_list[
            self.current_image_index
        ]
        self.show_image_info()

    def handle_set_image_ng_shortcut(self, event) -> None:
        self.handld_set_image_ng()

    # OCR操作
    def ocr_current_image(self):
        ocr_result = self.ocr_controller.run_model(self.current_image_path)
        if ocr_result:
            self.all_ocr_results[self.current_image_index] = ocr_result
            self.show_image_info()

    def ocr_all_images(self):
        for index, image in enumerate(self.image_folder_controller.image_list):
            result = self.ocr_controller.run_model(image)
            if result:
                self.all_ocr_results[index] = result

            percentage = int(((index + 1) / len(self.all_ocr_results)) * 100)

            self.ocr_progress_bar["value"] = index + 1
            self.image_name_stringvar.set(f"Progress: {percentage}%")
            self.ocr_progress_toplevel.update_idletasks()

        self.show_image_info()

        self.ocr_progress_toplevel.destroy()

    def show_ocr_progress(self):
        screen_width = self.parent_Tk.winfo_screenwidth()
        screen_height = self.parent_Tk.winfo_screenheight()

        window_width = 300
        window_height = 50

        position_right = int(screen_width / 2 - window_width / 2)
        position_down = int(screen_height / 2 - window_height / 2)

        self.ocr_progress_toplevel = tk.Toplevel(self.parent_Tk)
        self.ocr_progress_toplevel.title("OCR Progress")
        self.ocr_progress_toplevel.geometry(
            f"{window_width}x{window_height}+{position_right}+{position_down}"
        )
        self.ocr_progress_toplevel.resizable(False, False)
        self.ocr_progress_toplevel.focus_set()

        self.ocr_progress_bar = ttk.Progressbar(
            self.ocr_progress_toplevel,
            orient="horizontal",
            length=window_width,
            mode="determinate",
        )
        self.ocr_progress_bar.pack(padx=2)
        self.ocr_progress_bar["maximum"] = len(self.all_ocr_results)

        self.image_name_stringvar = tk.StringVar()
        self.ocr_progress_name = tk.Label(
            self.ocr_progress_toplevel, textvariable=self.image_name_stringvar
        )
        self.ocr_progress_name.pack(padx=2)

        threading.Thread(target=self.ocr_all_images).start()

    # 小工具功能
    def replace_in_filenames(self):
        self.tools_controller.show_replace_in_filenames(self.current_folder_path)

    def evaluate(self):
        golden = os.path.basename(self.current_folder_path)
        good = 0
        for result in self.all_ocr_results:
            texts = result["texts"]
            for text in texts:
                if text.find(golden) != -1:
                    good += 1

        self.image_info_controller.view.good_result_stringvar.set(
            f"{good}/{self.image_folder_controller.image_count}\tAccaracy: {int(good*100/self.image_folder_controller.image_count)}%"
        )
    
    def output_ocr_results(self) -> None:
        self.tools_controller.output_ocr_results(self.all_ocr_results)
