# layout_pack_side.py

# 此示例不意外边距

import tkinter
root = tkinter.Tk()

label1 = tkinter.Label(root, text="Label 1",
                       bg='red')
label1.pack(ipadx=50, ipady=20, pady=100, padx=20)

label2 = tkinter.Label(root, text='Label 2', bg='green')
label2.pack()


root.mainloop()