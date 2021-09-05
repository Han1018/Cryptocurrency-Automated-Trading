
from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *
from binance_f.model import *
import pandas as pd
import json
import csv
import time

# 印出Kline在下來的資料統整


def print_obj(obj):
    if not obj:
        return -1
    dict_r = {}
    members = [attr for attr in dir(obj) if not callable(
        attr) and not attr.startswith("__")]
    for member_def in members:
        val_str = str(getattr(obj, member_def))
        dict_r[member_def] = val_str
        # print(member_def + ":" + val_str)
    # print(dict_r)
    return dict_r


# Generate API OBject for Download Kline
request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)


# 設定參數
symbol = 'DOGEUSDT'
# 2021年6月20日星期日 09:01:00 GMT+08:00
starttime = 1624150860000
# 2021年6月20日星期日 17:20:00 GMT+08:00
endtime = 1624180800000
min_diff = 60000
times_diff = endtime-starttime
times = 1
# 29940000
starttime = starttime-(times_diff*(times-1))
endtime = starttime+times_diff

# 循環抓去過往資料
for i in range(0, times, 1):
    print(starttime, endtime)
    result_list = []
    r = request_client.get_candlestick_data(
        symbol=symbol, startTime=starttime, endTime=endtime, limit=1, interval=CandlestickInterval.MIN1)
    if((starttime != r[0].openTime) or (endtime != r[-1].openTime)):
        print(i, len(r))
        break
    time.sleep(1)
    for idx, row in enumerate(r):
        tmp = print_obj(row)
        result_list.append(tmp)
    df = pd.DataFrame(result_list)
    if(i == 0):
        print(df)
        df.to_csv('t2.csv')
    else:
        df.to_csv('t2.csv', mode='a', header=False)
    if(len(r) != 500):
        print(i, len(r))
        break
    starttime = endtime+min_diff
    endtime = starttime+times_diff
    print(df.shape, i)

# df.head()
# df.tail()


# dfTMP=df.drop(columns=['json_parse'])
# dfTMP.to_csv('t3.csv')


# PrintMix.print_data(result)
