# -*- coding: utf-8 -*-
# @Time    : 2020/9/14 8:53 下午
# @Author  : Dawein
# @File    : L100_same_tree.py
# @Software : PyCharm

"""
给定两个二叉树，编写一个函数来检验它们是否相同。
如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():

    def is_same_tree(self, p:TreeNode, q:TreeNode):
        if p is None and q is None:
            return True
        if p is None and q is not None:
            return False
        if p is not None and q is None:
            return False

        if p.val != q.val:
            return False
        left = self.is_same_tree(p.left, q.left)
        right = self.is_same_tree(p.right, q.right)

        if left and right:
            return True
        return False

## main
if __name__ == '__main__':
    p = TreeNode(val=1, right=TreeNode(2))
    q = TreeNode(val=1, left=TreeNode(2))
    s = Solution()
    print(s.is_same_tree(p, q))