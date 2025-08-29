# @Author    : 百年
# @FileName  :zhaobiao.py
# @DateTime  :2025/8/28 15:12
import requests
from lxml import etree
from urllib.parse import urljoin
import csv

fp = open('./demo.csv', 'a+', encoding='utf-8', newline='')
writer = csv.writer(fp)
if fp.tell() == 0:
    writer.writerow(['发布日期', '项目名称', '项目类型', '项目总投资', '招标内容', '招标人名称', '行政监督部门', '发布单位', '内容规划', '预计发布时间'])

url = 'https://www.sxbid.com.cn/f/new/notice/list/16'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'
}
all_ref_lst = []


def all_url(i: int):
    data = {
        'pageNo': i,
        'pageSize': 15
    }
    response = requests.post(url=url, headers=headers, data=data)
    content = response.text
    tree = etree.HTML(content)
    refs = tree.xpath('//tbody/tr/td/a/@href')
    for ref in refs:
        all_href = urljoin(url, ref)
        all_ref_lst.append(all_href)


def detail_page(detailurl):
    response = requests.get(url=detailurl, headers=headers)
    content = response.text
    tree = etree.HTML(content)
    pdate = tree.xpath('//div[@class="page_msg"]/span[1]/text()')
    pname = tree.xpath('//tbody/tr[2]/td[2]')

    ptype = tree.xpath('//tbody/tr[3]/td[2]')
    pvote = tree.xpath('//tbody/tr[3]/td[4]')

    pcontent = tree.xpath('//tbody/tr[4]/td[2]')

    ppeople = tree.xpath('//tbody/tr[5]/td[2]')
    pdepart = tree.xpath('//tbody/tr[5]/td[4]')
    pdanwei = tree.xpath('//tbody/tr[6]/td[4]')
    pmode = tree.xpath('//tbody/tr[8]/td[2]')
    ppredate = tree.xpath('//tbody/tr[9]/td[2]')
    writer.writerow([pdate, pname, ptype, pvote, pcontent, ppeople, pdepart, pdanwei, pmode, ppredate])


if __name__ == '__main__':
    for i in range(3):
        all_url(i)
    print(all_ref_lst, len(all_ref_lst))
    for ref in all_ref_lst:
        detail_page(ref)
