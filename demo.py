import finnhub
import pandas as pd
from pandas import json_normalize
import time
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from datetime import datetime


#Import data
import requests
import json
r = requests.get('https://finnhub.io/api/v1/stock/candle?symbol=QQQ&resolution=1&from=1572651390&to=1572910590&token=bq1qmlfrh5rd509cok5g')
data = pd.DataFrame(r.json())
open = data.o
times = data.t

# get open candle prices
openCandleList = []
for value in open:
    openCandleList.append(value)

# get date values

datetimeList = []
for value in times:
    temp = time.strftime('%Y/m/%d %H:%M:%S', time.localtime(value))
    datetimeList.append(datetime.strptime(temp,'%Y/m/%d %H:%M:%S'))



# they already have a resistance
# print(finnhub_client.support_resistance('AAPL', 'D'))

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
plt.gca().xaxis.set_major_locator(mdates.MinuteLocator(interval = 30))
plt.plot(datetimeList, openCandleList)
plt.gcf().autofmt_xdate()

plt.show()
