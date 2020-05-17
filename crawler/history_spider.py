"""
    作者：wanghuamin
    日期：20200308
    功能：股票历史数据下载，并保存mysql
    版本：1.0
"""
import requests
import time
from bs4 import BeautifulSoup
from url_config import http_config
from db_mysql import db_mysql_detail
dbconn = db_mysql_detail('python')
import csv
import os


url_config = http_config()


def html163(stockCode):
    url_key = '163_html'
    url = url_config.get_config(url_key).format(stockCode = stockCode)
    html_content = requests.get(url, timeout=3000)
    soup = BeautifulSoup(html_content.text, 'lxml')
    date_end = soup.find(name='input', attrs={"name": "date_end_type", "checked": "checked"})['value'].replace('-', '')
    date_start = soup.find(name='input', attrs={"name": "date_start_type", "checked": "checked"})['value'].replace('-', '')
    url_key = '163_download'
    down_url = url_config.get_config(url_key).format(stockCode = stockCode, date_start = date_start, date_end = date_end)
    down_res = requests.get(url = down_url)
    with open(stockCode+".csv", "wb") as code:
        code.write(down_res.content)


def historyData():
    query_sql = 'select distinct(symbol) from stock_base_163 limit 1564, 36'
    stock_codes = dbconn.selectAll(query_sql)
    for stockCode in stock_codes:
        html163(stockCode[0])
        resolve(stockCode[0])


def resolve(stockCode):
    dirfile = os.getcwd()+"/"+stockCode+".csv"
    col = ['day', 'symbol', 'name', 'tclose', 'high', 'low', 'topen',
           'lclose', 'chg', 'pchg', 'turnover', 'voturnover',
           'vaturnover', 'tcap', 'mcap']
    with open(dirfile, "r", encoding="GBK") as f:
        reader = csv.reader(f)
        arrays = []
        for i, row in enumerate(reader):
            if i==0:
                continue
            add_data = dict(zip(col, row))
            #add_data[]
            for k, v in add_data.items():
                if k == 'symbol':
                    add_data['symbol'] = str(v).replace("'", "")
                if v == 'None':
                    add_data[k] = '0'
            arrays.append(add_data)
        print(arrays)
        save(arrays)
        os.remove(dirfile)

def save(arrays):
    sql = ('INSERT INTO stock_history_163'
           '(day, symbol, name, tclose, high, low, topen, lclose, chg, pchg, turnover, voturnover, vaturnover, tcap, mcap)'
           'VALUES(%(day)s, %(symbol)s, %(name)s, %(tclose)s, %(high)s, %(low)s, %(topen)s, %(lclose)s, %(chg)s,'
           ' %(pchg)s, %(turnover)s, %(voturnover)s, %(vaturnover)s, %(tcap)s, %(mcap)s)')
    dbconn.insertBatch(sql, arrays)

if __name__ == '__main__':
    historyData()