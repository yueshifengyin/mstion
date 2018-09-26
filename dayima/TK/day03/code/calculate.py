# calculate.py

import tkinter


# 创建输入Frame
def create_top_frame(root):
    frm = tkinter.Frame(root)
    frm.pack(fill=tkinter.X)
    label = tkinter.Label(frm, text="社保基准数:")
    label.pack(side=tkinter.LEFT)
    # 创建输入框
    entry = tkinter.Entry(frm)
    entry.pack(side=tkinter.LEFT)
    # 创建城镇户籍Checkbutton
    v = tkinter.BooleanVar(value=True)
    ckbtn = tkinter.Checkbutton(frm, text="城镇户籍",
        variable=v)
    ckbtn.pack(side=tkinter.LEFT)

    def onCalBtn():
        base = int(entry.get())  # 得到用户输入的数
        isCity = v.get() #
        print(base, isCity)
        # 此处写计算的程序
        yl_gr = base * 0.08  # 个人社保
        yl_gs = base * 0.19  # 公司社保
        root.geren_list[0].config(text=str(yl_gr))
        root.qiye_list[0].config(text=str(yl_gs))

        if isCity:
            sy_gr = base * 0.002  # 个人失业
        else:
            sy_gr = 0  # 个人失业(农村户口)
        sy_gs = base * 0.008  # 公司失业
        root.geren_list[1].config(text=str(sy_gr))
        root.qiye_list[1].config(text=str(sy_gs))

    # 创建确认按钮
    btn = tkinter.Button(frm, text="开始计算",
                         command=onCalBtn)
    btn.pack(side=tkinter.RIGHT)


def create_bottom_grid(root):
    frm = tkinter.Frame(root)
    frm.pack(expand=1, fill=tkinter.BOTH)
    lbl = tkinter.Label(frm, text='项目')
    lbl.grid(row=0, column=0)
    lbl = tkinter.Label(frm, text='个人缴纳比例')
    lbl.grid(row=0, column=1)
    lbl = tkinter.Label(frm, text='单位缴纳比例')
    lbl.grid(row=0, column=2)
    lst = ['养老保险', '失业', '工伤保险', '生育保险',
           '医疗保险', '公积金']
    r = 0
    root.geren_list = []  # 此列表用于存放个项的Label
    root.qiye_list = []  # 此列表存入企业项的Label
    # 循环创建一列Label
    while r < len(lst):
        lbl = tkinter.Label(frm, text=lst[r])
        lbl.grid(row=r + 1, column=0)

        lbl_gr = tkinter.Label(frm, text='--')
        root.geren_list.append(lbl_gr)
        lbl_gr.grid(row=r + 1, column=1)

        lbl_qy = tkinter.Label(frm, text='--')
        root.qiye_list.append(lbl_qy)
        lbl_qy.grid(row=r + 1, column=2)

        r += 1 # 自增变量放在最后




#  主函数，用来创建窗口并设置窗口布局，然后进入主循环
def main():
    root = tkinter.Tk()
    root.title("五险一金计算器")
    create_top_frame(root)  # 此函数用来创建最上层输入窗口

    create_bottom_grid(root) # 此函数用来创建显示的grid窗口

    root.mainloop()

# 让主函数启动
main()    



