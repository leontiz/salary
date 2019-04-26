import tkinter as tk
import tkinter.filedialog as filedialog

class App(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.string_label = tk.Label(master, text="File name: ")
        self.address_string = tk.Entry(master, width=50)
        self.open_button = tk.Button(master, text="Browse...", command=lambda: self.open_file())
        self.string_label.pack(side="left")
        self.address_string.pack(side="left")
        self.open_button.pack(side="right")

    def open_file(self):
        filename = filedialog.askopenfilename()
        self.address_string.insert(0, filename)

window = tk.Tk()
app = App(window)
app.mainloop()
