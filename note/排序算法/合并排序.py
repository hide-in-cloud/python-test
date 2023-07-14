def merge_sort(A):
    if len(A) <= 1:
        return A
    middle = len(A) // 2
    leftA = A[:middle]
    rightA = A[middle:]
    leftA_Sorted = merge_sort(leftA)
    rightA_Sorted = merge_sort(rightA)
    return merge(leftA_Sorted, rightA_Sorted)


def merge(leftS, rightR):
    i, j = 0, 0
    alist = []
    while i < len(leftS) and j < len(rightR):
        if leftS[i] < rightR[j]:
            alist.append(leftS[i])
            i += 1
        else:
            alist.append(rightR[j])
            j += 1
    while i < len(leftS):
        alist.append(leftS[i])
        i += 1
    while j < len(rightR):
        alist.append(rightR[j])
        j += 1
    return alist


if __name__ == '__main__':
    A = [2, 7, 5, 9, 6, 4, 10, 1]
    print(merge_sort(A))
