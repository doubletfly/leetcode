# -*- coding: utf-8 -*-
# @Time    : 2020/9/27 7:46 下午
# @Author  : Dawein
# @File    : L73_set_zeros.py
# @Software : PyCharm

"""
给定一个m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

示例1:
输入:
[
 [1,1,1],
 [1,0,1],
 [1,1,1]
]
输出:
[
 [1,0,1],
 [0,0,0],
 [1,0,1]
]

示例2:
输入:
[
 [0,1,2,0],
 [3,4,5,2],
 [1,3,1,5]
]
输出:
[
 [0,0,0,0],
 [0,4,5,0],
 [0,3,1,0]
]
"""


class Solution():

    def set_zeros(self, matrix):

        is_col = False
        rows = len(matrix)
        cols = len(matrix[0])

        # 利用每行和每列的第一个元素作为标记；若当前的值为0，则将其所在的行和列的第一个元素置为0
        # 但当第一列有元素为0时，这一行才会被置为0
        for i in range(rows):
            if matrix[i][0] == 0:
                is_col = True
                continue
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # 重新遍历矩阵，当行或列的第一个元素为0时，则将行和列上的元素置为0
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        ## 第一行是否要置为0
        if matrix[0][0] == 0:
            for j in range(cols):
                matrix[0][j] = 0

        ## 第一列是否要置为0
        if is_col:
            for i in range(rows):
                matrix[i][0] = 0

        return matrix

## main
if __name__ == '__main__':
    s = Solution()
    print(s.set_zeros(matrix=[[0,1,2,0], [3,4,5,2], [1,3,1,5]]))