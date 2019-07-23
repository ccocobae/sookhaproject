from pandas import Series

series1 = Series([92600, 94800, 75400, 88800, 92300])
# print(series1)
# series -> 1차원, dataframe -> 2차원

# print('count', series1.count())
# print('dercribe', series1.describe())

# 인덱스 접근
# print(series1[2])

series2 = Series([92600, 94800, 75400, 88800, 92300], index=['2019-07-23', '2019-07-24', '2019-07-25', '2019-07-26', '2019-07-27'])
print(series2)

for date in series2.index:
    print('date', date)

for price in series2.values:
    print('price', price)

series_g1 = Series([10, 20, 30], index=['n1', 'n2', 'n3'])
series_g2 = Series([50, 40, 25], index=['n3', 'n2', 'n1'])  # 중요한 점은 index 가 같다는 것

sum = series_g1 + series_g2  # 같은 index 끼리 연산 & 새로운 시리즈 생성
mul = series_g1 * series_g2
cal = (series_g1 * series_g2) * 1.5

print(sum)
print(mul)
print(cal)