# 04_scale.py

import tkinter

root = tkinter.Tk()

# 创建一个Scale控件
scale1 = tkinter.Scale(root, from_=10, to=100)
scale1.pack()

def scale2_move(value):
    print("scale2的当前值是:", value)
    scale1.set(value)

scale2 = tkinter.Scale(root, from_=-100, to=100,
    orient=tkinter.HORIZONTAL,
    command=scale2_move)
scale2.pack()

root.mainloop()




