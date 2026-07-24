# -*- code=utf-8 -*-

import pandas 
#Pandas 是 Python 数据分析的"瑞士军刀"，几乎任何涉及表格数据的处理、清洗、分析和转换任务，都可以用它高效完成。它是数据科学、机器学习和商业分析中最基础也是最重要的库之一

pd = pandas.Series([1,2,3,4,5,6]) #带标签的一维数组，不声明索引，从0开始
print(pd)
print(pd.values) #值
print(pd.index) #索引

pd2 = pandas.Series([1,2,3,4,5,6], index=["a","b","c","d","e","f"])
print(pd2)

#取大于中位数的值
print(pd2[pd2 > pd2.median()])
#取大于平均数的值
print(pd2[pd2 > pd2.mean()])


#####DataFrame
print("DataFrame内容")
dic = {
    "user":["jack","marry","tom"],
    "pass":["1234","4567","7890"],
    "age": [23,24,25]
}
df = pandas.DataFrame(dic)
print(df)