# 登录验证
import time

islogin = False  # 默认没有登录


def login():
    """用户登录"""
    global islogin
    print('------登录验证------')
    user_name = input('请输入用户名：')
    password = input('请输入密码：')
    if user_name == 'liliya' and password == '123456':
        islogin = True
        print('-----用户登录成功!-----\n')
    else:
        print('用户名或密码输入错误！请重新输入！')


def login_require(func):
    """定义一个装饰器，进行付款验证"""
    print("外部函数被调用了")

    def wrapper(*args, **kwargs):  # 内部函数
        print("wrapper函数被调用")
        while True:
            if islogin:
                func(*args, **kwargs)
                break
            else:
                login()

    return wrapper  # 调用内部函数


@login_require
# pay = login_require(pay)
def pay():
    print('-------付款-------')
    money = input('请输入付款金额:')
    print('您的付款金额是：{}元'.format(money))
    print('付款中...')
    time.sleep(2)
    print('付款成功')


pay()
pay()
