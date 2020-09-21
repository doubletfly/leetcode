# -*- coding: utf-8 -*-
# @Time    : 2020/8/2 5:13 下午
# @Author  : Dawein
# @File    : rnn.py
# @Software : PyCharm


"""
循环神经网络：
rnn
lstm
gru
"""

import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    # y = 1 / (1 + exp(-x))
    y = []
    for k in x:
        y.append(1 / (1 + np.exp(-k)))
    return y

def tanh(x):
    # y = (exp(x) - exp(-x)) / (exp(x) + exp(-x))
    y = []
    for k in x:
        y.append((np.exp(k) - np.exp(-k)) / (np.exp(k) - np.exp(-k)))
    return y

class RNN:
    def __init__(self):
        pass

    def rnn(self, x):
        WT = 1
        return tanh(WT * x)

    def lstm(self, x, state):
        c = state[0]
        h = state[1]

        W1, W2 = 1, 1
        f = sigmoid(W1 * [x, h]) # 遗忘门
        r = sigmoid(W2 * [x, h]) # 输入门
        c_p = tanh(W1 * [x, h]) # 新状态
        c = f * c + r * c_p # 新细胞状态

        q = sigmoid(W2 * [x, h]) # 输出门
        h = q * tanh(c) # 新输出

        return (c, h)

    def gru(self, x, h):
        # 相比于LSTM而言，GRU只有两个门： 遗忘门和更新门，参数更少，但效果相当
        f = sigmoid([x, h]) # 遗忘门
        r = sigmoid([x, h]) # 更新门
        h_p = tanh([x, r * h])
        h = (1 - f) * h + f * h_p
        return h


# main
if __name__ == '__main__':
    x = [w for w in range(-10, 10)]
    y = sigmoid(x)
    z = tanh(x)
    plt.plot(y)
    plt.show()
