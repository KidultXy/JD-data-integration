# 京东电脑信息采集与集成
2022数据采集与集成课程期末大作业 【2051495 & 2052317】
## 运用技术
1. python
2. Flask框架
3. pandas
4. Beautiful soup
5. htmll+css+js
6. jquery
7. bootstrap框架 
8. echarts+pyecharts

## 文件说明
0. preview-pics 存放我们网站信息速览图

1. jd_crawler 京东数据爬虫

2. static 存放前端可视化所用到的css img js等文件，便于后面flask框架渲染

3. templates flask框架渲染前端界面html文件

    > 1. index 登录页面
    > 2. register 登录页面
    > 3. view 主页
    > 4. search 全部商品展示与搜索
    > 5. details 具体商品信息展示与可视化
    > 6. result 全部商品信息数据看板
    > 7. team 网页基本信息介绍-分工页面（后期希冀改进成用户信息界面）

4. visulize 利用pandas数据处理并对数据可视化

5. wordcloud 词云图绘制

6. app.py flask端口对接主文件 运行本程序通过配置环境后直接运行app.py即可

7. jd.sql 存放数据库结构与部分数据 可直接在本地数据库对其进行source从而导入本地数据库

    > products_details_info/products_basic_info/products_comment_info数据太多，sql文件中并没有再重复记录，批量导入jd_crawler中jd_computer和comment文件夹存储的对应产品评论信息即可。

