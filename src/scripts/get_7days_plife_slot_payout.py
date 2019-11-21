# coding:utf-8
# ----------------------------------------------
# 指定日付の台番ごとにデータを取得する
# payoutを出力する
# ----------------------------------------------
import argparse
import datetime
import subprocess
import sys
import time
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8') # UTF-8に
sys.stdout.flush()

GET_PLIFE_SLOT_PAYOUT_SCRIPT = "get_plife_slot_payout.py"

DEFAULT_DAY = 7


def get_args():
    # 準備
    parser = argparse.ArgumentParser()

    # # 標準入力以外の場合
    # if sys.stdin.isatty():
    #     parser.add_argument("file", help="please set me", type=str)

    parser.add_argument("--day")
    parser.add_argument("--test", action="store_false")

    # 結果を受ける
    args = parser.parse_args()

    return args


def main():
    try:
        args = get_args()

        day = DEFAULT_DAY
        if args.day:
            day = int(args.day)

        exec_cmds = []
        for i in reversed(range(1, day + 1)):
            target_day = datetime.datetime.today() - datetime.timedelta(i)
            exec_cmd = "python %s %s" % (GET_PLIFE_SLOT_PAYOUT_SCRIPT, target_day.strftime("%Y-%m-%d"));
            exec_cmds.append(exec_cmd)
            print("============ CMD: " + exec_cmd + " ============")

        for command in exec_cmds:
            if (args.test):
                print("============ Exec CMD: " + command + " ============")
                subprocess.call(command)
            else:
                print("============ Test CMD: " + command + " ============")

    except:
        print("エラー")


# ----------------------------------------
# main 処理実行
# ----------------------------------------
if __name__ == "__main__":

    try:
        # 実行時間計測

        start_time = time.time()
        main()

        # 実行時間出力
        elapsed_time = round(time.time() - start_time, 2)
        print("elapsed_time:{0}".format(elapsed_time) + "[sec]")

    except Exception as e:
        print(e)

sys.exit()
