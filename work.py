from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askinteger, askstring


class MainFrame(object):
    def __init__(self):
        self.all_items = []
        self.root = Tk()
        self.root.title("名片管理系统")
        self.root.wm_minsize(width=1000, height=600)
        mubar = Menu(self.root)
        muLogin = Menu(mubar)
        mubar.add_cascade(label="系统管理", menu=muLogin)
        muLogin.add_command(label="加载数据(未实现)", command=quit)
        tc = muLogin.add_command(label="退出", command=quit)
        muCard = Menu(mubar, tearoff=0)
        mubar.add_cascade(label="卡片管理", menu=muCard)
        muCard.add_command(label="显示所有卡片(未实现)")
        self.root.bind("<Button-1>,")
        muCard.add_command(label="新建卡片", command=lambda: self.showInputFrame("添加", None))
        muCard.add_command(label="查找卡片",command=self.findBox)
        subMu = Menu(muCard)
        muCard.add_cascade(label="卡片修改(无响应)", menu=subMu)
        subMu.add_command(label="修改卡片(无响应)")
        subMu.add_command(label="删除卡片(无响应)")
        muHelp = Menu(mubar)
        mubar.add_cascade(label="帮助", menu=muHelp)
        self.root["menu"] = mubar



    # 定义 show 方法：显示主窗口布局
    def show(self):
        self.addTopFrame()
        self.initContent()
        self.loadData()
        # 显示出所有的名片信息
        self.showAllItem()
        # 开启主界面，进入主循环
        self.root.mainloop()



    # 定义 showAllItem 方法，显示所有列表信息
    def showAllItem(self):
        # 遍历循环所有的列表信息
        for data in self.all_items:
            # 添加信息到列表界面
            self.showItem(data)


    # 定义 save_2_file 方法，将已经添加的名片信息存储到本地文件中
    def save_2_file(self):
        # 打开文件
        f = open("contacts.data", "w")
        # 将已经添加的信息以字符串形式写入次文件
        f.write(str(self.all_items))
        # 关闭文件
        f.close()

    # 定义一个loadData方法，加载本地存储文件中的所有数据
    def loadData(self):
        # 通过"try...except"异常点检验方法，检查存储名片信息的本地文件的存在性
        try:
            # 打开存储名片信息的本地文件
            f = open("contacts.data")
            # 读取本地文件中的所有数据
            self.all_items = eval(f.read())
            """eval 相关知识点以及用法
            功能：将字符串str当成有效的表达式来求值并返回计算结果。
　　        语法： eval(source[, globals[, locals]]) -> value
            参数：source：一个Python表达式或函数compile()返回的代码对象
                  globals：可选。必须是dictionary
                  locals：可选。任意map对象"""
            f.close()
        except Exception:
            pass

    # 添加主窗口布局需要的控件
    def addTopFrame(self):
        # 添加一个框架将首页的题目和添加按钮都放在一起
        topFrame = Frame(self.root)
        # 在次框架中添加一个标签，其题目：名片信息
        titlelable = Label(topFrame, text="名片信息")
        # 显示框架，并设定向左排列，x和y轴的宽度均为5个像素
        titlelable.pack(side=LEFT, padx=5, pady=6)

        # 定义一个添加按钮，其中command点击事件通过lambda函数实现：调用showInputFrame
        addButton = Button(topFrame, text="添加", command=lambda : self.showInputFrame("添加",None))
        # 显示按钮，并设定向左排列，x和y轴的宽度均为默认像素
        addButton.pack(side=RIGHT,padx=5, pady=6)
        # 定义一个查找按钮，其中command点击事件通过lambda函数实现：调用showInputFrame
        addButton = Button(topFrame, text="查找", command=self.findBox)
        # 显示按钮，并设定向左排列，x和y轴的宽度均为默认像素
        addButton.pack(side=RIGHT)


        # 设置此框架的背景颜色为蓝色
        topFrame.config(bg="#3f51b5")
        # 横向填充
        topFrame.pack(fill=X)

    # 显示添加页面
    def showInputFrame(self,title,dict):
        # 定义 inputFrame 实例，即创建一个添加界面
        self.inputFrame = InputFrame(self,title,dict)
        # 显示添加界面
        self.inputFrame.show()

    # 显示列表信息
    def initContent(self):
        # 初始化列表框架
        self.item_container = Frame(self.root)
        # 将这一框架整体整合
        self.item_container.pack()

    # 添加名片信息
    def addItem(self, dict):
        # 添加新信息到 all_items 列表
        self.all_items.append(dict)
        # 显示名片信息
        self.showItem(dict)
        # 将信息保存到本地文件夹
        self.save_2_file()

    # 修改信息
    def updateItem(self, origin_data,new_data):
        # 获取原始数据列表的索引
        index = self.all_items.index(origin_data)
        # 将需要修改的内容从数据列表中移除
        self.all_items.remove(origin_data)
        # 添加修改后的名片信息到数据列表
        self.all_items.insert(index,new_data)
        # 将修改后的信息保存到本地文件夹
        self.save_2_file()

        # 为了让修改后的信息整体生效，先将主界面上的所有信息都删除
        self.remove_allItem()
        # 然后在主界面上重新显示所有信息
        self.showAllItem()

    # 清空主界面上的每一行数据：
    def remove_allItem(self):
        # 通过for循环将主界面上的名片信息都逐一删除
        for child_item in self.item_container.winfo_children():
            child_item.destroy()

    # 在主界面上显示一行信息
    def showItem(self, dict):
        # 初始化主框架
        item_frame = Frame(self.item_container)

        # 添加姓名信息标签
        name_label = Label(item_frame, text='【姓名】: '+dict['name'])
        name_label.pack(side=LEFT, padx=5, pady=5)

        # 添加手机号信息标签
        mob_label = Label(item_frame, text='【手机号】: '+dict['mobile'])
        mob_label.pack(side=LEFT)

        # 添加QQ号信息标签
        qq_label = Label(item_frame, text='【QQ】: '+dict['qq'])
        qq_label.pack(side=LEFT)

        # 添加EMAIL信息标签
        email_label = Label(item_frame, text='【邮箱】: '+ dict['email'])
        email_label.pack(side=LEFT)

        # 添加删除按钮
        delete_button = Button(item_frame, text="删除", command=lambda: self.delete_item(dict,item_frame))
        # delete_button = Button(f2, text="删除", command=lambda dict : self.all_items.remove(dict))
        delete_button.pack(side=LEFT)

        # 添加修改按钮
        update_button = Button(item_frame, text="修改",command=lambda : self.showInputFrame("修改",dict))
        update_button.pack(side=LEFT)

        # 将整个框架整体封装
        item_frame.pack()

    # 删除信息
    def delete_item(self, data,item_frame):
        # 从数据列表中删除数据
        self.all_items.remove(data)
        # 将删除后的信息存储到本地文件
        self.save_2_file()
        # 在主界面中将删除的这条信息移除
        item_frame.pack_forget()
    #查找
    def findBox(self):
        name = askstring(title="请输入", prompt="需要查询的用户名：")
        print(self.all_items)
        for i in self.all_items:
            if i['name']==name:
                messagebox.showinfo('查询成功', '【'+i['name']+'】的【电话】为：'+i['mobile']+' 【QQ号】为：'+ i['qq']+' 【邮箱】为：'+i['email'])
                break
        else:
            messagebox.showerror('查询失败','结果莫得啊~')


# 定义了一个添加界面类，其父类为 object
class InputFrame(object):
    def __init__(self, mainFrame,title,dict):
        self.mainFrame = mainFrame
        self.data = dict
        # 初始化添加窗口
        self.inputRootFrame = Tk()
        # 设置这一窗口的题目
        self.inputRootFrame.title(title)
        # 设置窗口大小
        self.inputRootFrame.wm_minsize(width=200, height=250)


    def show(self):
        # 添加界面的展示信息
        self.addInputFrame()
        # 由于添加和编辑用了同一个界面,所以根据界面不同，按钮的文本需要改变
        if self.data == None:
            self.addButtonFrame('保存')
        else:
            self.addButtonFrame('确定修改')

        self.inputRootFrame.mainloop()

    # 添加界面布局信息展示
    def addInputFrame(self):
        # 初始化姓名框架以及界面
        fmname = Frame(self.inputRootFrame)
        # 添加姓名标签
        self.namelable = Label(fmname, text="姓名：")
        # 设置姓名标签的位置以及大小
        self.namelable.pack(side=LEFT, padx=5, pady=10)
        # 添加姓名输入框
        self.nameInput = Entry(fmname, width=50, textvariable=StringVar())
        # 设置姓名输入框的位置
        self.nameInput.pack(side=LEFT)
        # 将以前的姓名自动填写进来，便于用户核对方便修改
        if self.data != None:
            self.nameInput.insert(0, self.data['name'])
            self.nameInput['state'] = DISABLED
        fmname.pack()


        # 初始化手机号的框架以及显示内容
        fmMob = Frame(self.inputRootFrame)
        # 添加手机号标签
        moblelable = Label(fmMob, text="手机号：")
        # 设置手机号标签的位置
        moblelable.pack(side=LEFT, padx=5, pady=10)
        # 添加手机号输入框
        self.mobleInput = Entry(fmMob, width=50, textvariable=StringVar())
        # 设置手机号输入框的位置
        self.mobleInput.pack(side=LEFT)
        # 将以前的手机号自动填写进来，便于用户核对方便修改
        if self.data != None:
            self.mobleInput.insert(0, self.data['mobile'])
        fmMob.pack()

        # 初始化QQ的框架以及显示内容
        fmQQ = Frame(self.inputRootFrame)
        QQlable = Label(fmQQ, text="QQ：")
        QQlable.pack(side=LEFT, padx=5, pady=10)
        self.QQInput = Entry(fmQQ, width=50, textvariable=StringVar())
        self.QQInput.pack(side=LEFT)
        # 将以前的手机号自动填写进来，便于用户核对方便修改
        if self.data != None:
            self.QQInput.insert(0, self.data['qq'])
        fmQQ.pack()

        # 初始化邮箱的框架以及显示内容
        fmEmail = Frame(self.inputRootFrame)
        emaillable = Label(fmEmail, text="邮箱：")
        emaillable.pack(side=LEFT, padx=5, pady=10)
        self.emailInput = Entry(fmEmail, width=50, textvariable=StringVar())
        self.emailInput.pack(side=LEFT)
        if self.data != None:
            self.emailInput.insert(0, self.data['email'])
        fmEmail.pack()

    # 添加界面的按钮设置
    def addButtonFrame(self,title):
        # 初始化框架
        fmButton = Frame(self.inputRootFrame)
        # 设置框架位置
        fmButton.pack(side=BOTTOM, anchor=W, fill=X)

        # 添加保存按钮
        confrmButton = Button(fmButton, text=title, command=self.saveInput)
        confrmButton.pack(side=RIGHT, fill=BOTH)

        # 添加取消按钮
        cencelButton = Button(fmButton, text="取消", command=self.cancelInput)
        cencelButton.pack(side=RIGHT)

    # 名片信息存储
    def saveInput(self):
        # 获取输入的姓名
        name = self.nameInput.get()
        # 获取输入的手机号
        mobile = self.mobleInput.get()
        qq = self.QQInput.get()
        email = self.emailInput.get()

        # 确保输入的姓名不为空
        if name == None or name == '':
            messagebox.showinfo("提示","请输入姓名！")
            return
        # 确保输入的手机号不为空
        if mobile == None or mobile == '':
            messagebox.showinfo("提示","请输入手机号！")
            return
        if qq == None or qq == '':
            messagebox.showinfo("提示", "请输入QQ号！")
            return
        if email == None or email == '':
            messagebox.showinfo("提示", "请输入邮箱地址！")
            return
        # 将输入的整条名片信息以字典的形式存储
        info = {'name': name, 'mobile': mobile, 'qq': qq, 'email': email}
        # 如果在添加页面添加数据成功后，就把数据更新到主界面
        if self.data == None:
            self.mainFrame.addItem(info)
        else:
            self.mainFrame.updateItem(self.data,info)
        # 返回主界面
        self.inputRootFrame.destroy()

    # 点击修改页面上的“取消”按钮，就返回到主界面上
    def cancelInput(self):
        self.inputRootFrame.destroy()


# 程序入口
if __name__ == '__main__':
    # 创建一个 main frame 对象,即创建一个主窗口实例
    mainFrame = MainFrame()
    # 调用主窗口的show()方法显示主窗口
    mainFrame.show()