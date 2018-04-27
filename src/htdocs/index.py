# -*- coding:utf-8 -*-

from bottle import route, run, template, static_file
import os


@route('/')
def index(name='This is test by takako'):
    targetdir='../../data/2018/'
    files = os.listdir(targetdir)
    print("test")

    return template('index', name=name)


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
