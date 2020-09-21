# -*- coding: utf-8 -*-
# @Time    : 2020/8/19 7:22 下午
# @Author  : Dawein
# @File    : L27_remove_element.py
# @Software : PyCharm

"""
给你一个数组 nums和一个值 val，你需要 原地 移除所有数值等于val的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
"""

class Solution:

    def remove_element(self, arr: list, target: int)->list:

        if arr is None or len(arr) == 0:
            return []

        p0 = 0
        for i in range(len(arr)):
            if arr[i] != target:
                arr[p0] = arr[i]
                p0 = p0 + 1

        return arr[:p0]

# main
if __name__ == '__main__':
    arr = [3,2,2,3]
    s = Solution()
    print(s.remove_element(arr, 3))