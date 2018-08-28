# -*- coding: utf-8 -*-
# ----------------------------------------------
# 指定日付の台番ごとにデータを取得する
# payoutを出力する
# ----------------------------------------------
import datetime
import subprocess
import sys
import time

GET_PLIFE_SLOT_PAYOUT_SCRIPT = "get_plife_slot_payout.py"

def main():
    try:
        for i in range(1, 8):
            target_day = datetime.datetime.today() - datetime.timedelta(i)
            exec_cmd = "python %s %s" % (GET_PLIFE_SLOT_PAYOUT_SCRIPT, target_day.strftime("%Y-%m-%d"));
            print("============ Exec:" + exec_cmd + " ============")
            subprocess.call(exec_cmd)

    except:
        print("エラー")


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
