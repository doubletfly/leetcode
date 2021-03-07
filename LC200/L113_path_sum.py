# -*- coding: utf-8 -*-
# @Time    : 2021/1/12 7:58 下午
# @Author  : Dawein
# @File    : L113_path_sum.py
# @Software : PyCharm

"""
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
说明:叶子节点是指没有子节点的节点。
示例:
给定如下二叉树，以及目标和sum = 22，
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:
[
   [5,4,11,2],
   [5,8,4,5]
]
"""
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

# 需要注意的点 - 数中的节点值可能会是负数
class Solution:
    def pathSum(self, root:TreeNode, sum):

        # global
        results = []
        paths = []

        def sub(node:TreeNode, residual):
            if node is None:
                return
            paths.append(node.val)
            residual -= node.val

            # 遍历到叶子节点且剩余为0，则找到一条路径
            if node.left is None and node.right is None and residual==0:
                results.append(paths[:])

            # 继续遍历左子树、右子树
            sub(node.left, residual)
            sub(node.right, residual)

            # 遍历完没有找到，弹出最后插入的元素
            paths.pop()

        # ---
        sub(root, sum)
        return results

# main
if __name__ == '__main__':

    root = TreeNode(5, left=TreeNode(4, left=TreeNode(11, left=TreeNode(7), right=TreeNode(2))),
                        right=TreeNode(8, left=TreeNode(13),
                                            right=TreeNode(4, left=TreeNode(5), right=TreeNode(1))))

    s = Solution()
    results = s.pathSum(root, 22)
    print(results)