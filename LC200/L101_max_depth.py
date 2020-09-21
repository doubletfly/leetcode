# -*- coding: utf-8 -*-
# @Time    : 2020/9/15 4:18 下午
# @Author  : Dawein
# @File    : L101_max_depth.py
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
返回它的最大深度3。
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():

    def max_depth(self, head:TreeNode):
        if head is None:
            return 0
        if head.left is None and head.right is None:
            return 1

        left_depth = self.max_depth(head.left)
        right_depth = self.max_depth(head.right)
        depth = max(left_depth, right_depth) + 1
        return depth

# main
if __name__ == '__main__':
    head = TreeNode(val=3,
                    left=TreeNode(9),
                    right=TreeNode(20,
                                   left=TreeNode(15,
                                                 left=TreeNode(10,
                                                               right=TreeNode(5))),
                                   right=TreeNode(7)))
    s = Solution()
    print(s.max_depth(head))