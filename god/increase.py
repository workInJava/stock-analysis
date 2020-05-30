"""
    作者：wanghuamin
    日期：20200527
    功能：当日跌幅在8%的股图
    版本：1.0
"""
import chartUtil
from db_mysql import db_mysql_detail
import trade_date
from datetime import datetime,timedelta
dbconn = db_mysql_detail('python')

def getCode(percent, day, region=0):
    sql = 'select symbol,name from stock_base_163 where percent <= %s and open<100  and percent >=%s and day = %s'
    datas = dbconn.selectAll(sql, where=(percent+region, percent-region, day))
    return datas

def main():
    now = datetime.now()
    while trade_date.is_tradeday(str(now.strftime('%Y%m%d'))) != 1:
        now += timedelta(days=-1)
        print(now)
    datas = getCode(-0.08, str(now.strftime('%Y%m%d')), region=0.05)
    for data in datas:
        chartUtil.draw(data[0], data[1])

if __name__ == '__main__':
    main()



