########## GEMINI 行情接口 ##########
## https://api.gemini.com/v1/pubticker/:symbol

# import json
# import requests
#
# gemini_ticker = 'https://api.gemini.com/v1/pubticker/{}'
# symbol = 'btcusd'
# btc_data = requests.get(gemini_ticker.format(symbol)).json()
# print(json.dumps(btc_data, indent=4))

########## 输出 ##########
#
# {
#    "bid": "8825.88",
#    "ask": "8827.52",
#    "volume": {
#        "BTC": "910.0838782726",
#        "USD": "7972904.560901317851",
#        "timestamp": 1560643800000
#    },
#    "last": "8838.45"
# }


import matplotlib.pyplot as plt
import pandas as pd
import requests

# 选择要获取的数据时间段
periods = '3600'

# 通过 Http 抓取 btc 历史价格数据
resp = requests.get('https://api.cryptowat.ch/markets/gemini/btcusd/ohlc',
  params={
    'periods': periods
  })
data = resp.json()

# 转换成 pandas data frame
df = pd.DataFrame(
  data['result'][periods],
  columns=[
    'CloseTime',
    'OpenPrice',
    'HighPrice',
    'LowPrice',
    'ClosePrice',
    'Volume',
    'NA'])

# 输出 DataFrame 的头部几行
print(df.head())

# 绘制 btc 价格曲线
df['ClosePrice'].plot(figsize=(14, 7))
plt.show()


# ########### 输出 ###############
# CloseTime  OpenPrice  HighPrice  ...  ClosePrice     Volume             NA
# 0  1558843200    8030.55    8046.30  ...     8011.20  11.642968   93432.459964
# 1  1558846800    8002.76    8050.33  ...     8034.48   8.575682   68870.145895
# 2  1558850400    8031.61    8036.14  ...     8000.00  15.659680  125384.519063
# 3  1558854000    8000.00    8016.29  ...     8001.46  38.171420  304342.048892
# 4  1558857600    8002.69    8023.11  ...     8009.24   3.582830   28716.385009
