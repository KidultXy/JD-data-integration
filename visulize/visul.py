import matplotlib.pyplot as plt
import pandas as pd


path = r'../jd_crawler/jdcomputer.xlsx'
plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False


def boxplot_price():
    df = pd.read_excel(path)
    df['品牌'].replace('戴尔（DELL）','戴尔')
    df['品牌'].replace('苹果（Apple）','Apple')
    df['品牌'].replace('联想（Lenovo）','联想')
    df = df[(df['品牌'] == 'ThinkPad')|(df['品牌'] == '联想')| (df['品牌'] == '戴尔')| (df['品牌'] == '惠普（HP）')| (df['品牌'] == '荣耀（HONOR）')| (df['品牌'] == 'Apple')]
    print(df)
    # price_hw = df[(df['品牌'] == '华为（HUAWEI）')|(df['品牌'] == '华为')]['price']
    # price_apple = df[(df['品牌'] == '苹果（Apple）')|(df['品牌'] == 'Apple')]['price']
    # price_lenovo = df[(df['品牌'] == '联想（Lenovo）') | (df['品牌'] == '联想')]['price']
    # print(price_apple,price_hw,price_lenovo)
    # plt.boxplot([price_apple,price_hw,price_lenovo])
    # plt.show()
    df.boxplot(column='price', by='品牌',showfliers=False)
    # plt.title('不同品牌价格箱型图')
    plt.grid(axis='both')
    plt.grid(axis='y',linestyle='-.')
    plt.savefig('boxplot.png', transparent=True)
    plt.show()


def bubble():
    # 纵轴代表价格，横轴代表编号（1-300），气泡大小代表内存大小，根据品牌分类
    df_merge = pd.read_excel(path)
    df_merge['品牌'].replace('戴尔（DELL）', '戴尔')
    df_merge['品牌'].replace('苹果（Apple）', 'Apple')
    df_merge['品牌'].replace('联想（Lenovo）', '联想')
    df_merge = df_merge[(df_merge['品牌'] == 'ThinkPad') | (df_merge['品牌'] == '联想') | (df_merge['品牌'] == '戴尔')| (df_merge['品牌'] == '惠普（HP）')| (df_merge['品牌'] == '荣耀（HONOR）')| (df_merge['品牌'] == 'Apple')]
    df_merge['内存容量'] = df_merge['内存容量'].str.extract(r'(\d+)GB').astype(int)
    categories = df_merge['品牌'].unique()
    for i, category in enumerate(categories):
        plt.scatter(x= df_merge[df_merge['品牌'] == category]['编号']
                    , y=df_merge[df_merge['品牌'] == category]['price']
                    , s=df_merge[df_merge['品牌'] == category]['内存容量'] * 20  # 需要对比的属性
                    # , c=color_2(i) # 点的颜色
                    # , edgecolors=np.array(color_2(i)).reshape(1, -1)  # 点的边缘颜色
                    , label=str(category)  # 标签
                    , alpha=0.7  # 透明度
                    , linewidths=.5)  # 点的边缘线的宽度
    plt.legend()
    plt.ylabel('价格')
    plt.xlabel('产品编号')
    plt.title('不同品牌电脑价格与内存气泡图')
    plt.savefig("bubble.png", transparent=True)
    plt.show()
    pass


if __name__ == '__main__':
    bubble()