# -*- coding: utf-8 -*-
# @Time    : 2020/8/4 11:22 下午
# @Author  : Dawein
# @File    : max_area.py
# @Software : PyCharm

"""
盛最多的水：
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点(i,ai) 。
在坐标内画 n 条垂直线，垂直线 i的两个端点分别为(i,ai) 和 (i, 0)。
找出其中的两条线，使得它们与x轴共同构成的容器可以容纳最多的水。

解析：
每条垂直线的高度为ai，相邻两条垂直线的距离为1，例如：第1条垂直线和第2条垂直线之间的宽度为1；
水的体积取决于最短的那条垂直线的高度，以及首尾两条垂直线之间的距离；
设定两个指针，分别指向最开始的头部和尾部，然后计算体积；然后比较两条垂直线的高度，移动高度小的那一端，
重复以上至两条垂直线重合。
"""

class MaxArea:
    def __init__(self):
        pass

    def calculation(self, arr):
        if arr is None or len(arr) <= 1:
            return 0

        left = 0
        right = len(arr) - 1
        max_area = 0
        rst = []
        while left < right:
            w = right - left
            cur_area = w * min(arr[left], arr[right])
            if cur_area > max_area:
                max_area = cur_area
                rst = [arr[left], arr[right]]
            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1

        return max_area, rst

# main
if __name__ == '__main__':
    arr = [1,3,4,2,8,4,8,3,2]
    mr = MaxArea()
    print(mr.calculation(arr))
