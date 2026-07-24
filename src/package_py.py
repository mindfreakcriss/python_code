# -*- code = utf-8 -*-
import math #数学模块
import os #操作系统模块
import sys#变量的访问
import time#时间模块
import datetime#时间处理模块
import random#随机模块
import threading#线程内容

def func(*tup):
    for i in tup:
        print(i, end="")
        time.sleep(1)

if __name__ == "__main__":
    #数学函数的使用
    floor_data = math.floor(12.3)
    print(floor_data)

    #获取当前目录
    dir = os.getcwd()
    print(dir)
    #列出当前目录的文件
    files = os.listdir(".")
    print(files)
    #新建文件夹
    #判断是否为目录
    new_dir = dir + "/new_dir"
    if (os.path.isdir(new_dir)):
        print("目录已经存在")
        #删除文件夹，目录必须为空
        os.rmdir(new_dir)
    else:
        new_dir = os.mkdir('new_dir')
        print("目录已经创建完成")

    #获取当前的参数
    args = sys.argv
    print("当前脚本的参数为:")
    print(args)

    #时间模块(1784858398.091035)
    print(time.time())
    #格式化当前本地时间
    print(time.localtime())
    #格式化输出时间
    print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    #获取当前时间,可以传时区
    print(datetime.datetime.now())
    #获取随机数
    print(random.random())
    #从指定序列随机选出一个元素
    list = [1,2,3,4,5,6,7,8]
    print("随机一个元素:" + str(random.choice(list)))

    ##### 多线程内容
    tup1 = (1,2,3,4,5,6,7)
    tup2 = ("a","b","c","d","e","f")
    #创建线程1
    th1 = threading.Thread(target=func, args=tup1,name="thread_1")
    #创建线程2
    th2 = threading.Thread(target=func, args=tup2,name="thread_2")
    th1.start() #启动线程1
    th2.start()
    th1.join() #等待线程1执行完毕
    th2.join()
    print("线程运行结束")