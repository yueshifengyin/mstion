# 02_radiobutton.py

import tkinter

root = tkinter.Tk()
# 设置窗口标题
root.title("请投票")

# 选创建一个LabelFrame
lf = tkinter.LabelFrame(root, text="您的性别")
lf.pack()

# 创建一个IntVar类型的变量，
# 让如下Radiobutton关联在同一个变量
v = tkinter.IntVar(root, value=0)

rb1 = tkinter.Radiobutton(lf, text='男',
              value=1,  # 设置此控件代表的值
              variable=v)  # 设置此控件关联的变量
rb1.pack()

rb2 = tkinter.Radiobutton(lf, text='女', value=0,
            variable=v)
rb2.pack()

rb3 = tkinter.Radiobutton(lf, text='保密', value=2,
            variable=v)
rb3.pack()

def onBtn():
    print("按钮被按下")
    print("选中的值是:", v.get())


btn = tkinter.Button(root, text="打印所选的值:",
    command=onBtn
    )
btn.pack()

root.mainloop()