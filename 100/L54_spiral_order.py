# -*- coding: utf-8 -*-
# @Time    : 2020/9/4 6:41 下午
# @Author  : Dawein
# @File    : L54_spiral_order.py
# @Software : PyCharm

"""
给定一个包含m x n个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例1:
输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
"""

class Solution():

    def spiral_order(self, matrix):

        if len(matrix) == 0:
            return []

        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)

        rst = []
        while left < right and top < bottom:
            # from left to right
            for i in range(left, right):
                rst.append(matrix[top][i])

            # from top to bottom
            for i in range(top+1, bottom):
                rst.append(matrix[i][right-1])

            # from right to left
            for i in range(right-2, left, -1):
                rst.append(matrix[bottom-1][i])

            # from bottom to top
            for i in range(bottom-1, top, -1):
                rst.append(matrix[i][left])

            left += 1
            right -= 1
            top += 1
            bottom -= 1

        return rst

## main
if __name__ == '__main__':
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9,10,11,12]]
    # [1,2,3,4,8,12,11,10,9,5,6,7]
    s = Solution()
    print(s.spiral_order(matrix))