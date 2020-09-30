# -*- coding: utf-8 -*-
# @Time    : 2020/9/29 5:37 下午
# @Author  : Dawein
# @File    : L78_subsets.py
# @Software : PyCharm

"""
给定一组不含重复元素的整数数组nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。

示例:
输入: nums = [1,2,3]
输出:
[
  [3],
 [1],
 [2],
 [1,2,3],
 [1,3],
 [2,3],
 [1,2],
 []
]
"""

## 回溯法： 遍历当前元素，插入，然后合并下一个元素，插入，在合并下一个元素，插入；至遍历完，则回退一个继续

class Solution():

    def subsets(self, nums):
        if nums is None:
            return []
        if len(nums) == 0:
            return [[]]

        def backtrack(first=0, cur=[]):
            rst.append(cur[:])
            if first == n:
                return

            for i in range(first, n):
                cur.append(nums[i])
                backtrack(i+1, cur)
                cur.pop()

        rst = []
        n = len(nums)
        backtrack()
        return rst

## main
if __name__ == '__main__':
    s = Solution()
    print(s.subsets(nums=[1,2,3]))