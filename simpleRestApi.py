#sending json data in a given url
import json
import requests
data={"hi":"hello"}
jsondata=json.dumps(data)
url = 'http://httpbin.org/post'
headers = {'Content-type': 'application/json'}
response=requests.post(url,data=jsondata,headers=headers)
print(response.json())
