#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 20:52:44 2021

@author: picoasis
"""

'''
#处理英文txt
from wordcloud import WordCloud 
import matplotlib.pyplot as plt
#创建一个词云
wc = WordCloud(
    background_color = 'white',
    max_words = 100,
    max_font_size = 150,
    width = 2000,
    height = 1200,
    random_state = 30
    )
#读取文件
text =open(u'./outOfAfrica.txt','r',encoding='utf-8').read()
#生成词云
africaCloud = wc.generate(text)
#将词云图像保存为图片格式文件 wordcloud.tofile('a.jpg')
#或则会用matplotlib显示
plt.imshow(africaCloud)
plt.axis('off')
plt.show()
'''
#处理中文str
# 处理中文需要使用结巴分词
# 针对中文的情况需要设置中文字体，否则显示乱码
from wordcloud import WordCloud 
import matplotlib.pyplot as plt
import jieba
#from PIL import Image
#import numpy as np



def create_word_cloud(f):
    print('根据词频计算词云')
    text = " ".join(jieba.cut(f,cut_all=False,HMM=True))
    wc = WordCloud(
        font_path='STHeiti Light.ttc',
        max_words=100,
        width=2000,
        height = 1200,
        )
    wordcloud = wc.generate(text)
    #写词云图片
    #方法一：将词云文件直接保存为图片格式文件
    wordcloud.to_file("wordcloud.jpg")
    #方法二：显示词云文件
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()
    
f ='数据分析全景图及修炼指南\
    学习数据挖掘的最佳学习路径是什么？\
    Python基础语法：开始你的Python之旅\
    Python科学计算：NumPy\
    Python科学计算：Pandas\学习数据分析要掌握哪些基本概念？\
    用户画像：标签化就是数据的抽象能力\
    数据采集：如何自动化采集数据？\
    数据采集：如何用八爪鱼采集微博上的“D&G”评论？\
    Python爬虫：如何自动化下载王祖贤海报？\
    数据清洗：数据科学家80%时间都花费在了这里？\
    数据集成：这些大号一共20亿粉丝？\
    数据变换：大学成绩要求正态分布合理么？\
    数据可视化：掌握数据领域的万金油技能\
    一次学会Python数据可视化的10种技能'
    
#设置停用词
def remove_stop_words(f):
    stop_words = ['学会','就是','如何','的','掌握','及','什么','是']
    for stop_word in stop_words:
        f = f.replace(stop_word,'')
    return f
    
f = remove_stop_words(f)
create_word_cloud(f)