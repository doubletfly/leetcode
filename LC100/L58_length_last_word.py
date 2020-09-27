# -*- coding: utf-8 -*-
# @Time    : 2020/9/27 7:03 下午
# @Author  : Dawein
# @File    : L58_length_last_word.py
# @Software : PyCharm

"""
给定一个仅包含大小写字母和空格' '的字符串 s，返回其最后一个单词的长度。如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。
如果不存在最后一个单词，请返回 0。
说明：一个单词是指仅由字母组成、不包含任何空格字符的 最大子字符串。

示例:
输入: "Hello World"
输出: 5
"""

# 基本思路: 从后往前遍历，从非空字符串开始统计，直至遇到下一个空字符，则返回；如果字符串遍历玩，则直接返回。

class Solution():

    def length_of_last_word(self, s):
        if s is None or len(s) == 0 or s == " ":
            return 0

        n = len(s)
        rst_len = 0
        for i in range(n-1, -1, -1):
            if s[i] == " ":
                if rst_len == 0:
                    continue
                return rst_len
            rst_len += 1

        return rst_len

## main
if __name__ == '__main__':
    s = Solution()
    print(s.length_of_last_word(s="HelloWorld "))