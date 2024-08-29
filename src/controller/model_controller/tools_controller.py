import tkinter as tk

from model.tools import Tools
from view.top_toolbar.tools_toplevel import ToolsToplevel


class ToolsController:
    def __init__(self, parent_Tk: tk.Tk) -> None:
        self.parent_Tk = parent_Tk
        self.tools = Tools()
        self.view = ToolsToplevel(self.parent_Tk)

    def show_replace_in_filenames(self, directory):
        self.current_folder_path = directory
        self.view.show_replace_in_filename_ui()
        self.view.replace_button.config(command=self.replace)

    def replace(self):
        self.tools.replace_in_filenames(
            self.current_folder_path,
            self.view.old_entry.get(),
            self.view.new_entry.get(),
        )
        self.view.rif_toplevel.destroy()
