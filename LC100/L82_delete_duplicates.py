# -*- coding: utf-8 -*-
# @Time    : 2020/9/30 4:51 下午
# @Author  : Dawein
# @File    : L82_delete_duplicates.py
# @Software : PyCharm

"""
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:
输入: 1->2->3->3->4->4->5
输出: 1->2->5

示例 2:
输入: 1->1->1->2->3
输出: 2->3
"""

from L00_ListNode import ListNode, ListNodeOps

class Solution():

    def delete_duplicates(self, head:ListNode):
        if head is None:
            return head

        if head.next is None:
            return head

        lp = None
        fp = head
        bp = head
        while bp.next is not None:
            # 如果前节点值和后节点的值不相等
            if fp.val != bp.next.val:
                # 如果前节点和后节点不是同一个节点
                if fp != bp:
                    # 如果标志节点为None，说明遍历到当前位置，所有值都是一样的
                    if lp is None:
                        head = bp.next
                        fp = head
                        bp = head
                    else:
                        # 否则，标志节点指向后节点的下一个节点，实现节点的删除
                        lp.next = bp.next
                        fp = bp.next
                        bp = bp.next
                else:
                    # r如果当前节点和后节点指向同一个节点，则更新标志节点为当前节点；同时前后节点均后移
                    lp = fp
                    fp = fp.next
                    bp = bp.next
            else:
                # 如果当前节点的值和后一个节点的值相同，则后节点后移，继续遍历
                bp = bp.next

        # 最后，如果已经遍历到最后一个节点，且前节点值和后节点的值相同，且两个节点不一样，则更新节点，实现节点删除
        if bp.next is None and fp.val == bp.val and fp != bp:
            if lp is None:
                head = bp.next
            else:
                lp.next = bp.next

        return head

# main
if __name__ == '__main__':
    ops = ListNodeOps()
    print(ops.restore_list(ops.create_list(arr=[1, 2, 3, 3, 4, 4, 5])))
    s = Solution()
    print(ops.restore_list(s.delete_duplicates(head=ops.create_list(arr=[1, 1, 1, 2, 3]))))
