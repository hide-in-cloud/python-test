def count_inversions_simple(A):
    """
        暴力算法
    :param A: 序列
    :return: inv_count:统计有多少对逆序   inv_list:记录每一对逆序
    """
    inv_count = 0
    inv_list = []  # 用于记录每一对逆序
    lenA = len(A)
    for i in range(lenA):
        for j in range(i + 1, lenA):
            if A[i] > A[j]:
                inv_count += 1
                inv_list.append((A[i], A[j]))
    return inv_count, inv_list


def count_inversions_dc(A):
    """
        分治算法
    :param A:
    :return:
    """
    lenA = len(A)
    if lenA <= 1:
        return 0, A
    mid = lenA//2
    leftA = A[:mid]
    rightA = A[mid:]
    countLA, leftA = count_inversions_dc(leftA)  # 递归分解
    countRA, rightA = count_inversions_dc(rightA)  # 递归分解
    countLRA, mergedA = merge_and_count(leftA, rightA)  # 合并并计算逆序数
    return countLA+countRA+countLRA, mergedA


def merge_and_count(A, B):
    """
        合并计数，边排序边计算
    :param A:有序的序列
    :param B:有序的序列
    :return: inv_count:逆序数
             alist:排好序的序列
    """
    i, j, inv_count = 0, 0, 0
    alist = []
    lenA = len(A)
    lenB = len(B)
    while i < lenA and j < lenB:
        if A[i] > B[j]:            # 构成逆序
            inv_count += lenA - i  # B[j]与A当前及其所有右边的元素构成逆序
            alist.append(B[j])
            j += 1
        else:
            alist.append(A[i])
            i += 1
    while i < lenA:                # 处理A中剩余元素
        alist.append(A[i])
        i += 1
    while j < lenB:                # 处理B中剩余元素
        alist.append(B[j])
        j += 1
    return inv_count, alist


if __name__ == '__main__':
    A = [2, 4, 1, 3, 5]
    B = [3, 4, 1, 5, 2]
    inv_count, inv_list = count_inversions_dc(A)
    print(inv_list)
    print(inv_count)
