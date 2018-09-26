# 15_modify_attrbute.py


import tkinter
root = tkinter.Tk()
label = tkinter.Label(root, text="hello")
label.pack()

entry = tkinter.Entry(root)
entry.pack()

def onBtn():
    s = entry.get()  # 得到Entry的输入内容
    print("按钮被点击: ", s)
    label.config(text=s, bg='red')

button = tkinter.Button(root, text="点击修改Label",
                        command=onBtn)
button.pack()

root.mainloop()
