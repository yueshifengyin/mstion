# 01_labelframe.py

import tkinter

root = tkinter.Tk()

# 创建一个LabelFrame
labelframe = tkinter.LabelFrame(root,
                                text="远程协助")
labelframe.pack()

ckbtn = tkinter.Checkbutton(labelframe,
                            text="ABCDAAAAAAAAAAAAAA")
ckbtn.pack()

root.mainloop()