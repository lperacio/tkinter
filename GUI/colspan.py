from tkinter import *
from PIL import Image, ImageTk

root = Tk()

#Define icone da aplicação .ico 

#root.wm_iconbitmap("java-icon.ico")

#Define icone da aplicação outra extensão
ico = Image.open('./img/icon.png')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)


root.title("sistema de colunas")

Label(root, text="texto", width=20, bg="red").grid(column=0)
Label(root, text="texto", width=20, bg="blue").grid(column=1)
Label(root, text="texto", width=20, bg="purple").grid(columnspan=3, sticky='we')





root.mainloop()