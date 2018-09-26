# 05_spinbox.py


import tkinter

root = tkinter.Tk()

spin1 = tkinter.Spinbox(root, from_=0, to=100,
    increment=3)

spin1.pack()


root.mainloop()
