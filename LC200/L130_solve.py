# -*- coding: utf-8 -*-
# @Time    : 2021/1/13 5:05 下午
# @Author  : Dawein
# @File    : L130_solve.py
# @Software : PyCharm

"""
给定一个二维的矩阵，包含'X'和'O'（字母 O）。
找到所有被 'X' 围绕的区域，并将这些区域里所有的'O' 用 'X' 填充。

示例:
X X X X
X O O X
X X O X
X O X X
运行你的函数后，矩阵变为：
X X X X
X X X X
X X X X
X O X X
"""

class Solution:
    def solve(self, board):
        if board is None:
            return

        rows = len(board)
        cols = len(board[0])

        label = [[0 for _ in range(cols)] for _ in range(rows)]

        def fushi(i, j):
            # 上
            if label[max(0, i - 1)][j] == 1:
                label[max(0, i - 1)][j] = 0
                fushi(max(0, i - 1), j)

            # 下
            if label[min(rows - 1, i + 1)][j] == 1:
                label[min(rows - 1, i + 1)][j] = 0
                fushi(min(rows - 1, i + 1), j)

            # 左
            if label[i][max(0, j - 1)] == 1:
                label[i][max(0, j - 1)] = 0
                fushi(i, max(0, j - 1))

            # 右
            if label[i][min(cols - 1, j + 1)] == 1:
                label[i][min(cols - 1, j + 1)] = 0
                fushi(i, min(cols - 1, j + 1))

        for i in range(rows):
            for j in range(cols):
                value = board[i][j]
                if value == "O":
                    if i==0 or j==0 or i==rows-1 or j==cols-1:
                        fushi(i, j)
                    elif ((board[max(i-1, 0)][j] == "O" and label[max(i-1, 0)][j] ==0)
                          or (board[i][max(j-1, 0)]=="O" and label[i][max(j-1, 0)]==0)):
                        label[i][j] = 0
                    else:
                        label[i][j] = 1

        # copy
        for i in range(rows):
            for j in range(cols):
                if label[i][j] == 1 and board[i][j] == "O":
                    board[i][j] = "X"

# main
if __name__ == '__main__':
    # board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","O","X"]]
    # board = [["X","O","O","X","X","X","O","X","O","O"],["X","O","X","X","X","X","X","X","X","X"],["X","X","X","X","O","X","X","X","X","X"],["X","O","X","X","X","O","X","X","X","O"],["O","X","X","X","O","X","O","X","O","X"],["X","X","O","X","X","O","O","X","X","X"],["O","X","X","O","O","X","O","X","X","O"],["O","X","X","X","X","X","O","X","X","X"],["X","O","O","X","X","O","X","X","O","O"],["X","X","X","O","O","X","O","X","X","O"]]
    board = [["X","O","X","O","O","O","O"],
                ["X","O","O","O","O","O","O"],
                ["X","O","O","O","O","X","O"],
                ["O","O","O","O","X","O","X"],
                ["O","X","O","O","O","O","O"],
                ["O","O","O","O","O","O","O"],
                ["O","X","O","O","O","O","O"]]
    s = Solution()
    s.solve(board)
    print(board)
