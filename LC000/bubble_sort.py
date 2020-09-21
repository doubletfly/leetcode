# -*- coding: utf-8 -*-
# @Time    : 2020/8/3 9:47 上午
# @Author  : Dawein
# @File    : bubble_sort.py
# @Software : PyCharm

"""
冒泡排序
"""

class BubbleSort:
    def __init__(self):
        pass

    def sort(self, array: list)->list:
        if array is None or len(array) <= 1:
            return array

        arr_len = len(array)
        for i in range(arr_len):
            for j in range(i, arr_len):
                if array[i] < array[j]:
                    array[i], array[j] = array[j], array[i]

        return array

# main
if __name__ == '__main__':
    x = [1,3,2,6,5,9,8]
    bs = BubbleSort()
    print(bs.sort(x))
