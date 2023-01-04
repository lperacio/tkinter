from tkinter import *
from PIL import Image, ImageTk

def executar():
    l1['text']=t1.get()
    l2['text']=t2.get()
    l3['text']=t3.get()
    l4['text']=t4.get()



root = Tk()

#Define icone da aplicação outra extensão
ico = Image.open('./img/icon.png')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)


root.title("Focus")


#widget
t1=Entry(root)
t3=Entry(root)
t2=Entry(root)
t4=Entry(root)

l1=Label(root)
l2=Label(root)
l3=Label(root)
l4=Label(root)

b=Button(root, text="Executar", command=executar)

#layout
t1.grid()
t2.grid()
t3.grid()
t4.grid()

l1.grid(sticky='w')
l2.grid(sticky='w')
l3.grid(sticky='w')
l4.grid(sticky='w')

b.grid()

root.mainloop()