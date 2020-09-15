# -*- coding: utf-8 -*-
# @Time    : 2020/8/5 2:15 下午
# @Author  : Dawein
# @File    : LongestCommonPrefix.py
# @Software : PyCharm

"""
寻找一组字符串的最长公共前缀
"""

class LongestCommonPrefix:
    def __init__(self):
        pass

    def find(self, str_arrs):
        if str_arrs is None:
            return ""
        if len(str_arrs) == 0:
            return ""
        if len(str_arrs) == 1:
            return str_arrs[0]

        buffer = ""
        min_len = min(len(w) for w in str_arrs)
        i = 0
        while i < min_len:
            buffer += str_arrs[0][i]
            for cur in str_arrs[1:]:
                if cur[0:i+1] != buffer:
                    return buffer[:-1]
            i += 1

        return buffer

# main
if __name__ == '__main__':
    str_arrs = ["flower","flow","flight"]
    str_arrs = ["g dog", "g d"]
    lcp = LongestCommonPrefix()
    print(lcp.find(str_arrs))