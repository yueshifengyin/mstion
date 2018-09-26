# 04_scale.py

import tkinter

root = tkinter.Tk()

# 创建一个Scale控件
scale1 = tkinter.Scale(root, from_=1, to=2)
scale1.pack()

def scale2_move(value):
    scale1.set(value)

scale2 = tkinter.Scale(root, from_=1, to=2, width=10, height=3,
    orient=tkinter.HORIZONTAL,
    command=scale2_move)
scale2.pack()

root.mainloop()




