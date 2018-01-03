#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/2/16 17:11
# @Descript: 提供推荐算法，相似度评价值，欧几里德距离，皮尔逊相关度


from math import sqrt

critics = {
    'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5, 'Just my luck': 3.0, 'Superman Returns': 3.5,
                  'You,Me and Dupree': 2.5, 'The Night Listener': 3.0},
    'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 'Just my luck': 1.5, 'Superman Returns': 5.0,
                     'You,Me and Dupree': 3.0, 'The Night Listener': 3.5},
    'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0, 'Just my luck': 3.5,
                         'Superman Returns': 4.0, 'The Night Listener': 3.5},
    'Claudia Puig': {'Lady in the Water': 4.0, 'Snakes on a Plane': 4.5, 'Just my luck': 2.5, 'Superman Returns': 5.0,
                     'You,Me and Dupree': 3.0, 'The Night Listener': 3.5},
    'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 'Just my luck': 1.5, 'Superman Returns': 5.0,
                     'You,Me and Dupree': 3.0, 'The Night Listener': 3.5},
    'Toby': {'Lady in the Water': 3.0}
}


def sim_distance(prefs, person1, person2):
    '''欧几里德距离评价，返回一个有关person1与person2的基于距离的相似度评价
    '''

    # 得到shared_items的列表
    si = {}
    for i in prefs[person1]:
        if i in prefs[person2]:
            si[i] = 1

    # 如果二者没有共同之处，返回0
    if len(si) == 0:
        return 0
    # 计算所有差值的平方和
    sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item], 2)
                          for item in prefs[person1] if item in prefs[person2]])
    return 1 / (1 + sqrt(sum_of_squares))  # 偏好越相似，距离越短


def sim_pearson(prefs, p1, p2):
    '''皮尔逊相关系数算法，返回p1和p2的皮尔逊相关系数
    '''
    # 得到双方都评价过的物品列表
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1
    # 得到列表元素个数
    n = len(si)
    # 如果二者没有共同之处，返回1
    if n == 0:
        return 1
    # 对所有偏好者求和
    sum1 = sum(prefs[p1][t] for t in si)
    sum2 = sum(prefs[p2][t] for t in si)

    # 求平方和
    sum1_sqrt = sum([pow(prefs[p1][t], 2) for t in si])
    sum2_sqrt = sum([pow(prefs[p2][t], 2) for t in si])

    # 求乘积之和
    p_sum = sum([prefs[p1][t] * prefs[p2][t] for t in si])

    # 计算皮尔逊评价值
    num = p_sum - (sum1 * sum2 / n)
    den = sqrt((sum1_sqrt - pow(sum1, 2) / n) * (sum2_sqrt - pow(sum2, 2) / n))
    if den == 0:
        return 0
    r = num / den
    return r


def top_matches(prefs, person, n=5, similarity=sim_pearson):
    '''排序'''
    scores = [(similarity(prefs, person, other), other)
              for other in prefs if other != person]
    print(scores)
    scores.sort()
    scores.reverse()
    return scores[0:n]


# 欧几里德距离
lisa = critics['Lisa Rose']['Lady in the Water']
print(lisa)
critics['Toby']['Snakes on a Plane'] = 4.5
print(critics['Toby'])

sum_of_squares_ = sim_distance(critics, 'Lisa Rose', 'Gene Seymour')
print(sum_of_squares_)

# 皮尔逊相关性
perason = sim_pearson(critics, 'Lisa Rose', 'Gene Seymour')
print(perason)

toby = top_matches(critics, 'Lisa Rose', n=3)
print(toby)
