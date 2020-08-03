# -*- coding: utf-8 -*-
# @Time    : 2020/8/3 8:08 下午
# @Author  : Dawein
# @File    : smallest_k.py
# @Software : PyCharm

"""
给定一个数组，找出数组的最小的k个数
思路1：直接从小到大排序，然后取前k个值
思路2：借鉴快速排序的思想，找mid， 因为快速排序的思想是把小于mid位置值的放在mid左半部分，大于mid位置值的
      放在mid右半部分；那就有：1、如果mid = k+1， 直接返回数组，2、如果mid > k + 1， 则在左半部分
      继续查找，3、如果mid < k + 1， 则在有半部分继续查找
"""

class SmallestK:
    def __init__(self):
        pass

    def find_mid(self, arr, low, high, k):

        left = low
        right = high
        anchor = arr[low]
        while left < right:
            while left < right and arr[right] >= anchor:
                right -= 1
            if left < right:
                arr[left] = arr[right]
            while left < right and arr[left] <= anchor:
                left += 1
            if left < right:
                arr[right] = arr[left]

        arr[left] = anchor
        mid = left
        if mid == k:
            return arr
        elif mid > k:
            arr = self.find_mid(arr, low, mid-1, k)
        else:
            arr = self.find_mid(arr, mid+1, high, k)

        return arr


    def find(self, arr, n, k):
        if arr is None or len(arr) <=3:
            return arr

        low = 0
        high = n - 1
        arr = self.find_mid(arr, low, high, k)
        smallest_k = arr[:k]
        return smallest_k

# main
if __name__ == '__main__':
    arr = [3, 5, 3, 2, 5, 2, 1]
    n = len(arr)
    k = 3
    sk = SmallestK()
    print(sk.find(arr, n, k))