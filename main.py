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
#或者会用matplotlib显示
plt.imshow(africaCloud)
plt.axis('off')
plt.show()
'''
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

'''
'''
给毛不易的歌词制作词云
流程：
1. Python爬虫获取歌词列表————python爬虫获取HTML，Xpath对歌曲ID名称进行解析
2. 获取每首歌的歌词——————通过网易云音乐API接口获取每首歌的歌词
3. 获取歌词文本——————将所有的歌词合并得到一个变量
____________________数据准备
4. 设置词云模型
5. 通过歌词生成词云
6. 词云可视化
____________________词云分析
'''

import requests
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba 
from lxml import etree
import pdb

#获取歌曲
#得到指定歌手页面 热门钱50 的歌曲ID，歌曲名
def get_songs(artist_id):
    page_url ='https://music.163.com/artist?id='+artist_id
    #获取网页HTML
    res = requests.request('GET', page_url, headers=headers,stream=True, verify=False)
    #用XPATH机械 前50首热门歌曲
    pdb.set_trace()
    html = etree.HTML(res.text)
    href_xpath = "//*[@id='hotsong-list']//a/@href"
    name_xpath = "//*[@id='hotsong-list']//a/text()"
    hrefs = html.xpath(href_xpath)
    names = html.xpath(name_xpath)
    pdb.set_trace()
    #设置热门歌曲的ID，歌曲名称
    song_ids=[]
    song_names = []
    for href,name in zip(hrefs,names):
        song_ids.append(href[9:])
        song_names.append(name)
        print(href,'',name)
    return song_ids,song_names
    
    
#得到一首歌的歌词
def get_song_lyric(headers,lyric_url):
    res = requests.request('GET', lyric_url, headers=headers)

    if 'lrc' in res.json():
        lyric = res.json()['lrc']['lyric']
        new_lyric1 = re.sub(r'[\d:.[\]]','',lyric)#去除时间
        pdb.set_trace()
        #print('new_lyric______:',new_lyric1)        
        '''
         去除这些东西
             鼓Drums by：荒井十一
             贝斯 Bass by：许钧
             吉他 Guitars by  许钧
             键盘＆合成器 Keys＆Synth by 许钧
             弦乐编写 Strings Arranged by：胡静成、许钧
             弦乐监制 Strings Directed by：胡静成
         
         规律：大部分 “空格开头，\n结尾，包含 ：，” 的字符串
        '''
        new_lyric = re.sub(r'\s?.*[(by：)：:【】@]+.*\n?','',new_lyric1)
       # print('new_lyric______:',new_lyric)
        return new_lyric
    else:
        return ''

#停用词移除
def remove_stop_words(f):
    stop_words =['作词', '作曲', '编曲', '制作人','毛不易'] 
    for stop_word in stop_words:
        f = f.replace(stop_word,'')
    return f
    
#生成词云
def create_word_cloud(f):
    print('根据词频，开始生成词云...')
    #print(f)
    f = remove_stop_words(f)
    cut_text = ' '.join(jieba.cut(f,cut_all=False,HMM=True))
    wc = WordCloud(
        font_path='STHeiti Light.ttc',
        max_words=100,
        width = 2000,
        height = 1200,
        )
    #print(cut_text)
    wordcloud = wc.generate(cut_text)
    #词云图片
    wordcloud.to_file("maobuyi.jpg")
    #显示词云文件
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()
    

headers = {
    'Referer':'http://music.163.com',
    'Host':"music.163.com",
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'User-Agent':'Chrome/10'
    }

artist_id = '12138269'#毛不易的id
[song_ids,song_names] = get_songs(artist_id)
all_word = ''
for (song_id,song_name) in zip(song_ids, song_names):
    lyric_url = 'http://music.163.com/api/song/lyric?os=pc&id='+song_id + '&lv=-1&kv=-1&tv=-1'
    lyric = get_song_lyric(headers, lyric_url)
    #print('lyric:',lyric)
    all_word = all_word +' '+ lyric
    #print(song_name)

#print('all_word',all_word)    
create_word_cloud(all_word)
    
   