# -*- coding: utf-8 -*-
# @Time    : 2021/1/14 5:26 下午
# @Author  : Dawein
# @File    : L134_canComplete_circle.py
# @Software : PyCharm

"""
在一条环路上有N个加油站，其中第i个加油站有汽油gas[i]升。

你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1个加油站需要消耗汽油cost[i]升。
你从其中的一个加油站出发，开始时油箱为空。

如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。

说明:
如果题目有解，该答案即为唯一答案。
输入数组均为非空数组，且长度相同。
输入数组中的元素均为非负数。
示例1:
输入:
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
输出: 3
解释:
从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
因此，3 可为起始索引。

示例 2:
输入:
gas  = [2,3,4]
cost = [3,4,3]
输出: -1
解释:
你不能从 0 号或 1 号加油站出发，因为没有足够的汽油可以让你行驶到下一个加油站。
我们从 2 号加油站出发，可以获得 4 升汽油。 此时油箱有 = 0 + 4 = 4 升汽油
开往 0 号加油站，此时油箱有 4 - 3 + 2 = 3 升汽油
开往 1 号加油站，此时油箱有 3 - 3 + 3 = 3 升汽油
你无法返回 2 号加油站，因为返程需要消耗 4 升汽油，但是你的油箱只有 3 升汽油。
因此，无论怎样，你都不可能绕环路行驶一周。
"""

# 基本点： 如果汽油总量大于等于消耗总量，那必定存在一个起始点可以绕一圈
# 起始点的确定： 如果从某个点出发，到另外一个点后，加油的量小于消耗的量，那说明是达到不了新的点的；只有当加油的量大于
# 等于消耗的量，才能到达新的点。

class Solution():

    def canCompleteCircuit(self, gas: list, cost: list):

        if gas is None or cost is None:
            return -1
        if len(gas) != len(cost):
            return -1

        total_gas = 0
        total_cost = 0
        residual = 0
        start = 0
        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            residual += (gas[i] - cost[i])
            if residual < 0:
                start = i + 1
                residual = 0
        # 如果汽油总量小于消耗总量，则没有没有起点开始能绕一圈
        if total_gas < total_cost:
            return -1
        return start

# main
if __name__ == '__main__':
    # gas = [1, 2, 3, 4, 5]
    # cost = [3, 4, 5, 1, 2]
    gas = [4, 3, 5]
    cost = [3, 4, 3]
    s = Solution()
    print(s.canCompleteCircuit(gas, cost))