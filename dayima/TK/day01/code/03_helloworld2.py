# 02_helloworld.py

# 此程序示意在空白窗口上放置一个Label并显示
# hello world

# 第一步
import tkinter

# 第二步，创建空白窗口,用root变量绑定
root = tkinter.Tk()

btn = tkinter.Button(root, text='hello world!')

# 第四步, 让btn 放置到窗口的指定位置
btn.pack()

# 第五步，进入主事件循环
root.mainloop()




