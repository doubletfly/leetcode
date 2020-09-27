# -*- coding: utf-8 -*-
# @Time    : 2020/9/22 8:17 下午
# @Author  : Dawein
# @File    : L53_max_sub_array.py
# @Software : PyCharm

"""
给定一个整数数组 nums，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:
输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释:连续子数组[4,-1,2,1] 的和最大，为6。
进阶:
如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
"""

class Solution():

    def max_sub_array(self, nums):

        max_v = 0
        sum_v = 0
        for x in nums:
            sum_v += x
            if sum_v < 0:
                sum_v = 0
            else:
                max_v = max(sum_v, max_v)

        return max_v

# main
if __name__ == '__main__':
    s = Solution()
    print(s.max_sub_array(nums=[-2,1,-3,4,-1,2,1,-5,4]))