from pandas import Series, DataFrame

r_data = {'City': ['서울', '대구', '부산', '대전'], 'Total1': [55000, 49000, 52000, 50000], 'Total2': [67000, 43000, 56000, 45000]}
# print(type(r_data))  # <class 'dict'>
i_data = ['one', 'two', 'three', 'four']

d_frame = DataFrame(r_data, index=i_data)
# print(type(d_frame))  # <class 'pandas.core.frame.DataFrame'>
# print(d_frame)
print(d_frame['City'])  # Columns

print(d_frame.ix['one'])  # index로 가져오고 싶을 때, type : series

# 값 순회
for e in d_frame.values:
    for i, z in enumerate(e):
        print(i, z)
