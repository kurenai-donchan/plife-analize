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

def getSlotFileList(YEAR='2018'):
    slots_payout_data = {}
    target_dir = '../../data/' + YEAR + '/'

    # 読み込み
    files = os.listdir(target_dir)
    files.reverse()

    slotFiles = []
    # directory loop
    for name in files:
        # directory loop2
        if os.path.isdir(target_dir+name):
            dir2 = os.listdir(target_dir+name)
            dir2.reverse()
            for name2 in dir2:
                slotFiles.append(target_dir+name+'/'+name2)

    return slotFiles



def readingSlotData(YEAR='2018'):
    # 初期化
    slots_payout_data = {}
    payout = {}

    # 逆順
    files = getSlotFileList(YEAR)

    for filepath in files:

        # print(file)
        # # 日付抽出(Ymd)
        date = re.search('([0-9]{4})_', filepath)
        date = YEAR + date.group(1)

        #
        # # file読み込み
        # filepath = target_dir + file
        csv_file = open(filepath, "r", encoding="utf-8", errors="", newline="")
        # リスト形式
        # f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
        # 辞書形式
        f = csv.DictReader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

        rows = list(f)
        totalrows = len(rows)

        slots_payout_data[date] = {}
        payout[date] = {}
        for i, row in enumerate(rows):

            if (i + 1 == totalrows):
                payout[date] = row
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
        csv_file.close()

    return [slots_payout_data, payout]

