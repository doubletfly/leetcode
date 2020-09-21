# -*- coding: utf-8 -*-
# @Time    : 2020/9/2 8:09 下午
# @Author  : Dawein
# @File    : L46_permute.py
# @Software : PyCharm

"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

## 基本思路：采用回溯法
class Solution():

    def permute(self, nums: list)->list:
        if len(nums) == 0:
            return []

        def backtrack(first=0):
            if first == n:
                output.append(nums[:])
                return
            for i in range(first, n):
                nums[i], nums[first] = nums[first], nums[i]
                backtrack(first + 1)
                nums[i], nums[first] = nums[first], nums[i]


        output = []
        n = len(nums)
        backtrack()
        return output

# main
if __name__ == '__main__':
    nums = [1,2,3,4]
    s = Solution()
    print(s.permute(nums))