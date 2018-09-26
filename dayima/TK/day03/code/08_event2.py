# 07_event.py


import tkinter
root = tkinter.Tk()

def mouseDownEvent(e):
    print("鼠标左键按下, 在:",
        e.x, e.y, e.x_root, e.y_root, e.num)

def mouseUPEvent(e):
    print("鼠标左键抬起")

def keyDown(e):
    print("有按键按下:",
        e.keycode, e.keysym, e.keysym_num, e.char)

def keyUp(e):
    print("有按键抬起")

root.bind('<Button>', mouseDownEvent)
root.bind('<ButtonRelease>', mouseUPEvent)
root.bind('<KeyPress>', keyDown)
root.bind('<KeyRelease>', keyUp)


root.mainloop()
