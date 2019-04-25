import tkinter as tk
import tkinter.filedialog as dialog
from openpyxl import Workbook, load_workbook

# Code to add widgets will go here...

class Reader():
    def __init__(self, filename):
        wb = load_workbook(filename)


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.path_string_title = tk.Label(window, text="File name: ", height=1)
        # self.path_string_title.grid()
        self.path_string = tk.Entry(window, width=50)
        # self.path_string.grid()
        self.open_file = tk.Button(window, text="Browse...", command=lambda: self.select_file())
        # self.open_file.grid()
        self.pack()
        self.path_string_title.pack(side="left")
        self.path_string.pack(side="left")
        self.open_file.pack(side="left")

    def select_file(self):
        filename = dialog.askopenfilename()
        self.path_string.insert(0, filename)

window = tk.Tk()
app = App(master=window)
app.mainloop()
