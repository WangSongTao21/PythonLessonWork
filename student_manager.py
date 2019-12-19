from tkinter import *
from tkinter import messagebox

import pymysql


# 创建根窗口，并添加组件
def create_root():
    root = Tk()
    root.title('登录-学生管理系统')
    root.resizable(0, 0)  # 设置窗口大小不可变
    canvas = Canvas(root)  # 添加画布
    canvas.pack(side='top', fill=BOTH)
    canvas.create_window(100, 50, window=Label(root, font=('宋体', 10), text='账号', justify='left', padx=5,
                                               pady=4))  # 其中100,50为相对于画布的偏移量，左上角为0,0
    canvas.create_window(100, 90,
                         window=Label(root, font=('宋体', 10), width=5, text='密码 ', justify='left', padx=5, pady=4))
    # 账号密码输入框
    zh_entry = Entry(root, borderwidth=3)
    password_entry = Entry(root, borderwidth=3, show='*')
    canvas.create_window(210, 50, window=zh_entry)
    canvas.create_window(210, 90, window=password_entry)
    canvas.create_window(330, 90, window=Label(root, text='忘记密码', fg='red', font=('宋体', 10)))
    # 创建画布背景图
    global photo
    photo = PhotoImage(file='login.gif')
    canvas.create_image(200, 150, image=photo)

    # button点击事件
    def callback():

        if(zh_entry.get()==None or zh_entry.get()==''):
            messagebox.showerror("错误", "用户名不能为空！")
            return
        if(password_entry.get()==None or password_entry.get()==''):
            messagebox.showerror("错误", "密码不能为空！")
            return

        try:
            user = int(zh_entry.get())
        except:
            messagebox.showerror("错误", "密码不能为非法字符串！")
            return
        password = password_entry.get()
        user_information = sql_information('select * from user_information')
        print(user_information)

        for i in range(len(user_information)):
            print(user_information[i])
            if (user_information[i][0]==user and user_information[i][2]==password):
                student_information = sql_information('select * from student_information')
                root.state("iconic")  # 隐藏窗口，相当于窗口最小化
                new_root(student_information)
                return

        messagebox.showerror("错误", "用户名或密码错误！请重试！")
        return

        # for row in user_information:
        #     print()
        #     if user == row[0] and password == row[2]:
        #         # 从数据库中提取数据时，会以元组的形式返回每一行的数据，即每一行构成一个元组，并且所有的行构成一个大的元组，即嵌套元组。
        #         print(row[0])
        #         print(row[2])
        #         print("------------------------------------------------------------")
        #         student_information = sql_information('select * from student_information')
        #         root.state("iconic")  # 隐藏窗口，相当于窗口最小化
        #         new_root(student_information)
        #         return
        #     else:
        #         messagebox.showerror("错误", "用户名或密码错误！请重试！")
        #         return
        # return


    # 创建登录按钮
    canvas.create_window(190, 200, window=Button(root, width=15, command=callback, bg='#87CEEB', text='立即登录'))
    mainloop()


# 创建新窗口
def new_root(student_information):
    student_root = Toplevel()
    student_root.title('学生管理系统')
    student_root.resizable(0, 0)
    head_string = ('学号', '姓名', '年级', '年龄', '家庭住址')
    for i in range(len(student_information[0])):
        listbox = Listbox(student_root, width=20, height=20, bd=4, relief='flat', bg='#E0FFFF')
        listbox.pack(side=LEFT, fill=BOTH)
        listbox.insert(END, head_string[i])
        for each in student_information:
            listbox.insert(END, each[i])


# 进行数据库连接,传入sql语句,返回需要的信息
def sql_information(sql):
    connection = pymysql.connect('localhost', 'root', '123456', "manager")
    cursor = connection.cursor()
    try:
        cursor.execute(sql)
        # 获取所有记录
        user_information = cursor.fetchall()
    except Exception as e:
        print(e)
    finally:
        if connection:
            cursor.close()
        if cursor:
            connection.close()
    return user_information


if __name__ == '__main__':
    create_root()
