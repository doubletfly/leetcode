# -*- coding: utf-8 -*-
# @Time    : 2021/1/11 6:23 下午
# @Author  : Dawein
# @File    : L105_build_tree.py
# @Software : PyCharm

"""
根据一棵树的前序遍历与中序遍历构造二叉树。
注意:
你可以假设树中没有重复的元素。
例如，给出
前序遍历 preorder =[3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：
    3
   / \
  9  20
    /  \
   15   7
"""
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

# 前序遍历 - 先根节点，再左子树，再右子树
# 中序遍历 - 先左子树，再根节点，再右子树
class Solution:
    def buildTree(self, preorder, inorder):
        if len(preorder) != len(inorder):
            return None

        # 递归构造
        # 前序遍历的第一个值值根节点的值，然后再去中序遍历找根节点的位置；则左边为左子树序列，右边为右子树序列
        # 然后再递归构造
        def _turn(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return None

            # 先从前序遍历中找到根节点
            root_indices = pre_left

            # 在中序遍历中确定根节点值得位置
            root_indices_2 = inorder.index(preorder[root_indices])

            # 这个时候先把根节点构架起来
            root = TreeNode(x=preorder[root_indices])

            # 计算左子树的个数
            left_nums = root_indices_2 - in_left

            # 开始构建左子树
            left = _turn(pre_left+1, pre_left+left_nums,
                         in_left, root_indices_2-1)
            root.left = left

            # 开始构建右子树
            right = _turn(pre_left+left_nums+1, pre_right,
                          root_indices_2+1, in_right)
            root.right = right

            return root

        # main
        n = len(preorder)
        return _turn(0, n-1, 0, n-1)

# main
if __name__ == '__main__':
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    s = Solution()
    print(s.buildTree(preorder, inorder))
