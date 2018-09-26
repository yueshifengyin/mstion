# 05_lable_widget.py

import tkinter

root = tkinter.Tk()

label = tkinter.Label(root, text="Hello Xi'an!",
                      bg='orange',
                      fg='blue',
                      width=20,
                      height=2)

label.pack()

root.mainloop()
