import tkinter as tk

TOOLBAR_BUTTON_WIDTH = 5
TOOLBAR_BUTTON_PADDING_X = 2


class TopToolbarView:
    def __init__(self, parent_Tk: tk.Tk) -> None:
        self.parent_Tk = parent_Tk
        self.frame = tk.Frame(self.parent_Tk)

        self.setup_button()
        self.setup_menu()

    # 工具列按鈕
    def setup_button(self) -> None:
        self.file_button = tk.Button(
            self.frame,
            text="File",
            width=TOOLBAR_BUTTON_WIDTH,
            command=lambda: self.display_menu(self.file_button, self.file_menu),
        )
        
        self.model_button = tk.Button(
            self.frame,
            text="Model",
            width=TOOLBAR_BUTTON_WIDTH,
            command=lambda: self.display_menu(self.model_button, self.model_menu),
        )

        self.pack_button()

    def pack_button(self) -> None:
        self.file_button.pack(side=tk.LEFT)
        self.model_button.pack(side=tk.LEFT)
    
    # 下拉式選單
    def setup_menu(self) -> None:
        self.setup_file_menu()
        self.setup_model_menu()

    def setup_file_menu(self) -> None:
        self.file_menu = tk.Menu(self.frame, tearoff=0)

    def setup_model_menu(self) -> None:
        self.model_menu = tk.Menu(self.frame, tearoff=0)

    def display_menu(self, target_button: tk.Button, target_menu: tk.Menu) -> None:
        button_x = target_button.winfo_rootx()
        button_y = target_button.winfo_rooty() + target_button.winfo_height()
        target_menu.post(button_x, button_y)
