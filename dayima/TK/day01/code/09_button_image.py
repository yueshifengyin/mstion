# 09_button_image.py


import tkinter
root = tkinter.Tk()

# 用文件创建一个照片对象
img = tkinter.PhotoImage(file='./sign_images/stone.gif')

btn = tkinter.Button(root, image=img)  # 让img对象作为button前景
btn.pack()

root.mainloop()
