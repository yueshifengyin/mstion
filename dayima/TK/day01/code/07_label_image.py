# 05_lable_widget.py

import tkinter

root = tkinter.Tk()

img1 = tkinter.PhotoImage(file='./sign_images/stone.gif')
label = tkinter.Label(root, bg='orange', image=img1)
label.pack()

img2 = tkinter.PhotoImage(file='./sign_images/clipper.gif')
label = tkinter.Label(root, image=img2)
label.pack()

img3 = tkinter.PhotoImage(file='./sign_images/cloth.gif')
label = tkinter.Label(root, image=img3)
label.pack()

root.mainloop()
