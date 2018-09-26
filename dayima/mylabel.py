import tkinter
import datetime

# 创建一个带有时间,位置和点击事件的label类
class Mylabel(tkinter.Tk):
    
    def __init__(self, x, y, top3, solar_month, \
                  solar_day, solar_year):
        self.row = y               # 记录自身行号和列号
        self.column = x
        self.number = 7 * y + x    # 记录自身的编号
        self.frame = top3
        self.month = solar_month
        self.day = solar_day
        self.year = solar_year
        self.__init_date() 
        self.lb = None             # 创建label
   
    def __init_date(self):
        __var = tkinter.StringVar()
        __now = "%d%02d01" % (self.year, self.month)
        __week = datetime.datetime.strptime(__now, "%Y%m%d").weekday()
        __yueyue = self.__yufen()

        if self.column == __week and self.row == 0:
            __var.set(self.number - __week + 1)
        elif self.number - __week + 1 < 1:
            __var.set('')
        elif self.number - __week + 1 > __yueyue:
            __var.set('')
        else:
            __var.set(self.number - __week + 1)

        self.lb = tkinter.Label(self.frame, textvariable=__var, width='5', height='2', \
                           font=("黑体", 10)) 
        self.lb.grid(row=self.row, column=self.column, pady=1, padx=1)
        self.lb.bind('<Button-1>', self.now_date)
        self.textvariable = __var

    def __yufen(self):
        if self.month in [1,3,5,7,8,10,12]:
            return 31
        elif self.month in [4,6,9,11]:
            return 30
        elif self.month == 2:
            if self.year % 100 == 0:
                if self.year % 400 == 0:
                    return 29
                elif self.year % 4 == 0:
                    return 28
            elif self.year % 100 != 0 and self.year % 4 == 0:
                    return 29
            else:
                    return 28
    def now_date(self, e, zhuye=0):
        if zhuye == 0:
            self.lb = tkinter.Label(self.frame, textvariable=self.textvariable, \
                     width='5', height='2', font=("黑体", 10), fg="#3767f1") 
            self.lb.grid(row=self.row, column=self.column, pady=1, padx=1)
            self.lb.bind('<Button-1>', self.now_date)
            # self.lb['background']="blue"
        elif zhuye ==1:
            print("设置来了被点击")
            return self.number
        else:
            print("设置走了被点击")
            # self.__back_ground(1)
            return self.number

    # def __back_ground(self, bg_type):

    #     self.lb["background"] = "3767f1"

            
