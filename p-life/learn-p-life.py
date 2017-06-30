# -*- coding: utf-8 -*-
# ----------------------------------------------
# 学習させる
# ----------------------------------------------

import pandas as pd
import numpy as np
import sys
from sklearn import tree

def main():


    train_X, train_Y = train_data()
    print(train_X)
    print(train_Y)

    ## CSVファイルを取得
    #data = pd.read_csv("data.csv", sep=",")
    ## 説明変数(x1, x2に設定)
    #variables = ['x1', 'x2']

    # 決定木の分類器を生成
    clf = tree.DecisionTreeClassifier()
    ## 分類器にサンプルデータを入れて学習(目的変数はx）
    clf = clf.fit(train_X, train_Y)
    #
    #
    ## 学習結果を出力
    with open('graph.dot', 'w') as f:
        f = tree.export_graphviz(clf, out_file=f)

def train_data():
    train_X = []
    train_Y = []

    SLOT_NO_START = 4001
    SLOT_NO_END = 4266

    tmp_filepath = '../data/lot/%d.txt'

    # 過去分から取得
    for i in range(SLOT_NO_START, SLOT_NO_START+1):
        filepath =  tmp_filepath % i

        data = pd.read_csv(filepath, sep=",")

        x = data.ix[0:5,['payout']]
        print(x['payout'])

        train_X.append(x['payout']);

        y = data.ix[6,['payout']]
        train_Y.append(y.values);

        print(train_Y)

    return np.array(train_X), np.array(train_Y)

if __name__ == "__main__":
    main()
