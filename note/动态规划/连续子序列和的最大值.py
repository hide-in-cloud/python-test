def bottom_up_cout_subseq(alist):
    table = [None] * (len(alist) + 1)
    table[0] = 0
    for i in range(1, len(alist) + 1):
        table[i] = max(table[i - 1] + alist[i - 1], alist[i - 1])
    return table


def trace_back_subseq(alist, table):
    import numpy as np
    select = []
    max_sum = max(table)
    ind_max = np.argmax(table)  # 得到table中最大值的索引
    while ind_max >= 1:
        if table[ind_max] == table[ind_max - 1] + alist[ind_max - 1]:
            select.append(alist[ind_max - 1])
            ind_max -= 1
        else:
            select.append(alist[ind_max - 1])
            break
    return select


if __name__ == '__main__':
    subsequence = [-2, 11, -4, 13, -5, 2]
    table = bottom_up_cout_subseq(subsequence)
    select = trace_back_subseq(subsequence, table)
    print(select)
