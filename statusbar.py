import tkinter as tk
from tkinter import (filedialog, messagebox)


class Statusbar():
    """  Create a Statusbar at the bottom of textarea """

    def __init__(self, parent) -> None:
        # parent is root = tk.TK

        default_font = ("ubuntu", 10)

        self.status = tk.StringVar()
        self.status.set("TeksEditor - 0.1 Seneca")

        self.label = tk.Label(parent.textarea,
                              textvariable=self.status,
                              fg="black",
                              bg="lightgrey",
                              anchor='sw',
                              font=default_font)
        self.label.pack(side=tk.BOTTOM, fill=tk.BOTH)

    def update_status(self, *args):
        """ Show colored status bar upon different values"""
        if args[0] == 0:
            self.label["fg"] = "green"
            self.status.set("TeksEditor - Unsaved file")
        elif args[0] == 1:
            self.label["fg"] = "blue"
            self.status.set("TeksEditor - File saved ")
        elif args[0] == 2:
            self.label["fg"] = "red"
            self.status.set("* Modified file")
