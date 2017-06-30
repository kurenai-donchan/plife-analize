# -*- coding: utf-8 -*-
# ----------------------------------------------
# 学習させる
# ----------------------------------------------

import pandas as pd
import numpy as np
from sklearn import tree

def main():

    train_data()

    ## CSVファイルを取得
    #data = pd.read_csv("data.csv", sep=",")
    ## 説明変数(x1, x2に設定)
    #variables = ['x1', 'x2']
    ## 決定木の分類器を生成
    #clf = tree.DecisionTreeClassifier()
    ## 分類器にサンプルデータを入れて学習(目的変数はx）
    #clf = clf.fit(data[variables], data['x3'])
    ## 学習結果を出力
    #with open('graph.dot', 'w') as f:
    #    f = tree.export_graphviz(clf, out_file=f)

def train_data():
    train_X = []
    train_y = []

    SLOT_NO_START = 4001
    SLOT_NO_END = 4266

    tmp_filepath = '../data/lot/%d.txt'

    # 過去分から取得
    line = []
    for i in range(SLOT_NO_START, SLOT_NO_END+1):
        filepath =  tmp_filepath % i

        data = pd.read_csv(filepath, sep=",")

        # 2-6前を学習データとする
        feature = data.ix[0:5,['payout']] / 1000

        print(feature )

        #

#
#         train_X.append(object);
#
#
#
#
#
#
#         print(data.ix[0:5,['payout']])
#         print(data.ix[6,['payout','totalRotaion']])

        return np.array(train_X), np.array(train_y)



if __name__ == "__main__":
    main()
