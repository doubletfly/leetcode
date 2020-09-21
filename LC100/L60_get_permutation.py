# -*- coding: utf-8 -*-
# @Time    : 2020/9/8 7:00 下午
# @Author  : Dawein
# @File    : L60_get_permutation.py
# @Software : PyCharm

"""
给出集合[1,2,3,…,n]，其所有元素共有n! 种排列。
按大小顺序列出所有排列情况，并一一标记，当n = 3 时, 所有排列如下：
"123"
"132"
"213"
"231"
"312"
"321"
给定n 和k，返回第k个排列。

说明：
给定 n的范围是 [1, 9]。
给定 k的范围是[1, n!]。
示例1:
输入: n = 3, k = 3
输出: "213"

示例2:
输入: n = 4, k = 9
输出: "2314"
"""

class Solution():

    def get_permutation(self, n:int, k:int)->list:

        nums = [str(i + 1) for i in range(n)]
        outputs = [""]
        count = [0]
        n = len(nums)

        def backtrack(first=0):
            if first == n:
                count[0] += 1
                if count[0] == k:
                    outputs[0] = nums[:]
                return
            if len(outputs[0]) != 0:
                return

            for i in range(first, n):
                nums[i], nums[first] = nums[first], nums[i]
                backtrack(first + 1)
                nums[i], nums[first] = nums[first], nums[i]

        backtrack()
        return ''.join(outputs[0])

# main
if __name__ == '__main__':
    s = Solution()
    print(s.get_permutation(n=4, k=9))