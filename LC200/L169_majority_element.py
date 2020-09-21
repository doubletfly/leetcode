# -*- coding: utf-8 -*-
# @Time    : 2020/9/18 6:39 下午
# @Author  : Dawein
# @File    : L169_majority_element.py
# @Software : PyCharm

"""
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例1:
输入: [3,2,3]
输出: 3

示例2:
输入: [2,2,1,1,1,2,2]
输出: 2
"""

class Solution():

    # 分治法
    def majority_element_1(self, nums):
        def majority_rec(lo, lh):

            if lo == lh:
                return nums[lo]

            mid = (lh - lo) // 2 + lo
            left = majority_rec(lo, mid)
            right = majority_rec(mid+1, lh)

            if left == right:
                return left

            left_count = sum(1 for i in range(lo, lh + 1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, lh + 1) if nums[i] == right)

            if left_count > right_count:
                return left
            else:
                return right

        return majority_rec(0, len(nums)-1)

    # 投票法
    def majority_element_2(self, nums):

        candidate = 0
        count = 0
        for value in nums:
            if count == 0:
                candidate = value
                count += 1
                continue

            if value == candidate:
                count += 1
            else:
                count -= 1

        return candidate

## main
if __name__ == '__main__':
    s = Solution()
    print(s.majority_element_1(nums=[2,2,1,1,1,2,2]))
    print(s.majority_element_2(nums=[2,2,1,1,1,2,1]))
