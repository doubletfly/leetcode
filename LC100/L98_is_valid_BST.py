# -*- coding: utf-8 -*-
# @Time    : 2021/3/4 7:07 下午
# @Author  : Dawein
# @File    : L98_is_valid_BST.py
# @Software : PyCharm

"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。
假设一个二叉搜索树具有如下特征：
节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例1:
输入:
    2
   / \
  1   3
输出: true

示例2:
输入:
    5
   / \
  1   4
    / \
   3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
    根节点的值为 5 ，但是其右子节点值为 4 。
"""

# 二叉搜索的性质： 左子树的所有值小于根节点的值，右子树的所有值大于根节点的值
# 子树也应该满足二叉搜索树的性质
class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root:TreeNode):
        if root is None:
            return False

        # 左子树上所有值都要小于根节点的值
        # 右子树上所有的值都要大于根节点的值
        # 设置一个上下界，进行比较
        # 如果是判断左子树，则上边界为根节点的值；如果是判断右子树，则下边界是根节点的值
        def _bst(root, lower = float("-inf"), upper = float("inf")):
            if root is None:
                return True

            if root.val <= lower or root.val >= upper:
                return False

            b_left = _bst(root.left, lower, upper=root.val)
            b_right = _bst(root.right, lower=root.val, upper=upper)

            return b_left & b_right

        #
        return _bst(root)

# main
if __name__ == '__main__':
    # root = TreeNode(val=2, left=TreeNode(1), right=TreeNode(3))
    # root = TreeNode(val=5, left=TreeNode(1), right=TreeNode(7, left=TreeNode(5), right=TreeNode(8)))
    root = TreeNode(val=3, left=TreeNode(1, left=TreeNode(0), right=TreeNode(2)),
                    right=TreeNode(5, left=TreeNode(4), right=TreeNode(6)))
    s = Solution()
    print(s.isValidBST(root))