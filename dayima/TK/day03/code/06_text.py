# 06_text.py


import tkinter

root = tkinter.Tk()

txt = tkinter.Text(root, width=50, height=2)
txt.insert(tkinter.END, '老王日记')
txt.pack()

root.mainloop()
