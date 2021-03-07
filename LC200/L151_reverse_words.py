# -*- coding: utf-8 -*-
# @Time    : 2021/2/23 7:22 下午
# @Author  : Dawein
# @File    : L151_reverse_words.py
# @Software : PyCharm

from collections import deque

class Solution():

    def reverseWords(self, s):
        if s is None or len(s)==0:
            return s

        left, right = 0, len(s)-1

        # 去掉字符串前面的空格
        while left <= right:
            if s[left] == " ":
                left += 1
            else:
                break

        # 去掉字符串后面的空格
        while left <= right:
            if s[right] == " ":
                right -= 1
            else:
                break

        # 使用双端队列，遍历到一个word则放入
        rst = deque()
        word = ""
        while left <= right:
            if s[left] == " " and len(word) != 0:
                rst.appendleft(word)
                word = ""
            elif s[left] != " ":
                word += s[left]
            left += 1
        rst.appendleft(word)

        return " ".join(rst)

# main
if __name__ == '__main__':
    s = Solution()
    str = "  Bob    Loves  Alice   "
    print(s.reverseWords(str))