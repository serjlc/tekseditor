import tkinter as tk
from tkinter import (LEFT, TOP, X, messagebox, PhotoImage)
from helpers import abspath


class Toolbar():

    def __init__(self, parent):

        # Default Font
        # default_font = ("ubuntu", 12)

        # Toolbar Setup
        toolbar = tk.Frame(parent, bd=1)
        toolbar.pack(side=TOP, fill=X)

        # Buttons
        image_path = abspath("icons/bold.png", ".")
        self.img = PhotoImage(file=image_path)

        bold_button = tk.Button(toolbar,
                                  image=self.img,
                                  compound=LEFT,
                                  command=self.btn_clicked)
        bold_button.pack(side=LEFT, padx=2, pady=2)

        image_path = abspath("icons/italics.png", ".")
        self.img2 = PhotoImage(file=image_path)

        bold_button = tk.Button(toolbar,
                                  image=self.img2,
                                  compound=LEFT,
                                  command=self.btn_clicked)
        bold_button.pack(side=LEFT, padx=2, pady=2)


        tk.Label(toolbar, image=self.img).pack(side=LEFT, padx=2, pady=2)

    def btn_clicked(self):
        messagebox.showinfo("Info", "Wrench button")

        # Italics Option

        # Underline Option
