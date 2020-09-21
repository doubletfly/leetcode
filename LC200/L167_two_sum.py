# -*- coding: utf-8 -*-
# @Time    : 2020/9/17 5:27 下午
# @Author  : Dawein
# @File    : L167_two_sum.py
# @Software : PyCharm

"""
给定一个已按照升序排列的有序数组，找到两个数使得它们相加之和等于目标数。
函数应该返回这两个下标值 index1 和 index2，其中 index1必须小于index2。

说明:
返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
"""

class Solution():

    def two_sum(self, numbers, target):

        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            if numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1

        return []

## main
if __name__ == '__main__':
    s = Solution()
    print(s.two_sum(numbers=[2, 7, 11, 15], target=19))