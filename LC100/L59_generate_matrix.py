# -*- coding: utf-8 -*-
# @Time    : 2020/9/8 6:49 下午
# @Author  : Dawein
# @File    : L59_generate_matrix.py
# @Software : PyCharm


"""
给定一个正整数n，生成一个包含 1 到n^2所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:
输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""

class Solution():

    def generate_matrix(self, n:int):
        if n == 0:
            return [[]]
        if n == 1:
            return [[1]]

        left = 0
        right = n
        top = 0
        bottom = n
        value = 1
        rst = [[0 for _ in range(n)] for _ in range(n)]

        while left < right and top < bottom:
            for i in range(left, right):
                rst[top][i] = value
                value += 1

            for i in range(top+1, bottom):
                rst[i][right-1] = value
                value += 1

            for i in range(right-2, left, -1):
                rst[bottom-1][i] = value
                value += 1

            for i in range(bottom-1, top, -1):
                rst[i][left] = value
                value += 1

            left += 1
            right -= 1
            top += 1
            bottom -= 1

        return rst

# main
if __name__ == '__main__':
    s = Solution()
    print(s.generate_matrix(n=3))