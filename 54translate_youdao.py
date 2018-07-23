print('hello,world')

import urllib.request
import urllib.parse
import json

content = input("请输入需要翻译的内容：")

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
data = {}
data['i'] = content
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = '1532159431288'
data['sign'] = 'e54938df74964d7af0b38f716032edd2'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_REALTIME'
data['typoResult'] = 'false'


data = urllib.parse.urlencode(data).encode('utf-8')

response = urllib.request.urlopen(url,data)
html = response.read().decode('utf-8')

target = json.loads(html)
print('翻译结果：%s' % (target['translateResult'][0][0]['tgt']))

'''
print(html)

import json
print(json.loads(html))
target = json.loads(html)
print(type(target))
print(target['translateResult'])
print(target['translateResult'][0][0])
print(target['translateResult'][0][0]['tgt'])
'''
















































































