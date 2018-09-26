# personal_income_tax.py


# m = int(input("请输入您的当前收入: "))
# b = int(input("请输入三险一金的个人缴费: "))

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
    print("实际到手的月工资", money - baoxian - tax)


# cal_tax(m, b)

cal_tax(20000, 3000)
cal_tax(100000, 20000)

print(tax)  # 出错

