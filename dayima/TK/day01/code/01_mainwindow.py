# mainwindow.py

# 此示例用于示意用tkinter创建一个可交互的空白窗口


#第一步: 导入tkinter 模块包
import tkinter

# 第二步，创建一个空白窗口
# Tk是tkinter里的类，此时创建一个空白窗口对象
root = tkinter.Tk()

print("正要进入主事件循环")
# 第三步，进入主事件循环,等待用户输入相应的操作(键盘，鼠标等)
root.mainloop()
print("主事件循环结束!")

