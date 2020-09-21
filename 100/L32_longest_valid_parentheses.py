# -*- coding: utf-8 -*-
# @Time    : 2020/8/6 1:55 下午
# @Author  : Dawein
# @File    : L32_longest_valid_parentheses.py
# @Software : PyCharm

"""
Leetcode - 32
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串

示例1:
输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"

示例 2:
输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
"""

class LongestValidParentess:
    def __init__(self):
        pass

    def find(self, s):
        if s is None:
            return ""
        if s == "":
            return ""

        stack = []
        rst = ""
        max_rst = ""
        is_append = False
        mapping = {")": "("}
        for x in s:
            if len(stack):
                if x in mapping and stack[-1]==mapping[x]:
                    rst += stack.pop()
                    rst += x
                else:
                    if not is_append:
                        if len(rst) > len(max_rst):
                            max_rst = rst
                        rst = ""
                    stack.append(x)
                    is_append = True
            else:
                stack.append(x)
        if len(rst) > len(max_rst):
            max_rst = rst
        return len(max_rst), max_rst

# main
if __name__ == '__main__':
    s = ")()())())"
    lip = LongestValidParentess()
    print(lip.find(s))
