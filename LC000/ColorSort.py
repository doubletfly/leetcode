# -*- coding: utf-8 -*-
# @Time    : 2020/8/3 1:41 下午
# @Author  : Dawein
# @File    : ColorSort.py
# @Software : PyCharm

"""
给定3中颜色的小球，红、蓝、白，现在需要将相同颜色的小球放在一起
假定用数组表示，数组中元素0、1、2分别表示红、蓝、白三种小球
例如：【1, 2, 0, 0】 -> [0,0,1,2]
"""

class ColorSort:
    def __init__(self):
        pass

    def sort(self, nums: list)->list:
        if nums is None:
            return nums
        if len(nums) < 3:
            raise ValueError("length of input is wrong.")

        left = 0
        right = len(nums) - 1
        i = 0
        while i <= right:
            if nums[i] == 1:
                i += 1
                continue
            if nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            elif nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i += 1
        return nums

# main
if __name__ == '__main__':
    x = [2, 0, 1, 0, 1, 2]
    cs = ColorSort()
    print(cs.sort(x))
