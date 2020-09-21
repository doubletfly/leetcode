# -*- coding: utf-8 -*-
# @Time    : 2020/8/19 11:09 上午
# @Author  : Dawein
# @File    : L21_merge_two_lists.py
# @Software : PyCharm

"""
合并两个有序的链表
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def create_list(self, arr: list)->ListNode:
        if arr is None or len(arr)==0:
            return None

        head = ListNode(arr[0])
        p = head
        for x in arr[1:]:
            p.next = ListNode(x)
            p = p.next

        return head

    def restore_list(self, head: ListNode)->list:
        if head is None:
            return []

        p = head
        rst = []
        while p is not None:
            rst.append(p.val)
            p = p.next

        return rst

    def merge_two_lists(self, l1: ListNode, l2: ListNode)->ListNode:

        if l1 is None:
            return l2
        if l2 is None:
            return l1

        p1 = l1
        p2 = l2
        rst = ListNode(0)
        p3 = rst
        while p1 is not None and p2 is not None:
            x1 = p1.val
            x2 = p2.val
            if x1 > x2:
                p3.next = p2
                p2 = p2.next
            else:
                p3.next = p1
                p1 = p1.next
            p3 = p3.next

        if p1 is not None:
            p3.next = p1

        if p2 is not None:
            p3.next = p2

        return rst.next

## main
if __name__ == '__main__':

    s = Solution()
    l1 = s.create_list(arr=None)
    l2 = s.create_list(arr=[1,1,4])

    merged = s.merge_two_lists(l1, l2)
    print(s.restore_list(merged))