# 二分查找的模板


def biany_search(array, target):
    left, right = 0, len(array) - 1

    while left <= right:  # 假如还有搜索范围
        mid = (left + right) // 2

        if target > array[mid]:
            left = mid + 1
        elif target < array[mid]:
            right = mid -1
        else:
            return mid

    return None


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 34, 56, 78]
    print(biany_search(array, 78))
