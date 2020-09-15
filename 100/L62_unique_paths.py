# -*- coding: utf-8 -*-
# @Time    : 2020/9/10 8:07 下午
# @Author  : Dawein
# @File    : L62_unique_paths.py
# @Software : PyCharm

"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
问总共有多少条不同的路径？

示例1:
输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右

示例2:
输入: m = 7, n = 3
输出: 28
"""

class Solution():

    def unique_paths(self, m:int, n:int):

        paths = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            paths[i][0] = 1
        for i in range(n):
            paths[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                paths[i][j] = paths[i-1][j] + paths[i][j-1]

        return paths[-1][-1]

# main
if __name__ == '__main__':
    s = Solution()
    print(s.unique_paths(m=3, n=2))