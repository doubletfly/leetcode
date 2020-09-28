# -*- coding: utf-8 -*-
# @Time    : 2020/9/28 6:17 下午
# @Author  : Dawein
# @File    : L74_search_matrix.py
# @Software : PyCharm

"""
编写一个高效的算法来判断m x n矩阵中，是否存在一个目标值。该矩阵具有如下特性：
每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
示例1:
输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
输出: true

示例2:
输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
输出: false
"""

## 基本思路： 将矩阵当做一个数组，然后按照二分查找的方法
## 时间复杂度： O(log(m*n))
class Solution():

    def search_matrix(self, matrix, target):

        rows = len(matrix)
        cols = len(matrix[0])

        totals = rows * cols

        def search(low, high):
            if low >= high:
                return False

            i = low // cols
            j = low % cols
            if matrix[i][j] == target:
                return True

            i = high // cols
            j = high % cols
            if matrix[i][j] == target:
                return True

            mid = (low + high) // 2
            i = mid // cols
            j = mid % cols
            if matrix[i][j] == target:
                return True

            if matrix[i][j] < target:
                return search(mid + 1, high)
            else:
                return search(low, mid - 1)

        return search(0, totals-1)

## main
if __name__ == '__main__':
    s = Solution()
    print(s.search_matrix(matrix=[[1,  3,  5,  7], [10, 11, 16, 20], [23, 30, 34, 50]],
                          target=6))