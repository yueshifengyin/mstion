# layout_pack_side.py

# 此示例实现如下布局:

# +--------+---------+-------+
# |        |_Label 1_|       |
# +        +---------+       +
# | Label 2|         |Label 3|
# +--------------------------+
# |           Label 4        |
# +--------------------------+
import tkinter
root = tkinter.Tk()

label1 = tkinter.Label(root, text="Label 1",
                       bg='red')
label2 = tkinter.Label(root, text='Label 2', bg='green')
label3 = tkinter.Label(root, text='Label 3', bg='blue')
label4 = tkinter.Label(root, text='Label 4xxx', bg='orange')

label4.pack(side=tkinter.BOTTOM, fill=tkinter.X)

label2.pack(side=tkinter.LEFT, fill=tkinter.Y)
label3.pack(side=tkinter.RIGHT)

# 当有expand=1时，side的属性值没有任何意义
# label1.pack(side=tkinter.TOP, fill=tkinter.BOTH,
#             expand=1)
# label1.pack(expand=1, fill=tkinter.BOTH)
label1.pack(expand=1)

root.mainloop()