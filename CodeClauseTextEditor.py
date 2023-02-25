import tkinter as tk
from tkinter import filedialog

class TextEditor:
    def __init__(self, master):
        self.master = master
        master.title(" Purush Text Editor")

        self.textarea = tk.Text(self.master, undo=True)
        self.textarea.pack(fill=tk.BOTH, expand=1)

        self.menubar = tk.Menu(self.master)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New", command=self.new_file)
        self.filemenu.add_command(label="Open", command=self.open_file)
        self.filemenu.add_command(label="Save", command=self.save_file)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.master.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.editmenu = tk.Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Undo", command=self.textarea.edit_undo)
        self.editmenu.add_command(label="Redo", command=self.textarea.edit_redo)
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)

        self.master.config(menu=self.menubar)

    def new_file(self):
        self.textarea.delete("1.0", tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as file:
                self.textarea.delete("1.0", tk.END)
                self.textarea.insert("1.0", file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename()
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.textarea.get("1.0", tk.END))

root = tk.Tk()
text_editor = TextEditor(root)
root.mainloop()
