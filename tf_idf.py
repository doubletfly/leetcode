# -*- coding: utf-8 -*-
# @Time    : 2020/8/2 2:57 下午
# @Author  : Dawein
# @File    : tf_idf.py
# @Software : PyCharm

"""
tf-idf 计算
tf： Term Frequency - 词频 = 某个词在文档中出现的次数 / 该文档的总词数
idf： Inverse Document Frequency - 逆文档频率 = log（文档总数 / 含有某个词的文档数）
其中，tf要除以文档的总词数是为了消除文档过长带来的词频过大引起的不对称问题
idf取log是为了避免idf值线性增长，当文档数很大时
"""
import numpy as np
from collections import defaultdict

class TF_IDF:
    def __init__(self):
        pass

    # 统计每个文档中词的词频
    def count_word(self, corpus):

        corpus_cut = [doc.split(" ") for doc in corpus]
        # print(corpus_cut)

        word_freq = []
        for doc in corpus_cut:
            freq = defaultdict(int)
            for token in doc:
                freq[token] += 1
            word_freq.append(freq)
        # print(word_freq)
        return word_freq

    # 统计词在多少文档出现
    def count_doc(self, corpus):
        corpus_cut = [doc.split(" ") for doc in corpus]

        tokens = []
        for doc in corpus_cut:
            for token in doc:
                if token not in tokens:
                    tokens.append(token)

        doc_freq = defaultdict(int)
        for token in tokens:
            for doc in corpus_cut:
                if token in doc:
                    doc_freq[token] += 1
        # print(doc_freq)
        return doc_freq

    # 计算tf
    def calc_tf(self, word_freq):
        tf = []
        for doc in word_freq:
            total = 0
            for token in doc:
                total += doc[token]
            for token in doc:
                doc[token] = doc[token] / total
            tf.append(doc)
        # print(tf)
        return tf

    # 计算idf
    def calc_idf(self, corpus, doc_freq):
        doc_total = len(corpus)
        for key in doc_freq:
            doc_freq[key] = np.log((doc_total) / (doc_freq[key] + 1)) + 1
        # print(doc_freq)
        return doc_freq

    # 计算tf-idf
    def calc_tf_idf(self, corupus):
        word_list = self.count_word(corupus)
        doc_list = self.count_doc(corupus)

        tf = self.calc_tf(word_list)
        idf = self.calc_idf(corupus, doc_list)

        tf_idf = []
        for doc in tf:
            temp = defaultdict()
            for token in doc:
                temp[token] = doc[token] * idf[token]
            tf_idf.append(temp)

        for doc in tf_idf:
            print("doc: {}".format(list(doc.keys())))
            for token in doc:
                print("tf_idf of {}: {}".format(token, doc[token]))

# main
if __name__ == '__main__':
    corpus = ['this is the first document',
              'this is the second second document',
              'and the third one',
              'is this the first document']
    op = TF_IDF()
    op.calc_tf_idf(corpus)