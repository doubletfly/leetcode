# -*- coding: utf-8 -*-
# @Time    : 2021/1/11 6:10 下午
# @Author  : Dawein
# @File    : L104_max_depth.py
# @Software : PyCharm

"""
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
说明:叶子节点是指没有子节点的节点。
示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度3 。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1

# main
if __name__ == '__main__':

    root = TreeNode(x=3, left=TreeNode(9),
                         right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))

    s = Solution()
    rst = s.maxDepth(root)
    print(rst)