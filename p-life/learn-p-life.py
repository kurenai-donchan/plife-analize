# -*- coding: utf-8 -*-
# ----------------------------------------------
# 学習させる
# ----------------------------------------------

import pandas as pd
import numpy as np
import sys
from sklearn import tree
from sklearn.externals import joblib

def main():

    # CSVファイルを取得
    data = pd.read_csv("../data/sum/traning_data.csv", sep=",")
    # 説明変数(x1, x2に設定)
    variables = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6']
    # 決定木の分類器を生成
    clf = tree.DecisionTreeClassifier()
    # 分類器にサンプルデータを入れて学習(目的変数はx）
    clf = clf.fit(data[variables], data['x7'])
    # 学習結果を出力
    with open('graph.dot', 'w') as f:
        f = tree.export_graphviz(clf, out_file=f)

    joblib.dump(clf, 'tree.learn')

if __name__ == "__main__":
    main()
