from tkinter import * 
import time

menu_inicial = Tk()
menu_inicial.title("Sistema de Distribuição de salas")
menu_inicial.geometry("500x200+0+0")
menu_inicial.resizable(True,True)
menu_inicial['bg'] = "gray"

texto = StringVar()
texto.set("Entre com um valor")

label_1 = Label(menu_inicial, 
                textvariable=texto, 
                bg="#faf200", 
                fg="black", 
                font="Arial 20 bold italic")
label_1.pack()

texto.set("Leandro Barboza Peracio")

label_2 = Label(menu_inicial, 
                text="Este é o label 2\n\nLeandro Peracio ", 
                bg="#faf200", 
                fg="black", 
                font="Arial 12 bold italic", 
                width=40, 
                height=4,
                bd=10,
                relief="solid",
                anchor=CENTER)
label_2.pack()


label_3 = Label(menu_inicial, 
                text="Novo label", 
                bg="#fafafa", 
                fg="red", 
                font="Serif 12 bold",                 
                bd=10,
                relief="raised",
                padx=50,
                pady=0,
                justify=LEFT)
label_3.pack()



def cmd_click():
    time.sleep(5)
    label_3['bg'] ="#cbcbfb"
    label_3['fg'] = "blue"
    label_3['text'] = 'Velho label'
    texto="Fui clicado"

#dimensões
largura = 500
altura = 300

# resolução
largura_screen = menu_inicial.winfo_screenwidth()/2
altura_screen = menu_inicial.winfo_screenheight()

#posição
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2

print(largura_screen, altura_screen)


btn = Button(menu_inicial, text = "Executar", command=lambda: cmd_click())
btn.pack()

for item in label_3.keys():
    print(item, " : ", label_3[item])

menu_inicial.geometry("%dx%d+%d+%d"% (largura,altura,posx,posy))
menu_inicial.mainloop()

