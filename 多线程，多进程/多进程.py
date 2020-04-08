# from multiprocessing import Process
# import time
# import os

# def f(name):
#    time.sleep(2)
#    print('hello', name)
#    print("PID",os.getpid())
# if __name__ == '__main__':
#    for n in range(10):  # 创建一个进程
#        p = Process(target=f, args=('bob %s' % (n),))
#        # 启动
#        p.start()
#        # 等待进程执行完毕

from multiprocessing import Process, Queue
def ChildProcess(Q):
   Q.put(['Hello', None, 'World'])  # 在Queue里面上传一个列表
if __name__ == '__main__':
   q = Queue()  # 创建一个Queue
   p = Process(target=ChildProcess, args=(q,))  # 创建一个子进程，并把Queue传给子进程,相当于克隆了一份Queue
   p.start()  # 启动子进程
   print(q.get())  # 获取q中的数据
   p.join()