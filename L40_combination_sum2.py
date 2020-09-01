# -*- coding: utf-8 -*-
# @Time    : 2020/9/1 6:58 下午
# @Author  : Dawein
# @File    : L40_combination_sum2.py
# @Software : PyCharm

"""
给定一个无重复元素的数组candidates和一个目标数target，找出candidates中所有可以使数字和为target的组合。
candidates中的数字只能被选取一次。

说明：
所有数字（包括target）都是正整数。
解集不能包含重复的组合。
示例1：
输入：candidates = [2,3,5,7], target = 7,
所求解集为：
[
  [2, 5]
  [7]
]
"""

class Solution():

    def combination_sum2(self, candidates: list, target: int):

        def backtrack(first=0, curr=[]):
            if sum(curr) == target:
                output.append(curr[:])
                return
            if sum(curr) > target:
                return
            for i in range(first, n):
                curr.append(candidates[i])
                backtrack(first+1, curr)
                curr.pop()

        output = []
        n = len(candidates)
        backtrack()
        return output

# main
if __name__ == '__main__':
    candidates = [2,3,5,7]
    target = 7
    s = Solution()
    print(s.combination_sum2(candidates, target))