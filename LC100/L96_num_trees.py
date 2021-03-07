# -*- coding: utf-8 -*-
# @Time    : 2021/3/3 7:58 下午
# @Author  : Dawein
# @File    : L96_num_trees.py
# @Software : PyCharm

"""
给定一个整数 n，求以1 ...n为节点组成的二叉搜索树有多少种？
示例:
输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

# 从1~n遍历n，作为根节点；假定当前遍历到i，则此时左子树构建1~i-1,右子树构建i+1~n
# 定义G(n)表示二叉搜索树的总数，可知公式为sum(G(i-1) * G(n-i))
class Solution():

    def numTrees(self, n):
        if n is None or n==0:
            return 0

        G = [0] * (n + 1)
        G[0] = 1
        G[1] = 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j]

        return G[n]

## main
if __name__ == '__main__':
    s = Solution()
    print(s.numTrees(n=3))