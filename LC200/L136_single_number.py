# -*- coding: utf-8 -*-
# @Time    : 2020/9/17 4:20 下午
# @Author  : Dawein
# @File    : L136_single_number.py
# @Software : PyCharm

"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:
输入: [2,2,1]
输出: 1

示例2:
输入: [4,1,2,1,2]
输出: 4
"""

# 位运算 - 异或
class Solution():

    def single_number(self, nums):
        rst = nums[0]
        for i in range(1, len(nums)):
            rst = rst ^ nums[i]
        return rst

# main
if __name__ == '__main__':
    s = Solution()
    print(s.single_number(nums=[4,1,2,1,2]))