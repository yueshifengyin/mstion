# 12_entry.py


import tkinter as tk

root = tk.Tk()
entry = tk.Entry(root)
entry.pack()


def onBtn():
    # entry.get() 返回输入框内的内容字符串
    print("输入框里的内容是:", entry.get())


btn = tk.Button(root, text="在终端打印输入",
                command=onBtn)
btn.pack()
root.mainloop()



