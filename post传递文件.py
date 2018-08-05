

import requests

url ='http://httpbin.org/post'

# data = {'hello': 'world'}
textFile = {'file': open('./data.txt', 'r')}

r1 = requests.post(url, files=textFile)

print(r1.text)


