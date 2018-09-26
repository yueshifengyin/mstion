# 07_event.py


import tkinter
root = tkinter.Tk()

fb = tkinter.Frame(root, bg="#f88da6")
fb.pack()
l = tkinter.Button(fb, bg="#f88da6", text="12121", \
                          width=15, font=("黑体", 12))
l.pack()
t = tkinter.Label(fb, bg="#f88da6", text="12", width=10, height=10)
t.pack()
t = tkinter.Label(fb, bg="blue", text="12", width=10, height=10)
t.pack()
def mouseDownEvent(e):
    print("鼠标左键按下, 在:",
        e.x, e.y, e.x_root, e.y_root)

def mouseUPEvent(e):
    print("鼠标左键抬起")

def keyDown(e):
    print("有按键按下")

def keyUp(e):
    print("有按键抬起")

l.bind('<Button-1>', mouseDownEvent)
l.bind('<ButtonRelease-1>', mouseUPEvent)
root.bind('<KeyPress-a>', keyDown)
root.bind('<KeyRelease-a>', keyUp)


root.mainloop()
