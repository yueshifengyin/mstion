# 09_timer.py


import tkinter
root = tkinter.Tk()

label = tkinter.Label(root, text="--")
label.pack()

def onTimer():
    print("定时器函数已经调用!")
    global timer_id  # 声明timer_id 为全局变量
    timer_id = label.after(1000, onTimer)  # 让定时器重复启动


def onStartTimer():
    print("已启动定时器")
    global timer_id
    timer_id = label.after(5000, onTimer)


def onStopTimer():
    label.after_cancel(timer_id)  # 取消定时器
    print("定时器已取消!")


btn = tkinter.Button(root, text="启动定时器", 
                     command=onStartTimer)
btn.pack()

btn2 = tkinter.Button(root, text="取消定时器",
                      command=onStopTimer)
btn2.pack()

root.mainloop()