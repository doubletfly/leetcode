# -*- coding: utf-8 -*-
# @Time    : 2020/9/15 4:26 下午
# @Author  : Dawein
# @File    : L107_level_order_bottom.py
# @Software : PyCharm

"""
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
例如：
给定二叉树 [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

返回其自底向上的层次遍历为：
[
  [15,7],
  [9,20],
  [3]
]
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 基本思路：当下一层不为空时，返回下一层遍历组合；否则返回当前层左右子树组合
class Solution():

    def level_order_bottom(self, head:TreeNode):
        if head is None:
            return []

        rst = []
        def backtrack(left:TreeNode, right:TreeNode):
            if left is None and right is None:
                return []

            l, r = [], []
            if left is not None:
                l = backtrack(left.left, left.right)
            if right is not None:
                r = backtrack(right.left, right.right)
            tmp = []
            if len(l) ==0 and len(r) == 0:
                if left is not None:
                    tmp.append(left.val)
                if right is not None:
                    tmp.append(right.val)
            else:
                tmp += l
                tmp += r
            rst.append(tmp)
            return []


        backtrack(head, right=None)
        return rst


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
    print(s.level_order_bottom(head))
