#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/7/9 18:48
# Author: xycfree
# @Descript: 守护进程

import os
import sys
import atexit

def daemonize(pid_file=None):
    pid = os.fork()  # 从父进程fork一个子进程

    if pid:
        sys.exit()
    os.chdir('/')
    os.umask(0)
    os.setsid()

    _pid = os.fork()
    if _pid:
        sys.exit(0)
    sys.stdout.flush()
    sys.stderr.flush()

    with open('dev/null') as read_null, open('/dev/null', 'w') as write_null:
        os.dup2(read_null.fileno(), sys.stdin.fileno())
        os.dup2(write_null.fileno(), sys.stdout.fileno())
        os.dup2(write_null.fileno(), sys.stderr.fileno())

    if pid_file:
        with open(pid_file, 'w+') as f:
            f.write(str(os.getpid()))
        atexit.register(os.remove(), pid_file)

if __name__ == '__main__':
    daemonize(pid_file=None)