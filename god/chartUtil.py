"""
    作者：wanghuamin
    日期：20200308
    功能： 开盘，最高，昨收，涨跌额
    版本：1.0
"""
from db_mysql import db_mysql_detail
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from decimal import *
import matplotlib.dates as mdates
plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签
plt.rcParams['axes.unicode_minus']=False

dbconn = db_mysql_detail('python')

def selectData(symbol):

    sql = ("select day,open,high,yestClose,updown,lb,wb from stock_base_163 "
           "where symbol = %s order by day asc")

    history_sql = ("select day,topen as open, high, lclose as yestClose ,pchg*0.01 as updown,0.0 as lb,0.0 as wb from stock_history_163 "
           "where symbol = %s and day >'2020-01-01' order by day asc")

    datas = dbconn.selectAll(sql, where=(symbol,))
    history_datas = dbconn.selectAll(history_sql,  where=(symbol,))
    history_datas.extend(datas)
    return history_datas


def drawChar(datas, symbol=None):
    x = []
    y0 = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    y5 = []
    y6 = []
    y7 = []
    for data in datas:
        x.append(data[0])
        y0.append(0)
        y1.append(data[1].quantize(Decimal('0.00')))
        y2.append(data[2].quantize(Decimal('0.00')))
        y3.append((data[3]+data[4]).quantize(Decimal('0.00')))
        y4.append(data[4].quantize(Decimal('0.00')))
        y5.append(data[3].quantize(Decimal('0.00')))
        y6.append(data[5].quantize(Decimal('0.00')))
        y7.append(data[6].quantize(Decimal('0.00')))
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
    ax1.set_title(symbol)
    fig.set_size_inches(30, 30, forward=True)
    my_plotter(ax1, x, y0, {'marker': '.'}, label='0刻度')
    my_plotter(ax1, x, y4, {'marker': 'x'}, label='updown')
    my_plotter(ax2, x, y1, {'marker': 'o'}, label='open')
    my_plotter(ax2, x, y2, {'marker': '*'}, label='high')
    my_plotter(ax2, x, y3, {'marker': '+'}, label='Close')
    my_plotter(ax3, x, y6, {'marker': '+'}, label='lb')
    my_plotter(ax3, x, y7, {'marker': '+'}, label='wb')
   # my_plotter(ax2, x, y5, {'marker': '|'}, label='yestClose')
    plt.gcf().autofmt_xdate()
    fig.tight_layout()
    plt.show()
    plt.close(fig=fig)

def my_plotter(ax, data1, data2, param_dict, label):
    out = ax.plot(data1, data2, **param_dict, label=label)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=2))
    #ax.yaxis.set_major_locator(mticker.MultipleLocator(1))
    ax.yaxis.set_minor_locator(mticker.MultipleLocator(0.1))
    ax.set_xlabel('日期')
    ax.set_ylabel('价格')
    ax.legend()
    ax.grid(True)
    return out



def draw(symbol, name):
    #symbol = "601099"
    #symbol = '600809'
    try:
        drawChar(selectData(symbol), symbol=name+symbol)
    except RuntimeError:
        print("Error: 输出异常symbol:"+symbol)
   # drawChar(selectData('600302'))

if __name__ == '__main__':
    symbol = "601099"
    name = ""
    draw(symbol, name)