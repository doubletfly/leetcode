# -*- coding: utf-8 -*-
# @Time    : 2020/8/2 10:24 上午
# @Author  : Dawein
# @File    : distance_two_node.py
# @Software : PyCharm

"""
二叉树中任意两个节点之间的距离
给定一棵二叉树，每个节点的值都不相同，计算任意两个节点之间的距离
1、先找出给定两个节点的LCA，即lower common ancestor，最低公共祖先节点
2、从LCA节点出发，分别计算到两个节点的距离，最后相加（也可以计算root节点到LCA的距离，root节点分别到两个节点的距离，
最后距离 = dist(root, n1) + dist(root, n2) - 2*dist(root, lca)）
"""

# 定义二叉树节点
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Distance():

    def find_lca(self, root, n1, n2):
        if root is None:
            return None

        if root.value == n1 or root.value == n2:
            return root

        left = self.find_lca(root.left, n1, n2)
        right = self.find_lca(root.right, n1, n2)

        if left is not None and right is not None:
            # 两个节点分别在左右子树中
            return root

        # 在左子树或右子树中找到，则返回相应的根节点
        if left is not None:
            return left
        if right is not None:
            return right


    def find_depth(self, root, x):
        if root is None:
            return -1
        if root.value == x:
            return 0

        # 现在左子树中找
        depth = self.find_depth(root.left, x)
        if depth == -1:
            depth = self.find_depth(root.right, x)

        if depth != -1:
            return depth + 1

        return -1

    def calc_dist(self, root, n1, n2):
        if root is None:
            return -1

        lca = self.find_lca(root, n1, n2)
        lca_d = self.find_depth(root, lca.value)
        n1_d = self.find_depth(root, n1)
        n2_d = self.find_depth(root, n2)

        if lca_d == -1 or n1_d == -1 or n2_d == -1:
            return -1

        return n1_d + n2_d - 2*lca_d

# main
if __name__ == '__main__':
    # 构建一棵二叉树
    LT = Tree(2, left=Tree(4), right=Tree(5))
    RT = Tree(3, left=Tree(6), right=Tree(7))
    root = Tree(1, LT, RT)

    calc = Distance()
    lca = calc.find_lca(root, 7, 6)
    print(lca.value)

    print(calc.find_depth(root, 9))
    print(calc.calc_dist(root, 2, 3))
