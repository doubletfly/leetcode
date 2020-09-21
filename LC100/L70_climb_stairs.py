# -*- coding: utf-8 -*-
# @Time    : 2020/9/14 8:27 下午
# @Author  : Dawein
# @File    : L70_climb_stairs.py
# @Software : PyCharm


"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。

-- 动态规划

"""

class Solution():

    def climb_stairs(self, n:int):

        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        rst = [0] * (n + 1)
        rst[1] = 1
        rst[2] = 2
        for i in range(3, n+1):
            rst[i] = rst[i-1] + rst[i-2]

        return rst[n]

## main
if __name__ == '__main__':
    s = Solution()
    print(s.climb_stairs(n=10))