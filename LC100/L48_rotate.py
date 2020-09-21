# -*- coding: utf-8 -*-
# @Time    : 2020/9/3 6:58 下午
# @Author  : Dawein
# @File    : L48_rotate.py
# @Software : PyCharm

"""
给定一个 n×n 的二维矩阵表示一个图像。
将图像顺时针旋转 90 度。

说明：
你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像
"""

## 基本思路： 先将图像做对称变换，然后对列进行左右置换
class Solution():

    def rotate(self, matrix):
        if len(matrix) == 0:
            return matrix

        rows = len(matrix)
        cols = len(matrix[0])
        if rows != cols:
            return None

        # 对称置换
        print("previous: ", matrix)
        for i in range(rows):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print("after: ", matrix)

        # 列左右置换
        left = 0
        right = cols - 1
        while left < right:
            for i in range(rows):
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
            left += 1
            right -= 1
        print("after: ", matrix)

        return matrix

## main
if __name__ == '__main__':
    # matrix = [[1,2,3], [4,5,6], [7,8,9]]
    matrix = [[ 5, 1, 9,11], [ 2, 4, 8,10], [13, 3, 6, 7], [15,14,12,16]]
    s = Solution()
    print(s.rotate(matrix))