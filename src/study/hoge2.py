# coding:utf-8

import sys,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8') # UTF-8に

s = 'あいうえお'

b = s.encode('unicode-escape')

print(b)
# b'\\u3042\\u3044\\u3046\\u3048\\u304a'

print(type(b))
# <class 'bytes'>

s_from_b = b.decode('unicode-escape')

print(s_from_b)
# あいうえお

print(type(s_from_b))
# <class 'str'>


s1 = '日本語文字列(s1)'
s2 = u'日本語文字列(s2)'

print (s1) # 文字化け
print (s2) # 文字化けしない

print(sys.stdout.encoding) # ANSI_X3.4-1968 等を出力