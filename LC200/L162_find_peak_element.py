# -*- coding: utf-8 -*-
# @Time    : 2021/2/24 8:19 下午
# @Author  : Dawein
# @File    : L162_find_peak_element.py
# @Software : PyCharm

"""
峰值元素是指其值大于左右相邻值的元素。
给你一个输入数组nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。
你可以假设nums[-1] = nums[n] = -∞ 。

示例 1：
输入：nums = [1,2,3,1]
输出：2
解释：3 是峰值元素，你的函数应该返回其索引 2。
示例2：

输入：nums = [1,2,1,3,5,6,4]
输出：1 或 5
解释：你的函数可以返回索引 1，其峰值元素为 2；
    或者返回索引 5， 其峰值元素为 6。
"""

class Solution():

    def findPeakElement(self, nums):

        if nums is None or len(nums) == 0:
            return None

        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1

        return left

# main
if __name__ == '__main__':
    s = Solution()
    print(s.findPeakElement(nums=[1,2,1,3,5,6,4]))