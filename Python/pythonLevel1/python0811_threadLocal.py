# -*- coding: utf-8 -*-


global_dict = {}


def std_thread(name):
    std = Student(name)
    # 把std放到全局变量global_dict中：
    global_dict[threading.current_thread()] = std
    do_task_1()
    do_task_2()


def do_task_1():
    # 不传入std，而是根据当前线程查找：
    std = global_dict[threading.current_thread()]


def do_task_2():
    # 任何函数都可以查找出当前线程的std变量：
    std = global_dict[threading.current_thread()]

print '-------ThreadLocal-------'
import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()


def process_student():
    print 'Hello, %s (in %s)' % (local_school.student1, threading.current_thread().name)


def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student1 = name
    process_student()

t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')

t1.start()
t2.start()
t1.join()
t2.join()

# local_school.student都是线程的局部变量，可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理。

# ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。

# 计算密集型 vs. IO密集型
# 用单进程 单线程 模型来执行多任务，这种全新的模型称为事件驱动模型。
# Nginx就是支持异步IO的Web服务器

# 协程 单进程的异步编程模型

print '-------分布式进程-------'
# https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386832973658c780d8bfa4c6406f83b2b3097aed5df6000
# 未学
