# -*- coding: utf-8 -*-
# @Time    : 2020/9/21 7:54 下午
# @Author  : Dawein
# @File    : L189_rotate.py
# @Software : PyCharm

"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
"""

class Solution():

    def rotate(self, nums, k):
        if len(nums) == 0:
            return nums
        if k == 0:
            return nums

        if k == len(nums):
            return nums

        k = k % len(nums)

        def reverse(arrs, start, end):
            while start < end:
                arrs[start], arrs[end] = arrs[end], arrs[start]
                start += 1
                end -= 1

        # 1. 反转整个数组
        reverse(nums, start=0, end=len(nums)-1)

        # 2. 反转数组前k个
        reverse(nums, start=0, end=k-1)

        # 3. 反转数组后n-k个
        reverse(nums, start=k, end=len(nums)-1)

        return nums

# main
if __name__ == '__main__':
    s = Solution()
    print(s.rotate(nums=[-1,-100,3,99], k=2))