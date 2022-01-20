# -*- coding: UTF-8 -*-
# 分词，文本分析学习

import numpy as np
import pandas as py

import jieba
import jieba.analyse

# 中文分词，载入数据，分析文本
def printf(txt):
    for i in txt:
        print(i)

def readdata(datanum):
    if datanum == 1:
        with open('data/text.txt', 'r', encoding='utf-8-sig') as f:  # 用于读取txt文件
            a = f.read()
            return a
    else:
        print("无数据读取")

def del_stopword():
    stopword=[]
    with open('data/stopword.txt','r',encoding='utf-8-sig') as f:
        stopword=f.readlines()
        for line in f.readlines():
            l=line.strip()
            if l=='\\n':
                l='\n'      #换行符
            if l=='\\u3000':
                l='\u3000'      #制表符
            stopword.append()
    return stopword

def main():
    print('程度开始')
    a_readdata1 = readdata(1)                #调用读取函数
    # 分词之前，需要运用，自定义词典，将词典中没有的词语，添加到词典中去，自定义词典名称为custom.txt
    jieba.load_userdict('data/custom.txt')   #载入自定义词典，加入新添加的词语，一旦写入字典，改动必须重新执行代码
    jieba.del_word('中出')                    #去出jieba词库中的一些错误分词
    jieba.add_word('出了')                    #手动加入一些词语，可以随删随改，在当前代码后再加入代码删改
    jieba.suggest_freq('中','出',tune=True)   #增加分开的‘中’‘出’的概率，这样会将两个字分来,提高词的权重
    jieba.suggest_freq('一个人',tune=True)    #使得一个人这三个字不会被分开


    b_cutdata1 = jieba.cut(a_readdata1)      #完成分词
    c_joindata1=' '.join(b_cutdata1)         #将分词后的拼接
    with open('data/text1_data1.txt','w',encoding='utf-8-sig') as f:
        f.write(c_joindata1)
    # 使用with open完成数据的写出，重新将分词后语句输出到txt文件


if __name__ == '__main__':
    stopword=del_stopword()
    printf(stopword)
    #main()
