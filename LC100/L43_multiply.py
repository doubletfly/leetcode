# -*- coding: utf-8 -*-
# @Time    : 2020/9/2 7:51 下午
# @Author  : Dawein
# @File    : L43_multiply.py
# @Software : PyCharm

"""
给定两个以字符串形式表示的非负整数num1和num2，返回num1和num2的乘积，它们的乘积也表示为字符串形式。

示例 1:
输入: num1 = "2", num2 = "3"
输出: "6"
"""

##基本思路：拆分计算
## 将num2的每个数分别与num1进行乘积计算，然后移位叠加
class Solution():

    def multiply(self, num1: str, num2: str)->str:

        if len(num1)==0 or len(num2)==0:
            return ""

        ref = {str(w): w for w in range(10)}

        rst = 0
        for i in range(len(num2)):
            m = 10 ** (len(num2) - i - 1)
            n = ref[num2[i]]
            rst1 = 0
            for j in range(len(num1)):
                m1 = 10 ** (len(num1) - j - 1)
                rst1 += m1 * ref[num1[j]] * n
            rst += m * rst1

        return str(rst)

## main
if __name__ == '__main__':
    num1 = "1"
    num2 = "4"
    s = Solution()
    print(s.multiply(num1, num2))
