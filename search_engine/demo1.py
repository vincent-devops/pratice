import tkinter
import tkinter.messagebox

# 创建控件
top = tkinter.Tk()
top.geometry("200x100")  # 设置窗口大小

class Cat():
    def __init__(self, name):
        self.name = name
        self.__shout_nums = 3

    def shout(self):
        result = ""
        i = 0
        while i < self.__shout_nums:
            result += " 喵"
            i += 1
        return "我的名字叫" + self.name + result

    @property
    def shout_num(self):
        return self.__shout_nums

    @shout_num.setter
    def shout_num(self, number):
        # if number <= 10:  # 控制最多只能叫10声
        self.__shout_nums = number
        # else:
        #     self.__shout_nums = 10

    @shout_num.deleter
    def shout_num(self):
        del self.__shout_nums


def button_click1():
    cat = Cat("咪咪")
    cat.shout_num = 1000
    tkinter.messagebox.showinfo("", cat.shout())


B = tkinter.Button(top, text="猫叫", command=button_click1)

B.pack()  # 将小部件放置到主窗口中
# 进入消息循环
top.mainloop()
