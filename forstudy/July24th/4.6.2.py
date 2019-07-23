import pandas as pd
import xlrd
import openpyxl

dir1 = '/Users/soo/PycharmProjects/sookhaproject/forstudy/July24th/excel_s1.xlsx'
df = pd.read_excel(dir1, header=0)

# 컬럼 값 수정
# df['State'] = df['State'].str.replace(' ', '-')
# print(df)

df['Avg'] = df[['2003', '2004', '2005']].mean(axis=1).round(2)
# print(df)

df['Sum'] = df[['2003', '2004', '2005']].sum(axis=1).round(2)
print(df)

# 최대값 & 최소값 출력
print(df[['2003', '2004', '2005']].max(axis=0))  # or min(axis=0)
# 2003    82406
# 2004    82879
# 2005    82702
# dtype: int64

# 상세 정보 출력
print(df.describe())

df.to_excel('/Users/soo/PycharmProjects/sookhaproject/forstudy/July24th/result_s1.xlsx')
