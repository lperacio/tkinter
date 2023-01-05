from tkinter import * 
from PIL import Image, ImageTk


root = Tk()
root.title("Aplicação menu")
root.geometry("300x200")


def file():
    print('File')

ico = Image.open("./img/icon.png")
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False,photo)



myMenu = Menu(root)


myMenu.add_command(label="Arquivo", command=file)
myMenu.add_command(label="Edit")


fileMenu = Menu(myMenu, tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_command(label="Open")
fileMenu.add_command(label="Salve")
myMenu.add_cascade(label="File", menu=fileMenu)


root.config(menu=myMenu)

root.mainloop()