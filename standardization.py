# -*- coding: utf-8 -*-
# 时间    : 2018/10/18 15:40
# 作者    : xcl

#数据标准化到[0,1]
import pandas as pd

#参数初始化
filename = 'C:\\Users\\Administrator\\Desktop\\PositioningDataAnalysis\\data\\business_circle.xls' #原始数据文件
standardizedfile = 'C:\\Users\\Administrator\\Desktop\\standardized.xls' #标准化后数据保存路径

data = pd.read_excel(filename, index_col = '基站编号') #读取数据

data = (data - data.min())/(data.max() - data.min()) #离差标准化
data = data.reset_index() #重设索引为0、1、2…

data.to_excel(standardizedfile, index = False) #保存结果