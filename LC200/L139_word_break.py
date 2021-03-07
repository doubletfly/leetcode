# -*- coding: utf-8 -*-
# @Time    : 2021/1/18 7:32 下午
# @Author  : Dawein
# @File    : L139_word_break.py
# @Software : PyCharm

"""
给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定s 是否可以被空格拆分为一个或多个在字典中出现的单词。
说明：
拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。

示例 1：
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
注意你可以重复使用字典中的单词。

示例 3：
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
"""

class Solution():

    def wordBreak(self, s, wordDict):

        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] & (s[j:i] in wordDict):
                    dp[i] = True
                    break
        return dp[-1]

# main
if __name__ == '__main__':
    s = "leetcode"
    wordDict = ["leet", "code"]
    result = Solution().wordBreak(s, wordDict)
    print(result)