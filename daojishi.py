import time
import tkinter
from threading import Thread

root = tkinter.Tk()
root.title("回家倒计时")
root.geometry()
xiaoshi = tkinter.StringVar()
fenzhong = tkinter.StringVar()
miaoshu = tkinter.StringVar()



def handler():
    try:
        while True:
            xianzai1 = time.mktime(time.localtime()[0:])
            daojia = time.mktime((2018, 10, 2, 1, 4, 0, 0, 0, 0))
            juli = daojia - xianzai1
            hour = juli // (3600)
            minth = (juli % 3600) // 60
            miao = juli - 3600 * hour - 60 * minth

            xiaoshi.set(str(int(hour))+'小时')
            fenzhong.set(str(int(minth))+'分钟')
            miaoshu.set(str(int(miao))+"秒")
            time.sleep(1)
    except:
        pass


bg = tkinter.PhotoImage(file='./123.png')
bg1 = tkinter.Frame(root)
bg1.pack()
tupian = tkinter.Label(bg1,image=bg)
tupian.pack(expand=1)

top = tkinter.Frame(bg1,bg="#f88da6")
hui = tkinter.Label(top, text="加油!", font=("黑体", 30))
# hui.bind('<ButtonRelease>',handler)
hui.pack()
top.pack()

down = tkinter.Frame(bg1, bg="#f88da6")
diyi = tkinter.Label(down, textvariable=xiaoshi, font=("黑体", 20))
diyi.pack(side=tkinter.LEFT)
dier = tkinter.Label(down, textvariable=fenzhong, font=("黑体", 20))
dier.pack(side=tkinter.LEFT)
disan = tkinter.Label(down, textvariable=miaoshu, font=("黑体", 20))
disan.pack(side=tkinter.LEFT)
down.pack()

xianzai1 = time.mktime(time.localtime()[0:])
daojia = time.mktime((2018, 10, 2, 1, 4, 0, 0, 0, 0))
juli = daojia - xianzai1
hour = juli // (3600)
minth = (juli % 3600) // 60
miao = juli - 3600 * hour - 60 * minth
print("距离回家还有%d小时%d分钟%d秒" % (hour,minth,miao))

xiaoshi.set(str(int(hour))+'小时')
fenzhong.set(str(int(minth))+'分钟')
miaoshu.set(str(int(miao))+"秒")
try:
    t = Thread(target=handler)
    t.start()
except:
    t.join()
    
root.mainloop()