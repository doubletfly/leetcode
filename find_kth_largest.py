# -*- coding: utf-8 -*-
# @Time    : 2020/8/6 8:30 下午
# @Author  : Dawein
# @File    : find_kth_largest.py
# @Software : PyCharm


"""
给定一个无序整数数组，找出整数的第K大值，例如：
nums = [4,5,7,6,3], k = 2
输出： 6

1、比较容易想到的是从大到小排序后，取排序后数组的第2个值，时间复杂度O(n*log(n)) - 快速排序
2、可以利用快速排序的分段处理思想，左半部分是较大值，右半部分是较少值，那当找到的mid==k时，则mid位置的值为输出值；
   其中，当mid < k时，则在右半部分找，当mid > k时，则在左半部分找
"""

class FindKthLargest:
    def __init__(self):
        pass


    def find_mid(self, nums, low, high, k):
        left = low
        right = high
        key = nums[low]

        while left < right:
            while left<right and nums[right] <= key:
                right -= 1
            if left < right:
                nums[left] = nums[right]
            while left<right and nums[left] >= key:
                left += 1
            if left < right:
                nums[right] = nums[left]

        nums[left] = key
        mid = left
        if mid == k-1:
            return nums
        elif mid < k - 1:
            nums = self.find_mid(nums, mid+1, high, k)
        else:
            nums = self.find_mid(nums, low, mid-1, k)
        return nums


    def find(self, nums, k):
        if nums is None or k<=0:
            return -1
        if len(nums) < k or len(nums) < k:
            return -1

        nums = self.find_mid(nums, 0, len(nums)-1, k)
        return nums[k-1]

# main
if __name__ == '__main__':

    nums = [4,5,7,6,3]
    fkl = FindKthLargest()
    print(fkl.find(nums, k=3))