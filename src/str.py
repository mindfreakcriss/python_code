# -*- coding = utf-8 *-*

str = "python"

#下标访问
s1 = str[0]
print("index访问: " + s1)

#循环遍历
for s in str:
    print("循环遍历：" + s + " ")

#字符串拼接
print("字符串拼接：" + "+".join(str))

#字符计数
print("P出现的次数：{0}".format(str.count('p')))

#字符串格式化
# %格式符 %s 字符串，%d 整数 %f 浮点数，可指定小数表示精度
name = 'python'
age = 14
score = 15.678
print("%s is %d years old, and he score is %.2f " % (name, age, score))
# format() 
print("{0} is {1} years old , and he score is {2:.2f}".format(name, age, score))
# f-string 性能好，推荐 直接使用，需要表明浮点数位数，加：即可
print(f"{name} is {age} years old, and he score is {score:.2f}")


