from tkinter import *
from PIL import Image, ImageTk


class PythonImageing(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_windows()

    def init_windows(self):
        self.master.title("Image Processing")
        self.pack(fill=BOTH, expand=1)
        menu = Menu(self)
        self.master.config(menu=menu)
        file = Menu(menu)
        file.add_command(label='Show Image', command=self.showImage)
        file.add_command(label="Show Text", command=self.showText)
        menu.add_cascade(label='File', menu=file)

    def showImage(self):
        load = Image.open('extendedterminal.png')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

    def showText(self):
        text = Label(self, text='example of image processing')
        text.pack()


root = Tk()
root.geometry("580x420")

app = PythonImageing(root)

root.mainloop()
