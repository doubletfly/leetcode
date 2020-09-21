# -*- coding: utf-8 -*-
# @Time    : 2020/9/1 7:19 下午
# @Author  : Dawein
# @File    : L41_first_missing_positive.py
# @Software : PyCharm

"""
给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数
例如：
输入: [3,4,-1,1]
输出: 2
"""

class Solution():

    def first_missing_positive(self, nums: list)->int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1

## main
if __name__ == '__main__':
    nums = [3,4,-1,1]
    s = Solution()
    print(s.first_missing_positive(nums))