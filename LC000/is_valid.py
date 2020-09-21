# -*- coding: utf-8 -*-
# @Time    : 2020/8/6 10:46 上午
# @Author  : Dawein
# @File    : is_valid.py
# @Software : PyCharm

"""
给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串，判断字符串是否有效。

有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。

注意空字符串可被认为是有效字符串。
"""

class IsValid:
    def __init__(self):
        pass

    def check(self, s):
        if s is None:
            return False
        if s == "":
            return True

        mapping = {")": "(",
                   "}": "{",
                   "]": "["}
        stack = []
        for x in s:
            if len(stack) and x in mapping:
                if stack[-1] != mapping[x]:
                    stack.append(x)
                else:
                    stack.pop()
            else:
                stack.append(x)
        if len(stack):
            return False
        return True

# main
if __name__ == '__main__':
    s = "[}"
    ii = IsValid()
    print(ii.check(s))