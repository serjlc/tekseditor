import tkinter as tk
from tkinter import filedialog, messagebox


class Menubar():
    def __init__(self, parent) -> None:

        # Default Font
        font_settings = ("ubuntu", 14)

        menubar = tk.Menu(parent.master, font=font_settings)
        parent.master.config(menu=menubar)

        # Dropdown Options
        file_dropdown = tk.Menu(menubar, font=font_settings, tearoff=0)
        file_dropdown.add_command(
            label="New File", accelerator="Ctrl+N", command=parent.new_file)
        file_dropdown.add_command(
            label="Open File", accelerator="Ctrl+O", command=parent.open_file)
        file_dropdown.add_command(
            label="Save", accelerator="Ctrl+S", command=parent.save_file)
        file_dropdown.add_command(
            label="Save As", accelerator="Ctrl+Shift+S", command=parent.save_as)
        file_dropdown.add_separator()
        file_dropdown.add_command(
            label="Exit", accelerator="Ctrl+Q", command=parent.master.destroy)
        menubar.add_cascade(label="File", menu=file_dropdown)

        edit_dropdown = tk.Menu(menubar, font=font_settings, tearoff=0)
        edit_dropdown.add_command(label="Undo", accelerator="Ctrl+Z")
        edit_dropdown.add_command(label="Redo", accelerator="Ctrl+Y")
        menubar.add_cascade(label="Edit", menu=edit_dropdown)

        help_dropdown = tk.Menu(menubar, font=font_settings, tearoff=0)
        help_dropdown.add_command(label="About", command=self.about_popup)
        help_dropdown.add_command(
            label="Release Notes", command=self.release_notes)

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


class Statusbar:
    def __init__(self, parent) -> None:

        font_settings = ("ubuntu", 10)

        self.status = tk.StringVar()
        self.status.set("TeksEditor - 0.1 Seneca")

        label = tk.Label(parent.textarea, textvariable=self.status,
                         fg="black", bg="lightgrey", anchor='sw', font=font_settings)
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
        master.geometry("1200x700")

        # Default Font
        font_settings = ("ubuntu", 18)

        # File
        self.filename = None

        # Text Widget
        self.textarea = tk.Text(master, font=font_settings)

        # Allows text area scroll on Y axis
        self.scroll = tk.Scrollbar(master, command=self.textarea.yview)

        # Allows text area scroll with mousewheel
        self.textarea.configure(yscrollcommand=self.scroll.set)
        self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

        # Menu Bar
        self.menubar = Menubar(self)

        # Status Bar
        self.statusbar = Statusbar(self)

        # Enable Shortcuts
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
        self.filename = filedialog.askopenfilename(defaultextension=".txt", filetypes=[
                                                   ("All files", "*.*"), ("Text Files", "*.txt"), ("PDF File ", "*.pdf"), ("Python Scripts", "*.py"), ("Markdown Files", "*.md"), ("HTML Files", "*.html"), ("CSS Files", "*.css"), ("Javascript Files", "*.js")])
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

    def save_as(self, *args):
        """Choose file format/name and write it to a new file"""
        try:
            new_file = filedialog.asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[
                                                   ("All files", "*.*"), ("Text Files", "*.txt"), ("PDF File ", "*.pdf"), ("Python Scripts", "*.py"), ("Markdown Files", "*.md"), ("HTML Files", "*.html"), ("CSS Files", "*.css"), ("Javascript Files", "*.js")])
            textarea_content = self.textarea.get(1.0, tk.END)
            with open(new_file, "w") as f:
                f.write(textarea_content)
            self.statusbar.update_status(True)

            self.filename = new_file
            self.set_window_title(self.filename)
        except Exception as e:
            print(e)

    #def exit(self, *args):
        try:
            pass
        except Exception as e:
            print(e)

    def bind_shortcuts(self):
        self.textarea.bind('<Control-n>', self.new_file)
        self.textarea.bind('<Control-o>', self.open_file)
        self.textarea.bind('<Control-s>', self.save_file)
        self.textarea.bind('<Control-S>', self.save_as)
        self.textarea.bind('<Control-q>', self.exit)
        self.textarea.bind('<Key>', self.statusbar.update_status)


if __name__ == "__main__":
    master = tk.Tk()
    app = Teks(master)
    master.mainloop()
