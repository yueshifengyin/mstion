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

label1 = tkinter.Label(root, text="Label 1", bg='red')
label2 = tkinter.Label(root, text='Label 2', bg='green')
label3 = tkinter.Label(root, text='Label 3', bg='blue')
label4 = tkinter.Label(root, text='Label 4xxx', bg='orange')

label1.pack(expand=1, fill=tkinter.BOTH)
label2.pack(expand=1, fill=tkinter.BOTH)
label3.pack(expand=0, fill=tkinter.BOTH)
label4.pack(expand=0, fill=tkinter.BOTH)


root.mainloop()