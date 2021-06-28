"""
REST
HTTPメソッド クライアントが行いたい処理をサーバーに伝える

GET データの参照
POST データの新規登録
PUT データの更新
DELETE データの削除
"""

import json
import urllib.request

payload = {'key1': 'val1', 'key2': 'val2'}
payload = json.dumps(payload).encode('utf-8')
url = 'http://httpbin.org/get'
# url = 'http://httpbin.org/get' + '?' + urllib.parse.urlencode(payload)

# get
with urllib.request.urlopen(url) as f:
    r = json.loads(f.read().decode('utf-8'))
    print(r)
    print(type(r))

# post
req = urllib.request.Request(
    'http://httpbin.org/post', data=payload, method='POST')
with urllib.request.urlopen(req) as f:
    print(json.loads(f.read().decode('utf-8')))

# put
req = urllib.request.Request(
    'http://httpbin.org/put', data=payload, method='PUT')
with urllib.request.urlopen(req) as f:
    print(json.loads(f.read().decode('utf-8')))

# delete
req = urllib.request.Request(
    'http://httpbin.org/delete', data=payload, method='DELETE')
with urllib.request.urlopen(req) as f:
    print(json.loads(f.read().decode('utf-8')))
