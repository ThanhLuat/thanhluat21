import pandas as pd
import numpy as np
import math

df = pd.read_excel("C:/Users/VICTUS/Downloads/Dataset-Temperature-by-years (1).xls")
print(df,'\n')

## Lấy ra n dòng đầu của dữ liệu
dau = df.head(5)
print('5 dòng đầu của dataset: \n',dau,'\n')

## Lấy ra n dòng cuối của dữ liệu
cuoi = df.tail(5)
print('5 dòng cuối của dataset: \n',cuoi,'\n')

## Trả về một cột của DataFrame
cot = df['CHLFa']
print('Cột dữ liệu CHLFa: \n',cot,'\n')

## Trả về hai cột của DataFrame
cott = df[['CHLFa','Temperature']]
print('Cột dữ liệu CHLFa và Temperature: \n',cott,'\n')

## Lấy dữ liệu của cột thứ 4 ##
col3 = df.iloc[:,3]
print('Dữ liệu của cột thứ 4: \n',col3,'\n')

## Lấy dữ liệu của hàng thứ 4 ##
colh = df.loc[4]
print('Dữ liệu của hàng thứ 4: \n',colh,'\n')

## Lấy giá trị của một ô dữ liệu bất kì ##
pos = df.iloc[4,4]
print('Giá trị của ô ở hàng 5, cột 5: \n',pos,'\n')

## Lấy từ dòng 1 đến dòng 15 cột đầu tiên và cột thứ 4 ##
vnb = df.iloc[1:16,[0,3]]
print('Từ dòng 1 đến dòng 15 với cột đầu tiên và cột thứ 4: \n',vnb,'\n')

## Lọc theo điều kiện
lon = df[ df['Salinity'] > 30 ]
print('Thỏa mãn độ muối > 30: \n',lon,'\n')

row = df.loc[(df['Temperature'] <= 5) &(df['Season'] == 'winter') &(df['CHLFa'] <= 5)]
print('Dữ liệu có Temperature <= 5, mùa đông và CHLFa <= 5: ','\n',row)