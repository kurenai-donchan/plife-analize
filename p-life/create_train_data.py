# -*- coding: utf-8 -*-
# ----------------------------------------------
# 学習させる
# ----------------------------------------------

import pandas as pd
import numpy as np
from sklearn import tree

def main():

    df_sample =\
    res = train_data()
    for row in res:
        print(row[0])
    #print(train_X)
    #print(train_Y)

    ## CSVファイルを取得
    #data = pd.read_csv("data.csv", sep=",")
    ## 説明変数(x1, x2に設定)
    #variables = ['x1', 'x2']



def train_data():


    SLOT_NO_START = 4001
    SLOT_NO_END = 4266

    tmp_filepath = '../data/lot/%d.txt'

    # 過去分から取得

    res = []
    for i in range(SLOT_NO_START, SLOT_NO_END+1):
        line = []
        filepath =  tmp_filepath % i

        data = pd.read_csv(filepath, sep=",")


    return line




if __name__ == "__main__":
    main()
