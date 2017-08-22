# -*- coding: utf-8 -*-
import os

print '-------多进程-------'

# print 'Process (%s) start...' % os.getpid()
# pid = os.fork()
# if pid == 0:
#     print 'I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid())
# else:
#     print 'I (%s) just created a child process (%s).' % (os.getpid(), pid)


from multiprocessing import Process

# 子进程要执行的代码


def run_proc(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())

if __name__ == '__main__':
    print 'Parent process %s.' % os.getpid()
    p = Process(target=run_proc, args=('test',))
    print 'Process will start.'
    p.start()
    p.join() # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    print 'Process end.'

# 需要传入一个执行函数和函数的参数
# p = Process(target=run_proc, args=('test',))


print '-------Pool-------'

from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))

if __name__=='__main__':
    print 'Parent process %s.' % os.getpid()
    p = Pool() # p = Pool(5) 默认4个进程
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print 'Waiting for all subprocesses done...'
    p.close() # 调用close()之后就不能继续添加新的Process了
    p.join() # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    print 'All subprocesses done.'

# 调用join()之前必须先调用close()
# 调用close()之后就不能继续添加新的Process了

print '-------多进程-------'
print '-------多进程-------'
print '-------多进程-------'


