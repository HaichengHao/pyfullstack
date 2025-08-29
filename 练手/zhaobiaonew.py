# @Author    : 百年
# @FileName  :zhaobiaonew.py
# @DateTime  :2025/8/28 16:02
# @Author    : 百年
# @FileName  : zhaobiao.py
# @DateTime  :2025/8/28 15:12

import requests
from lxml import etree
from urllib.parse import urljoin
import csv

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


def detail_page(detailurl, writer):
    try:
        response = requests.get(url=detailurl, headers=headers, timeout=10)
        response.raise_for_status()
        content = response.text
        tree = etree.HTML(content)

        # 提取文本，使用 .xpath(...) 并取 [0] 或默认值
        def safe_extract(xpath):
            result = tree.xpath(xpath)
            return result[0].strip() if result else ''

        pdate = safe_extract('//div[@class="page_msg"]/span[1]/text()')
        pname = safe_extract('//tbody/tr[2]/td[2]/text()')
        ptype = safe_extract('//tbody/tr[3]/td[2]/text()')
        pvote = safe_extract('//tbody/tr[3]/td[4]/text()')
        pcontent = safe_extract('//tbody/tr[4]/td[2]/text()')
        ppeople = safe_extract('//tbody/tr[5]/td[2]/text()')
        pdepart = safe_extract('//tbody/tr[5]/td[4]/text()')
        pdanwei = safe_extract('//tbody/tr[6]/td[4]/text()')
        pmode = safe_extract('//tbody/tr[8]/td[2]/text()')
        ppredate = safe_extract('//tbody/tr[9]/td[2]/text()')

        # 写入一行
        writer.writerow([pdate, pname, ptype, pvote, pcontent, ppeople, pdepart, pdanwei, pmode, ppredate])
    except Exception as e:
        print(f"解析页面失败: {detailurl}, 错误: {e}")


if __name__ == '__main__':
    # 获取所有链接
    for i in range(1, 4):  # 注意：页码通常从 1 开始
        all_url(i)

    print(f"共获取 {len(all_ref_lst)} 个链接")

    # 在 with 块中打开文件，并传入 writer
    with open('./demo.csv', 'a+', encoding='utf-8', newline='') as fp:
        writer = csv.writer(fp)
        # 如果文件为空，写入表头
        if fp.tell() == 0:
            writer.writerow(['发布日期', '项目名称', '项目类型', '项目总投资', '招标内容', '招标人名称', '行政监督部门', '发布单位', '内容规划', '预计发布时间'])

        # 遍历链接并写入数据
        for ref in all_ref_lst:
            detail_page(ref, writer)