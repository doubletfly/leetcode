# -*- coding: utf-8 -*-
# @Time    : 2020/10/12 6:22 下午
# @Author  : Dawein
# @File    : L86_partition.py
# @Software : PyCharm

"""
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
你应当保留两个分区中每个节点的初始相对位置。

示例:
输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5
"""

from L00_ListNode import ListNode, ListNodeOps

class Solution():

    def partition(self, head:ListNode, x:int):
        if head is None:
            return head

        # 创建两个辅助节点
        bf_head = bf = ListNode(0)
        af_head = af = ListNode(0)

        # 小于x的连接到bf节点后面，大于或等于x的连接到af节点后面
        while head is not None:
            if head.val < x:
                bf.next = head
                bf = bf.next
            else:
                af.next = head
                af = af.next

            head = head.next

        # 最后将bf链表和af链表合并
        af.next = None
        bf.next = af_head.next
        return bf_head.next

## main
if __name__ == '__main__':
    ops = ListNodeOps()
    head = ops.create_list(arr=[1,1,2,3,3])
    print(ops.restore_list(head))

    s = Solution()
    print(ops.restore_list(s.partition(head=ops.create_list(arr=[1,4,3,2,5,2]), x=3)))