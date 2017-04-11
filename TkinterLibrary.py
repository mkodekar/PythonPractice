#!/usr/bin/python
from tkinter import *


# before running this file please install python3-tk
# on ubuntu sudo apt-get install python3-tk

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_windows()

    def init_windows(self):
        self.master.title('Gui')
        self.pack(fill=BOTH, expand=1)
        exampleButton = Button(self, text="quit", command=self.client_exit)
        exampleButton.place(x=5, y=10)

    def client_exit(self):
        exit()


root = Tk()
root.geometry("400x300")

app = Window(root)

root.mainloop()
