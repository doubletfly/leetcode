# -*- coding: utf-8 -*-
# @Time    : 2020/9/7 6:53 下午
# @Author  : Dawein
# @File    : L56_merge.py
# @Software : PyCharm

"""
给出一个区间的集合，请合并所有重叠的区间。

示例 1:
输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

示例2:
输入: intervals = [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
"""

class Solution():

    def merge(self, intervals):
        if len(intervals) < 2:
            return intervals

        intervals = sorted(intervals, key=lambda x: x[0], reverse=False)
        rst = []
        for item in intervals:
            if len(rst) == 0:
                rst.append(item)
                continue
            if rst[-1][1] < item[0]:
                rst.append(item)
                continue
            rst[-1][1] = max(rst[-1][1], item[1])

        return rst

# main
if __name__ == '__main__':
    intervals = [[1,4],[4,6]]
    s = Solution()
    print(s.merge(intervals))