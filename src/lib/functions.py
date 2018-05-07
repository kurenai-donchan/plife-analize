# -*- coding: utf-8 -*-
# ----------------------------------------------
# python 関数郡
# ----------------------------------------------

import csv
import os
import re


def touch(path):
    with open(path, 'a'):
        os.utime(path, None)


def readingSlotData(YEAR='2018'):
    slots_payout_data = {}
    target_dir = '../../data/' + YEAR + '/'
    files = os.listdir(target_dir)

    for file in files:
        # 日付抽出(Ymd)
        date = re.search('[0-9]{4}', file)
        date = YEAR + date.group()

        # file読み込み
        filepath = target_dir + file
        csv_file = open(filepath, "r", encoding="utf-8", errors="", newline="")
        # リスト形式
        # f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
        # 辞書形式
        f = csv.DictReader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

        rows = list(f)
        totalrows = len(rows)

        slots_payout_data[date] = {}
        for i, row in enumerate(rows):

            if (i + 1 == totalrows):
                continue

            No = row.get("No")
            lotName = row.get("lotName") if row.get("lotName") is not None else '-'
            Payout = row.get("Payout") if row.get("Payout") is not None else '-'
            Rotation = row.get("Rotation") if row.get("Rotation") is not None else '-'
            Big = row.get("Big") if row.get("Big") is not None else '-'
            Reg = row.get("Reg") if row.get("Reg") is not None else '-'

            slots_payout_data[date].update(
                {No: {"lotName": lotName,
                      "Payout": Payout,
                      "Rotation": Rotation,
                      "Big": Big,
                      "Reg": Reg
                      }}
            )

    return slots_payout_data
