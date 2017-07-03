# -*- coding: utf-8 -*-
# ----------------------------------------------
# 学習させる
# ----------------------------------------------

import pandas as pd
import numpy as np
import time
import sys
from sklearn import tree

def main():

    train_X = []
    train_Y = []

    SLOT_NO_START = 4001
    #SLOT_NO_END = 4266
    SLOT_NO_END = 4266

    output_file_path = '../data/sum/traning_data.csv'
    tmp_input_filepath = '../data/lot2/%d.txt'

    # 学習結果を出力
    with open(output_file_path, 'w') as f:
        f.write("x1,x2,x3,x4,x5,x6,x7\n" )

        # 過去分から取得
        for i in range(SLOT_NO_START, SLOT_NO_END+1):
            filepath =  tmp_input_filepath % i

            data = pd.read_csv(filepath, sep=",")

            line = []
            for i in data['payout']:
                line.append(str(createTraningData(i)))


            f.write(','.join(line)+"\n")


def createTraningData(payout):
    # `payouをまとめる
    tmp_i = int(round(payout / 1000))
    if (tmp_i > 5):
        # 5000枚以上は5で統一
        tmp_i = 5
    if (tmp_i < 0 and tmp_i > -2):
        # -0 -2 以内は-1で統一
        tmp_i = -1
    if (tmp_i <= -2):
        # -2 以下は-2で統一
        tmp_i = -2

    return tmp_i

### ------------------
### main
### ------------------

# 実行時間計測
start = time.time()

if __name__ == "__main__":
    main()

# 実行時間出力
elapsed_time = round(time.time() - start, 2)
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")