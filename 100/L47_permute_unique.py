# -*- coding: utf-8 -*-
# @Time    : 2020/9/3 6:53 下午
# @Author  : Dawein
# @File    : L47_permute_unique.py
# @Software : PyCharm

"""
给定一个可包含重复数字的序列，返回所有不重复的全排列。
示例:
输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

class Solution():

    def permute_unique(self, nums:list)->list:

        if len(nums) == 0:
            return [[]]

        def backtrack(first=0):
            if first == n:
                output.append(nums[:])
                return
            for i in range(first, n):
                # 判断置换的两个元素是否相同，相同则不做排列
                if i != first and nums[i] == nums[first]:
                    continue
                nums[i], nums[first] = nums[first], nums[i]
                backtrack(first + 1)
                nums[i], nums[first] = nums[first], nums[i]

        output = []
        n = len(nums)
        backtrack()

        return output

# main
if __name__ == '__main__':
    nums = [1,1,1,2]
    s = Solution()
    print(s.permute_unique(nums))
