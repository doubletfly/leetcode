# -*- coding: utf-8 -*-
# @Time    : 2020/8/6 7:40 下午
# @Author  : Dawein
# @File    : search_rotate_array.py
# @Software : PyCharm

"""
Leetcode - 33
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组[0,1,2,4,5,6,7]可能变为[4,5,6,7,0,1,2])。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回-1。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是O(logn) 级别

例 1:
输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1
"""

class SearchRotateArray:
    def __init__(self):
        pass

    def search(self, nums, target):
        if nums is None:
            return -1
        if target is None:
            return -1

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[0] < nums[mid]:
                # 左半部分有序
                # 如果target在左半部分有序中，则从左半部分找；否则，从有半部分找
                if nums[0] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # 右半部分有序
                # 如果target在右半部分有序中，则在右半部分找；否则，从左半部分找
                if nums[mid] <= target <= nums[len(nums) - 1]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

# main
if __name__ == '__main__':

    nums = [4,5,6,7,0,1,2]
    sra = SearchRotateArray()
    print(sra.search(nums, target=2))
