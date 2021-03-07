# -*- coding: utf-8 -*-
# @Time    : 2021/3/3 2:45 下午
# @Author  : Dawein
# @File    : L95_generate_trees.py
# @Software : PyCharm

"""
给定一个整数 n，生成所有由 1 ...n 为节点所组成的 二叉搜索树 。

示例：
输入：3
输出：
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释：
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

# 二叉搜索树： 左子树比根节点值小，右子树比根节点值大
# 遍历n，每一个i作为根节点，生成左右子树: 左子树[start, i-1], 右子树[i+1, end]

class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution():

    def generateTrees(self, n):
        if n is None or n==0:
            return []

        # backtrace
        def _generate(start, end):
            if start > end:
                return [None]

            res = []
            for i in range(start, end+1):
                # 生成左子树
                left_trees = _generate(start, i-1)

                # 生成右子树
                right_trees = _generate(i+1, end)

                for m in left_trees:
                    for n in right_trees:
                        trees = TreeNode(i)
                        trees.left = m
                        trees.right = n
                        res.append(trees)

            return res

        # main
        return _generate(1, n)

# main
if __name__ == '__main__':
    s = Solution()
    print(s.generateTrees(3))