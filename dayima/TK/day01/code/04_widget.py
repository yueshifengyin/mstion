# 04_widget.py

# 此示例用于示意常见的窗口部件的样式

import tkinter

root = tkinter.Tk()

# 创建一个label并添加到主窗口
label = tkinter.Label(root, text="我是一个Label")
label.pack()

# 创建一个Button 并添加到主窗口
btn = tkinter.Button(root, text="我是一个Button")
btn.pack()

# 创建一个Entry
entry=tkinter.Entry(root, text="我是Entry!")
entry.pack()

# 创建一个Checkbutton...
cb = tkinter.Checkbutton(root, text='点我试试')
cb.pack()

# 进入主事件循环
root.mainloop()







