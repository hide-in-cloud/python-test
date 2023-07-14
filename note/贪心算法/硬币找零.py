def get_min_coins(amount_remain):
    coin_combinations = [1, 5, 10, 25, 100]
    coin_list = []
    sorted_coin_combinations = sorted(coin_combinations, reverse=True)  # 从大到小排序
    for coin_val in sorted_coin_combinations:
        coin_count = int(amount_remain / coin_val)  # 面值个数
        coin_list += [coin_val, ] * coin_count  # 将面值和张数添加到输出列表
        amount_remain -= coin_val * coin_count  # 计算剩余额度
        if amount_remain <= 0.0:
            break
    return coin_list


if __name__ == '__main__':
    print(get_min_coins(149))
