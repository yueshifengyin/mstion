# import time

# solar_year      = int(time.strftime("%Y", time.localtime()))
# solar_month     = int(time.strftime("%02m", time.localtime()))
# solar_day       = int(time.strftime("%d", time.localtime()))
# solar_weekday   = int(time.strftime("%w", time.localtime()))

# print(solar_year, solar_month, solar_day, solar_wee


import tkinter


root = tkinter.Tk()

btn = tkinter.Label(root, text='hello world!', width=20, height=3)
btn.pack()

btn['fg'] = "green"


root.mainloop()
# l = []
# for x in range(42):
#     a = 'f' + str(x)
#     l.append(a)
# print(l)
