import random


def select_fct(array, k):
    if len(array) <= 10:  # 边界条件
        array.sort()
        return array[k]
    pivot = get_pivot(array)  # 得到数组的支点数
    array_less, array_greater, array_equal = partition_array(array, pivot)  # 按照支点数划分数组
    if k < len(array_less):             # 所求数在支点数左边
        return select_fct(array_less, k)
    elif k < len(array_less) + len(array_equal):  # 所求数等于支点数
        return array_equal[0]
    else:             # 所求数在支点数右边
        normalized_k = k - (len(array_less) + len(array_greater))
        return select_fct(array_greater, normalized_k)


def get_pivot(array):
    """
        得到数组的支点数
    :param array:
    :return:
    """
    subset_size = 5  # 分割大小，每组5个
    subsets = []     # 记录各组元素
    num_medians = len(array) // subset_size  # 所分的组数
    if (len(array) % subset_size) > 0:  # 没有能够整除，即有余数，组数加一
        num_medians += 1
    for i in range(num_medians):
        begin = i * subset_size  # 每组的开头
        end = min(len(array), begin + subset_size)  # 每组的末尾
        subset = array[begin:end]  # 每组的元素
        subsets.append(subset)
    medians = []  # 记录每组的中间数
    for subset in subsets:
        median = select_fct(subset, len(subset)//2)  # 计算每一组的中间数
        medians.append(median)
    pivot = select_fct(medians, len(medians)//2)  # 中间数的中间数
    return pivot


def partition_array(array, pivot):
    """
        按照支点数划分数组
    :param array:
    :param pivot:
    :return:
    """
    array_less, array_greater, array_equal = [], [], []
    for item in array:
        if item < pivot:
            array_less.append(item)  # 比支点小的数
        elif item > pivot:
            array_greater.append(item)  # 比支点大的数
        else:
            array_equal.append(item)  # 等于支点的数
    return array_less, array_greater, array_equal


if __name__ == '__main__':
    num = 100
    array = [random.randint(1, 1000) for i in range(num)]
    random.shuffle(array)
    k = 7
    value = select_fct(array, k)
    print(value)
    sorted_array = sorted(array)
    print(sorted_array)
    assert sorted_array[k] == value
