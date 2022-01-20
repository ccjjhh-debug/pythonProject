# -*- coding:UTF-8 -*-
# @time: 2022-01-19 14:38
# @file: pandas_learn.py
# @software: PyCharm
# author CJH

import numpy as np

# 创建数组，再转化为矩阵
array=np.array([[1,2,3],
                [4,5,6]])
print(array)
print('number of dim:',array.ndim)  #二维数组
print('shape:',array.shape)         #输出矩阵的行列数
print('array_size:',array.size)     #矩阵的大小

a = np.array([[2,23,4],
             [3,33,34]],dtype=np.double)    #设置浮点数，float
print(a.dtype)

b=np.ones((4,5),dtype=np.double)     #生成3,4纬的矩阵
print(b)

a1=np.arange(12).reshape(3,4)      #生成1,2....11数列
print(a1)

a2=np.linspace(1,10,20).reshape(4,5)      #等差数列生成20，1~10
print(a2)

b_a2=b-a2       #逐个元素相减
print(b_a2)

b_a22=b_a2**2
print(b_a22)

c=10*np.sin(b_a22)     #三角函数，大小判断输出
print(c<5)

a_mut=np.array([[1,1],
                [2,2]],dtype=np.double)
b_mut=np.arange(4).reshape((2,2))
# 运行矩阵乘法
cmul = a_mut*b_mut   #逐个相乘
cdot = np.dot(a_mut,b_mut)    #矩阵乘法  c_dot = a_mut.dot(b_mut)
print(cmul)
print(cdot)

a_random = np.random.random((2,4))*10   #随机生成2,4的矩阵
print(a_random)

print(np.sum(a_random,axis=0))
print(np.max(a_random,axis=0))
print(np.min(a_random,axis=1))   #axis=1,求行的。。得出列向量，axis=0求列的。。。得出行向量

# 寻找最大值的索引
# array=np.array([[1,2,3],
#                 [4,5,6]])
print(np.argmax(array,axis=1))
print(np.max(array,axis=1))    #加上arg求索引，不加arg求数值
#python中索引使用[]中括号
print(np.mean(array,axis=1))    #mean求平均数
print(array.mean(axis=1))
print(np.median(array,axis=1))   # 求中位数

print(np.cumsum(array,axis=0))    #前缀和  ，0列求和，1行求和
print(np.diff(array,axis=1))      #前项差
print(array.T)                    #矩阵转置   np.transpose(array)
print(array.dot(array.T))         #矩阵乘法   未重新赋值，不影响原本矩阵的数值

print(np.clip(array,2,7))         #截数字，小于2的变为2，大于7的变为7

array1=np.arange(3,15).reshape(3,4)
print(array1)
print(array1[1][2])               #[1][2]=[1,2]

print(array1[1][:])               #:打印全部行or全部列   [1,:]
for i in array1:
    print(i)    #迭代输出每一个，先输出行，如要先输出列，使用array1.T,将其转置再迭代
    #python先遍历行

A = np.array([[1,1,1]])
B = np.array([[2,2,2]])           #列不相等，无法进行列合并
print(np.hstack((A,B)))         #行合并
print(np.vstack((A,B)))         #列合并
print(A[np.newaxis,:].T)          #在行上加了一个维度，方便转置为列向量,再对行向量进行转置,
print(B.shape[0])                 #如果在一开始就加入2个[]就不需要在后期加维度
print(B.shape[1])
print(A.T)


