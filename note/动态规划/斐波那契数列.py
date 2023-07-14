memo = {}


def fib2(n):
    """有记忆的递归"""
    if n in memo:
        return memo[n]  # 查表
    else:
        if n <= 1:  # 边界条件
            f = 1
        else:
            f = fib2(n - 1) + fib2(n - 2)  # 递归调用
        memo[n] = f  # 将结果存储于表中
        return f


def fib_bottom_up(n):
    """用循环代替递归"""
    fib = {}
    for k in range(n+1):  # 0到n
        if k <= 1:
            f = 1
        else:
            f = fib[k-1] + fib[k-2]  # 自底向上填表
        fib[k] = f
    return fib[n]


def fib_mat(n):
    """用矩阵求斐波那契数列"""
    import numpy as np
    f = np.mat('1 1; 1 0')
    return (f**n)[0,0]  # f的n次幂的第一个元素


if __name__ == '__main__':
    print(fib2(5))
    print(fib_bottom_up(5))
    print(fib_mat(5))
