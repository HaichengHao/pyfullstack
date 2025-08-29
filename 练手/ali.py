# @Author    : 百年
# @FileName  :ali.py
# @DateTime  :2025/8/28 15:04
import requests

headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'
}
url='https://p4psearch.1688.com/hamlet/async/v1.json?beginpage=1&asyncreq=3&keywords=&keyword=%E6%B0%B4%E7%A8%BB%E4%B8%93%E7%94%A8%E8%82%A5&sortType=&descendOrder=&province=&city=&priceStart=&priceEnd=&dis=&ptid=&exp=pcSemFumian%3AC%3BpcDacuIconExp%3AA%3BpcCpxGuessExp%3AB%3BpcCpxCpsExp%3AB%3Bqztf%3AE%3BhotBangdanExp%3AB%3BpcSemWwClick%3AA%3Basst%3AD%3BpcSemDownloadPlugin%3AA&cosite=&salt=17563645559220&sign=8028676fcb5086ecde664dd13f690df4&hmaTid=3&hmaQuery=graphDataQuery&pidClass=pc_list_336&cpx=cpc%2Cfree%2Cnature&api=pcSearch&pv_id='


response = requests.get(url=url,headers=headers)

content = response.json()

print(content)