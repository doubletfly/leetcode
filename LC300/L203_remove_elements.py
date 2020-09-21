# -*- coding: utf-8 -*-
# @Time    : 2020/9/21 8:36 下午
# @Author  : Dawein
# @File    : L203_remove_elements.py
# @Software : PyCharm

"""
删除链表中等于给定值 val 的所有节点。

示例:
输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
"""

from LC100.L00_ListNode import ListNode, ListNodeOps

class Solution():

    def remove_elements(self, head:ListNode, val):

        while head is not None:
            if head.val == val:
                head = head.next
            else:
                break
        if head is None:
            return head

        p1 = head
        p2 = head.next
        while p2 is not None:
            if p2.val == val:
                p1.next = p2.next
            else:
                p1 = p1.next
            p2 = p2.next

        return head

# main
if __name__ == '__main__':
    ops = ListNodeOps()
    print(ops.restore_list(head=ops.create_list(arr=[1,2,3])))

    s = Solution()
    head = ops.create_list(arr=[1,6,6,6,6,6,6])
    print(ops.restore_list(head=s.remove_elements(head=head, val=6)))