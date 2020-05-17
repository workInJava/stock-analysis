"""
    作者：wanghuamin
    日期：20200308
    功能：601099 开盘，最高，昨收，涨跌幅
    版本：1.0
"""
from db_mysql import db_mysql_detail
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

import matplotlib.dates as mdates
plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签
plt.rcParams['axes.unicode_minus']=False

dbconn = db_mysql_detail('python')

def selectData(symbol):

    sql = ("select day,open,high,yestClose,updown from stock_base_163 "
           "where symbol = %s")

    history_sql = ("select day,topen as open,high,lclose as yestClose ,pchg*0.01 as updown from stock_history_163 "
           "where symbol = %s")

    datas = dbconn.selectAll(sql, where=(symbol,))
    #history_datas = dbconn.selectAll(history_sql,  where=(symbol,))
    #datas.extend(history_datas)
    return datas


def drawChar(datas, code=None):
    x = []
    y0 = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    for data in datas:
        x.append(data[0])
        y0.append(0)
        y1.append(data[1])
        y2.append(data[2])
        y3.append(data[3])
        y4.append(data[4])

    fig, (ax1, ax2) = plt.subplots(2, 1)
    ax1.set_title(code)
    fig.set_size_inches(30, 30, forward=True)
    my_plotter(ax1, x, y0, {'marker': '.'}, label='0刻度')
    my_plotter(ax1, x, y4, {'marker': 'x'}, label='updown')
    my_plotter(ax2, x, y1, {'marker': 'o'}, label='open')
    my_plotter(ax2, x, y2, {'marker': '*'}, label='high')
    my_plotter(ax2, x, y3, {'marker': '+'}, label='yestClose')
    plt.gcf().autofmt_xdate()
    fig.tight_layout()
    plt.show()

def my_plotter(ax, data1, data2, param_dict, label):
    out = ax.plot(data1, data2, **param_dict, label=label)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))
    ax.xaxis.set_major_locator(mdates.DayLocator())
    ax.yaxis.set_major_locator(MultipleLocator(0.01))
    ax.set_xlabel('日期')
    ax.set_ylabel('价格')
    ax.legend()
    ax.grid(True)
    return out

def main():
    code1 = "601099"
    drawChar(selectData(code1), code='太平洋'+code1)
   # drawChar(selectData('600302'))

if __name__ == '__main__':
    main()