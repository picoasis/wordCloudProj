# -*- coding:utf-8 -*-
# 网易云音乐 通过歌单ID，生成歌单中歌名的词云
# url 来自网页版的网易云音乐console 
import requests
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
from lxml import etree
import re
#import pdb
headers = {
    'Referer': 'http://music.163.com',
    'Host': 'music.163.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'User-Agent': 'Chrome/10'
}

# 获取到歌单
def get_song_list(headers,song_list_url):
    res = requests.request("GET",song_list_url,headers=headers, verify=False)
    if res.status_code == 200:
        xpathObj = etree.HTML(res.text)
        href_xpath='//*[@id="song-list-pre-cache"]//a/@href'
        name_xpath='//*[@id="song-list-pre-cache"]//a/text()'
        #pdb.set_trace()
        hrefs = xpathObj.xpath(href_xpath)
        names = xpathObj.xpath(name_xpath)
        #pdb.set_trace()
        songs_id = []
        songs_name = []
        for href,name in zip(hrefs,names):
            songs_id.append(re.sub(r'\D','',href))
            songs_name.append(re.sub(r'\s','',name))
        return songs_id,songs_name
    else:
        print(res.text)
 
        
# 创建词云展示
def createWordcloud(f):
    print("根据词频结果进行词云展示！")
    cut_text = " ".join(jieba.cut(f,cut_all=False,HMM=True))
    wc = WordCloud(
        font_path="STHeiti Light.ttc",
        max_words=100,
        width=2000,
        height=1200,
    )
    wordcloud = wc.generate(cut_text)
    wordcloud.to_file("song_list_wordcloud.jpg")
    # 词云展示
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

# 开始
song_list_id = '2829883282'
song_list_url = 'https://music.163.com/playlist?id=' + song_list_id
[songs_id,songs_name]= get_song_list(headers,song_list_url)
all_songs_name = ''
for name in songs_name:
    all_songs_name += name
createWordcloud(all_songs_name)