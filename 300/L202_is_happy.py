# -*- coding: utf-8 -*-
# @Time    : 2020/9/21 8:26 下午
# @Author  : Dawein
# @File    : L202_is_happy.py
# @Software : PyCharm

"""
编写一个算法来判断一个数 n 是不是快乐数。
「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。如果 可以变为  1，那么这个数就是快乐数。
如果 n 是快乐数就返回 True ；不是，则返回 False 。
示例：
输入：19
输出：true
解释：
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""

## 基本思路：
## 类比于判断一个链表是否带有环
## 那么就可以利用快慢指针，慢指针每次走一步，快指针每次走两步
## 如果有环，则快指针会与慢指针相遇；否则快指针达到最后一步
## 那么在这个题目中，当一个数是快乐数时，快指针会最终等于1
class Solution():

    def is_happy(self, n):
        if n == 1:
            return True

        def get_next(x):
            rst = 0
            while x > 0:
                tmp = x % 10
                rst += tmp**2
                x = x // 10

            return rst

        slow_num = n
        fast_num = get_next(n)
        while fast_num != 1 and slow_num != fast_num:
            slow_num = get_next(slow_num)
            fast_num = get_next(get_next(fast_num))

        return fast_num == 1

## main
if __name__ == '__main__':
    s = Solution()
    print(s.is_happy(n=19))