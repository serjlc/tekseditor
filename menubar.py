import tkinter as tk
from tkinter import messagebox


class Menubar():

    def __init__(self, parent):

        # Default Font
        default_font = ("ubuntu", 12)

        # Initialize the shortcuts
        self.bind_shortcuts(parent)

        # Menubar Setup
        menubar = tk.Menu(parent, font=default_font)
        parent.config(menu=menubar)

        # Dropdown Options
        file_dropdown = tk.Menu(menubar, font=default_font, tearoff=0)
        file_dropdown.add_command(label="New File",
                                  accelerator="Ctrl+N",
                                  command=parent._new_file)
        file_dropdown.add_command(label="Open File",
                                  accelerator="Ctrl+O",
                                  command=parent._open_file)
        file_dropdown.add_command(label="Save",
                                  accelerator="Ctrl+S",
                                  command=parent._save_file)
        file_dropdown.add_command(label="Save As",
                                  accelerator="Ctrl+Shift+S",
                                  command=parent._save_file_as)

        file_dropdown.add_separator()

        file_dropdown.add_command(label="Exit",
                                  accelerator="Ctrl+Q",
                                  command=parent._exit)
        menubar.add_cascade(label="File", menu=file_dropdown)

        edit_dropdown = tk.Menu(menubar, font=default_font, tearoff=0)
        edit_dropdown.add_command(
            label="Undo",
            accelerator="Ctrl+Z",
            command=lambda: parent.focus_get().event_generate('<<Undo>>'))
        edit_dropdown.add_command(
            label="Redo",
            accelerator="Ctrl+Y",
            command=lambda: parent.focus_get().event_generate('<<Redo>>'))
        edit_dropdown.add_command(
            label="Copy",
            accelerator="Ctrl+C",
            command=lambda: parent.focus_get().event_generate('<<Copy>>'))
        edit_dropdown.add_command(
            label="Cut",
            accelerator="Ctrl+X",
            command=lambda: parent.focus_get().event_generate('<<Cut>>'))
        edit_dropdown.add_command(
            label="Paste",
            accelerator="Ctrl+V",
            command=lambda: parent.focus_get().event_generate('<<Paste>>'))
        edit_dropdown.add_command(label="Select All",
                                  accelerator="Alt+A",
                                  command=parent.select_all)
        edit_dropdown.add_command(label="Clear Selection",
                                  accelerator="Alt+Shift+A",
                                  command=parent.clear_selection)

        menubar.add_cascade(label="Edit", menu=edit_dropdown)

        help_dropdown = tk.Menu(menubar, font=default_font, tearoff=0)
        help_dropdown.add_command(label="About", command=self.about_popup)
        help_dropdown.add_command(label="Release Notes",
                                  command=self.release_notes)

        menubar.add_cascade(label="Help", menu=help_dropdown)

    def bind_shortcuts(self, parent):
        """ These shortcuts act on the root = parent """

        parent.bind('<Control-n>', parent.new_file)
        parent.bind('<Control-o>', parent.open_file)
        parent.bind('<Control-s>', parent.save_file)
        parent.bind('<Control-S>', parent.save_as)
        parent.bind('<Control-q>', parent.exit)
        parent.bind('<Alt-a>', parent.select_all)
        parent.bind('<Alt-A>', parent.clear_selection)

    def about_popup(self):
        """Shows About section"""
        about_title = "About TeksEditor"
        about_message = "A simple text editor built with Python. Adapted from pymike00"
        messagebox.showinfo(about_title, about_message)

    def release_notes(self):
        """Shows release notes"""
        release_title = "Release Notes"
        release_message = "TeksEditor - 0.1 Seneca"
        messagebox.showinfo(release_title, release_message)
