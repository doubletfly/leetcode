# -*- coding: utf-8 -*-
# @Time    : 2020/9/7 6:04 下午
# @Author  : Dawein
# @File    : L55_can_jump.py
# @Software : PyCharm

"""
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个位置。

示例1:
输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。

示例2:
输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
"""

# 记录一个目前能到达的最远距离，如果最远距离大于或等于最后一个位置，则直接返回True；
# 否则，遍历每一个位置并计算其能到达的最远距离
# 时间复杂度O(n), 空间复杂度O(1)
class Solution():

    def can_jump(self, nums: list)->bool:
        if len(nums) < 2:
            return True

        most_pos = 0
        n = len(nums) - 1
        for i in range(n):
            most_pos = max(most_pos, i + nums[i])
            if most_pos >= n:
                return True

        return False

# main
if __name__ == '__main__':
    nums = [3,2,1,1,4]
    s = Solution()
    print(s.can_jump(nums))