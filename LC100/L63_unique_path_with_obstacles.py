# -*- coding: utf-8 -*-
# @Time    : 2020/9/10 8:20 下午
# @Author  : Dawein
# @File    : L63_unique_path_with_obstacles.py
# @Software : PyCharm

"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
网格中的障碍物和空位置分别用 1 和 0 来表示。

说明：m和 n 的值均不超过 LC100。
示例1:
输入:
[
    [0,0,0],
    [0,1,0],
    [0,0,0]
]
输出: 2
解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
"""

class Solution():

    def unique_with_obstacles(self, obstacleGrid):

        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        paths = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            if obstacleGrid[i][0] == 1:
                break
            paths[i][0] = 1
        for i in range(cols):
            if obstacleGrid[0][i] == 1:
                break
            paths[0][i] = 1

        for i in range(1, rows):
            for j in range(1, cols):
                if obstacleGrid[i][j] == 1:
                    continue
                paths[i][j] = paths[i-1][j] + paths[i][j-1]

        return paths[-1][-1]

# main
if __name__ == '__main__':
    s = Solution()
    matrix = [[0,0,0,0],[0,1,1,0],[0,0,0,0]]
    print(s.unique_with_obstacles(obstacleGrid=matrix))