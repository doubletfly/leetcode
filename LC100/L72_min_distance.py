# -*- coding: utf-8 -*-
# @Time    : 2020/9/27 7:20 下午
# @Author  : Dawein
# @File    : L72_min_distance.py
# @Software : PyCharm

"""
给你两个单词word1 和word2，请你计算出将word1转换成word2 所使用的最少操作数。
你可以对一个单词进行如下三种操作：
插入一个字符
删除一个字符
替换一个字符

示例1：
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')

示例2：
输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
"""

## 动态规划
## 操作可以转换成：
## 1、将A字符串变成B的前n-1个字符串，然后在插入一个字符 - D[i][j-1] + 1
## 2、将A的前n-1个字符串变成B字符串，然后删除一个字符 - D[i-1][j] + 1
## 3、将A的前n-1个字符串变成B的前n-1个字符串，然后替换一个字符 - D[i-1][j-1] + 1
## 另外，需要注意的是，当A的第n字符 == B的第n字符时是不需要任何操作的。

class Solution():

    def min_distance(self, word1, word2):

        len1 = len(word1)
        len2 = len(word2)

        if len1 * len2 == 0:
            return len1 + len2

        Dij = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]

        for i in range(len1 + 1):
            Dij[i][0] = i

        for j in range(len2 + 1):
            Dij[0][j] = j


        for i in range(1, len1+1):
            for j in range(1, len2+1):
                c1 = Dij[i-1][j] + 1
                c2 = Dij[i][j-1] + 1
                if word1[i-1] == word2[j-1]:
                    c3 = Dij[i - 1][j - 1]
                else:
                    c3 = Dij[i - 1][j - 1] + 1
                Dij[i][j] = min(c1, c2, c3)

        return Dij[len1][len2]

## main
if __name__ == '__main__':
    s = Solution()
    print(s.min_distance(word1="intention", word2="execution"))