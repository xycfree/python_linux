#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-17 14:48:00
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import psutil
import datetime,time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

'''
Python处理Windows进程
psutil(Python system and process utilities)是一个跨平台的进程管理和系统工具的python库，
可以处理系统CPU，memory，disks，network等信息。主要用于系统资源的监控，分析，以及对进程
进行一定的管理。通过psutil可以实现如ps，top，lsof，netstat，ifconfig， who，df，kill，free，
nice，ionice，iostat，iotop，uptime，pidof，tty，taskset，pmap。在Linux，windows，OSX，freebsd

文／Zhaifg（简书作者）
原文链接：http://www.jianshu.com/p/64e265f663f6
著作权归作者所有，转载请联系作者获得授权，并标注“简书作者”。
'''
#CPU
print psutil.cpu_count() #CPU物理个数
print psutil.cpu_count(logical=True) #逻辑个数
print psutil.cpu_stats() #CPU状态
print psutil.cpu_times() #cpu时间
     # - user
     # - system
     # - idle
     # - nice (UNIX)
     # - iowait (Linux)
     # - irq (Linux, FreeBSD)
     # - softirq (Linux)
     # - steal (Linux >= 2.6.11)
     # - guest (Linux >= 2.6.24)
     # - guest_nice (Linux >= 3.2.0)

print psutil.cpu_times(percpu=True) #每个cpu时间
print  psutil.cpu_times_percent() #cpu时间占比
print 'CPU占比:',psutil.cpu_percent() #CPU占比
psutil.cpu_percent(interval=2) #5秒内的CPU占比
psutil.cpu_percent(interval=2, percpu=True) #5秒内每个CPU占比，percpu=True

psutil.cpu_percent(interval=None, percpu=False)
# 返回一个浮点数，代表当前cpu的利用率的百分比，包括sy+user. 当interval为0或者None时，
# 表示的是interval时间内的sys的利用率。
# 当percpu为True返回是每一个cpu的利用率。

#Memory
print psutil.virtual_memory() #内存

#返回一个内存信息的元组，大小为字节

# total: 内存的总大小.
# available: 可以用来的分配的内存，不同系统计算方式不同； Linux下的计算公式:free+ buffers +　cached
# percent: 已经用掉内存的百分比 (total - available) / total 100.
# used: 已经用掉内存大小，不同系统计算方式不同
# *free: 空闲未被分配的内存，Linux下不包括buffers和cached

# Platform-specific fields:

# active: (UNIX): 最近使用内存和正在使用内存。
# inactive: (UNIX): 已经分配但是没有使用的内存
# buffers: (Linux, BSD): 缓存，linux下的Buffers
# cached:(Linux, BSD): 缓存，Linux下的cached.
# wired: (BSD, OSX): 一直存在于内存中的部分，不会被移除
# shared: (BSD): 缓存
# 内存总大小不等于Used+available,在windows系统可用内存和空闲内存是用一个

print psutil.virtual_memory()[1]/1024/1024/1024.0

print psutil.swap_memory() #返回系统的swap信息

# total: swap的总大小 单位为字节
# used: 已用的swap大小 bytes
# free: 空闲的swap大小 bytes
# percent: 已用swap的百分比
# sin: 从磁盘调入是swap的大小
# sout: 从swap调出到disk的大小
# sin， sout在windows没有意义。


#disks
print psutil.disk_partitions(all=False) #磁盘信息

# 返回所有挂载的分区的信息的列表，列表中的每一项类似于df命令的格式输出，包括分区，挂载点，
# 文件系统格式，挂载参数等，会忽略掉/dev/shm,/proc/filesystem等，
# windows上分区格式 "removable", "fixed", "remote", "cdrom", "unmounted" or "ramdisk"。

#print psutil.disk_usage('/dev/sda1')
#返回硬盘，分区或者目录的使用情况，单位字节   如果不存在会报“OSError”错误

print psutil.disk_io_counters(perdisk=False) #返回当前磁盘的io情况
# read_count: number of reads
# write_count: number of writes
# read_bytes: number of bytes read
# write_bytes: number of bytes written
# read_time: time spent reading from disk (in milliseconds)
# write_time: time spent writing to disk (in milliseconds)


#network
print psutil.net_io_counters(pernic=False) #返回整个系统的网络信息
# bytes_sent: 发送的字节数
# bytes_recv: 接收的字节数
# packets_sent: 发送到数据包的个数
# packets_recv: 接受的数据包的个数
# errin:
# errout: 发送数据包错误的总数
# dropin: 接收时丢弃的数据包的总数
# dropout: 发送时丢弃的数据包的总数(OSX和BSD系统总是0)
# 如果 pernic值为True，会显示具体各个网卡的信息。

print psutil.net_connections(kind='inet')
#返回系统的整个socket连接的信息，可以选择查看哪些类型的连接信息，类似于netstat命令


print psutil.users() #返回当前系统用户登录信息
# user: 用户的名称
# terminal: 运行终端，tty还是pts等
# host: 登录的IP
# started: 登录了多长时间

print psutil.boot_time() #返回当前时间
print datetime.datetime.fromtimestamp(psutil.boot_time()).strftime('%y-%m-%d %H:%M:%S')

#Processes
psutil.pids() #返回当前运行的进程pid列表

psutil.pid_exists(pid) #是否存在次pid，快速的验证方式pid in psutil.pids()

psutil.process_iter()
#返回一个包含Process对象的迭代器。每一个对象只创建一次，创建后缓存起来。
#当一个进程更新时，会更新缓存。遍历所有进程首选psutil.pids().迭代器排序是根据pid。
