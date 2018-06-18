# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 19:45:32 2018

@author: M.Kurashina
"""
#https://app.box.com/s/kudx94dbbud3bx6wqky4teaj8lyhxxrk



#ライブラリの読み込み
import pandas as pd

# データのロード
#data = pd.read_csv('hfda_ch04_home_page1.csv', index_col=0)
#print ('')
#print ('◆全レコード出力')
#print (data)

##統計量の出力
#print ('')
#print ('◆統計量[平均]の出力（1項目ずつ）')
#print ('mean_of_income:' ,data['Income'].mean())
#print ('mean_of_SiteStayTime:' ,data['SiteStayTime'].mean())
#print ('mean_of_PV:' ,data['PV'].mean())
#print ('mean_of_Num_Revisit:' ,data['Num_Revisit'].mean())

##全ての統計量を出力
#print ('')
#print ('◆主な統計量の自動出力')
#print (data.describe(include='all'))

##全項目で散布図
#print ('')
#print ('◆全項目で散布図(Pandas ScatterMatrix)')
#from pandas.tools.plotting import scatter_matrix
#scatter_matrix(data, diagonal='kde', color='Green', alpha=1)
#
# データのロード
data = pd.read_csv('hfda_ch04_home_page1.csv', index_col=0)
#全項目で散布図（イケてる版）
print ('')
print ('◆全項目で散布図(Seaborn Pairplot)')
import seaborn as sns #“グラフ描画，ビジュアライゼーション用パッケージ
sns.pairplot(data) ##全ての変数同士の散布図がみられる, "hue="オプションでカテゴリ別に色分け可能