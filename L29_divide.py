# -*- coding: utf-8 -*-
# @Time    : 2020/8/19 7:51 下午
# @Author  : Dawein
# @File    : L29_divide.py
# @Software : PyCharm

"""
两个整数相除

给定两个整数，被除数dividend和除数divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数dividend除以除数divisor得到的商。

整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2
"""

class Solution:

    def divide(self, dividend: int, divisor: int)->int:
        if dividend == 0:
            return 0

        if divisor == 0:
            raise ValueError("divisor should be not 0.")

        rst = 0
        step = 1
        if dividend * divisor < 0:
            step = -step

        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            dividend = dividend - divisor
            rst += step

        return rst


# main
if __name__ == '__main__':
    s = Solution()
    print(s.divide(dividend=7, divisor=-3))