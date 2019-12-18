#-*- coding:UTF-8 -*-
import tkinter.messagebox
import tkinter as tk
import pymysql
# 构造窗口
window = tk.Tk()
window.title('登陆窗口')
window.geometry('450x300')
# 构造画布
canvas = tk.Canvas(window,height=200,width=500)
image_file = tk.PhotoImage(file='')
image=canvas.create_image(0,0,anchor='nw',image=image_file)
canvas.pack(side='top')

tk.Label(window,text='Username:').place(x=50,y=150)
tk.Label(window,text='Password:').place(x=50,y=190)

var_user_name = tk.StringVar()
var_user_name.set('example@python.com')
entry_user_name = tk.Entry(window,textvariable=var_user_name)
entry_user_name.place(x=160,y=150)

var_user_password=tk.StringVar()
entry_user_password = tk.Entry(window,textvariable=var_user_password,show='*')
entry_user_password.place(x=160,y=190)

def user_login():
    # 获取label中的输入
    user_name = var_user_name.get()
    user_password = var_user_password.get()

    db = pymysql.connect(host="localhost", user="root",
                         password="123456", db="test", port=3306)
    try:
        cursor = db.cursor()
        sql='select * from users_name where username = "'"%s"'";'%user_name #动态sql拼接
        cursor.execute(sql)
        result = cursor.fetchall()
        if user_name == result[0][1] and user_password == result[0][2]:
            tk.messagebox.showinfo(title='welcome',message='How are you? ' + str(user_name))
        else:
            tk.messagebox.showerror(message='Erro,your password is wrong,try again!')
    except Exception as e:
        tk.messagebox.showerror(e)
    finally:
        db.close()


def user_registe():
    pass
# 构造登陆/注册按钮
btn_login = tk.Button(window,text='Login',command=user_login)
btn_login.place(x=170,y=230)
btn_sign_up = tk.Button(window,text='Regist',command=user_registe)
btn_sign_up.place(x=270,y=230)

window.mainloop()