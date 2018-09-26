# 08_colors.py

import tkinter

root = tkinter.Tk()

label = tkinter.Label(root, text="文字",
                      bg='#FF0000',
                      fg='#0000FF')

label.pack()
root.mainloop()

