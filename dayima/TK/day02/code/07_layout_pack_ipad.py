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
label1.pack(ipadx=50, ipady= 20)

label2 = tkinter.Label(root, text='Label 2', bg='green')
label2.pack()


root.mainloop()