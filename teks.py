import tkinter as tk
from tkinter import (BOTH, FLAT, LEFT, RAISED, RIGHT, TOP, Button, E, W,
                     X, Y, filedialog, messagebox, font)

from PIL import Image, ImageTk


class Menubar():

    def __init__(self, parent) -> None:

        # Default Font
        font_settings = ("ubuntu", 12)

        # Menubar Setup
        menubar = tk.Menu(parent.master, font=font_settings)
        parent.master.config(menu=menubar)

        # Dropdown Options
        file_dropdown = tk.Menu(menubar, font=font_settings, tearoff=0)
        file_dropdown.add_command(label="New File",
                                  accelerator="Ctrl+N",
                                  command=parent.new_file)
        file_dropdown.add_command(label="Open File",
                                  accelerator="Ctrl+O",
                                  command=parent.open_file)
        file_dropdown.add_command(label="Save",
                                  accelerator="Ctrl+S",
                                  command=parent.save_file)
        file_dropdown.add_command(label="Save As",
                                  accelerator="Ctrl+Shift+S",
                                  command=parent.save_as)
        file_dropdown.add_separator()
        file_dropdown.add_command(label="Exit",
                                  accelerator="Ctrl+Q",
                                  command=parent.master.destroy)
        menubar.add_cascade(label="File", menu=file_dropdown)

        edit_dropdown = tk.Menu(menubar, font=font_settings, tearoff=0)
        edit_dropdown.add_command(label="Undo",
                                  accelerator="Ctrl+Z",
                                  command=lambda: parent.master.focus_get().
                                  event_generate('<<Undo>>'))
        edit_dropdown.add_command(label="Redo",
                                  accelerator="Ctrl+Y",
                                  command=lambda: parent.master.focus_get().
                                  event_generate('<<Redo>>'))
        edit_dropdown.add_command(label="Copy",
                                  accelerator="Ctrl+C",
                                  command=lambda: parent.master.focus_get().
                                  event_generate('<<Copy>>'))
        edit_dropdown.add_command(label="Cut",
                                  accelerator="Ctrl+X",
                                  command=lambda: parent.master.focus_get().
                                  event_generate('<<Cut>>'))
        edit_dropdown.add_command(label="Paste",
                                  accelerator="Ctrl+V",
                                  command=lambda: parent.master.focus_get().
                                  event_generate('<<Paste>>'))
        edit_dropdown.add_command(label="Select All",
                                  accelerator="Alt+A",
                                  command=parent.select_all)
        edit_dropdown.add_command(label="Clear Selection",
                                  accelerator="Alt+Shift+A", command=parent.clear_selection)

        menubar.add_cascade(label="Edit", menu=edit_dropdown)

        help_dropdown = tk.Menu(menubar, font=font_settings, tearoff=0)
        help_dropdown.add_command(label="About", command=self.about_popup)
        help_dropdown.add_command(label="Release Notes",
                                  command=self.release_notes)

        menubar.add_cascade(label="Help", menu=help_dropdown)

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


class Toolbar():

    def __init__(self, parent) -> None:

        # Default Font
        font_settings = ("ubuntu", 12)

        # Toolbar Setup
        toolbar = tk.Frame(parent.master, bd=1, relief=RAISED, bg='red')
        toolbar.pack(fill=X)

        # Bold Option
        self.img = Image.open("icons/bold.png")
        bold_icon = ImageTk.PhotoImage(self.img)
        bold_button = Button(toolbar, image=bold_icon, relief=FLAT,
                             command=parent.bold_text)
        bold_button.image = bold_icon
        bold_button.grid(row=0, column=0, sticky=E)

        # Italics Option

        # Underline Option


class Statusbar():

    def __init__(self, parent) -> None:

        font_settings = ("ubuntu", 10)

        self.status = tk.StringVar()
        self.status.set("TeksEditor - 0.1 Seneca")

        label = tk.Label(parent.textarea,
                         textvariable=self.status,
                         fg="black",
                         bg="lightgrey",
                         anchor='sw',
                         font=font_settings)
        label.pack(side=tk.BOTTOM, fill=tk.BOTH)

    def update_status(self, *args):
        """If instanced, check whether arg 0 is True or False to update status accordingly"""
        if isinstance(args[0], bool):
            self.status.set("File saved successfully")
        else:
            self.status.set("TeksEditor - 0.1 Seneca")


class Teks():

    def __init__(self, master) -> None:

        # Master Window
        self.master = master
        master.title("Untitled - TeksEditor")
        master.geometry("1200x700+350+150")

        # App Icon
        master.iconphoto(False, tk.PhotoImage(file='icons/app.png'))

        # Default Font
        font_settings = ("ubuntu", 18)

        # File
        self.filename = None
        self.hasBeenSaved = False

        # Text Widget
        self.textarea = tk.Text(master, font=font_settings, undo=True,
                                selectbackground="yellow", selectforeground="black")

        # Allows text area scroll on Y axis
        self.scroll = tk.Scrollbar(master, command=self.textarea.yview)

        # Allows text area scroll with mousewheel
        self.textarea.configure(yscrollcommand=self.scroll.set)
        self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

        # Menubar
        self.menubar = Menubar(self)

        # Toolbar
        self.toolbar = Toolbar(self)

        # Statusbar
        self.statusbar = Statusbar(self)

        # Enable general shortcuts
        self.bind_shortcuts()

    def set_window_title(self, name=None):
        """ If file exists, use its name. Otherwise leave as Untitled."""
        if name:
            self.master.title(name + " - TeksEditor")
        else:
            self.master.title("Untitled - TeksEditor")

    def new_file(self, *args):
        """Grab and delete text from first character onwards and reset its name"""
        self.textarea.delete(1.0, tk.END)
        self.filename = None
        self.set_window_title()

    def open_file(self, *args):
        """Prompt file browser and replace current opened file with the new selected file"""
        self.filename = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("All files", "*.*"), ("Text Files", "*.txt"),
                       ("PDF File ", "*.pdf"), ("Python Scripts", "*.py"),
                       ("Markdown Files", "*.md"), ("HTML Files", "*.html"),
                       ("CSS Files", "*.css"), ("Javascript Files", "*.js")])
        if self.filename:
            self.textarea.delete(1.0, tk.END)
            with open(self.filename, "r") as f:
                self.textarea.insert(1.0, f.read())
            self.set_window_title(self.filename)

    def save_file(self, *args):
        """Grab text and write it to the current file. Otherwise prompt 'Save As'"""
        if self.filename:
            try:
                textarea_content = self.textarea.get(1.0, tk.END)
                with open(self.filename, "w") as f:
                    f.write(textarea_content)
                self.statusbar.update_status(True)
            except Exception as e:
                print(e)
        else:
            self.save_as()

        # Whether the file has been saved or not. Used for exit pop up warning
        self.hasBeenSaved = True

    def save_as(self, *args):
        """Choose file format and name and write it to a new file"""
        try:
            new_file = filedialog.asksaveasfilename(
                initialfile="Untitled.txt",
                defaultextension=".txt",
                filetypes=[("All files", "*.*"), ("Text Files", "*.txt"),
                           ("PDF File ", "*.pdf"), ("Python Scripts", "*.py"),
                           ("Markdown Files", "*.md"),
                           ("HTML Files", "*.html"), ("CSS Files", "*.css"),
                           ("Javascript Files", "*.js")])
            textarea_content = self.textarea.get(1.0, tk.END)
            with open(new_file, "w") as f:
                f.write(textarea_content)
            self.statusbar.update_status(True)

            self.filename = new_file
            self.set_window_title(self.filename)
        except Exception as e:
            print(e)

    def exit(self, *args):
        """Exits program or prompts 'save as' option"""
        if self.hasBeenSaved:
            master.destroy()
        else:
            exit_title = "File not saved"
            exit_message = "Are you sure you want to leave without saving?"
            msg_box = messagebox.askquestion(exit_title, exit_message)
            if msg_box == 'no':
                self.save_as()
            else:
                master.destroy()

    # Text selection and formatting functions

    def select_all(self, *args):
        """Select all text"""
        self.textarea.tag_add('sel', '1.0', 'end')

    def clear_selection(self, *args):
        """Clears text selection"""
        self.textarea.tag_remove('sel', '1.0', 'end')

    def bold_text(self, *args):
        "Format text as bold"

        # Create the bold font
        bold_font = font.Font(self.textarea, self.textarea.cget("font"))
        bold_font.configure(weight="bold")

        # Define current tags
        self.current_tags = self.textarea.tag_names("sel.first")

        # Configure the tag
        self.textarea.tag_configure("bold", font=bold_font)

        # Checks if tag has been set
        if "bold" in self.current_tags:
            self.textarea.tag_remove("bold", "sel.first", "sel.last")
        else:
            self.textarea.tag_add("bold", "sel.first", "sel.last")

    def italics_text(self, *args):
        "Format text as italics"

        # Create the italic font
        italics_font = font.Font(self.textarea, self.textarea.cget("font"))
        italics_font.configure(slant="italic")

        # Define current tags
        current_tags = self.textarea.tag_names("sel.first")

        # Configure the tag
        self.textarea.tag_configure("italics", font=italics_font)

        # Checks if tag has been set
        if "italics" in current_tags:
            self.textarea.tag_remove("italics", "sel.first", "sel.last")
        else:
            self.textarea.tag_add("italics", "sel.first", "sel.last")

    def bind_shortcuts(self):
        self.textarea.bind('<Control-n>', self.new_file)
        self.textarea.bind('<Control-o>', self.open_file)
        self.textarea.bind('<Control-s>', self.save_file)
        self.textarea.bind('<Control-S>', self.save_as)
        self.textarea.bind('<Control-q>', self.exit)
        self.textarea.bind('<Alt-a>', self.select_all)
        self.textarea.bind('<Alt-A>', self.clear_selection)

        self.textarea.bind('<Key>', self.statusbar.update_status)


if __name__ == "__main__":
    master = tk.Tk()
    Teks(master)
    master.mainloop()
