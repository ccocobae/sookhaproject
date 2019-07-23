import pandas as pd
import xlrd
import openpyxl

dir1 = '/Users/soo/PycharmProjects/sookhaproject/forstudy/July24th/excel_s1.xlsx'

# 기본 읽기 1
df = pd.read_excel(dir1, sheet_name=0)
# print(df.head())  # 상위 5개 항목
# print(df.tail())  # 하위 5개 항목

# 행, 푸터(Footer) 스킵 (하위 10개 항목 제외)
# df = pd.read_excel(dir1, sheet_name=0, skip_footer=10)
# print(df)

# 특정 값 치환
# df = pd.read_excel(dir1, header=0, na_values='...', converters={'2003': lambda w: w if w > 60000 else None})
# print(df)
# print(pd.isnull(df))

df = pd.read_excel(dir1, header=0)
print(df.rename(index=lambda x: x+1))
# print(list(df.index))