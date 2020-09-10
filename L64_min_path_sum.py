# -*- coding: utf-8 -*-
# @Time    : 2020/9/10 8:31 下午
# @Author  : Dawein
# @File    : L64_min_path_sum.py
# @Software : PyCharm

"""
给定一个包含非负整数的 mxn网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。

示例:
输入:
[
 [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
"""

class Solution():

    def min_path_sum(self, grid):

        rows = len(grid)
        cols = len(grid[0])

        path_sum = [[0 for _ in range(cols)] for _ in range(rows)]
        path_sum[0][0] = grid[0][0]
        for i in range(1, rows):
            path_sum[i][0] = path_sum[i-1][0] + grid[i][0]

        for i in range(1, cols):
            path_sum[0][i] = path_sum[0][i-1] + grid[0][i]

        for i in range(1, rows):
            for j in range(1, cols):
                path_sum[i][j] = min(path_sum[i-1][j], path_sum[i][j-1]) + grid[i][j]

        return path_sum[-1][-1]

# main
if __name__ == '__main__':
    s = Solution()
    grid = [[1,3,5],[1,5,1],[4,2,1]]
    print(s.min_path_sum(grid))