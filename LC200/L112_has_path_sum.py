# -*- coding: utf-8 -*-
# @Time    : 2020/9/15 6:30 下午
# @Author  : Dawein
# @File    : L112_has_path_sum.py
# @Software : PyCharm

"""
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
说明:叶子节点是指没有子节点的节点。
示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution():

    def has_path_sum(self, head:TreeNode, target:int):
        if head is None:
            return False
        if head.val == target and head.left is None and head.right is None:
            return True
        if head.val > target:
            return False

        l = self.has_path_sum(head.left, target - head.val)
        r = self.has_path_sum(head.right, target - head.val)
        if l or r:
            return True
        return False

# main
if __name__ == '__main__':
    head = TreeNode(5,
                    left=TreeNode(4,
                                  left=TreeNode(11,
                                                left=TreeNode(7),
                                                right=TreeNode(2))),
                    right=TreeNode(8,
                                   left=TreeNode(13),
                                   right=TreeNode(8,
                                                  right=TreeNode(1))))
    s = Solution()
    print(s.has_path_sum(head, target=22))