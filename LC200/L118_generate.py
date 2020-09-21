# -*- coding: utf-8 -*-
# @Time    : 2020/9/15 6:41 下午
# @Author  : Dawein
# @File    : L118_generate.py
# @Software : PyCharm

"""
给定一个非负整数 numRows，生成杨辉三角的前numRows行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:
输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution():

    def generate(self, numRows:int):
        if numRows == 1:
            return [1]

        rst = [[1]]
        for i in range(1, numRows):
            pre_line = i - 1
            tmp = [0] * (i + 1)
            for j in range(i+1):
                if j == 0:
                    tmp[j] = 1
                else:
                    if j >= len(rst[pre_line]):
                        tmp[j] = rst[pre_line][j-1]
                    else:
                        tmp[j] = rst[pre_line][j-1] + rst[pre_line][j]
            rst.append(tmp[:])
        return rst

# main
if __name__ == '__main__':
    s = Solution()
    print(s.generate(numRows=5))