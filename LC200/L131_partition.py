# -*- coding: utf-8 -*-
# @Time    : 2021/1/14 2:32 下午
# @Author  : Dawein
# @File    : L131_partition.py
# @Software : PyCharm

"""
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
返回 s 所有可能的分割方案。

示例:
输入:"aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]
"""

class Solution():

    def partition(self, s: str):
        if len(s) == 0:
            return []

        results = []
        length = len(s)

        # 回溯法
        def backtrans(start, path=[]):
            if start == length:
                results.append(path[:])
                return

            for i in range(start, length):
                if not self.isPalindrome(s, start, i):
                    continue
                path.append(s[start:i+1])
                backtrans(i+1, path)
                path.pop()

        # main
        backtrans(0)
        return results

    # 判断是否是回文串
    def isPalindrome(self, s:str, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

# main
if __name__ == '__main__':
    S = Solution()
    results = S.partition("aabbc")
    print(results)

