# -*- coding:utf-8 -*-

from bottle import route, run, template, static_file
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lib import functions

@route('/')
def index(name='This is test by takako'):
    slots_payout_data = functions.readingSlotData()
    print(slots_payout_data )

    return template('index', {'slots_payout_data':slots_payout_data, 'count':5})


@route('/count')
@route('/count/<count:int>')
def hello(count='10'):
    return template('count', count=count)


# smaple hello
@route('/hello')
@route('/hello/<name>')
def hello(name='World'):
    return template('hello_template', name=name)

# 静的ファイル
@route('/static/<file_path:path>')
def static(file_path):
    return static_file(file_path, root='./static')

# run localhost
run(host='localhost', port=8080, debug=True)
