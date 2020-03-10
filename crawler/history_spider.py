"""
    作者：wanghuamin
    日期：20200308
    功能：股票历史数据下载，并保存mysql
    版本：1.0
"""
import requests
from bs4 import BeautifulSoup
from url_config import http_config
from datetime import datetime
import json
from db_mysql import db_mysql_detail
import trade_date
dbconn = db_mysql_detail('python')

url_config = http_config()


def html163(stockCode):
    url_key = '163_html'
    url = url_config.get_config(url_key).format(stockCode = stockCode)
    html_content = requests.get(url, timeout=30)
    soup = BeautifulSoup(html_content.text, 'lxml')
    date_end = soup.find(name='input', attrs={"name": "date_end_type", "checked": "checked"})['value'].replace('-', '')
    date_start = soup.find(name='input', attrs={"name": "date_start_type", "checked": "checked"})['value'].replace('-', '')
    url_key = '163_download'
    down_url = url_config.get_config(url_key).format(stockCode = stockCode, date_start = date_start, date_end = date_end)
    down_res = requests.get(url = down_url)

    with open(stockCode+".csv", "wb") as code:
        code.write(down_res.content)


def historyData():
    stockCode = ''
    html163(stockCode)


if __name__ == '__main__':
    historyData()