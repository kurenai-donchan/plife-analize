# -*- coding: utf-8 -*-
# ----------------------------------------------
# スロットの指定台番の日付でデータを取得する
# ----------------------------------------------

import datetime
import os.path
import random
import sys
import time
import lxml.html
import requests

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
        target_lot_no = int(args[1])

    # file open date/yyyy/mmdd.txt
    filepath = '../data/lot/%d.txt' % target_lot_no

    total = 0
    with open(filepath, 'a') as f:
        # 初回ならヘッダー追加
        if not os.path.getsize(filepath):
            # outout header
            f.write("%s,%s,%s,%s,%s\n" % ('lotno', 'date', 'day', 'payout', 'totalRotaion'))

        slots_payout = {}
        # 過去分から取得
        for i in reversed(range(DATE_START, DATE_END + 1)):
            # 今日の日付
            today = datetime.datetime.today()
            target_day = today - datetime.timedelta(days=i)

            slotInfo = getSlotInfo(i, target_lot_no)

            f.write("%s,%s,%s,%s,%s\n" % (target_lot_no, target_day.strftime("%Y-%m-%d"), target_day.strftime("%w"), slotInfo['payout'], slotInfo['totalRotation']))

            # 負荷かけないようにsleepいれる
            sleep_time = random.uniform(0, 2)
            print('sleep:' + str(sleep_time))
            time.sleep(sleep_time)


# ----------------------------------------
# 指定したURLの台番号情報を取得する
# ----------------------------------------
def getSlotInfo(target_day, target_lot_no):
    # 取得元URL設定
    BASE_URL = 'http://api.p-ken.jp/p-arkst/bonusinfo/detailToShrRec?day=%d&lot_no=%d'
    HEADERS = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'}

    target_url = BASE_URL % (int(target_day), int(target_lot_no))

    print('target_lot_no:' + str(target_lot_no) + ' target_day:' + str(target_day))
    print("get url:" + target_url)

    # データ取得
    target_html = requests.get(target_url, headers=HEADERS).text
    root = lxml.html.fromstring(target_html)

    totalRotation = '-'
    payout = '-'

    # payoutの取得
    if root.cssselect('#chart.data tbody td:last-child')[0].text is not None:
        payout = root.cssselect('#chart.data tbody td:last-child ')[0].text

    # 総回転数の取得
    if root.cssselect('.score-large .middle')[0].text is not None:
        totalRotation = root.cssselect('.score-large .middle')[0].text

    # 最終payout保存
    slots_payout = {
        'payout': payout,
        'totalRotation': totalRotation
    }

    return slots_payout


# ----------------------------------------
# main 処理実行
# ----------------------------------------
if __name__ == "__main__":
    main()

sys.exit()
