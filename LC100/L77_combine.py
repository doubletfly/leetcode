# -*- coding: utf-8 -*-
# @Time    : 2020/9/28 6:57 下午
# @Author  : Dawein
# @File    : L77_combine.py
# @Software : PyCharm

"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:
输入:n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

## 回溯法：先往buffer中放一个元素，再遍历后面的元素，每次当buffer中元素个数等于给定的k时，则回退一个元素出来
## 再继续遍历下一个元素，直至所有元素都遍历完

class Solution():

    def combine(self, n, k):

        if n < k:
            return []


        def backtrack(first=0, cur=[]):
            if len(cur) == k:
                rst.append(cur[:])
                return

            for i in range(first, n):
                cur.append(i + 1)
                backtrack(i+1, cur)
                cur.pop()

        rst = []
        backtrack()
        return rst

## main
if __name__ == '__main__':
    s = Solution()
    print(s.combine(n=6, k=6))