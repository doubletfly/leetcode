# -*- coding: utf-8 -*-
# @Time    : 2020/9/1 6:37 下午
# @Author  : Dawein
# @File    : L39_combination_sum.py
# @Software : PyCharm


"""
给定一个无重复元素的数组candidates和一个目标数target，找出candidates中所有可以使数字和为target的组合。
candidates中的数字可以无限制重复被选取。

说明：
所有数字（包括target）都是正整数。
解集不能包含重复的组合。
示例1：
输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]
"""

class Solution():

    # 思路：回溯法
    # 遍历第一个，回溯遍历查找，当等于时填充到输出中；当和值大于target时，结束回溯
    # 为了保证结果中不会重复，回溯填充的值当且仅能从当前位置开始往后遍历
    def combination_sum(self, candidates: list, target: int):

        def backtrack(first=0, curr=[]):
            if sum(curr) == target:
                output.append(curr[:])
                return
            if sum(curr) > target:
                return
            for i in range(first, n):
                curr.append(candidates[i])
                backtrack(i, curr)
                curr.pop()

        output = []
        n = len(candidates)
        backtrack()
        return output

##
if __name__ == '__main__':
    candidates = [2,3,5]
    target = 9
    s = Solution()
    print(s.combination_sum(candidates, target))