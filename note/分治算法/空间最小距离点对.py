import math


def closest(P, n):
    """
        主函数
    :param P:点对集合
    :param n: n个点
    :return:
    """
    X = list(P)
    Y = list(P)
    X.sort()                                  # 预处理，按照X轴进行排序
    Y = sorted(Y, key=lambda last: last[-1])  # 预处理，按照Y轴进行排序
    return closest_pair(X, Y, n)


def closest_pair(X, Y, n):
    """
        分治算法
    :param X:
    :param Y:
    :param n:
    :return:
    """
    if n <= 3:
        return brute_force(X, n)
    mid = n // 2
    Y_left = []
    Y_right = []
    for p in Y:
        if p in X[:mid]:
            Y_left.append(p)
        else:
            Y_right.append(p)
    dis_left = closest_pair(X[:mid], Y_left, mid)
    dis_right = closest_pair(X[mid:], Y_right, n - mid)  # 递归处理P_R
    min_dis = min(dis_left, dis_right)                   # 得到P_L和P_R中的最小距离
    strip = []
    for (x, y) in Y:
        if abs(x - X[mid][0]) < min_dis:
            strip.append((x, y))
    return min(min_dis, strip_closest(strip, min_dis))


def brute_force(X, n):
    """
        当点数小于3时，直接计算最小距离
    :param X:
    :param n:
    :return:
    """
    min_d = distance(X[0], X[1])
    for i in range(len(X)):
        for j in range(i + 1, n):
            if distance(X[i], X[j]) < min_d:
                min_d = distance(X[i], X[j])
    return min_d


def distance(a, b):
    """
        计算两点之间的欧拉距离
    :param a:
    :param b:
    :return:
    """
    return math.sqrt(math.pow((a[0] - b[0]), 2) + math.pow((a[1] - b[1]), 2))


def strip_closest(strip, d):
    """
        处理边界内最近点对(跨界情况)
    :param strip:
    :param d:
    :return:
    """
    min_d = d
    for i in range(len(strip)):
        for j in range(i + 1, 8):   # 只需要考虑最多7个点
            if i + j < len(strip):  # 预防数组越界
                temdis = distance(strip[i], strip[j])
                if temdis < min_d:
                    min_d = temdis
    return min_d


if __name__ == '__main__':
    points = [(2, 3), (10, 1), (3, 25), (23, 15), (18, 3), (8, 9), (12, 30), (25, 30), (9, 2), (13, 10), (3, 4), (5, 6),
              (22, 32),(5, 32), (23, 9), (19, 25), (14, 1), (11, 25), (26, 26), (12, 9), (18, 9), (27, 13), (32, 13)]
    print(closest(points, len(points)))
