# -*- coding: utf-8 -*-
# @Time    : 2020/9/28 6:35 下午
# @Author  : Dawein
# @File    : L75_sort_colors.py
# @Software : PyCharm

"""
给定一个包含红色、白色和蓝色，一共n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
此题中，我们使用整数 0、1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:
输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
进阶：

一个直观的解决方案是使用计数排序的两趟扫描算法。
首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
你能想出一个仅使用常数空间的一趟扫描算法吗？
"""

## 给定首尾两个指针，再遍历整个数组
## 1、如果遍历到的数为2，则交换当前数和尾指针的数
## 2、如果遍历到数为1，则不交换，继续下一步遍历
## 3、如果遍历到数为0，则交换当前数和首指针的数

class Solution():

    def sort_colors(self, nums):
        if nums is None or len(nums) == 0:
            return nums

        left = 0
        right = len(nums) - 1
        i = 0
        while i <= right:
            if nums[i] == 1:
                i += 1
                continue

            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                i += 1
                left += 1
                continue

            if nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1

        return nums

## main
if __name__ == '__main__':
    s = Solution()
    print(s.sort_colors(nums=[0,0,2,1,1,0]))
