from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Two frames")
root.geometry("500x200+0+0")

#set image of application
ico = Image.open("./img/icon.png")
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

#------------------------------------------------------#
# CENTER APPLICATION
# dimensões
largura = 500
altura = 300

# resolução
# In this case i have two screen because of this i do => root.winfo_screenwidth()/2
largura_screen = root.winfo_screenwidth()/2
altura_screen = root.winfo_screenheight()

#posição
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2
root.geometry("%dx%d+%d+%d"% (largura,altura,posx,posy))
#------------------------------------------------------#


# widgets
frame_nome = Frame(root)
frame_casa = Frame(root)

label_nome    = Label(frame_nome, text="Nome: ")
label_apelido = Label(frame_nome, text="Apelido: ")
label_rua     = Label(frame_casa, text="Rua: ")
label_cidade  = Label(frame_casa, text="Cidade: ")

text_nome = Entry(frame_nome)
text_apelido = Entry(frame_nome)
text_rua = Entry(frame_casa)
text_cidade = Entry(frame_casa)

cmd_Salvar = Button(root, text="Salvar")

#layout
label_nome.grid(row=0, column=0,sticky="e")
text_nome.grid(row=0, column=1)

label_apelido.grid(row=1,column=0,sticky="e")
text_apelido.grid(row=1,column=1)

label_rua.grid(row=0,column=0,sticky="e")
text_rua.grid(row=0,column=1)

label_cidade.grid(row=1,column=0,sticky="e")
text_cidade.grid(row=1,column=1)

frame_casa["bd"] = 5
frame_casa["relief"] = SOLID
frame_casa["pady"] = 50


frame_nome["bd"] = 5
frame_nome["relief"] = SOLID

frame_casa.grid(row=0,column=0)
frame_nome.grid(row=0,column=1)

cmd_Salvar.grid(column=1, sticky="e")




#main 
root.mainloop()
