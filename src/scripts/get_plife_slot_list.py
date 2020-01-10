# coding:utf-8
# ----------------------------------------------
# 機種一覧を出力する
# ----------------------------------------------

import codecs
import datetime
import sys
import lxml.html
import requests
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8') # UTF-8に

target_url = 'http://api.p-ken.jp/p-arkst/bonusinfo/styleAsGauge?term_id=&cost=21.7&ps_div=2&p=1&mode='
headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'}


def main():
    # 今日の日付
    today = datetime.datetime.today()

    # 取得
    target_html = requests.get(target_url, headers=headers).text

    root = lxml.html.fromstring(target_html)

    filepath = '../../data/slot_list/%s.txt' % today.strftime("%Y%m%d")
    f = codecs.open(filepath, 'w', 'utf-8')

    i = 1
    for slot in root.xpath('//li[@data-theme="c"]/a|//li[@data-theme="c"]/span'):
        if (i % 2 == 1):
            f.write(slot.text_content())
        else:
            f.write(" (" + slot.text_content() + ") \n")

        i = i + 1

    f.close()
    print("output:" + filepath);

# ----------------------------------------
# main 処理実行
# ----------------------------------------
if __name__ == "__main__":
    main()

sys.exit()