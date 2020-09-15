# -*- coding: utf-8 -*-
# @Time    : 2020/8/19 8:04 下午
# @Author  : Dawein
# @File    : L35_search_insert.py
# @Software : PyCharm

"""
给定一个排序数组（升序）和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素
"""

class Solution:

    def search_insert(self, nums: list, target: int)->list:
        if nums is None or target is None:
            return None

        if len(nums) == 0:
            return [target]

        for index in range(len(nums)):
            if nums[index] == target:
                return index

            if nums[index] > target:
                return index

            if nums[index] < target and index==len(nums)-1:
                return len(nums)

# main
if __name__ == '__main__':
    s = Solution()
    print(s.search_insert(nums=[1,3,4,5,6], target=2))