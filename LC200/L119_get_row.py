# -*- coding: utf-8 -*-
# @Time    : 2020/9/15 6:52 下午
# @Author  : Dawein
# @File    : L119_get_row.py
# @Software : PyCharm

"""
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:
输入: 3
输出: [1,3,3,1]

进阶：
你可以优化你的算法到 O(k) 空间复杂度吗？
"""

class Solution():

    def get_row(self, rowIndex):
        if rowIndex == 0:
            return [1]

        rst = [0] * (rowIndex + 1)
        for i in range((rowIndex + 1) // 2 + 1):
            if i == 0:
                rst[i] = 1
            else:
                rst[i] = rst[i-1] * (rowIndex - i + 1) // i  # rst[i-1] * (n - i + 1) / i
            rst[rowIndex-i] = rst[i]
        return rst

# main
if __name__ == '__main__':
    s = Solution()
    print(s.get_row(rowIndex=3))
