# -*- coding: utf-8 -*-
# @Time    : 2020/8/19 7:28 下午
# @Author  : Dawein
# @File    : L28_strStr.py
# @Software : PyCharm

"""
实现strStr()
给定一个haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。
如果不存在，则返回 -1。

示例 1:
输入: haystack = "hello", needle = "ll"
输出: 2

示例 2:
输入: haystack = "aaaaa", needle = "bba"
输出: -1
"""

class Solution:

    def strStr(self, haystack: str, needle: str)->int:
        if haystack is None or needle is None:
            return 0

        if len(haystack)==0 or len(needle)==0:
            return 0

        L, n = len(needle), len(haystack)
        if L > n:
            return -1

        # base value for the rolling hash function
        a = 26
        # modulus value for the rolling hash function to avoid overflow
        modulus = 2 ** 31

        # lambda-function to convert character to integer
        h_to_int = lambda i: ord(haystack[i]) - ord('a')
        needle_to_int = lambda i: ord(needle[i]) - ord('a')

        # compute the hash of strings haystack[:L], needle[:L]
        h = ref_h = 0
        for i in range(L):
            h = (h * a + h_to_int(i)) % modulus
            ref_h = (ref_h * a + needle_to_int(i)) % modulus
        if h == ref_h:
            return 0

        # const value to be used often : a**L % modulus
        aL = pow(a, L, modulus)
        for start in range(1, n - L + 1):
            # compute rolling hash in O(1) time
            h = (h * a - h_to_int(start - 1) * aL + h_to_int(start + L - 1)) % modulus
            if h == ref_h:
                return start

        return -1


# main
if __name__ == '__main__':
    s = Solution()
    haystack = "hello"
    needle = "llj"
    print(s.strStr(haystack, needle))