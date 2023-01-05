from tkinter import *

def excute():
    print(listBox.get(ACTIVE))
    idx = listBox.get(0, END).index(listBox.get(ACTIVE))
    listBox.delete(idx)

root = Tk()

listBox = Listbox(root)
listBox["bg"] = "white"
listBox.pack()

names = ["João", "Guga", "Francy"]

for name  in names:
    listBox.insert(END, name)

cmd = Button(root, text="Remove", command=excute).pack()

root.mainloop()