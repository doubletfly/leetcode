# -*- coding: utf-8 -*-
# @Time    : 2020/10/15 6:53 下午
# @Author  : Dawein
# @File    : L92_reverse_between.py
# @Software : PyCharm

"""
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
说明:
1 ≤m≤n≤ 链表长度。

示例:
输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
"""

from L00_ListNode import ListNode, ListNodeOps

class Solution():

    def reverse_between(self, head:ListNode, m:int, n:int):
        if head is None:
            return head

        aux = ListNode(0)
        aux.next = head
        left = aux
        for i in range(1, m):
            left = left.next
        head = left.next
        for i in range(m, n):
            nxt = head.next
            head.next = nxt.next
            nxt.next = left.next
            left.next = nxt

        return aux.next


## main
if __name__ == '__main__':
    ops = ListNodeOps()
    head = ops.create_list(arr=[1, 1, 2, 3, 3])
    # print(ops.restore_list(head))

    s = Solution()
    head = ops.create_list(arr=[1,2,3,4,5])
    rst = s.reverse_between(head, m=2, n=4)
    print(ops.restore_list(rst))