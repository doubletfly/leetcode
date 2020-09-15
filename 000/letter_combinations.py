# -*- coding: utf-8 -*-
# @Time    : 2020/8/17 7:17 下午
# @Author  : Dawein
# @File    : letter_combinations.py
# @Software : PyCharm

"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

class Solution:

    def letter_combinations(self, digits):

        mappings = {"2": "abc", "3": "def", "4": "ghi",
                    "5": "jkl", "6": "mno", "7": "pqrs",
                    "8": "tuv", "9": "wxyz"}

        for k in mappings:
            mappings[k] = list(mappings[k])

        for d in digits:
            if d not in mappings:
                return []


        def backtrace(combinations, digits):
            if len(digits) == 0:
                output.append(combinations)
            else:
                for letter in mappings[digits[0]]:
                    backtrace(combinations + letter, digits[1:])


        output = []
        if digits:
            backtrace("", digits)

        return output

## main
if __name__ == '__main__':

    s = Solution()
    print(s.letter_combinations(digits="230"))