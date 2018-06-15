#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016/10/23 21:08
# @Author  : xycfree
# @Link    : http://example.org
# @Version : $
# @Descript: Python排序算法
"""
排序算法：
    内部排序
        插入排序
            直接插入排序
            希尔排序
        选择排序
            简单选择排序
            堆排序
        交换排序
            冒泡排序
            快速排序
        归并排序
        基数排序
    外部排序
        内存和外存结合使用
"""
import random
from datetime import datetime

li = []
for i in range(10000):
    li.append(random.randint(1, 1000))
# print(li)

# li = [11, 38, 20, 89, 16, 95, 46, 28, 17, 78, 18, 44, 85, 99, 56, 43, 98, 71, 95, 47]
# print('初始化数据: {}'.format(li))


# 显示函数执行时间
def exectime(func):
    def inner(*args, **kwargs):
        begin = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        inter = end - begin
        print('E-time:{0}.{1}'.format(
            inter.seconds,
            inter.microseconds
        ))
        return result

    return inner


# 交换排序

@exectime
def bubble_sort(li):  # 无序列表
    """ 交换排序_冒泡排序
        时间复杂度：O(n²)
        空间复杂度：O(1)
        稳定性：稳定
    """
    lens = len(li)  # 列表长度
    for i in range(lens):
        for j in range(i):
            if li[j] > li[i]:
                li[j], li[i] = li[i], li[j]
    return li


def quick_sort(array):
    """ 快速排序
        时间复杂度：O(nlog₂n)
        空间复杂度：O(nlog₂n)
        稳定性：不稳定

        快排的思想：首先任意选取一个数据（通常选用数组的第一个数）作为关键数据，然后将所有比它小的数都放到它前面，所有比它大的数都放到它
        后面，这个过程称为一趟快速排序。
        百度百科给的算法：
        一趟快速排序的算法是：
        1）设置两个变量i、j，排序开始的时候：i=0，j=N-1；
        2）以第一个数组元素作为关键数据，赋值给key，即key=A[0]；
        3）从j开始向前搜索，即由后开始向前搜索(j--)，找到第一个小于key的值A[j]，将A[j]和A[i]互换；
        4）从i开始向后搜索，即由前开始向后搜索(i++)，找到第一个大于key的A[i]，将A[i]和A[j]互换；
        5）重复第3、4步，直到i=j； (3,4步中，没找到符合条件的值，即3中A[j]不小于key,4中A[i]不大于key的时候改变j、i的值，
        使得j=j-1，i=i+1，直至找到为止。找到符合条件的值，进行交换的时候i， j指针位置不变。另外，i==j这一过程一定正好是i+或j-
        完成的时候，此时令循环结束）。
    """

    def recursive(begin, end):

        # 判断low是否大于high,如果为True,直接返回
        if begin > end:
            return

        l, r = begin, end
        pivot = array[l]  # 设置基准数
        while l < r:
            # 如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
            while l < r and array[r] > pivot:
                r -= 1

            # 同样的方式比较前半区
            while l < r and array[l] <= pivot:
                l += 1
            array[l], array[r] = array[r], array[l]
        array[l], array[begin] = pivot, array[l]
        recursive(begin, l - 1)
        recursive(r + 1, end)

    recursive(0, len(array) - 1)
    return array

@exectime
def qsort(L):
    """快速排序"""
    if len(L) <= 1:
        return L
    return qsort([lt for lt in L[1:] if lt < L[0]]) + L[0:1]+ qsort([ge for ge in L[1:] if ge >= L[0]])



# 插入排序

def insert_sort(lists):
    """ 插入排序_直接插入排序 """
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    return lists


def insert_sort_1(array):
    """ 直接插入排序
        时间复杂度：O(n²)
        空间复杂度：O(1)
        稳定性：稳定
    :param array: lists
    :return:
    """
    for i in range(len(array)):
        for j in range(i):
            if array[i] < array[j]:
                array.insert(j, array.pop(i))
                break
    return array


def shell_sort(array):
    """ 希尔排序
        时间复杂度：O(n)
        空间复杂度：O(n√n)
        稳定性：不稳定
    :param array: list
    :return: list
    """
    gap = len(array)
    while gap > 1:
        gap = gap // 2  # 增量
        print('gap: {}'.format(gap))
        for i in range(gap, len(array)):
            for j in range(i % gap, i, gap):
                if array[i] < array[j]:
                    array[i], array[j] = array[j], array[i]
                    print('array: {}'.format(array))
    return array

# 选择排序

def select_sort(array):
    """简单选择排序
        时间复杂度：O(n²)
        空间复杂度：O(1)
        稳定性：不稳定
    """
    for i in range(len(array)):
        x = i  # min index
        for j in range(i, len(array)):
            if array[j] < array[x]:
                x = j
        array[i], array[x] = array[x], array[i]
    return array

def heap_sort(array):
    """
    堆排序
        时间复杂度：O(nlog₂n)
        空间复杂度：O(1)
        稳定性：不稳定
    :param array:
    :return:
    """
    def heap_adjust(parent):
        child = 2 * parent + 1  # left child
        while child < len(heap):
            if child + 1 < len(heap):
                if heap[child + 1] > heap[child]:
                    child += 1  # right child
            if heap[parent] >= heap[child]:
                break
            heap[parent], heap[child] = \
                heap[child], heap[parent]
            parent, child = child, 2 * child + 1

    heap, array = array.copy(), []
    for i in range(len(heap) // 2, -1, -1):
        heap_adjust(i)
    while len(heap) != 0:
        heap[0], heap[-1] = heap[-1], heap[0]
        array.insert(0, heap.pop())
        heap_adjust(0)
    return array


def merge_sort(array):
    """
    归并排序
        时间复杂度：O(nlog₂n)
        空间复杂度：O(1)
        稳定性：稳定
    :param array:
    :return:
    """
    def merge_arr(arr_l, arr_r):
        array = []
        while len(arr_l) and len(arr_r):
            if arr_l[0] <= arr_r[0]:
                array.append(arr_l.pop(0))
            elif arr_l[0] > arr_r[0]:
                array.append(arr_r.pop(0))
        if len(arr_l) != 0:
            array += arr_l
        elif len(arr_r) != 0:
            array += arr_r
        return array

    def recursive(array):
        if len(array) == 1:
            return array
        mid = len(array) // 2

        # 对拆分过后的左右再拆分 一直到只有一个元素为止
        # 最后一次递归时候ll和lr都会接到一个元素的列表
        # 最后一次递归之前的ll和rl会接收到排好序的子序列

        arr_l = recursive(array[:mid])
        arr_r = recursive(array[mid:])
        return merge_arr(arr_l, arr_r)

    return recursive(array)


def radix_sort(array):
    """
    基数排序
        时间复杂度：O(d(r+n))
        空间复杂度：O(rd+n)
        稳定性：稳定
    :param array:
    :return:
    """
    bucket, digit = [[]], 0
    while len(bucket[0]) != len(array):
        bucket = [[], [], [], [], [], [], [], [], [], []]
        for i in range(len(array)):
            num = (array[i] // 10 ** digit) % 10
            print('num: {}'.format(num))
            bucket[num].append(array[i])
            print('bucket: {}'.format(bucket))
        array.clear()
        for i in range(len(bucket)):
            array += bucket[i]
        digit += 1
    return array


if __name__ == '__main__':
    # print(bubble_sort(li))
    # print(insert_sort(li))
    # print(insert_sort_1(li))
    # print(shell_sort(li))
    # print(quick_sort(li))
    print(qsort(li))
    # print(select_sort(li))
    # print(heap_sort(li))
    # print(radix_sort(li))
