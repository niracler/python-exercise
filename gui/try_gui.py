# 第一步，导入tkinter包的所有内容
from tkinter import *


# 第二步，从Frame派生出一个Application类,这是所有widget(窗口小部件)类的父容器
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text="Hello World!!!")  # Lable(标签)
        self.helloLabel.pack()
        self.quitButton = Button(self, text="Quit", command=self.quit)  # 退出的按钮,# 有括号是执行，没括号是函数对象

app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()