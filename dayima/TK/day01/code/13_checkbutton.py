

import tkinter

root = tkinter.Tk()

def onCheckBtn():
    # var.get() 方法可以得到Checkbutton的状态
    print("Checkbutton按钮被点击!", var.get())


var = tkinter.IntVar(root)
check = tkinter.Checkbutton(root,
                            text="自动登陆",
                            command=onCheckBtn,
                            variable=var)
check.pack()
root.mainloop()
