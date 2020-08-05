# -*- coding: utf-8 -*-
# @Time    : 2020/8/4 11:37 下午
# @Author  : Dawein
# @File    : IntToRoman.py
# @Software : PyCharm

"""
整数转罗马数字
LeetCode 12
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
需要注意的是：
I可以放在V(5) 和X(10) 的左边，来表示 4 和 9。
X可以放在L(50) 和C(100) 的左边，来表示 40 和90。
C可以放在D(500) 和M(1000) 的左边，来表示400 和900。

输入在区间【1， 3999】
"""

class IntToRoman:
    def __init__(self):
        pass

    def convert(self, x):

        if x is None:
            return ""
        if x < 1 or x > 3999:
            return ""

        # 先构建映射表
        mapping = {1: "I", 5: "V", 10: "X",
                   50: "L", 100: "C", 500: "D", 1000: "M"}

        # 构建特殊映射表
        sp_mapping = {4: "IV", 9: "IX", 40: "XL", 90: "XC",
                      400: "CD", 900: "CM"}

        roman = ""
        r = 1
        y = x
        while y > 10:
            y = y // 10
            r = r * 10
        d = y * r
        r = x - d
        if d == 0:
            d = x
            r = 0
        if d in sp_mapping:
            roman += sp_mapping[d]
            roman += self.convert(r)
        else:
            pre_num = 0
            for key in mapping:
                if x < key:
                    break
                pre_num = key
            r = x - pre_num
            roman += mapping[pre_num]
            roman += self.convert(r)

        return roman

# main
if __name__ == '__main__':
    itr = IntToRoman()
    print(itr.convert(3000))

