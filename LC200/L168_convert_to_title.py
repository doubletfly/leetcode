# -*- coding: utf-8 -*-
# @Time    : 2020/9/17 5:34 下午
# @Author  : Dawein
# @File    : L168_convert_to_title.py
# @Software : PyCharm

"""
给定一个正整数，返回它在 Excel 表中相对应的列名称。
例如，
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
"""
import string

class Solution():

    def convert_to_titles(self, n):
        upper_case = string.ascii_uppercase

        rst = ""
        if n <= 26:
            return upper_case[n-1]

        while n > 0:
            if n > 26:
                red = n % 26
            else:
                red = n

            if red != 0:
                rst = upper_case[red - 1] + rst
            n = (n - red) // 26

        return rst

## main
if __name__ == '__main__':
    s = Solution()
    print(s.convert_to_titles(809))
