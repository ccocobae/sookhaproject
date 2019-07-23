import pandas as pd

dir2 = '/Users/soo/PycharmProjects/sookhaproject/forstudy/July24th/csv_s2.csv'

df2 = pd.read_csv(dir2, sep=';', skiprows=[0], header=None, names=['Name', "Test1", "Test2", "Test3", "Final", "Grade"])  # 구분자를 ;로 지정
# print(df)

# 원하는 열만 key 값으로 가져올 수 있음
df2['Grade'] = df2['Grade'].str.replace('C', 'A')  # 컬럼의 내용을 쉽게 변경 가능
# print(df2)

# 평균 컬럼 추가
df2['Avg'] = df2[['Test1', 'Test2', 'Test3', 'Final']].mean(axis=1)  # 0이면 세로로 합계, 1이면 가로로 합계
print(df2)

# df2['Sum'] = df2[['Test1', 'Test2', 'Test3', 'Final']].sum(axis=1)
# print(df2)

df2.to_csv('/Users/soo/PycharmProjects/sookhaproject/forstudy/July24th/result_s2.csv', index=False)