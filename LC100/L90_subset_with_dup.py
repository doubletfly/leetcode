# -*- coding: utf-8 -*-
# @Time    : 2020/10/15 6:02 下午
# @Author  : Dawein
# @File    : L90_subset_with_dup.py
# @Software : PyCharm

"""
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。

示例:
输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

class Solution():

    def subset_with_dup(self, nums):
        if nums is None or len(nums) == 0:
            return [[]]

        nums.sort(key=lambda x: x, reverse=False)
        def backtrack(first=0, cur=[]):
            if cur not in rst:
                rst.append(cur[:])
            if first == n:
                return

            for i in range(first, n):
                cur.append(nums[i])
                backtrack(i + 1, cur)
                cur.pop()

        n = len(nums)
        rst = []
        backtrack()
        return rst

## main
if __name__ == '__main__':
    s = Solution()
    print(s.subset_with_dup(nums=[4,4,4,1,4]))