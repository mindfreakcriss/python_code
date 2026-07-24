# -*- code=utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

#基础画布
def basic_demo():
    fig = plt.figure("figure name") #创建画布
    ax = fig.add_subplot(221)
    ax.set(xlim=[0.5, 4.5], ylim=[1,10],title='Axis title',ylabel='Y-Axis', xlabel="X-Axis")
    ax=fig.add_subplot(222)
    ax.set(xlim=[0.5, 4.5], ylim=[1,10],title='Axis title',ylabel='Y-Axis', xlabel="X-Axis")
    plt.show()

#折线图
def zx_demo():
    fig = plt.figure("figure name")
    ax = fig.add_subplot(111)
    x = np.linspace(0, np.pi)
    y = np.sin(x)
    y2 = np.cos(x) + 6
    y3 =np.cos(x) + 3
    # linestyle 线的样式，marker 控制点的样式 color 线的颜色
    ax.plot(x, y, color="#1cba28", linestyle='--',linewidth=2,label='first',marker='o') #第一根线
    ax.plot(x,y2, color="#0598ff", linestyle=':',linewidth=2,label='second',marker='+') #第二根线
    ax.plot(x,y3, color="#ffc105", linestyle='-',linewidth=2,label='three',marker='*') #第三根线
    plt.legend(loc=2) #显示图例
    plt.show()

#散点图
def sd_demo():
    fig = plt.figure('figure name')
    ax = fig.add_subplot(111)
    x = np.arange(10)
    y = np.random.randn(10)
    ax.scatter(x, y, color='red', marker='o')
    plt.show()

#柱状图
def zz_demo():
    fig = plt.figure('figure name')
    ax = fig.add_subplot(111)
    x = np.arange(10)
    y = np.random.randn(10)
    ax.bar(x, y, color="#c248be",label='bar')
    ax.legend(loc=2)
    plt.show()

# 饼图
def pie_demo():
    fig = plt.figure('figure name')
    ax = fig.add_subplot(111)
    labels = "A","B","C","D"
    sizes = [10,10,20,60]
    explode = (0,0,0.1,0)
    colors = ['r','g','y','b']

    #x --> 每一块的百分比
    #labels --> 外侧说明文字
    # explode 每一块离开中心的距离
    # startangle 起始绘制角度
    # shadow 阴影

    ax.pie(sizes, explode=explode, labels=labels,colors=colors,pctdistance=0.4,shadow=True,labeldistance=0.8,startangle=30,radius=1.3,counterclock=False,textprops={'fontsize':20,'color':'black'})
    plt.show()


if __name__ == "__main__":
    #zx_demo()
    #sd_demo()
    #zz_demo()
    pie_demo()
