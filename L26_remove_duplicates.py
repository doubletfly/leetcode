# -*- coding: utf-8 -*-
# @Time    : 2020/8/19 1:50 下午
# @Author  : Dawein
# @File    : L26_remove_duplicates.py
# @Software : PyCharm

"""
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成
"""

class Solution:

    def remove_duplicates(self, arr: list)->list:
        if arr is None or len(arr) <= 1:
            return arr

        p1 = 0
        for p2 in range(1, len(arr)):
            if arr[p1] != arr[p2]:
                p1 = p1 + 1
                arr[p1] = arr[p2]

        return arr[:p1+1]


# main
if __name__ == '__main__':
    arr = [0]
    s = Solution()
    print(s.remove_duplicates(arr))