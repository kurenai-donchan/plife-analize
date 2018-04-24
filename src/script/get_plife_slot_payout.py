# -*- coding: utf-8 -*-
# ----------------------------------------------
# 指定日付の台番ごとにデータを取得する
# payoutを出力する
# ----------------------------------------------

import sys
import lxml.html
import requests
import time
import datetime
import codecs
import sys
import random

# 対象の大番号の範囲
# SLOT NO 4001 - 4266
SLOT_NO_START = 4001
SLOT_NO_END = 4266

# 取得先URL
BASE_URL = 'http://api.p-ken.jp/p-arkst/bonusinfo/detailToShrRec?day=%d&lot_no=%d'
# SmartPhoneでの取得しかできない
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

# 実行時間計測
start = time.time()

# data 取得
slots_payout = {}
for i in range(SLOT_NO_START, SLOT_NO_END+1):
    if i not in slots_payout:
        slots_payout[i] = []

    target_url = BASE_URL % (target_days, i)

    print("get url:"+target_url)
    target_html = requests.get(target_url, headers=HEADERS).text
    root = lxml.html.fromstring(target_html)

    # payoutの取得
    payout = ""
    if root.cssselect('#chart.data tbody td:last-child')[0].text is not None:
        payout = root.cssselect('#chart.data tbody td:last-child ')[0].text

    # 総回転数の取得
    rotation = ""
    if root.cssselect('.score-large .middle')[0].text is not None:
        rotation = root.cssselect('.score-large .middle')[0].text

    # BBの取得
    big = ""
    if root.cssselect('.score-large .big')[0].text is not None:
        big = root.cssselect('.score-large .big')[0].text

    reg = ""
    if root.cssselect('.score-large .reg')[0].text is not None:
        reg = root.cssselect('.score-large .reg')[0].text

    print("No:" + str(i) +  ",Payout:"+payout+',Rotation:'+rotation,",BB:"+big+",RB:"+reg)

    # 最終payout保存
    slots_payout[i] = {
        'payout' : payout,
        'rotation':rotation,
        'big':big,
        'reg':reg
    }

    # 負荷かけないようにsleepいれる
    sleep_time = random.uniform(0,1)
    # print('sleep:'+str(sleep_time))
    time.sleep(sleep_time)


# file open date/yyyy/mmdd.txt
filepath = '../../data/'+target_day.strftime("%Y/%m%d_%w.txt")

totalPayout = 0
totalRotation = 0
f = open(filepath , 'w')

# outout header
f.write("%s,%s,%s,%s,%s\n" % ('No', 'Payout', 'Rotation', 'Big', 'Reg'))

# output contents
for k, v in slots_payout.items():
    # 一行出力
    f.write("%d,%s,%s,%s,%s\n" % (k, str(v['payout']), str(v['rotation']), str(v['big']), str(v['reg'])))

    # 店舗の全体の差枚数を求める
    if v['payout'][0]=='-' and v['payout'][1:].isdigit() or v['payout'].isdigit():
        totalPayout = totalPayout + int(v['payout'])

    # 店舗総回転数を出す(稼働率)
    if (v['rotation'].isdigit()) :
        totalRotation = totalRotation + int(v['rotation'])

print(totalPayout)
f.write("%s,%s,%s,-,-\n" % ('total', str(totalPayout), str(totalRotation)))

f.close()


# 実行時間出力
elapsed_time = round(time.time() - start, 2)
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

sys.exit()