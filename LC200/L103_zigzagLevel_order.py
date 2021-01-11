# -*- coding: utf-8 -*-
# @Time    : 2021/1/11 6:00 下午
# @Author  : Dawein
# @File    : L103_zigzagLevel_order.py
# @Software : PyCharm

"""
给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
例如：
给定二叉树[3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层序遍历如下：
[
  [3],
  [20,9],
  [15,7]
]
"""

## 利用层的编号进行插入顺序的改变

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode):

        # global buff
        results = []

        if root is None:
            return results

        def dfs(index, r):
            if len(results) < index:
                results.append([])

            if index % 2 != 0:
                results[index - 1].append(r.val)
            else:
                results[index - 1].insert(0, r.val)

            if r.left:
                dfs(index + 1, r.left)
            if r.right:
                dfs(index + 1, r.right)

        #
        dfs(1, root)
        return results

# main
if __name__ == '__main__':

    root = TreeNode(x=3, left=TreeNode(9),
                         right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))

    s = Solution()
    rst = s.zigzagLevelOrder(root)
    print(rst)