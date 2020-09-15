# -*- coding: utf-8 -*-
# @Time    : 2020/9/3 7:20 下午
# @Author  : Dawein
# @File    : L49_group_anagrams.py
# @Software : PyCharm

"""
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""

class Solution():

    def group_anagrams(self, strs):
        if len(strs) == 0:
            return None

        def is_anagram(str1, str2):
            for t in str2:
                if t not in str1:
                    return False
            return True

        rst = []
        for str_s in strs:
            if len(rst) == 0:
                rst.append([str_s])
                continue
            is_insert = False
            for i in range(len(rst)):
                item = rst[i]
                if is_anagram(item[-1], str_s):
                    rst[i].append(str_s)
                    is_insert = True
                    break
            if not is_insert:
                rst.append([str_s])

        return rst

## main
if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat", "abc"]
    s = Solution()
    print(s.group_anagrams(strs))