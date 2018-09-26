import tkinter
import time
import datetime

# 左侧的第一列按钮
def left1data(root):
    var = tkinter.StringVar()
    solar_year = int(time.strftime("%Y", time.localtime()))
    solar_month = int(time.strftime("%m", time.localtime()))
    solar_day = int(time.strftime("%d", time.localtime()))
    solar_weekday = int(time.strftime("%w", time.localtime()))
    var.set(str(solar_year) + "年" + str(solar_month) + "月")

    # 创建第一个Frame
    left1 = tkinter.Frame(root, bg="#f88da6", width=300, height=340)
    # 创建Frame中的上层Frame
    top1 = tkinter.Frame(left1, bg="#f88da6")
    # 显示月份
    yuefen = tkinter.Label(top1, bg="#f88da6", textvariable=var,
                           width=14, font=("黑体", 15))
    yuefen.pack(side=tkinter.LEFT, pady=4, padx=8)
    # 控制月份

    def jianshao():
        nonlocal solar_year, solar_month
        solar_month -= 1
        if solar_month < 1:
            solar_month = 12
            solar_year -= 1
        damaozi()
        var.set(str(solar_year) + "年" + str(solar_month) + "月")

    yuefen = tkinter.Button(top1, bg="#f88da6", text=" < ", width=2,
                            command=jianshao)
    yuefen.pack(side=tkinter.LEFT, pady=3, padx=5)

    def zengjia():
        nonlocal solar_year, solar_month
        solar_month += 1
        if solar_month > 12:
            solar_month = 1
            solar_year += 1
        var.set(str(solar_year) + "年" + str(solar_month) + "月")
        damaozi()

    yuefen = tkinter.Button(top1, bg="#f88da6", text=" > ", width=2,
                            command=zengjia)
    yuefen.pack(side=tkinter.LEFT, pady=3, padx=5)
    top1.grid(stick='N')
    # 创建Frame中的中层Frame
    top2 = tkinter.Frame(left1, bg="#f88da6")
    # 显示星期
    btn = tkinter.Label(top2,
                        text="一          二          三          四          五          六          日",
                        width=39, font=("黑体", 10))
    btn.grid(stick='N', pady=1, padx=8)
    top2.grid(stick='N')
    # 创建下层Frame
    top3 = tkinter.Frame(left1, bg="#f88da6", borderwidth=5)
    # 显示具体时间
    label_list = ['f0', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6',\
                 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', 'f13', \
                 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', \
                 'f20', 'f21', 'f22', 'f23', 'f24', 'f25', \
                 'f26', 'f27', 'f28', 'f29', 'f30', 'f31', 'f32', \
                 'f33', 'f34', 'f35', 'f36', 'f37', 'f38', 'f39', \
                 'f40', 'f41']

    for y in range(6):
        for x in range(7):
            i = 7 * y + x
            label_list[i] = __init(x, y, top3, solar_month, \
                   solar_day, solar_year)
            label_list[i].bind('<Button-1>', \
                 zhong__now_date(__now_date,label_list[i],label_list))
    top3.grid(stick='N')

    left1.grid(row=0, column=0)
    return label_list

# 左侧的第二列按钮


def left2data(root, label_list):
    label_list = label_list
    left2 = tkinter.Frame(root, bg="#f88da6", width=300,
                          height=170, borderwidth=4)
    # 备注的Frame
    beizhu = tkinter.Frame(left2, bg="#f88da6")

    btn = tkinter.Label(beizhu, bg="#f8262b", width=1, height=1)
    btn.pack(side=tkinter.LEFT, pady=1, padx=4)
    btn = tkinter.Label(beizhu, bg="#f88da6", text="月经期", width=5, height=2)
    btn.pack(side=tkinter.LEFT, pady=1, padx=4)
    btn = tkinter.Label(beizhu, bg="#ffc0c0", width=1, height=1)
    btn.pack(side=tkinter.LEFT, pady=1, padx=4)
    btn = tkinter.Label(beizhu, bg="#f88da6", text="预测期", width=5, height=2)
    btn.pack(side=tkinter.LEFT, pady=1, padx=4)
    btn = tkinter.Label(beizhu, bg="#62fa4a", width=1, height=1)
    btn.pack(side=tkinter.LEFT, pady=1, padx=4)
    btn = tkinter.Label(beizhu, bg="#f88da6", text="安全期", width=5, height=2)
    btn.pack(side=tkinter.LEFT, pady=1, padx=4)
    btn = tkinter.Label(beizhu, bg="#f22df0", width=1, height=1)
    btn.pack(side=tkinter.LEFT, pady=1, padx=4)
    btn = tkinter.Label(beizhu, bg="#f88da6", text="危险期", width=5, height=2)
    btn.pack(side=tkinter.LEFT, pady=1, padx=4)
    btn = tkinter.Label(beizhu, bg="#f88da6", text="＊排卵日", width=7, height=2)
    btn.pack(side=tkinter.LEFT, pady=1, padx=4)

    beizhu.pack()
    # 来否的Frame
    yuejing = tkinter.StringVar()
    panduan = False

    def laile():
        nonlocal panduan
        nonlocal label_list
        if panduan == False:
            yuejing.set("大姨妈来喽!")
            panduan = True
            now_hit = __now_date(e=0, zhuye=1)
            # label_list[12]["background"]="blue"
        else:
            yuejing.set("大姨妈走喽!")
            panduan = False
            now_hit = __now_date(e=0, zhuye=2)

    laifou = tkinter.Frame(left2, bg="#f88da6")

    btn = tkinter.Label(laifou, textvariable=yuejing, width=15,
                        height=2, font=("黑体", 13))
    btn.grid(row=0, column=0, pady=2, padx=4)

    btn = tkinter.Button(laifou, bg="#f88da6", text='设置大姨妈',
                         width=6, height=1, command=laile)
    btn.grid(row=0, column=1)

    btn = tkinter.Label(laifou, text='设置小可爱的日期', width=18,
                        height=2)
    btn.grid(row=1, column=0, pady=1, padx=2)

    date_jiange = tkinter.StringVar()
    date_jiange.set(28)
    btn = tkinter.Spinbox(laifou, textvariable=date_jiange, from_=0,
                          to=60, increment=1)
    btn.grid(row=1, column=1)

    laifou.pack()

    left2.grid(row=1, column=0)


# 右侧第一列
def right1data(root, bg):
    right1 = tkinter.Frame(root, bg="#f88da6", width=600,
                           height=345, borderwidth=2)
    btn = tkinter.Label(right1, image=bg)
    btn.pack(pady=1, padx=0)

    right1.grid(row=0, column=1)


# 右侧第二列
def right2data(root, label_list):
    right2 = tkinter.Frame(root, bg="#f88da6", width=600,
                           height=170, borderwidth=5)
    # 创建痛的LabelFrame
    tong_s = tkinter.LabelFrame(right2, bg="#f88da6", text='很痛T_T')
    tong_s.pack()
    tongma = tkinter.IntVar(root, value=1)
    rb2 = tkinter.Radiobutton(tong_s, text='痛的没力气拆快递 T_T           ',
                              value=0, variable=tongma)
    rb2.pack(side=tkinter.LEFT)
    rb2 = tkinter.Radiobutton(tong_s, text='也无风雨也无晴吧 -_-           ',
                              value=1, variable=tongma)
    rb2.pack(side=tkinter.LEFT)
    rb2 = tkinter.Radiobutton(tong_s, text='开心的想爬山 ^_^                ',
                              value=2, variable=tongma)
    rb2.pack(side=tkinter.LEFT)
    # 创建量的LabelFrame
    liang_s = tkinter.LabelFrame(right2, bg="#f88da6", text='量呢T_T')
    liang_s.pack()
    liang_l = tkinter.IntVar(root, value=1)
    rb2 = tkinter.Radiobutton(liang_s, text='悲伤已经逆流成河 T_T           ',
                              value=0, variable=liang_l)
    rb2.pack(side=tkinter.LEFT)
    rb2 = tkinter.Radiobutton(liang_s, text='也无风雨也无晴吧 -_-           ',
                              value=1, variable=liang_l)
    rb2.pack(side=tkinter.LEFT)
    rb2 = tkinter.Radiobutton(liang_s, text='还是很少的呢 ^_^                ',
                              value=2, variable=liang_l)
    rb2.pack(side=tkinter.LEFT)
    # 创建备忘录的LabelFrame
    beiwang_s = tkinter.LabelFrame(right2, bg="#f88da6", text="我的备忘录")
    beiwang_s.pack()
    btn = tkinter.Text(beiwang_s, width=69, height=1)
    btn.pack(side=tkinter.LEFT, pady=2, padx=20)
    btn = tkinter.Button(beiwang_s, text="保存", width=2, height=1)
    btn.pack(side=tkinter.LEFT)

    right2.grid(row=1, column=1)



def __init(x, y, top3, solar_month, \
              solar_day, solar_year):
    number = 7 * y + x    # label编号
    # 创建label
    __var = tkinter.StringVar()
    __now = "%d%02d01" % (solar_year, solar_month)
    __week = datetime.datetime.strptime(__now, "%Y%m%d").weekday()
    __yueyue = __yufen(solar_month)

    if x == __week and y == 0:
        __var.set(number - __week + 1)
    elif number - __week + 1 < 1:
        __var.set('')
    elif number - __week + 1 > __yueyue:
        __var.set('')
    else:
        __var.set(number - __week + 1)

    lb = tkinter.Label(top3, textvariable=__var, width='5', height='2', \
                       font=("黑体", 10)) 
    lb.grid(row=y, column=x, pady=1, padx=1)
    
    textvariable = __var
    return lb

def __yufen(solar_month):
    if solar_month in [1,3,5,7,8,10,12]:
        return 31
    elif solar_month in [4,6,9,11]:
        return 30
    elif solar_month == 2:
        if solar_year % 100 == 0:
            if solar_year % 400 == 0:
                return 29
            elif solar_year % 4 == 0:
                return 28
        elif solar_year % 100 != 0 and solar_year % 4 == 0:
                return 29
        else:
                return 28

def zhong__now_date(func, args, label_list):
    return lambda event,func=func,args=args,\
                 label_list=label_list: func(event, args, label_list)

def __now_date(event, args=0, label_list=[], zhuye=0):
    if zhuye == 0:
        args['background']="#3767f1"
        for x in label_list:
            if x != args:
                x['background']="#d9d9d9"
    elif zhuye == 1:
        print("设置来了被点击")
        return 1
    else:
        print("设置走了被点击")
    #     # self.__back_ground(1)
        return 2
# def __back_ground(self, bg_type):

#     self.lb["background"] = "3767f1"


def main():
    root = tkinter.Tk()
    root.title("悦是疯淫")
    root.geometry("917x525")
    bg = tkinter.PhotoImage(file='./images/美图.png')

    label_list = left1data(root)
    left2data(root, label_list)
    right1data(root, bg)
    right2data(root, label_list)

    root.mainloop()



            


if __name__ == "__main__":
    main()
