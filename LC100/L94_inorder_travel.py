# -*- coding: utf-8 -*-
# @Time    : 2020/10/20 6:44 下午
# @Author  : Dawein
# @File    : L94_inorder_travel.py
# @Software : PyCharm

"""
给定一个二叉树，返回它的中序 遍历。

示例:
输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Soluation():

    def inorder_travel(self, head:TreeNode):
        rst = []
        stack = []
        while head is not None or len(stack):
            while head is not None:
                stack.append(head)
                head = head.left

            # 弹出，写入rst
            head = stack[-1]
            stack.pop()
            rst.append(head.val)
            head = head.right

        return rst

# main
if __name__ == '__main__':
    s = Soluation()
    head = TreeNode(val=1,
                    left=None,
                    right=TreeNode(val=2, left=3, right=None))
    print(s.inorder_travel(head))