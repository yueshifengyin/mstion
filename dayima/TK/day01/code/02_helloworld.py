# 02_helloworld.py

# 此程序示意在空白窗口上放置一个Label并显示
# hello world

# 第一步
import tkinter

# 第二步，创建空白窗口,用root变量绑定
root = tkinter.Tk()

# 第三步, 创建一个Label 窗口控件,
# 让root作为它的父窗口
label = tkinter.Label(root, text='hello world!')

# 第四步, 让label 放置到窗口的指定位置
label.pack()

# 第五步，进入主事件循环
root.mainloop()




