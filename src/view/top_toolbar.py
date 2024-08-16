import tkinter as tk
import utilities.constants as Constants

from tkinter import filedialog
from controller.view_controller.main_frame_controller import MainFrameController

TOOLBAR_BUTTON_WIDTH = 5
TOOLBAR_BUTTON_PADDING_X = 2


class TopToolbar:
    def __init__(
        self, parent: tk.Tk, main_frame_controller: MainFrameController
    ) -> None:
        self.parent_frame = parent
        self.main_frame_controller = main_frame_controller

        self.frame = tk.Frame(self.parent_frame)

        self.bind_shortcuts()
        self.manage_button()
        self.initialize_file_management_menu()
        self.initialize_edit_menu()

    def manage_button(self) -> None:
        self.file_management_button = tk.Button(
            self.frame,
            text="Folder",
            width=TOOLBAR_BUTTON_WIDTH,
            command=lambda: self.display_menu(
                self.file_management_button, self.file_management_menu
            ),
        )
        self.file_management_button.pack(side=tk.LEFT, padx=TOOLBAR_BUTTON_PADDING_X)

        self.edit_button = tk.Button(
            self.frame,
            text="Edit",
            width=TOOLBAR_BUTTON_WIDTH,
            command=lambda: self.display_menu(self.edit_button, self.edit_menu),
        )
        self.edit_button.pack(side=tk.LEFT, padx=TOOLBAR_BUTTON_PADDING_X)

    def bind_shortcuts(self):
        # 快捷鍵需綁定在主窗口 (tk.Tk) 上，因為快捷鍵僅在當前焦點窗口中有效
        self.parent_frame.bind("<Control-o>", self.handle_ocr_shortcut)

    def display_menu(self, target_button: tk.Button, target_menu: tk.Menu) -> None:
        button_x = target_button.winfo_rootx()
        button_y = target_button.winfo_rooty() + target_button.winfo_height()
        target_menu.post(button_x, button_y)

    def initialize_file_management_menu(self) -> None:
        self.file_management_menu = tk.Menu(self.frame, tearoff=0)
        self.file_management_menu.add_command(label="開啟資料夾", command=self.open_folder)
        self.file_management_menu.add_command(label="儲存標記點")

    def initialize_edit_menu(self) -> None:
        self.edit_menu = tk.Menu(self.frame, tearoff=0)
        self.edit_menu.add_command(label="OCR檢測", command=self.image_ocr)

    def open_folder(self) -> None:
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.main_frame_controller.image_folder.folder_path = folder_path

    def handle_ocr_shortcut(self, event) -> None:
        self.image_ocr()

    def image_ocr(self) -> None:
        self.main_frame_controller.image_editor.ocr_current_image()

    def enable_rectangle_selection_mode(self) -> None:
        self.main_frame_controller.image_editor.selection_mode = (
            Constants.SELECTION_RECTANGLE_MODE
        )

    def enable_freeform_selection_mode(self) -> None:
        self.main_frame_controller.image_editor.selection_mode = (
            Constants.SELECTION_FREEFORM_MODE
        )
