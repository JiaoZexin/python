import threading
import time
from multiprocessing.dummy import Pool
def seq(string):
    print(string,"star :%.f s"%(time.time()))
    time.sleep(2)
    print(string,"end :%.f s"%(time.time()))

# th1=threading.Thread(target=seq,args=("music",2,))
# th2=threading.Thread(target=seq,args=("movie",3,))

# print("start :%.f s"%(time.time()))
t1=time.time()
# th1.setDaemon(True)
# th2.setDaemon(True)
# th1.start()
# th2.start()
# time.sleep(1)
lis=["A","B","C","D"]
pool=Pool(4)
pool.map(seq,lis)
print("all finished :%.f s"%(time.time()-t1))