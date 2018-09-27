def main():
    global wenjian_save,filename,fanwei,yuejing
    root = tkinter.Tk()
    root.title("悦是疯淫")
    root.geometry("917x525")
    bg = tkinter.PhotoImage(file='./images/美图.png')
    yuejing = tkinter.StringVar()

    wenjian_save = file_save()
    left1data(root)
    left2data(root)
    right1data(root, bg)
    right2data(root)
    
    solar_month = time.strftime("%m", time.localtime())
    dir_month = 'm' + solar_month
    try:
        b = wenjian_save[dir_month]['zoule_date']
        if dir_month in wenjian_save:
            a = wenjian_save[dir_month]['jilu_date']
            fanwei[0] = a
            fanwei[1] = b
            for x in range(6):
                label_list[a]['bg'] = "#f8262b"
                a += 1
                if a == b:
                    break

    except:
        try:
            if dir_month in wenjian_save:
                a = wenjian_save[dir_month]['jilu_date']
                fanwei[0] = a
                fanwei[1] = a + 5            
                for x in range(6):
                    label_list[a]['bg'] = "#f8262b"
                    a += 1
                    if a > 41:
                        break
        except:
            pass
    try:
        b = wenjian_save[dir_month]['youzoule_date']
        if dir_month in wenjian_save:
            a = wenjian_save[dir_month]['youjilu_date']
            fanwei[0] = a
            fanwei[1] = b
            for x in range(6):
                label_list[a]['bg'] = "#f8262b"
                a += 1
                if a == b:
                    break

    except:
        try:
            if dir_month in wenjian_save:
                a = wenjian_save[dir_month]['youjilu_date']
                fanwei[0] = a
                fanwei[1] = a + 5            
                for x in range(6):
                    label_list[a]['bg'] = "#f8262b"
                    a += 1
                    if a > 41:
                        break
        except:
            pass
        

                
    root.mainloop()
