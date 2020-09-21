# -*- coding: utf-8 -*-
# @Time    : 2020/8/19 1:40 下午
# @Author  : Dawein
# @File    : L24_swap_pairs.py
# @Software : PyCharm

"""
两两交换链表中的元素

例如:
1->2->3->4->5
2->1->4->3->5
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

    def swap_pairs(self, head: ListNode)->ListNode:
        if head is None:
            return head

        p1 = head
        p2 = head.next
        while p1 is not None and p2 is not None:
            temp = p1.val
            p1.val = p2.val
            p2.val = temp

            p1 = p2.next
            if p1 is None:
                break
            p2 = p2.next.next

        return head

## main
if __name__ == '__main__':
    s = Solution()
    head = s.create_list(arr=[1,2,3,4,5,6,7,8,9])
    head = s.swap_pairs(head)
    print(s.restore_list(head))