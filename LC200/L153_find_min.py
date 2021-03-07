# -*- coding: utf-8 -*-
# @Time    : 2021/2/23 7:57 下午
# @Author  : Dawein
# @File    : L153_find_min.py
# @Software : PyCharm

"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。例如，数组[0,1,2,4,5,6,7] 可能变为[4,5,6,7,0,1,2] 。
请找出其中最小的元素。
示例 1：
输入：nums = [3,4,5,1,2]
输出：1
示例 2：

输入：nums = [4,5,6,7,0,1,2]
输出：0
示例 3：

输入：nums = [1]
输出：1
"""

class Solution():

    def findMin(self, nums):
        if nums is None or len(nums) == 0:
            return None

        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1

        # 数据没有被旋转
        if nums[left] < nums[right]:
            return nums[0]

        # 开始二分查找
        while left <= right:
            mid = left + (right - left) // 2

            # 正好处在中间
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]

            if nums[mid] < nums[mid - 1]:
                return nums[mid]

            if nums[mid] > nums[left]:
                left = mid + 1
            else:
                right = mid - 1

#  main
if __name__ == '__main__':
    s = Solution()
    print(s.findMin(nums=[4,5,6,7,0,1,2]))