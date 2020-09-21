# -*- coding: utf-8 -*-
# @Time    : 2020/8/2 4:09 下午
# @Author  : Dawein
# @File    : bike_racing.py
# @Software : PyCharm

"""
一条道路上有m辆自行车，每辆车都有初始坐标和初始速度，速度都朝同一个方向。(匀速或加速)
1.判断会不会有自行车相撞
2.如果多建几条道路，最少几条能让这些车都不相撞
"""

class BikeRacing:
    def __init__(self):
        pass

    # (p: 10, v: 20)
    def is_collide(self, bikes):
        if bikes is None:
            return False
        if len(bikes) < 2:
            return False

        # 先按照自行车的起始位置从大到小排列
        bikes = sorted(bikes, key=lambda x: x[0], reverse=True)

        # 相当于： p(t) = p(0) + v * t
        # 自行车不碰撞的条件时，从最大起始位置开始，斜率v递减
        v_set = []
        v_set.append(bikes[0][1])
        for p, v in bikes[1:]:
            for k in v_set:
                if v > k:
                    return True
            v_set.append(v)
        return False

    # 至少需要多少条路才会不相撞
    def less_path(self, bikes):
        if bikes is None:
            return -1
        if len(bikes) == 1:
            return [bikes]
        if not self.is_collide(bikes):
            return [bikes]

        bikes = sorted(bikes, key=lambda x: x[0], reverse=True)

        paths = [[bikes[0]]]
        for next in bikes[1:]:
            copy_path = paths[:]
            is_in = False
            for i in range(len(copy_path)):
                cur = paths[i][:]
                cur.append(next)
                if self.is_collide(cur):
                    continue

                is_in = True
                paths[i].append(next)
                break
            if not is_in:
                paths.append([next])

        return paths



# main
if __name__ == '__main__':
    bikes = [(9,10), (7,6), (6,7)]
    br = BikeRacing()
    print(br.is_collide(bikes))

    paths = br.less_path(bikes)
    print("less path: {}, each path has bike: {}".format(len(paths), paths))