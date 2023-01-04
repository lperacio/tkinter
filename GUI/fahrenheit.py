from tkinter import *
from PIL import Image, ImageTk


#funcoes
# c = (f - 32)* 5/9

def calcular():
    F = float(textbox1.get())
    C = (F-32) * (5/9)
    final.set(str(round(C,1)) + " graus Celsius")


root = Tk()
root.title("Fahrenheit para Celsius")

final = StringVar()

ico = Image.open("./img/icon.png")
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)


# widgets
label1 = Label(root, text="Graus Fahreinheit")
textbox1 = Entry(root)
button1 = Button(root, text="Calcular", command=calcular)
label_resultado = Label(root, textvariable=final)






# layouts
label1.grid()
textbox1.grid()
button1.grid()
label_resultado.grid()


root.mainloop()