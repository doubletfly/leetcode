# -*- coding: utf-8 -*-
# @Time    : 2020/10/13 5:59 下午
# @Author  : Dawein
# @File    : L89_gray_code.py
# @Software : PyCharm

"""
格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。
给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。即使有多个不同答案，你也只需要返回其中一种。
格雷编码序列必须以 0 开头。

示例 1:
输入:2
输出:[0,1,3,2]
解释:
00 - 0
01 - 1
11 - 3
10 - 2
对于给定的n，其格雷编码序列并不唯一。
例如，[0,2,3,1]也是一个有效的格雷编码序列。
00 - 0
10 - 2
11 - 3
01 - 1
"""

## 基本思路：回溯法
class Solution():

    def gray_code(self, n):
        if n == 0:
            return [0]

        candidates = [0, 1]
        def backtrack(first=0, cur=[]):
            if len(cur) == n:
                rst.append(int("".join([str(w) for w in cur[:]]), 2))
                # rst.append(cur[:])
                return

            for i in range(0, len(candidates)):
                cur.append(candidates[i])
                candidates[i], candidates[first] = candidates[first], candidates[i]
                backtrack(i, cur)
                candidates[i], candidates[first] = candidates[first], candidates[i]
                cur.pop()

        rst = []
        backtrack()
        return rst


## main
if __name__ == '__main__':
    s = Solution()
    print(s.gray_code(n=3))