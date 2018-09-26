# 09_layout_grid_row_col.py

import tkinter
root = tkinter.Tk()

btn1 = tkinter.Button(root, text="按钮1")
btn1.grid(row=0, column=0, rowspan=2)

btn2 = tkinter.Button(root, text="按钮2")
btn2.grid(row=0, column=1)

btn3 = tkinter.Button(root, text="按钮3")
btn3.grid(row=1, column=1)

btn4 = tkinter.Button(root, text="按钮4")
btn4.grid(row=2, column=0, columnspan=2)

root.mainloop()

