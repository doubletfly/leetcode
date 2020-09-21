# -*- coding: utf-8 -*-
# @Time    : 2020/9/15 5:39 下午
# @Author  : Dawein
# @File    : L110_is_balanced.py
# @Software : PyCharm
"""
给定一个二叉树，判断它是否是高度平衡的二叉树。
本题中，一棵高度平衡二叉树定义为：
一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():

    def is_balanced(self, head:TreeNode):
        if head is None:
            return True

        def backtrack(root:TreeNode):
            if root is None:
                return 0
            if root.left is None and root.right is None:
                return 1

            left_depth = backtrack(root.left)
            right_depth = backtrack(root.right)

            depth = max(left_depth, right_depth) + 1
            return depth

        left = backtrack(head.left)
        right = backtrack(head.right)
        if abs(left - right) > 1:
            return False
        return True

# main
if __name__ == '__main__':
    head = TreeNode(val=3,
                    left=TreeNode(9),
                    right=TreeNode(20,
                                   left=TreeNode(15),
                                   right=TreeNode(7)))

    s = Solution()
    print(s.is_balanced(head))
