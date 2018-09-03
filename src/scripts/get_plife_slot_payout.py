# -*- coding: utf-8 -*-
# ----------------------------------------------
# 指定日付の台番ごとにデータを取得する
# payoutを出力する
# ----------------------------------------------

import datetime
import json
import os
import random
import sys
import time
from collections import OrderedDict

import lxml.html
import requests

# 対象の大番号の範囲
# SLOT NO 4001 - 4266
SLOT_NO_START = 4001
SLOT_NO_END = 4266

# Sleep timeの秒数(この秒数以内でらんだむ時間)
SLEEP_TIME_SECOND = 1

# 取得先URL
BASE_URL = 'http://api.p-ken.jp/p-arkst/bonusinfo/detailToShrRec?day=%d&lot_no=%d'
# SmartPhoneでの取得しかできない
HEADERS = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'}


def main():
    args = sys.argv
    if len(args) == 1:
        # デフォルトの対象日付(昨日)
        target_day = datetime.datetime.today() - datetime.timedelta(1)
    else:
        # 指定されていればそれを利用 YYYY-mm-ddの形式
        target_day = datetime.datetime.strptime(args[1], "%Y-%m-%d")

    print(target_day.strftime("%Y-%m-%d %H:%M:%S"))

    # data 取得
    slots_payout = geSlotData(target_day)

    # File 出力
    output(target_day, slots_payout)

    # END


# slot payoutデータ取得
# 取得対象の日付
def geSlotData(target_day):
    # 日本語の曜日一覧
    day_of_week_list = ["月", "火", "水", "木", "金", "土", "日"]

    # 今日のから何日前か？の算出
    today = datetime.datetime.today()
    before_day = (today - target_day).days

    # data 取得
    win_information = OrderedDict() # 大当たり情報
    total_payout = 0 # 店舗総ペイアウト
    total_rotation = 0 # 店舗総回転数
    for i in range(SLOT_NO_START, SLOT_NO_END + 1):
        if i not in win_information:
            # 初期化
            win_information[i] = OrderedDict()

        # 対象のURL算出
        target_url = BASE_URL % (before_day, i)
        print("get url:" + target_url)
        target_html = requests.get(target_url, headers=HEADERS).text
        root = lxml.html.fromstring(target_html)

        # 機種名取得
        lot_name = ""
        if root.cssselect('#model_nm')[0].text is not None:
            lot_name = root.cssselect('#model_nm')[0].text

        # payoutの取得
        payout = ""
        if root.cssselect('#chart.data tbody td:last-child')[0].text is not None:
            payout = root.cssselect('#chart.data tbody td:last-child ')[0].text

        # 総回転数の取得
        rotation = ""
        if root.cssselect('.score-large .middle')[0].text is not None:
            rotation = root.cssselect('.score-large .middle')[0].text

        # ボーナス回数
        bonus = ""
        if root.cssselect('.score-large .large')[0].text is not None:
            bonus = root.cssselect('.score-large .large')[0].text

        # BB回数の取得
        big = ""
        if root.cssselect('.score-large .big')[0].text is not None:
            big = root.cssselect('.score-large .big')[0].text

        # RB回数の取得
        reg = ""
        if root.cssselect('.score-large .reg')[0].text is not None:
            reg = root.cssselect('.score-large .reg')[0].text

        # BB確率の取得
        big_probability = ""
        if root.cssselect('.score-middle .middle')[0].text is not None:
            big_probability = root.cssselect('.score-middle .middle')[0].text

        # RB確率の取得
        reg_probability = ""
        if root.cssselect('.score-middle .middle')[1].text is not None:
            reg_probability = root.cssselect('.score-middle .middle')[1].text

        # トータル確率の取得
        total_probability = ""
        if root.cssselect('.score-middle .middle')[2].text is not None:
            total_probability = root.cssselect('.score-middle .middle')[2].text

        # 最終payout保存
        win_information[i] = OrderedDict([
            ("lot_no", i),
            ("lot_name", lot_name),
            ("payout", payout),
            ("rotation", rotation),
            ("bonus", bonus),
            ("big", big),
            ("reg", reg),
            ("big_probability", big_probability),
            ("reg_probability", reg_probability),
            ("total_probability", total_probability),
            ("date", target_day.strftime("%Y-%m-%d")),
            ("day_of_week", day_of_week_list[target_day.weekday()])
        ]);

        # LOG
        print("No:" + str(i) + ",lotName:" + lot_name + ",Payout:" + payout + ',Rotation:' + rotation, ",BB:" + big + ",RB:" + reg)

        # 店舗の全体の差枚数を求める
        if payout[0] == '-' and payout[1:].isdigit() or payout.isdigit():
            total_payout = total_payout + int(payout)

        # 店舗総回転数を出す(稼働率)
        if (rotation.isdigit()):
            total_rotation = total_rotation + int(rotation)

        # 負荷かけないようにsleepいれる
        sleep_time = random.uniform(0, SLEEP_TIME_SECOND)
        time.sleep(sleep_time)

    result = {
        "total_payout": total_payout,
        "total_rotation": total_rotation,
        "win_information": win_information
    }

    return result


# fileに出力
def output(target_day, slots_payout):
    # file open date/yyyy/mm/mmdd_w.json
    dir_path = '../../data/' + target_day.strftime("%Y/%m")
    file_name = target_day.strftime("%m%d_%w.json")
    file_path = dir_path + '/' + file_name

    # dir生成
    os.makedirs(dir_path, 777, True)

    # JSON出力
    f = open(file_path, 'w', encoding='utf-8')
    json.dump(slots_payout, f, ensure_ascii=False, indent=4, sort_keys=None, separators=(',', ': '))
    f.close()


# ----------------------------------------
# main 処理実行
# ----------------------------------------
if __name__ == "__main__":
    # 実行時間計測
    start = time.time()

    main()

    # 実行時間出力
    elapsed_time = round(time.time() - start, 2)
    print("elapsed_time:{0}".format(elapsed_time) + "[sec]")

sys.exit()
