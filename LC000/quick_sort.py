# -*- coding: utf-8 -*-
# @Time    : 2020/8/3 11:00 上午
# @Author  : Dawein
# @File    : quick_sort.py
# @Software : PyCharm

"""
快速排序
"""

class QuickSort:
    def __init__(self):
        pass

    # 寻找分割位置
    def _find_anchor(self, nums, low, high):
        left = low
        right = high
        anchor = nums[low]

        while left < right:
            while left < right and nums[right] >= anchor:
                right -= 1
            if left < right:
                nums[left] = nums[right]

            while left < right and nums[left] <= anchor:
                left += 1
            if left < right:
                nums[right] = nums[left]

        nums[left] = anchor
        return left, nums

    def sort(self, nums, low, high):
        if low < high:
            mid, nums = self._find_anchor(nums, low, high)
            nums = self.sort(nums, low, mid - 1)
            nums = self.sort(nums, mid + 1, high)

        return nums


# main
if __name__ == '__main__':
    x = [1,3,2,5,4,7,6, 1, 2, 3]
    qs = QuickSort()
    print(qs.sort(x, 0, len(x)-1))
