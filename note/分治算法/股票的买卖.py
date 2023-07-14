def max_profit_simple(prices):
    """
        暴力算法
    :param prices: 股票价格的数据
    :return: 买入和卖出的时间点，最大利润值
    """
    max_profit = 0  # 记录当前最优值
    index_best = []  # 记录买进和卖出的时间点
    len_prices = len(prices)
    for i in range(len_prices):
        for j in range(i + 1, len_prices):
            if prices[j] - prices[i] > max_profit:
                max_profit = prices[j] - prices[i]
                index_best = [i, j]
    return index_best, max_profit


def max_profit_dc(prices):
    len_prices = len(prices)
    if len_prices <= 1:  # 边界条件
        return 0
    mid = len_prices // 2
    prices_left = prices[:mid]
    prices_right = prices[mid:]
    maxProfit_left = max_profit_dc(prices_left)     # 递归求解左子序列
    maxProfit_right = max_profit_dc(prices_right)   # 递归求解右子序列
    maxProfit_left_right = max(prices_right) - min(prices_left)  # 考虑跨界情况
    return max(maxProfit_left, maxProfit_right, maxProfit_left_right)


if __name__ == '__main__':
    prices = [13, 17, 15, 8, 14, 15, 19, 6, 7, 9]
    max_profit = max_profit_dc(prices)
    print(max_profit)
