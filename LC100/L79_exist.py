# -*- coding: utf-8 -*-
# @Time    : 2020/9/29 5:59 下午
# @Author  : Dawein
# @File    : L79_exist.py
# @Software : PyCharm

"""
给定一个二维网格和一个单词，找出该单词是否存在于网格中。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false
"""

class Solution():

    def exist(self, board, word):

        if word == "":
            return False

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def search(i, j, k):
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True

            visited.add((i, j))
            # 上下左右搜索
            rst = False
            for di, dj in directions:
                i_ = i + di
                j_ = j + dj
                if (i_, j_) in visited:
                    continue
                if 0 <= i_ < rows and 0 <= j_ < cols:
                    if search(i_, j_, k+1):
                        rst = True
                        break

            visited.remove((i, j))
            return rst

        rows = len(board)
        cols = len(board[0])
        visited = set()
        for i in range(rows):
            for j in range(cols):
                if search(i, j, 0):
                    return True

        return False

## main
if __name__ == '__main__':
    s = Solution()
    print(s.exist(board=[['A','B','C','E'],['S','F','C','S'], ['A','D','E','E']],
                  word="ABCCED"))
