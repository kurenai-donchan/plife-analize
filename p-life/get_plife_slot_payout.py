# -*- coding: utf-8 -*-
import sys
import lxml.html
import requests
import time
import datetime
import codecs
import sys
import random

# SLOT NO
SLOT_NO_START = 4001
SLOT_NO_END = 4266

# 前日
BASE_URL = 'http://api.p-ken.jp/p-arkst/bonusinfo/detailToShrRec?day=%d&lot_no=%d'
HEADERS = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'}

#今日の日付
today = datetime.datetime.today()

target_day = None
args = sys.argv
if len(args) == 1:
    # デフォルトの対象日付(昨日)
    target_day = datetime.datetime.today() -datetime.timedelta(1)
else:
    # 指定されていればそれを利用 YYYY-mm-ddの形式
    target_day = datetime.datetime.strptime(args[1], "%Y-%m-%d")

print(target_day.strftime("%Y-%m-%d %H:%M:%S"))


# 何日前か？の算出
target_days = (today - target_day).days


# data 取得
slots_payout = {}
for i in range(SLOT_NO_START, SLOT_NO_END+1):
    if i not in slots_payout:
        slots_payout[i] = []

    target_url = BASE_URL % (target_days, i)
    print(target_url)
    target_html = requests.get(target_url, headers=HEADERS).text
    root = lxml.html.fromstring(target_html)
    if root.cssselect('#chart.data tbody td:last-child ')[0].text is not None:
        payout = root.cssselect('#chart.data tbody td:last-child ')[0].text
    else:
        continue

    # 最終payout保存
    slots_payout[i] = payout

    # 負荷かけないようにsleepいれる
    sleep_time = random.uniform(0,1)
    print('sleep:'+str(sleep_time))
    #time.sleep(sleep_time)
    time.sleep(sleep_time)

# file open date/yyyy/mmdd.txt
filepath = '../data/'+target_day.strftime("%Y/%m%d.txt")

total = 0
f = open(filepath , 'w')
for k, v in slots_payout.items():
    f.write("%d,%s\n" % (k, v));
    # 店舗の全体の差枚数を求める
    total = total + int(v)

f.write("%s,%s\n" % ('total', total));
f.close()

sys.exit()
