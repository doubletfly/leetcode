# -*- coding: utf-8 -*-
# @Time    : 2020/9/16 5:47 下午
# @Author  : Dawein
# @File    : L122_max_profit.py
# @Software : PyCharm

"""
给定一个数组，它的第i 个元素是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
示例 1:
输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
    随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。

示例 2:
输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
    注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
    因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。

示例3:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
"""

# 基本思路： 最低买，最高卖
class Solution():

    def max_profit(self, prices:list):
        if prices is None or len(prices) < 2:
            return 0

        n = len(prices)
        i = 0
        max_p = 0
        while i < n-1:
            while i<n-1 and prices[i+1] <= prices[i]:
                i += 1
            bottom = prices[i]
            while i<n-1 and prices[i+1] >= prices[i]:
                i += 1
            top = prices[i]
            max_p += (top - bottom)
        return max_p


# main
if __name__ == '__main__':
    s = Solution()
    print(s.max_profit(prices=[1,2,3,4,5]))