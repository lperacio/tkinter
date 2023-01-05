from tkinter import *

def show():
    print(valor_check.get())


root = Tk()

valor_check = IntVar()

check = Checkbutton(
    root,
    text="You are sure of this?",
    variable=valor_check,
    command=show
)
check.grid()
root.mainloop()