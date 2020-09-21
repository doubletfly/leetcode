# -*- coding: utf-8 -*-
# @Time    : 2020/9/10 8:51 下午
# @Author  : Dawein
# @File    : L66_plus_one.py
# @Software : PyCharm

"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。

示例1:
输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。

示例2:
输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。
"""

class Solution():

    def plus_one(self, digits:list):

        n = len(digits)
        i = n - 1
        add = 1
        while i >= 0:
            cur = digits[i] + add
            if cur < 10:
                digits[i] = cur
                break
            digits[i] = cur % 10
            add = cur // 10
            i -= 1

        if i==-1 and add != 0:
            digits.insert(0, add)

        return digits

# main
if __name__ == '__main__':
    s = Solution()
    print(s.plus_one(digits=[8,9,9]))