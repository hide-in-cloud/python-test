#!/usr/bin/python
# -*- coding: UTF-8 -*-
# This is note foe exception
"""
try：
  code    #需要判断是否会抛出异常的代码，如果没有异常处理，python会直接停止执行程序

except:  #这里会捕捉到上面代码中的异常，并根据异常抛出异常处理信息
#except ExceptionName，args：    #同时也可以接受异常名称和参数，针对不同形式的异常做处理
  code  #这里执行异常处理的相关代码，打印输出等

else：  #如果没有异常则执行else
  code  #try部分被正常执行后执行的代码

finally：
  code  #退出try语句块总会执行的程序
"""

filename = 'digits.txt'


def count_words(filename):
    try:
        with open(filename, 'r') as f:
            contents = f.read()  # 读取整个文件
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + "does not exist."
        print(msg)
    else:
        words = contents.split()  # 得到一个列表
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")


count_words(filename)


def addition_calculator():
    print("-----加法计算器-----")
    while True:
        try:
            num1 = int(input("请输入第一个数字:"))
            num2 = int(input("请输入第二个数字:"))
        except ValueError:
            print("输入格式不对，请重新输入")
        else:
            answer = num1 + num2
            print(answer)


addition_calculator()
