"""
    作者：wanghuamin
    日期：20200308
    功能：爬去当天股票数据
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


def httpClient(url_key):
    url = url_config.get_config(url_key)
    html_content = requests.get(url, timeout=30)
    soup = BeautifulSoup(html_content.text, 'lxml')
    return soup


def currentData(dateStr):
    url_key = '163_current'
    soup = httpClient(url_key)
    jsondata = json.loads(soup.p.string)

    sql = ("INSERT INTO stock_base_163 "
           "(day, code, five_minute, high, open,"
           "low, yestClose, hs, lb, mcap, mfratio, mfsum, name,"
           "pe, updown, percent, sname, symbol, tcap, turnover, volume, wb, zf)"
           "VALUES (%(day)s, %(code)s,  %(five_minute)s, %(high)s, %(open)s, %(low)s, %(yestClose)s, %(hs)s, %(lb)s, %(mcap)s,"
           "%(mfratio)s, %(mfsum)s, %(name)s, %(pe)s, %(updown)s, %(percent)s, %(sname)s, %(symbol)s, %(tcap)s,"
           "%(turnover)s, %(volume)s, %(wb)s, %(zf)s)")

    columes = ['code', 'five_minute', 'high', 'open', 'low', 'yestClose', 'hs', 'lb',
              'mcap', 'mfratio', 'mfsum', 'name', 'pe', 'updown', 'percent', 'sname', 'symbol',
              'tcap', 'turnover', 'volume', 'wb', 'zf']

    batch_data =[]
    for data in jsondata['list']:
        add_data = {'day': dateStr}
        for col in columes:
            try:
                value = data[col.upper()]
                if type(value) is float:
                        value = round(value, 4)
                add_data[col] = str(value)
            except:
                add_data[col] = '0'
                print(data)
       # dbconn.insertOne(sql, add_data)
        batch_data.append(add_data)
    dbconn.insertBatch(sql, batch_data)


if __name__ == '__main__':
    now = str(datetime.now().strftime('%Y%m%d'))
    if trade_date.is_tradeday(now) == 1:
        print(now)
        currentData(now)