'''
Frame 完成界面刷新
'''
# 导入模块
from tkinter import *


# 定义Frame 基类
class BaseFrame(Frame):

    def __init__(self, master):
        super().__init__(master=master)
        self.master = master


# 定义基类
class BaseActivity:
    b = 0.0

    def __init__(self, master):
        self.master = master
        self.__setUI__()
        self.__addEvent()

    def __setUI__(self):
        self.interface = BaseFrame(self.master)
        self.interface['bg'] = 'red'
        self.interface.pack(fill=BOTH, expand=1)
        frame_top = BaseFrame(self.interface)
        frame_top['bg'] = 'blue'
        frame_top.pack(side=TOP, anchor=CENTER, fill=X)
        self.frame_top = frame_top
        self.title = Label(frame_top, text='标题')
        self.title.pack(side=LEFT, fill=X, expand=1)

        self.backbtn = Button(frame_top, text='返回', command=self.back)
        self.backbtn.pack(side=RIGHT)

        self.gobtn = Button(frame_top, text='下一页', command=self.go)
        self.gobtn.pack(side=RIGHT)
        self.content = BaseFrame(self.interface)
        self.content.pack_propagate(0)
        self.content['bg'] = 'green'
        self.content.pack(side=TOP, anchor=CENTER, fill=BOTH, expand=1)

        self.contentview = BaseFrame(self.content)
        self.contentview.place(relx=0, rely=0)
        for i in range(12):
            Label(self.contentview, text='{}-'.format(i) * 8).pack(side=TOP)

        self.frame_bottom = BaseFrame(self.interface)
        self.frame_bottom['bg'] = 'yellow'
        self.frame_bottom.pack(side=BOTTOM, fill=X)
        # Label(frame_bottom,text='bottom').pack()
        # photo = PhotoImage(file=r'images\gotop.png')

        self.topbtn = Button(self.content, text='╱︵╲\n(    ↑    )\n╲︶╱')
        # # self.topbtn = Button(self.content,text='返回顶部',image=photo,compound='center')
        # self.topbtn = Button(self.content,width=40,height=40,text='返回顶部',fg='green',image=photo,compound='right',bg='red')
        # self.topbtn.pack(side=RIGHT)

    def __addEvent(self):
        self.content.bind('<MouseWheel>', self.mousewheel)
        self.topbtn.bind('<Button-1>', self.gotop)

    def gotop(self, event):
        self.b = 0
        self.contentview.place_configure(rely=self.b)
        self.topbtn.pack_forget()

    def mousewheel(self, event):
        if event.delta > 0:
            self.b -= 0.1
        else:
            self.b += 0.1
        print(self.b)

        if self.b < 0:
            self.b = 0
            return
        elif self.b > 0:
            self.topbtn.pack_configure(side=RIGHT)

        self.contentview.place_configure(rely=self.b)

    # 返回
    def back(self):
        self.interface.destroy()

    # 下一页
    def go(self):
        pass


# first -page
class MainActivity(BaseActivity):
    def __setUI__(self):
        super().__setUI__()
        # self.contentview.place_configure(relx=0.5,rely=0,anchor = CENTER)
        self.backbtn.config(text='退出')
        self.title.config(text='xx教育', font=('黑体', 28), bg='#D9D9D9')
        Label(self.frame_bottom, text='空白处可使用鼠标滚动', bg='#FFFFFF').pack()
        # 如果是第一次打开，简单介绍一下
        if 1:
            Label(self.contentview, text='welcome to here!').pack(anchor=CENTER)
        else:  # 不是第一次打开，直接进入界面
            pass

    def back(self):
        quit()

    def go(self):
        self.interface.destroy()
        ListAcitvity(self.master)


# second -page
class ListAcitvity(BaseActivity):
    def __setUI__(self):
        super().__setUI__()
        self.interface['bg'] = 'green'
        self.gobtn.forget()

    # def __addEvent(self):
    #     super().__addEvent()

    def back(self):
        self.interface.destroy()
        MainActivity(self.master)


# 定义窗口类--重写窗口
class Win(Tk):
    def __init__(self):
        super().__init__()
        self.attributes('-fullscreen', True)
        self.title('试题练习')
        self.geometry('600x600')
        self['bg'] = '#FFFFFF'
        MainActivity(self)


# 程序入口
if __name__ == '__main__':
    win = Win()

    win.mainloop()