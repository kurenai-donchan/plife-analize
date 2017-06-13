# -*- coding: utf-8 -*-
import sys
import lxml.html
import requests


target_url = 'http://api.p-ken.jp/p-arkst/bonusinfo/styleAsGauge?term_id=&cost=20&ps_div=2&p=1&mode='
headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'}

# 取得
target_html = requests.get(target_url, headers=headers).text
root = lxml.html.fromstring(target_html)


for slot in root.cssselect('ul li a'):
   sys.stdout.buffer.write((slot.text + '\n').encode('utf-8'))


