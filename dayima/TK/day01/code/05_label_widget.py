# 05_lable_widget.py

import tkinter

root = tkinter.Tk()

label = tkinter.Label(root, text="Hello Xi'an!",
                      bg='orange',
                      fg='blue')

# class Label(widget):
#     def __init__(self, master, text='', bg='black', fg='gray'):
#         self.__text= text


label.pack()

root.mainloop()
