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

# 再创建另一个LabelFrame,里面放三个Radiobutton
# 分别是"支持", "反对", "弃权"
lf2 = tkinter.LabelFrame(root, text='请投票')
lf2.pack()

# 创建一个IntVar对象，默认值为1,(选中支持)
# 将其关联在以下三个按钮上
v2 = tkinter.IntVar(root, value=1)

rb4 = tkinter.Radiobutton(lf2, text="支持", value=1)
rb4.config(variable=v2)
rb4.pack(side=tkinter.LEFT)

rb5 = tkinter.Radiobutton(lf2, text="反对", value=-1)
rb5.config(variable=v2)
rb5.pack(side=tkinter.LEFT)

rb6 = tkinter.Radiobutton(lf2, text="弃权", value=0)
rb6.config(variable=v2)
rb6.pack(side=tkinter.LEFT)

def onBtn():
    print("按钮被按下")
    print("性别选择的值是:", v.get())
    print("您的投票值:", v2.get())


btn = tkinter.Button(root, text="打印所选的值:",
    command=onBtn
    )
btn.pack(side=tkinter.BOTTOM)


root.mainloop()