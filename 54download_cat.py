print('hello,world')

import urllib.request

response = urllib.request.urlopen("http://placekitten.com/400/500")
#等同于：
#res = urllib.request.Request("http://placekitten.com/400/500")
#response = urllib.request.urlopen(req)

cat_img = response.read()

with open('cat_400_500.jpg','wb') as f:
	f.write(cat_img)

print(response.geturl())

print(response.info())

print(response.getcode())















































































