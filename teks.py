#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk
from tkinter import (filedialog, messagebox)

from helpers import abspath
from functools import partial
from menubar import Menubar
from toolbar import Toolbar
from statusbar import Statusbar


class Teks(tk.Tk):
    """ Create a simple text editor"""

    # Inherit from tk.Tk so its like tk.Tk
    def __init__(self):
        super().__init__()

        # Configure title and geometry
        self.title("Untitled - TeksEditor")
        self.geometry("1200x700+350+150")

        # App Icon
        self.iconphoto(False, tk.PhotoImage(file='icons/app.png'))

        # Default Font
        default_font = ("ubuntu", 16)

        # File name
        self.filename = ""

        # Flags, warn if file not saved
        self.hasBeenSaved = False

        # Toolbar. Pass self=root to Statusbar
        Toolbar(self)

        # Text Widget
        self.textarea = tk.Text(self,
                                font=default_font,
                                undo=True,
                                bg="lavender",
                                selectbackground="yellow",
                                selectforeground="black")

        # Configure Scrollbar on textarea Y axis
        self.scroll = tk.Scrollbar(self, command=self.textarea.yview)

        # Add Scrollbar to textarea
        self.textarea.configure(yscrollcommand=self.scroll.set)
        self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

        # Statusbar. Pass self=root to Statusbar
        self.statusbar = Statusbar(self)

        # The edit_modified() method detects changes in the text widget.
        # If no modification sends 0 else 1
        # This value is passed to the statusbar, which acts accordingly
        self.textarea.bind(
            '<<Modified>>', lambda event: self.statusbar.update_status(
                self.textarea.edit_modified()))

        # Menubar
        Menubar(self)

    def set_window_title(self, name: str = "") -> None:
        """ If file exists, use its name. Otherwise leave as Untitled."""

        if name:
            self.title(f"{name} - TeksEditor")
        else:
            self.title("Untitled - TeksEditor")

    def new_file(self, event) -> None:
        """Grab and delete text from first character onwards and reset its name"""

        self.hasBeenSaved = False

        self.set_window_title()
        self.textarea.delete(1.0, tk.END)

    def open_file(self, event) -> None:
        """Prompt file browser and replace current opened file with the new selected file"""

        self.filename = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("All files", "*.*"), ("Text Files", "*.txt"),
                       ("Python Scripts", "*.py"), ("Markdown Files", "*.md"),
                       ("HTML Files", "*.html"), ("CSS Files", "*.css"),
                       ("Javascript Files", "*.js")])

        if self.filename:
            self.textarea.delete(1.0, tk.END)
            with open(self.filename, "r") as f:
                self.textarea.insert(1.0, f.read())

            self.set_window_title(self.filename)
        # This resets any modification and waits for the next one
        self.textarea.edit_modified(0)

    def save_file(self, event) -> None:
        """Grab text and write it to the current file. Otherwise prompt 'Save As'"""

        if self.filename:
            try:
                textarea_content = self.textarea.get(1.0, tk.END)
                with open(self.filename, "w") as f:
                    f.write(textarea_content)

                self.hasBeenSaved = True
                self.textarea.edit_modified(0)

            except Exception as e:
                print(e)
        else:
            self.save_as(event)

    def save_as(self, event) -> None:
        """Choose file format and name and write it to a new file"""
        try:
            new_file = filedialog.asksaveasfilename(
                initialfile="Untitled.txt",
                defaultextension=".txt",
                filetypes=[("All files", "*.*"), ("Text Files", "*.txt"),
                           ("Python Scripts", "*.py"),
                           ("Markdown Files", "*.md"),
                           ("HTML Files", "*.html"), ("CSS Files", "*.css"),
                           ("Javascript Files", "*.js")])

            textarea_content = self.textarea.get(1.0, tk.END)

            with open(new_file, "w") as f:
                f.write(textarea_content)

            self.filename = new_file
            self.set_window_title(self.filename)
            self.hasBeenSaved = True
            # This resets any modification and waits for the next one
            self.textarea.edit_modified(0)

        except Exception as e:
            print(e)

    def exit(self, event) -> None:
        """Exits program or prompts 'save as' option"""
        if self.hasBeenSaved:
            self.destroy()
        else:
            exit_title = "File not saved"
            exit_message = "Are you sure you want to leave without saving?"
            msg_box = messagebox.askquestion(exit_title, exit_message)
            if msg_box == 'no':
                self.save_as(event)
            else:
                self.destroy()

    # File and text formatting functions

    def select_all(self, *args) -> None:
        """Select all text"""
        self.textarea.tag_add('sel', '1.0', 'end')

    def clear_selection(self, *args) -> None:
        self.textarea.tag_remove('sel', '1.0', 'end')

    def bold_text(self) -> None:
        pass

    def _new_file(self) -> None:
        """ Method call with accelerator """
        try:
            event = None
            remove_event = partial(self.new_file(event))
            remove_event(event)
        except TypeError:
            pass

    def _open_file(self) -> None:
        """ Method call with accelerator """
        try:
            event = None
            remove_event = partial(self.open_file(event))
            remove_event(event)
        except TypeError:
            pass

    def _save_file(self) -> None:
        """ Method call with accelerator """
        try:
            event = None
            remove_event = partial(self.save_file(event))
            remove_event(event)
        except TypeError:
            pass

    def _save_file_as(self) -> None:
        """ Method call with accelerator """
        try:
            event = None
            remove_event = partial(self.save_as(event))
            remove_event(event)
        except TypeError:
            pass

    def _exit(self) -> None:
        """ Method call with accelerator """
        try:
            event = None
            remove_event = partial(self.exit(event))
            remove_event(event)
        except TypeError:
            pass


if __name__ == "__main__":
    root = Teks()
    root.mainloop()
