import tkinter as tk

TOOLBAR_BUTTON_WIDTH = 5
TOOLBAR_BUTTON_PADDING_X = 2


class TopToolbarView:
    def __init__(self, parent_Tk: tk.Tk) -> None:
        self.parent_Tk = parent_Tk

        self.frame = tk.Frame(self.parent_Tk)

        self.setup_toolbar_button()
        self.setup_menu()

    def setup_toolbar_button(self) -> None:
        self.file_button = tk.Button(
            self.frame,
            text="檔案",
            width=TOOLBAR_BUTTON_WIDTH,
            command=lambda: self.display_menu(self.file_button, self.file_menu),
        )
        self.file_button.pack(side=tk.LEFT, padx=TOOLBAR_BUTTON_PADDING_X)

        self.model_button = tk.Button(
            self.frame,
            text="模型",
            width=TOOLBAR_BUTTON_WIDTH,
            command=lambda: self.display_menu(self.model_button, self.model_menu),
        )
        self.model_button.pack(side=tk.LEFT, padx=TOOLBAR_BUTTON_PADDING_X)

    def display_menu(self, target_button: tk.Button, target_menu: tk.Menu) -> None:
        button_x = target_button.winfo_rootx()
        button_y = target_button.winfo_rooty() + target_button.winfo_height()
        target_menu.post(button_x, button_y)

    def setup_menu(self) -> None:
        self.setup_file_menu()
        self.setup_model_menu()

    def setup_file_menu(self) -> None:
        self.file_menu = tk.Menu(self.frame, tearoff=0)

    def setup_model_menu(self) -> None:
        self.model_menu = tk.Menu(self.frame, tearoff=0)
