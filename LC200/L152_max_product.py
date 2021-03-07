# -*- coding: utf-8 -*-
# @Time    : 2021/2/23 7:36 下午
# @Author  : Dawein
# @File    : L152_max_product.py
# @Software : PyCharm

"""
给你一个整数数组 nums，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
示例 1:
输入: [2,3,-2,4]
输出: 6
解释:子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释:结果不能为 2, 因为 [-2,-1] 不是子数组。
"""

class Solution():

    def maxProduct(self, nums):
        if nums is None or len(nums)==0:
            return None
        if len(nums) == 1:
            return nums[0]

        dp_max, dp_min = nums[0], nums[0]
        maxp = nums[0]
        for i in range(1, len(nums)):
            dp_max = max(nums[i], dp_max * nums[i], dp_min * nums[i])
            dp_min = min(nums[i], dp_max * nums[i], dp_min * nums[i])
            maxp = max(maxp, dp_max)
        return maxp

# main
if __name__ == '__main__':
    s = Solution()
    print(s.maxProduct(nums=[2,3,-2,4]))