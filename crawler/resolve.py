"""
    作者：wanghuamin
    日期：20200308
    功能：tools 163，sin 解析
    版本：1.0
"""
from bs4 import BeautifulSoup
from db_mysql import db_mysql_detail
dbconn = db_mysql_detail('python')
import csv
import os


def sinaCrawler(html_content):
    soup = BeautifulSoup(html_content.text, 'lxml')
    return soup.p.get_text().split("=")[1]



def resolve(stockCode):
    url = "http://hq.sinajs.cn/list="+stockCode
    dataStr = sinaCrawler(url)
    return dataStr

def resolve():
    col = ['day', 'symbol', 'name', 'tclose', 'high', 'low', 'topen',
           'lclose', 'chg', 'pchg', 'turnover', 'voturnover',
           'vaturnover', 'tcap', 'mcap']
    dirfile = "/Users/wanghuamin/Documents/repository/stock-analysis/crawler/688026.csv"
    with open(dirfile, "r", encoding="GBK") as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i==0:
                continue

            add_data = dict(zip(col, row))
            print(add_data)





def writeCvs():
    resolve("sh601099")


def main():
    print(resolve("sh601099"))



if __name__ == '__main__':
    resolve()