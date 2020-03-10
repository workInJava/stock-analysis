"""
    作者：wanghuamin
    日期：20200308
    功能：tools 163，sin 解析
    版本：1.0
"""
from bs4 import BeautifulSoup
import pandas as pd
from db_mysql import db_mysql_detail
dbconn = db_mysql_detail('python')





def sinaCrawler(html_content):
    soup = BeautifulSoup(html_content.text, 'lxml')
    return soup.p.get_text().split("=")[1]



def resolve(stockCode):
    url = "http://hq.sinajs.cn/list="+stockCode
    dataStr = sinaCrawler(url)
    return dataStr




def writeCvs():
    resolve("sh601099")


def main():
    print(resolve("sh601099"))



if __name__ == '__main__':
    main()