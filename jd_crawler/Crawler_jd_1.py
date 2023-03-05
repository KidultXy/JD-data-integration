import importlib,sys
import random
import pandas as pd
import time
import urllib
import requests
import numpy as np
from bs4 import BeautifulSoup
import re
from Crawler_jd_comment import jdComment

importlib.reload(sys)
# sys.setdefaultencoding('utf8')
start_url = 'https://list.jd.com/list.html?cat=670%2C671%2C672&go=0'
page_url = 'https://list.jd.com/list.html?cat=670%2C671%2C672&page='
# 获取指定个数的电脑url
def get_son_url(num=10):
    headers = {
        'Accept':'text / html, application / xhtml + xml, application / xml;q = 0.9, image / avif, image / webp, * / *;q = 0.8'
        ,'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'
        ,'Connection':'keep-alive'
        ,'Host':'list.jd.com'
        ,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'
        ,
    }
    jd_data = requests.get(start_url, headers=headers)
    jd_data.encoding = 'utf-8'
    soup = BeautifulSoup(jd_data.text, 'lxml')
    li = soup.select('ul.gl-warp > li.gl-item')
    # print(len(li))
    result = []
    k = 0  # 记录当前的个数
    for i,tg in enumerate(li):
        if k>=num:
            break
        # print(tg)
        li1 = tg.select('div.p-img')[0]
        # print(li1)
        rep = re.compile(r'<a.*?href="(.*?)".*?>')
        href = rep.findall(str(li1))[0]
        # print(href)
        if href[0] == '/':
            result.append('https:'+href)
            k+=1
        # break
    return result


def get_basic_info(num=10):
    # 每一页最多纪录30个，超出就要翻页
    headers = {
        'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / avif, image / webp, * / *;q = 0.8'
        , 'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'
        , 'Connection': 'keep-alive'
        , 'Host': 'list.jd.com'
        , 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'
    }
    pages = num // 30
    result = []
    for i in range(pages):
        jd_data = requests.get(page_url + str(i*2+1), headers=headers)
        jd_data.encoding = 'utf-8'
        soup = BeautifulSoup(jd_data.text, 'lxml')
        li = soup.select('ul.gl-warp > li.gl-item')
        print(len(li))

        for i in range(30):
            dic = {}  # 应该包含，产品id，价格price，图片链接imgurl，名字name，是否七天无理由sevendays，是否京东物流jdexpress，评论comments
            dic['id'] = li[i]['data-sku']
            price_tag = li[i].find_all(attrs={"data-price": dic['id']})[0]
            dic['price'] = price_tag.string
            name_tag = li[i].select('div.p-name > a')[0]
            dic['name'] = name_tag['title']
            imgurl_tag = li[i].find_all('img')[0]
            print(imgurl_tag)
            dic['imgurl'] = imgurl_tag['data-lazy-img']
            result.append(dic)
        time.sleep(random.randint(1,3))
    return result


def download_all_img(result):
    for li in result:
        url = 'http:' + li['imgurl']
        headers = {
            'Connection': 'keep-alive'
            ,'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'
            ,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'
            ,'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
        }
        img = requests.request('GET', url,headers=headers).content
        with open('../static/assets/jd-img/' + li['id'] + '.jpg', 'wb') as f:
            # print('正在下载: %s' % url)
            f.write(img)
    pass


def crawl_single_url(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'
        ,'Connection':'keep - alive'
        ,'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'
        ,'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
        ,'Host':'item.jd.com'
    }
    res_dict = {}  # 应该包含价格price，图片名img，名字name，是否七天无理由sevendays，是否京东物流jdexpress，评论comments
    jd_data = requests.get(url, headers=headers)
    jd_data.encoding = 'utf-8'
    soup = BeautifulSoup(jd_data.text, 'lxml')
    # print('soup\n',str(soup))
    li = soup.select('div.tab-con > div > div.p-parameter')[0]
    # print(li)
    try:
        res_dict['商品名称'] = re.compile(r'>商品名称：(.*?)<').findall(str(li))[0]
        res_dict['内存容量'] = re.compile(r'>内存容量：(.*?)<').findall(str(li))[0]
        res_dict['系统'] = re.compile(r'>系统：(.*?)<').findall(str(li))[0]
        res_dict['显卡型号'] = re.compile(r'>显卡型号：(.*?)<').findall(str(li))[0]
        res_dict['屏幕刷新率'] = re.compile(r'>屏幕刷新率：(.*?)<').findall(str(li))[0]
        res_dict['厚度'] = re.compile(r'>厚度：(.*?)<').findall(str(li))[0]
        res_dict['id'] = re.compile(r'>商品编号：(.*?)<').findall(str(li))[0]
        # li = soup.select('div#spec-n1.jqzoom > img#spec-img')[0]
        # res_dict['imgurl'] = li['src']
    except Exception:
        print(Exception)
    try:
        res_dict['品牌'] = li.select('ul#parameter-brand > li')[0]['title']
    except Exception:
        print(Exception)
    # li = soup.select('div.itemInfo-wrap > div.sku-name')[0]
    # res_dict['imgurl'] = li.select('img')[0]['src']
    # li = soup.select('div#J_LogisticsService > div.dd > div.icon-wl')
    # print(len(li))
    print(res_dict)
    return res_dict


def crawl_single_url_1(pid):
    url = 'https://item.jd.com/{}.html'.format(pid)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'
        , 'Connection': 'keep - alive'
        , 'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'
        , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
        , 'Host': 'item.jd.com'
    }
    res_dict = {}  # 应该包含品牌brand，好评率like_rate，发货地district
    res_dict['id'] = pid
    jd_data = requests.get(url, headers=headers)
    jd_data.encoding = 'utf-8'
    soup = BeautifulSoup(jd_data.text, 'lxml')
    li = soup.select('div.tab-con > div > div.p-parameter')[0]
    try:
        res_dict['商品名称'] = re.compile(r'>品牌：(.*?)<').findall(str(li))[0]
    except:
        res_dict['brand'] = '未知'
    # li = soup.select('div#summary-service')[0]
    # print(li.string)
    try:
        res_dict['district'] = re.compile(r'从(.*?)发货').findall(li.text)[0]
    except:
        res_dict['district'] = '京东'
    print(res_dict)
    return res_dict


def crawl_jd_computer(num):
    result = get_basic_info(num)
    df = pd.DataFrame(result)
    ret = []
    for index,li in enumerate(result):
        print('爬取第{}个'.format(index+1))
        ret_url = crawl_single_url('https://item.jd.com/{}.html'.format(li['id']))
        ret.append(ret_url)
        # time.sleep(random.randint(1,3))
    df_new = pd.DataFrame(ret)
    df_all = pd.merge(df,df_new,on='id')
    df_all.to_excel('jdcomputer.xlsx')
    download_all_img(result)


if __name__ == '__main__':
    # crawl_jd_computer(300)
    data = pd.read_excel('jdcomputer.xlsx')
    for id in data['id']:
        jdComment(int(id))
    # data = pd.read_excel('jdcomputer.xlsx')
    # ret = []
    # for id in data['id']:
    #     ret_url = crawl_single_url_1(id)
    #     ret.append(ret_url)
    # df_1 = pd.DataFrame(ret)
    # df_1.to_excel('jdcomputer_new.xlsx')






