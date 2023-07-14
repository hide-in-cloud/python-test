import tkinter
import time


def get_time():
    var.set(time.strftime("%H:%M:%S"))
    root.after(1000, get_time)  # 每隔1s调用函数 get_time 自身获取时间


root = tkinter.Tk()
root.title("时钟")
var = tkinter.StringVar()

label = tkinter.Label(root, textvariable=var, fg='blue', font=('黑体', 40))
label.pack()
get_time()
root.mainloop()
