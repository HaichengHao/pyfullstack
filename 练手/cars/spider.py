# @Author    : 百年
# @FileName  :spider.py
# @DateTime  :2025/8/28 14:27

import requests

url='https://car-web-api.autohome.com.cn/car/rank/getList?from=28&pm=2&pluginversion=11.75.8&model=1&channel=0&pageindex=1&pagesize=100&typeid=1&subranktypeid=1&levelid=0&price=0-9000&date=2025-07'
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'
}

response = requests.get(url=url,headers=headers)

content = response.json()

print(content)