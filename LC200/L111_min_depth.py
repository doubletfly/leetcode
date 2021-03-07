# -*- coding: utf-8 -*-
# @Time    : 2021/1/12 7:41 下午
# @Author  : Dawein
# @File    : L111_min_depth.py
# @Software : PyCharm

"""
给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
说明：叶子节点是指没有子节点的节点。

输入：root = [3,9,20,null,null,15,7]
输出：2
"""
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:

    def minDepth(self, root:TreeNode):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        # 如果左子树或右子树为空，则返回兄弟树的深度
        if left == 0:
            return right + 1
        if right == 0:
            return left + 1

        return min(left, right) + 1

# main
if __name__ == '__main__':

    # root = TreeNode(x=3, left=TreeNode(9),
    #                          right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))

    root = TreeNode(x=3,
                    right=TreeNode(20,
                                   right=TreeNode(7,
                                                  right=TreeNode(10))))

    s = Solution()
    rst = s.minDepth(root)
    print(rst)