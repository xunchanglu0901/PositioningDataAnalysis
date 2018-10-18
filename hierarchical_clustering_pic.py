# -*- coding: utf-8 -*-
# 时间    : 2018/10/18 15:47
# 作者    : xcl

#谱系聚类图
import pandas as pd

#参数初始化
standardizedfile = 'C:\\Users\\Administrator\\Desktop\\PositioningDataAnalysis\\data\\standardized.xls' #标准化后的数据文件
data = pd.read_excel(standardizedfile, index_col = '基站编号') #读取数据

import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage,dendrogram
#这里使用scipy的层次聚类函数，即系统聚类

Z = linkage(data, method = 'ward', metric = 'euclidean') #谱系聚类图
P = dendrogram(Z, 0) #画谱系聚类图
plt.show()