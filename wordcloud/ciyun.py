import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
import re
from PIL import Image
import numpy as np
import pandas as pd

def getwordcloud(pid):
    stopwords = open("stopwords.txt",encoding='utf-8').read()
    text = ''
    path = '../jd_crawler/comments/jdcomment_{}.csv'.format(pid)
    df = pd.read_csv(path,encoding='gbk')
    # print(df['content'])
    result = df['content']
    for i in range(len(result)):
        p1 = re.compile(r'(运行速度：)')
        p2 = re.compile(r'(屏幕效果：)')
        p3 = re.compile(r'(散热性能：)')
        p4 = re.compile(r'(外形外观：)')
        p5 = re.compile(r'(轻薄程度：)')
        p6 = re.compile(r'(其他特色：)')
        result[i] = p1.sub('',result[i])
        result[i] = p2.sub('', result[i])
        result[i] = p3.sub('', result[i])
        result[i] = p4.sub('', result[i])
        result[i] = p5.sub('', result[i])
        result[i] = p6.sub('', result[i])
    print(result)
    # text=[]
    for item in result:
        # if item[0] not in stopwords:
        #     # text.append(str(item[0]))
        #     text=text+item[0]
        # # print(item[0])
        text+=item
    # print(text)
    # 分词
    cut = list(jieba.cut(text))
    # print(type(stopwords),stopwords)
    for cu in cut:
        if cu in stopwords:
            while cu in cut:
                cut.remove(cu)
    print('test','非常' in stopwords)
    string_s = ' '.join(cut)
    # print(string_s)
    # text = ' '.join(jieba.cut(s))

    img = Image.open(r'jd.jpg')
    # 图片转数组
    img_array = np.array(img)
    wc = WordCloud(
        # 设置字体，否则出现乱码
        font_path='C:/Windows/Fonts/STXINGKA.TTF',
        # 背景颜色
        background_color='white',
        # 词云形状
        mask=img_array,
    )
    # 准备切好的分词
    wc.generate_from_text(string_s)
    fig = plt.figure(1)
    plt.imshow(wc)
    # 关闭坐标
    plt.axis('off')
    plt.savefig(r'../static/assets/cy-img/wordtree{}-jd.jpg'.format(pid), transparent=True, bbox_inches='tight', pad_inches=0.0)
    plt.show()


def white_to_transparent(png_dir,out_dir):

    img = Image.open(png_dir)
    img = img.convert("RGBA") # 模式转换
    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save(out_dir, "PNG")


if __name__ == '__main__':
    df = pd.read_excel('../jd_crawler/jdcomputer.xlsx')
    for pid in df['id']:
        try:
            getwordcloud(pid)
        except:
            continue
    # getwordcloud(25168769082)


