"""
    作者：wanghuamin
    日期：20200801
    功能：ma
    版本：1.0
"""

from db_mysql import db_mysql_detail
dbconn = db_mysql_detail('python')



class maUtil():


    def save_ma(self, arrays):
        sql = ('INSERT INTO stock_ma'
               '(day, symbol, name, ma5, ma10, ma20, ma30, ma60, ma120, ma250)'
               'VALUES(%(day)s, %(symbol)s, %(name)s, %(ma5)s, %(ma10)s, %(ma20)s, %(ma30)s, %(ma60)s, %(ma120)s,'
               ' %(ma250)s)')
        dbconn.insertBatch(sql, arrays)

    def core(self, symbol,  start, count):
        sql = ('select h.symbol as symbol, max(h.day) as day ,avg(h.tclose) as ma from stock_history h '
              'right join (select a.day as day,a.symbol as symbol '
              'from stock_history a where a.symbol = \'{symbol}\' '
              'order by day limit {start},{count}) t on h.day = t.day where h.symbol=t.symbol')

        print(sql.format(symbol=symbol, start=start, count=count))
        ma = dbconn.selectAll(sql.format(symbol=symbol, start=start, count=count))
        print(ma)

util = maUtil()
util.core('603356', '0', '5')



def query_tclose():
    query_sql = 'select symbol from temp'
    stock_codes = dbconn.selectAll(query_sql)
    return stock_codes