# -*- coding: utf-8 -*-
# @Time    : 2020/9/14 8:36 下午
# @Author  : Dawein
# @File    : L00_ListNode.py
# @Software : PyCharm

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class ListNodeOps():

    def __init__(self):
        pass

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