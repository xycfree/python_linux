#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/2/16 15:38
# @Descript: 机器学习，KNN,k-近邻算法

from numpy import *
import operator

def create_data_set():
    group = array([[1.0,1.1], [1.0,1.0], [0, 0.1]])
    labels = ['A', 'B', 'C', 'D']
    return group, labels

def classify(inx, dataset,labels,k):
    data_set_size = dataset.shape[0]
    diffmat = tile(inx, (data_set_size,1)) - dataset
    sqdiffmat = diffmat ** 2
    sqdistances = sqdiffmat.sum(axis=1)
    distances = sqdistances ** 0.5
    sorted_distindicies = distances.argsort()
    class_count = {}
    for i in range(k):
        vote_label = labels[sorted_distindicies[i]]
        class_count[vote_label] = class_count.get(vote_label,0) + 1
    sorted_class_count = sorted(class_count.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sorted_class_count[0][0]

def file_matrix(filename):
    fr = open(filename)
    array_line = fr.readlines()
    number_line = len(array_line)  # 得到文件行数
    return_mat = zeros((number_line, 3))  # 创建返回的nunpy矩阵
    class_label_vector = []
    index = 0
    for line in array_line:
        line = line.strip()  # 解析文件数据列表
        list_line = line.split('\t')
        return_mat[index, :] = list_line[0:3]
        class_label_vector.append(int(list_line[-1]))
        index += 1
    return return_mat, class_label_vector

