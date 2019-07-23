import pandas as pd
import numpy as np

# 랜덤으로 Dataframe 생성
# df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
df = pd.DataFrame(np.random.randn(100, 4), columns=['One', 'Two', 'Three', 'Four'])
# print(df.rename(index=lambda x: x+1))

df.to_excel('/Users/soo/PycharmProjects/sookhaproject/forstudy/July24th/result_s2.xlsx', index=False)