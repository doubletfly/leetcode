# -*- coding: utf-8 -*-
# @Time    : 2020/8/18 6:37 下午
# @Author  : Dawein
# @File    : L20_is_valid.py
# @Software : PyCharm

"""
Leetcode - 20: 有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
"""

class Solution:

    def isValid(self, str):
        if str is None:
            return False
        if len(str)==0:
            return True

        mappings = {")": "(", "}": "{", "]": "["}
        stack = []
        for c in str:
            if len(stack) and c in mappings and mappings[c] == stack[-1]:
                stack.pop(-1)
            else:
                stack.append(c)

        if len(stack):
            return False
        return True

## main
if __name__ == '__main__':
    str = "()[[]{}"
    s = Solution()
    print(s.isValid(str))