# 09_button_image.py


import tkinter
root = tkinter.Tk()


def onClick():
    print("'Click me!' 按钮被点击")

btn = tkinter.Button(root, text='Click me!',
                     command=onClick)

btn.pack()

root.mainloop()
