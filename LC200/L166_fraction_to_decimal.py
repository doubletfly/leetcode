# -*- coding: utf-8 -*-
# @Time    : 2021/2/25 7:30 下午
# @Author  : Dawein
# @File    : L166_fraction_to_decimal.py
# @Software : PyCharm

"""
给定两个整数，分别表示分数的分子numerator 和分母 denominator，以 字符串形式返回小数 。
如果小数部分为循环小数，则将循环的部分括在括号内。
如果存在多个答案，只需返回 任意一个 。
对于所有给定的输入，保证 答案字符串的长度小于 104 。

示例 1：
输入：numerator = 1, denominator = 2
输出："0.5"
示例 2：

输入：numerator = 2, denominator = 1
输出："2"
示例 3：

输入：numerator = 2, denominator = 3
输出："0.(6)"
示例 4：

输入：numerator = 4, denominator = 333
输出："0.(012)"
示例 5：

输入：numerator = 1, denominator = 5
输出："0.2"
"""

class Solution():

    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return "0"

        res = []
        # 分子或分母有一个为负数则需要添加负号
        if numerator * denominator < 0:
            res.append("-")

        # 转成正数
        numerator = abs(numerator)
        denominator = abs(denominator)

        num, residual = divmod(numerator, denominator)
        res.append(str(num))
        if residual == 0:
            return "".join(res)

        # 添加小数点
        res.append(".")

        # 如果余数不为0，则当余数第二次出现时则开始循环
        # 这里利用一个map记录余数的位置
        positions = {}
        while residual != 0:
            if residual in positions:
                indices = positions[residual]
                res.insert(indices, "(")
                res.append(")")
                break

            positions[residual] = len(res)
            residual = residual * 10
            res.append(str(residual // denominator))
            residual = residual % denominator

        return "".join(res)

# main
if __name__ == '__main__':
    s = Solution()
    print(s.fractionToDecimal(numerator=2, denominator=333))