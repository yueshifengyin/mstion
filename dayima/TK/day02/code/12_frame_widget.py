# 12_frame_widget.py

import tkinter
root = tkinter.Tk()

# 左侧的竖直的一列按钮
left = tkinter.Frame(root)
btn = tkinter.Button(left, text='左侧按钮1')
btn.pack(pady=5, padx=5)

btn = tkinter.Button(left, text='左侧按钮2')
btn.pack(pady=5, padx=5)

btn = tkinter.Button(left, text='左侧按钮3')
btn.pack(pady=5, padx=5)

left.pack(side=tkinter.LEFT, fill=tkinter.Y)

# 上部的一行按钮
top = tkinter.Frame(root)
btn = tkinter.Button(top, text='顶端按钮1')
btn.pack(side=tkinter.LEFT, padx=2)

btn = tkinter.Button(top, text='顶端按钮2')
btn.pack(side=tkinter.LEFT, padx=2)

btn = tkinter.Button(top, text='顶端按钮3')
btn.pack(side=tkinter.LEFT, padx=2)

top.pack(side=tkinter.TOP, fill=tkinter.X)

# 添加一个中心内容区域的Frame
center = tkinter.Frame(root, bg="green")
center.pack(expand=1, fill=tkinter.BOTH)

# 在中心内容区域添加两列，center_left靠左，center_right靠右
center_left = tkinter.Frame(center)
btn = tkinter.Button(center_left, text="左上按钮")
btn.pack()

btn = tkinter.Button(center_left, text="左下按钮")
btn.pack(side=tkinter.BOTTOM)

center_left.pack(side=tkinter.LEFT, expand=1, fill=tkinter.BOTH)
# 创建右侧的 center_right 的 Frame
center_right = tkinter.Frame(center)
btn = tkinter.Button(center_right, text="右上按钮")
btn.pack()

btn = tkinter.Button(center_right, text="右下按钮")
btn.pack(side=tkinter.BOTTOM)

center_right.pack(side=tkinter.RIGHT, expand=1, fill=tkinter.BOTH)


root.mainloop()






