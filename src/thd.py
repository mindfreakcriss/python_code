# -*- utf-8 -*-
import threading
import time

list = [1,2,3,4]
lock = threading.Lock() #

class thread_one(threading.Thread):
    def __init__(self, name, list, i = 0):
        threading.Thread.__init__(self)
        self.name = name
        self.list = list
        self.i = i

    # 线程同步，利用一个锁
    def run(self):
        while self.i < (len(self.list)):
            lock.acquire() #获取锁
            self.list[self.i] = self.list[self.i] + 1 #每个值+1
            self.i = self.i + 1
            print("%s:%s" % (self.name,self.list[self.i-1]))
            lock.release() #释放锁
            time.sleep(1)

class mythread_two(threading.Thread): #继承类
    def __init__(self, name, list, i = 0):
        threading.Thread.__init__(self)
        self.name = name
        self.list = list
        self.i = i

    def run(self):
        while self.i < (len(self.list)):
            lock.acquire() #获取锁
            self.list[self.i] = self.list[self.i] - 2 #每个值-2
            self.i = self.i + 1
            print("%s:%s" % (self.name,self.list[self.i-1]))
            lock.release() #释放锁
            time.sleep(1)


if __name__ == "__main__":
    th1 = thread_one("th1",list)
    th2 = mythread_two('th2',list)
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    print("结束线程")
    print(list)
