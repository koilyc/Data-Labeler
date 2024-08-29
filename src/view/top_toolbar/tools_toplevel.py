import tkinter as tk

TEXT_FONT = ("Arial", 10)


class ToolsToplevel:
    def __init__(self, parent_Tk: tk.Tk) -> None:
        self.parent_Tk = parent_Tk

    def show_replace_in_filename_ui(self):
        self.rif_toplevel = tk.Toplevel(self.parent_Tk)
        self.rif_toplevel.title("Replace Filename")
        self.rif_toplevel.geometry("200x100")
        self.rif_toplevel.resizable(False, False)
        self.rif_toplevel.focus_set()

        self.old_frame = tk.Frame(self.rif_toplevel)
        self.old_label = tk.Label(self.old_frame, text="Old")
        self.old_entry = tk.Entry(self.old_frame, font=TEXT_FONT)

        self.new_frame = tk.Frame(self.rif_toplevel)
        self.new_lable = tk.Label(self.new_frame, text="New")
        self.new_entry = tk.Entry(self.new_frame, font=TEXT_FONT)

        self.replace_button = tk.Button(self.rif_toplevel, text="Replace")

        self.pack_rif_components()

    def pack_rif_components(self):
        self.old_frame.pack(fill=tk.X)
        self.old_label.grid(column=0, row=0, sticky='w')
        self.old_entry.grid(column=1, row=0, sticky='e', padx=(0, 10))
        self.new_frame.pack(fill=tk.X)
        self.new_lable.grid(column=0, row=0, sticky='w')
        self.new_entry.grid(column=1, row=0, sticky='e', padx=(0, 10))
        self.replace_button.pack(anchor="e")