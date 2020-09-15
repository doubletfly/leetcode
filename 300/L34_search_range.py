# -*- coding: utf-8 -*-
# @Time    : 2020/8/6 8:03 下午
# @Author  : Dawein
# @File    : L34_search_range.py
# @Software : PyCharm

"""
leetcode - 34
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
你的算法时间复杂度必须是O(log n) 级别。
如果数组中不存在目标值，返回[-1, -1]。

示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]

示例2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]

"""

class SearchRange:
    def __init__(self):
        pass

    def sub_search(self, nums, target, d_left):
        lf = 0
        rt = len(nums)
        while lf < rt:
            mid = (lf + rt) // 2
            if nums[mid] > target or (d_left and nums[mid]==target):
                rt = mid
            else:
                lf = mid + 1

        return lf

    def search(self, nums, target):
        if nums is None or len(nums) == 0:
            return [-1, -1]
        if target is None:
            return [-1, -1]

        left_index = self.sub_search(nums, target, d_left=True)
        if left_index == len(nums) or nums[left_index] != target:
            return [-1, -1]

        right_index = self.sub_search(nums, target, d_left=False) - 1

        return [left_index, right_index]

# main
if __name__ == '__main__':

    nums = [5,7,7,8,8,10]
    sr = SearchRange()
    print(sr.search(nums, target=10))
