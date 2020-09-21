# -*- coding: utf-8 -*-
# @Time    : 2020/9/2 7:35 下午
# @Author  : Dawein
# @File    : L42_trap.py
# @Software : PyCharm


"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
例如：
输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
"""

## 双指针
## left和right指针分别从数组的左边和右边遍历数据：
## 如果left位置的值小于right位置的值，则从左边开始处理；
## 如果left位置的值大于或等于right位置的值，则从右边开始处理；
## 处理规则：和自己这一边的当前max值进行比较，如果小于max值可以积水
class Solution():

    def tarp(self, height: list)->int:
        if len(height) < 3:
            return 0

        n = len(height)
        left_max = 0
        right_max = 0
        left = 0
        right = n - 1
        rst = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] < left_max:
                    rst += (left_max - height[left])
                else:
                    left_max = height[left]
                left += 1
            else:
                if height[right] < right_max:
                    rst += (right_max - height[right])
                else:
                    right_max = height[right]
                right -= 1
        print(left, right)
        return rst

##  main
if __name__ == '__main__':
    heights = [0,1,0,2,1]
    s = Solution()
    print(s.tarp(heights))