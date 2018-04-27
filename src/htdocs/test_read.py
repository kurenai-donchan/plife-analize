# -*- coding:utf-8 -*-

import os,sys
import csv
import re

YEAR='2018'

def main(name='This is test by takako'):
    slots_payout_data = readingSlotData()

    # print(slots_payout_data )


def readingSlotData():
    slots_payout_data = {}
    targetdir='../../data/'+YEAR+'/'
    files = os.listdir(targetdir)

    for file in files:
        # 日付抽出(Ymd)
        date = re.search('[0-9]{4}' , file)
        date=YEAR+date.group()

        # file読み込み
        filepath=targetdir+file
        csv_file = open(filepath, "r", encoding="utf-8", errors="", newline="" )
        #リスト形式
        # f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
        #辞書形式
        f = csv.DictReader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)


        rows = list(f)
        totalrows = len(rows)
        print(totalrows)

        for i, row in enumerate(rows):

            if ( i+1 == totalrows):
                 continue

            No = row.get("No")
            Payout = row.get("Payout") if row.get("Payout") is not None else '-'
            Rotation = row.get("Rotation") if row.get("Rotation") is not None else '-'
            Big = row.get("Big") if row.get("Big") is not None else '-'
            Reg = row.get("Reg") if row.get("Reg") is not None else '-'

            slots_payout_data[date][No] = {
                "No": No,
                "Payout": Payout,
                "Rotation": Rotation,
                "Big": Big,
                "Reg": Reg
            }

    return slots_payout_data






# ----------------------------------------
# main 処理実行
# ----------------------------------------
if __name__ == "__main__":
    main()

sys.exit()