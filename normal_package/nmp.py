# -*- code=utf-8 -*-

import numpy #矩阵计算，NumPy提供了高性能的多维数组对象和丰富的数学函数，是Python进行数值计算和数据科学不可或缺的基础工具

#创建一个数组
arr = numpy.array(
    [
        (1,2,1),
        (2,2,1),
        (2,1,1)
    ]
)

#返回轴的个数
print(arr.ndim) #几维数组

#返回组的维度
print(arr.shape) #表示维度数组的大小 (n,m) n行，m列矩阵

#返回元素的总数
print(arr.size) #数组元素的总数

#返回元素的类型
print(arr.dtype)

#返回元素的大小
print(arr.itemsize)

#访问数组元素
print(arr[0][1])

#返回数组类型
print(type(arr))

#创建一个1行0列的数组，元素长度为5
array = numpy.ones((5,),dtype=int)
print(array)