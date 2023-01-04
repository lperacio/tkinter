from tkinter import *
from PIL import Image, ImageTk



#meu widget
class FrameNome(Frame):
    def __init__(self, meumaster):
        super().__init__()
        self['height'] = 150
        self['width'] = 200
        self['bd'] = 2
        self['relief'] = SOLID

        label_nome = Label(self,text="Nome: ")
        text_nome = Entry(self)
        label_nome.grid(row=0, column=0)
        text_nome.grid(row=0, column=1)




#gui
root = Tk()
root.title("Self Widget")

ico = Image.open("./img/icon.png")
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False,photo)


frame_nome1 = FrameNome(root).grid()
frame_nome2 = FrameNome(root).grid()
frame_nome3 = FrameNome(root).grid()
frame_nome4 = FrameNome(root).grid()




root.mainloop()