# -*- coding: utf-8 -*-
# @Time    : 2021/1/13 4:06 下午
# @Author  : Dawein
# @File    : L125_palindrome.py
# @Software : PyCharm

"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true

示例 2:
输入: "race a car"
输出: false
"""

# python中判断字符是不是数字或字母， "1".isdigit(), "a".isalpha()

class Solution:
    def isPalindrome(self, s: str):
        if s is None:
            return False
        if len(s) == 0:
            return True

        head = 0
        tail = len(s) - 1

        while head < tail:
            h = s[head].lower()
            t = s[tail].lower()
            if not h.isdigit() and not h.isalpha():
                head += 1
                continue
            if not t.isdigit() and not t.isalpha():
                tail -= 1
                continue

            head += 1
            tail -= 1
            if h != t:
                return False
        return True

# main
if __name__ == '__main__':
    # s = "A man, a plan, a canal: Panama"
    s = "race a car"
    slt = Solution()
    print(slt.isPalindrome(s))