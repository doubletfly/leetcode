# -*- coding: utf-8 -*-
# @Time    : 2020/9/14 8:33 下午
# @Author  : Dawein
# @File    : L83_remove_duplicates.py
# @Software : PyCharm


"""
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
示例1:
输入: 1->1->2
输出: 1->2

示例2:
输入: 1->1->2->3->3
输出: 1->2->3
"""

from L00_ListNode import ListNode, ListNodeOps

class Solution():

    def remove_duplicates(self, head:ListNode):
        if head == None:
            return None

        p1 = head
        p2 = head.next
        while p2 != None:
            if p1.val == p2.val:
                p2 = p2.next
            else:
                p1.next.val = p2.val
                p1 = p1.next
                p2 = p2.next
        p1.next = None

        return head


## main
if __name__ == '__main__':
    ops = ListNodeOps()
    head = ops.create_list(arr=[1,1,2,3,3])
    print(ops.restore_list(head))

    s = Solution()
    print(ops.restore_list(s.remove_duplicates(head)))