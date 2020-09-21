# -*- coding: utf-8 -*-
# @Time    : 2020/8/18 4:56 下午
# @Author  : Dawein
# @File    : L19_remove_Nth_from_end.py
# @Software : PyCharm

"""
Leetcode - 19: 删除链表的倒数第N个节点
给定一个链表，删除链表的倒数第n个节点，并且返回链表的头结点。

示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.
"""

"""
题解： 一趟扫描
设置两个指针，first和second， first指针先前进n+1步，此时first和second间隔n个数；
再同时移动first和second两个指针，当first为None时，second指向需要删除元素的前一个元素；
此时将second的next指向下下个元素，即完成指定元素的删除。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def create_list(self, arr: list)->ListNode:
        if len(arr) == 0:
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

    def removeNthFromEnd(self, head: ListNode, n: int)->ListNode:

        if head == None:
            return None

        p1 = head
        p2 = head
        i = 0
        while i < n+1 and p1 is not None:
            p1 = p1.next
            i += 1

        if i != n+1:
            head = head.next
            return head

        while p1 is not None:
            p1 = p1.next
            p2 = p2.next

        p2.next = p2.next.next

        return head

## main
if __name__ == '__main__':
    arr = [1,2,3,4,5]
    n = 5
    s = Solution()
    head = s.create_list(arr)
    head = s.removeNthFromEnd(head, n)
    print("{} {}".format(arr, n))
    print(s.restore_list(head))
