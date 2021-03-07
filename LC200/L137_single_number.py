# -*- coding: utf-8 -*-
# @Time    : 2021/1/15 2:58 下午
# @Author  : Dawein
# @File    : L137_single_number.py
# @Software : PyCharm

"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。
说明：你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:
输入: [2,2,3,2]
输出: 3

示例2:
输入: [0,1,0,1,0,1,99]
输出: 99
"""

class Solution():

    def singleNumber(self, nums):
        if nums is None or len(nums) == 0:
            return -1

        seen_once = 0
        seen_twice = 0

        for k in nums:
            seen_once = ~seen_twice & (seen_once ^ k)
            seen_twice = ~seen_once & (seen_twice ^ k)

        return seen_once

# main
if __name__ == '__main__':
    nums = [-2,-2,-3,-2]
    result = Solution().singleNumber(nums)
    print(result)