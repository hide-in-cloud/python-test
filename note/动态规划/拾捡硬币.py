"""
    要求不能拾捡相邻的两个硬币，以获得累加面值最大的拾取子序列
"""


def bottom_up_coins(row_coins):
    table = [None] * (len(row_coins) + 1)  # 申明表格
    table[0] = 0
    table[1] = row_coins[0]
    for i in range(2, len(row_coins) + 1):
        table[i] = max(table[i - 1], table[i - 2] + row_coins[i - 1])  # 填表
    return table


def trace_back_coins(row_coins, table):
    select = []
    i = len(row_coins)  # i从表格最后一位索引
    while i >= 1:
        if table[i] > table[i - 1]:
            select.append(row_coins[i - 1])
            i -= 2
        else:
            i -= 1
    return select


if __name__ == '__main__':
    coins = [5, 1, 2, 10, 6, 2]
    table = bottom_up_coins(coins)
    select = trace_back_coins(coins, table)
    print(select)
