import pandas as pd
import os
import sys
import re
import datetime

data_file_path = 'C:\\Users\\김진태\\Jupyter_Folder\\Data\\order20180101to20190430.xlsx'
df = pd.read_excel(data_file_path, Sheet_name='주문 고객 현황')

read_columns = ['주담당채널', '영업채널명', '영업담당자명', '고객명', '사업자/주민', '주문일자', '주문상태',
                '주문현황', '납입구분', '상품명', '단위상품명', '사용자', '공급가', '금액(VAT별도)', '판매유형', '기회시작일']

df2 = df[read_columns]
print('조회 건수 : %d건' % df2.shape[0])
df2['판매유형'].value_counts()
df2.head(3)

# 상품명
product_category = {'ICUBE 클라우드서버', 'ICUBE/IU 클라우드서버', 'ICUBE/GW 클라우드서버', 'IU 클라우드서버', 'IU/GW 클라우드서버', 'GW 클라우드서버', '클라우드서버'}
#product_category = {'GW 클라우드서버', 'ICUBE/GW 클라우드서버', 'IU/GW 클라우드서버'}  # 집합(중복값 불허)
df3 = df2[df2['상품명'].isin(product_category)]
print('조회 건수 : %d건' % df3.shape[0])
print(df3['상품명'].value_counts())
df3.head(3)

#df['단위상품명'].unique()
print(df3.head(3).keys())
unit_product_category = {'클라우드서버(기본)'}  # 집합(중복값 불허)
df4 = df3[df3['단위상품명'].isin(unit_product_category)]
print('조회 건수 : %d건' % df4.shape[0])
df4.head(3)

# 클라우드서버에는 '업셀'이 없음
df4['판매유형'].value_counts()

#df['단위상품명'].unique()
print(df4.head(3).keys())
sale_type_category = {'신규'}  # 집합(중복값 불허)
df5 = df4[df4['판매유형'].isin(sale_type_category)]
print('조회 건수 : %d건' % df5.shape[0])
df5.head(3)

# group by
# 상품명이 ICUBE/GW 복합형일때 단위상품명인 '클라우드서버(기본)'가 도입서버 대수만큼 있어 그룹바이 처리함
groupby_columns_list = ['영업채널명', '영업담당자명', '고객명', '사업자/주민', '주문일자', '상품명', '단위상품명', '사용자', '판매유형', '기회시작일']
grouped = df5.groupby(groupby_columns_list)
"""
for name, group in grouped:
    print(name, end=' : ')
    print(str(len(group)))
    print(group)
    print('-' * 50)
"""

# column rename
df6 = grouped.size().reset_index()
print(df6.columns)
#df6.rename(columns={'NEW_NAME':'OLD_NAME'}, inplace=True)   # 속도 느림
df6.columns = ['CNT' if x == 0 else x for x in df6.columns]    # 속도 빠름
print(df6.columns)

# sort
df6.sort_values(by=['주문일자', 'CNT'], ascending=[False, True], inplace=True)
print('조회 건수 : %d건' % df6.shape[0])
df6.head(3)

# IT코디센터는 C로 대리점은 B로 새로운칼럼에 추가한다
channel_series = df6.apply(lambda v: 'C' if ((v[0].endswith('IT코디센터'))|(v[0]=='강원지점')|(v[0]=='제주지점')) else 'B', axis=1)   #
#df6['CB'] = channel_series
df6.loc[:, 'C_B'] = channel_series
print(df6['C_B'].value_counts())
df6.head(3)

# 년도-월까지 잘라서 YM 칼럼에 저장한다
df6.loc[:,'YM'] = df6['주문일자'].str[0:7]
print('조회 건수 : %d건' % df6.shape[0])
df6.head(3)

for i, v in df6['상품명'].items():
    #print(i, v)
    df6.loc[i, 'ICUBE'] = 1 if 'ICUBE' in v else 0
    df6.loc[i, 'IU'] = 1 if 'IU' in v else 0
    df6.loc[i, 'GW'] = 1 if 'GW' in v else 0

p_cnt = df6['상품명'].value_counts()
print(p_cnt)
ICUBE_CNT = p_cnt['ICUBE 클라우드서버'] + p_cnt['ICUBE/IU 클라우드서버'] + p_cnt['ICUBE/GW 클라우드서버']
IU_CNT = p_cnt['IU 클라우드서버'] + p_cnt['ICUBE/IU 클라우드서버'] + p_cnt['IU/GW 클라우드서버']
GW_CNT = p_cnt['GW 클라우드서버'] + p_cnt['ICUBE/GW 클라우드서버'] + p_cnt['IU/GW 클라우드서버']
print('ICUBE = {0}, IU = {1}, GW = {2}'.format(ICUBE_CNT, IU_CNT, GW_CNT))
df6.head(3)

# 전체 클라우드서버 월별 수주 건수 확인
s1 = df6['YM'].value_counts().sort_index(ascending=True)
print(s1)

# 제품별 클라우드서버 월별 수주 건수 확인
s1 = df6[df6['ICUBE']==1]['YM'].value_counts().sort_index(ascending=True)
s2 = df6[df6['IU']==1]['YM'].value_counts().sort_index(ascending=True)
s3 = df6[df6['GW']==1]['YM'].value_counts().sort_index(ascending=True)
df_product = pd.DataFrame({'ICUBE':s1, 'IU':s2, 'GW':s3})
print(df_product)

#s1.keys()
#s1.values
df_temp = df6[df6['YM']=='2018-01'] #2018-08
print('조회 건수 : %d건' % df_temp.shape[0])
df_temp.head(3)

# 선택한 월에 발주한 영업채널 별 건수 조회
df7 = df6[(df6['YM']=='2019-01') & (df6['GW']==1)] #2018-08
print('조회 건수 : %d건' % df7.shape[0])
df7['영업채널명'].value_counts().sort_values(ascending=False).head(100)

df_temp = pd.DataFrame({'주문일자':[], 'ICUBE':[], 'IU':[], 'GW':[]})

#df_temp['주문일자'].append('2019-01-01')
#print(df_temp)

for label, content in df7.items():  #df6.iteritems():
    #print(label)
    #print(content)
    if label == '주문일자':
        for v in content:
            print(label, ' : ' , v)
    elif label == 'ICUBE':
        for v in content:
            print(label, ' : ' , v)
            #df_temp['ICUBE'].append()
    elif label == 'IU':
        for v in content:
            print(label, ' : ' , v)
    elif label == 'GW':
        for v in content:
            print(label, ' : ' , v)

# 영업채널별 전체 발주 건수
df6['영업채널명'].value_counts().sort_values(ascending=False)
df6.head(3)

# 인덱스를 YM(년월)으로 바꾼다
df8 = df6.copy()
#df8.set_index('YM')['2018-06':'2018-06']
df8.set_index('YM', inplace=True)
df8.sort_index(ascending=True, inplace=True)
print('조회 건수 : %d건' % df8.shape[0])
df8.head(3)


# 인덱스로 시작:종료 구간을 지정하여 조회한다
print(df4.index.unique())
#df4['2018-06':'2018-06']
df4['2018-01':'2018-02'][{'영업채널명', '고객명', '주문일자', '상품명'}].head(3)

df4.sort_values(by=['주문일자', '고객명'], ascending=True).head(3)
