# -*- coding: utf-8 -*-
# @Time    : 2021/1/11 4:53 下午
# @Author  : Dawein
# @File    : L102_level_order.py
# @Software : PyCharm

"""
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

示例：
二叉树：[3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回其层序遍历结果：
[
  [3],
  [9,20],
  [15,7]
]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode):

        # define a global buffer
        results = []

        if root is None:
            return results

        def dfs(index, r):
            if len(results) < index:
                results.append([])

            results[index - 1].append(r.val)
            if r.left is not None:
                dfs(index + 1, r.left)
            if r.right is not None:
                dfs(index + 1, r.right)

        dfs(1, root)
        return results

# main
if __name__ == '__main__':

    root = TreeNode(x=3, left=TreeNode(9),
                         right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))

    s = Solution()
    rst = s.levelOrder(root)
    print(rst)
