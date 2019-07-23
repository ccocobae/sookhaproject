import pandas as pd
import pandas_datareader.data as wb
import datetime


# 조회 시작 날짜
start = datetime.datetime(2019, 3, 1)
end = datetime.datetime(2019, 7, 1)

# Google 정보 호출
GS = wb.DataReader('KRX: 035720', 'google', start, end)
print(GS)