# personal_income_tax_cal.py

# 此示例用于演示简单个人所得税的计算器

import tkinter


def show_result(tax, money):
    # 创建一个新窗口,此窗口用于显示计算结果
    result = tkinter.Tk()
    str_tax = "缴税总额: " + str(tax)
    label = tkinter.Label(result, text=str_tax)
    label.pack()
    str_money = "税后工资: " + str(money)
    label2 = tkinter.Label(result,
                           text=str_money)
    label2.pack()

    # result.mainloop()  # <<---- 此处可能出错


def cal_tax(money, baoxian):
    yingnashui = money - baoxian - 3500
    if yingnashui <= 0:
        tax = 0  # 需要缴的税
    elif 0 < yingnashui <= 1500:
        tax = yingnashui * 0.03 - 0
    elif 1500 < yingnashui <= 4500:
        tax = yingnashui * 0.1 - 105
    elif 4500 < yingnashui <= 9000:
        tax = yingnashui * 0.2 - 555
    elif 9000 < yingnashui <= 35000:
        tax = yingnashui * 0.25 - 1005
    elif 35000 < yingnashui <= 55000:
        tax = yingnashui * 0.3 - 2755
    elif 55000 < yingnashui <= 80000:
        tax = yingnashui * 0.35 - 5505
    else:
        tax = yingnashui * 0.45 - 13505
    print("应纳个人所得税税额", tax)
    m = money - baoxian - tax
    print("实际到手的月工资", m)
    show_result(tax, m)



root = tkinter.Tk()

label = tkinter.Label(root, text='税前收入')
label.pack(expand=1, fill=tkinter.Y, pady=20)
income = tkinter.Entry(root)
income.pack(fill=tkinter.X, padx=40)

label = tkinter.Label(root, text='三险一金')
label.pack(expand=1, fill=tkinter.Y, pady=20)
bx = tkinter.Entry(root)
bx.pack(fill=tkinter.X, padx=40)


def on_btn_cal():
    money = int(income.get())
    baoxian = int(bx.get())
    cal_tax(money, baoxian)

btn = tkinter.Button(root,
                     text='开始计算:',
                     command=on_btn_cal)
btn.pack(side=tkinter.BOTTOM, pady=30)

root.mainloop()

