# -*- coding: utf-8 -*-
# @Time    : 2021/1/13 4:43 下午
# @Author  : Dawein
# @File    : L129_sum_numbers.py
# @Software : PyCharm

"""
给定一个二叉树，它的每个结点都存放一个0-9的数字，每条从根到叶子节点的路径都代表一个数字。
例如，从根到叶子节点路径 1->2->3 代表数字 123。
计算从根到叶子节点生成的所有数字之和。
说明:叶子节点是指没有子节点的节点。
示例 1:

输入: [1,2,3]
    1
   / \
  2   3
输出: 25
解释:
从根到叶子节点路径 1->2 代表数字 12.
从根到叶子节点路径 1->3 代表数字 13.
因此，数字总和 = 12 + 13 = 25.
示例 2:

输入: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
输出: 1026
解释:
从根到叶子节点路径 4->9->5 代表数字 495.
从根到叶子节点路径 4->9->1 代表数字 491.
从根到叶子节点路径 4->0 代表数字 40.
因此，数字总和 = 495 + 491 + 40 = 1026.
"""
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root:TreeNode):
        if root is None:
            return 0

        results = []
        path = []

        def travel(r_node: TreeNode):
            if r_node is None:
                return
            path.append(r_node.val)

            # 遍历到叶子节点，将路径上的值转换成整数，并插入到结果中
            if r_node.left is None and r_node.right is None:
                s = 0
                for v in path:
                    s = s * 10 + v
                results.append(s)

            travel(r_node.left)
            travel(r_node.right)
            # 弹出上一个插入的元素
            path.pop()

        # all
        travel(root)
        return sum(results)

# main
if __name__ == '__main__':
    root = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
    s = Solution()
    numbers = s.sumNumbers(root)
    print(numbers)