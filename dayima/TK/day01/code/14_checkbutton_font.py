# 14_checkbutton_font.py


import tkinter

root = tkinter.Tk()

check1 = tkinter.Checkbutton(root,
                             text="这是中文",
                             font=("黑体", 20))
check1.pack()

check2 = tkinter.Checkbutton(root,
                             text="这是中文",
                             font=("宋体", 30))
check2.pack()

root.mainloop()







