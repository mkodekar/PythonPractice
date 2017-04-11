#!/usr/bin/python
from tkinter import *


class MainMenuWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_windows()

    def init_windows(self):
        self.master.title("Main menu example")
        self.pack(fill=BOTH, expand=1)
        menu = Menu(self)
        self.master.config(menu=menu)
        file = Menu(menu)
        file.add_command(label='Save')
        file.add_command(label="exit", command=self.client_exit)
        menu.add_cascade(label='File', menu=file)
        file2 = Menu(menu)
        file2.add_command(label='Here is an edit menu', command=self.client_exit)
        menu.add_cascade(label='Edit', menu=file2)

    def client_exit(self):
        exit()


root = Tk()
root.geometry("540x430")
app = MainMenuWindow(root)
root.mainloop()
