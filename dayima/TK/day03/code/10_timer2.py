# 09_timer.py


import tkinter
import random

root = tkinter.Tk()

gifs = ["sign_images/clipper.gif",
        "sign_images/cloth.gif",
        "sign_images/stone.gif"
       ]

photos = []
i = 0
while i < len(gifs):
    image = tkinter.PhotoImage(file=gifs[i])
    photos.append(image)
    i += 1

cur_select = 0  # 设置当前选中的图片为0


label = tkinter.Label(root, text="--",
                      image=photos[cur_select])

label.pack()

def onTimer():
    print("定时器函数已经调用!")
    global timer_id  # 声明timer_id 为全局变量
    timer_id = label.after(20, onTimer)  # 让定时器重复启动
    global cur_select
    # 生成0,1,2三个随机数中的一个,改变全局的cur_select
    cur_select = random.randrange(0, 3)
    label.config(image=photos[cur_select])


def onStartTimer():
    print("已启动定时器")
    global timer_id
    timer_id = label.after(100, onTimer)


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