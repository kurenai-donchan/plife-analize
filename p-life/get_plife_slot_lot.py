# -*- coding: utf-8 -*-
# ----------------------------------------------
# スロットの指定台番の日付でデータを取得する
# ----------------------------------------------

import sys
import lxml.html
import requests
import time
import datetime
import codecs
import sys
import random

def main():

    # 何日前から何日分取得するか
    DATE_START = 1
    DATE_END = 7
    # SLOT_NO_END = 4001

    # 台番号設定
    target_lot_no = None
    args = sys.argv
    if len(args) == 1:
        # デフォルトの対象台番号(ひとつめ）
        target_lot_no = 4001
    else:
        # 指定されていればそれを利用 YYYY-mm-ddの形式
        target_lot_no = args[1]

    # file open date/yyyy/mmdd.txt
    filepath = '../data/lot/%d.txt' % target_lot_no

    total = 0
    f = open(filepath , 'a')

    # outout header
    #f.write("%s,%s,%s,%s,%s\n" % ('lotno', 'date','day','payout', 'totalRotaion'))

    slots_payout = {}
    # 過去分から取得
    for i in reversed(range(DATE_START, DATE_END+1)):

        #今日の日付
        today = datetime.datetime.today()
        target_day = today - datetime.timedelta(days=i)

        slotInfo = getSlotInfo(i, target_lot_no)

        f.write("%s,%s,%s,%s,%s\n" % (target_lot_no, target_day.strftime("%Y-%m-%d"),target_day.strftime("%w"),slotInfo['payout'], slotInfo['totalRotation']))

        # 負荷かけないようにsleepいれる
        #sleep_time = random.uniform(0,1)
        #print('sleep:'+str(sleep_time))
        #time.sleep(sleep_time)
        #time.sleep(sleep_time)

    # 閉じる
    f.close()


# ----------------------------------------
# 指定したURLの台番号情報を取得する
# ----------------------------------------
def getSlotInfo(target_day, target_lot_no):

    # 取得元URL設定
    BASE_URL = 'http://api.p-ken.jp/p-arkst/bonusinfo/detailToShrRec?day=%d&lot_no=%d'
    HEADERS = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'}

    target_url = BASE_URL % (int(target_day), int(target_lot_no))

    print('target_lot_no:'+str(target_lot_no) + ' target_day:'+str(target_day))
    print("get url:"+target_url)

    # データ取得
    target_html = requests.get(target_url, headers=HEADERS).text
    root = lxml.html.fromstring(target_html)

    totalRotation = '-'
    payout        = '-'

    # payoutの取得
    if root.cssselect('#chart.data tbody td:last-child')[0].text is not None:
        payout = root.cssselect('#chart.data tbody td:last-child ')[0].text

    # 総回転数の取得
    if root.cssselect('.score-large .middle')[0].text is not None:
        totalRotation = root.cssselect('.score-large .middle')[0].text

    # 最終payout保存
    slots_payout = {
        'payout' : payout,
        'totalRotation':totalRotation
    }

    return slots_payout



# ----------------------------------------
# main 処理実行
# ----------------------------------------
if __name__ == "__main__":
    main()





sys.exit()




































# SLOT NO
DATE_NO_START = -1
SLOT_NO_END   = -90
#SLOT_NO_END = 4001

# 前日
BASE_URL = 'http://api.p-ken.jp/p-arkst/bonusinfo/detailToShrRec?day=%d&lot_no=%d'
HEADERS = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'}

target_lot_no = None
args = sys.argv
if len(args) == 1:
    # デフォルトの対象台番号(ひとつめ）
    target_lot_no = 4001
else:
    # 指定されていればそれを利用 YYYY-mm-ddの形式
    target_lot_no = args[1]

print(target_lot_no)
sys.exit()


#今日の日付
today = datetime.datetime.today()

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
    if root.cssselect('#chart.data tbody td:last-child')[0].text is not None:
        payout = root.cssselect('#chart.data tbody td:last-child ')[0].text
    else:
        continue

    # 総回転数の取得
    if root.cssselect('.score-large .middle')[0].text is not None:
        totalRotation = root.cssselect('.score-large .middle')[0].text
    else:
        continue
    print("payout:"+payout)
    print(root.cssselect('.score-large .middle')[0].text)
    # 総回転数
    #print(root.cssselect('#chart..score-large .middle')[0].text)

#     if root.cssselect('#chart..score-large .middle lump')[5].text is not None:
#         totalcount = root.cssselect('#chart.data tbody td:last-child ')[0].text
#     else:
#         continue

#     payout('total count:'+totalcount)


    # 最終payout保存
    slots_payout[i] = {
        'payout' : payout,
        'totalRotation':totalRotation
    }

    # 負荷かけないようにsleepいれる
    sleep_time = random.uniform(0,1)
    print('sleep:'+str(sleep_time))
    #time.sleep(sleep_time)
    time.sleep(sleep_time)

# file open date/yyyy/mmdd.txt
filepath = '../data/'+target_day.strftime("%Y/%m%d.txt")

total = 0
f = open(filepath , 'w')

# outout header
f.write("%s,%s,%s\n" % ('lotno', 'payout', 'totalRotaion'))

# output contents
for k, v in slots_payout.items():
    f.write("%d,%s,%s\n" % (k, str(v['payout']), str(v['totalRotation'])))
    # 店舗の全体の差枚数を求める
    total = total + int(v['totalRotation'])

f.write("%s,%s\n" % ('total', total))
f.close()


# 実行時間出力
elapsed_time = round(time.time() - start, 2)
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

sys.exit()
