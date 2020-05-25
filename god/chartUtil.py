"""
    作者：wanghuamin
    日期：20200308
    功能：601099 开盘，最高，昨收，涨跌幅
    版本：1.0
"""
from db_mysql import db_mysql_detail
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import matplotlib.ticker as mticker
from decimal import *
import matplotlib.dates as mdates
plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签
plt.rcParams['axes.unicode_minus']=False

dbconn = db_mysql_detail('python')

def selectData(symbol):

    sql = ("select day,open,high,yestClose,updown from stock_base_163 "
           "where symbol = %s order by day asc")

    history_sql = ("select day,topen as open,high,lclose as yestClose ,pchg*0.01 as updown from stock_history_163 "
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
    for data in datas:
        x.append(data[0])
        y0.append(0)
        y1.append(data[1])
        y2.append(data[2])
        y3.append(data[3]+data[4])
        y4.append(data[4])
        y5.append(data[3])
    fig, (ax1, ax2) = plt.subplots(2, 1)
    ax1.set_title(symbol)
    fig.set_size_inches(30, 30, forward=True)
    my_plotter(ax1, x, y0, {'marker': '.'}, label='0刻度')
    my_plotter(ax1, x, y4, {'marker': 'x'}, label='updown')
    my_plotter(ax2, x, y1, {'marker': 'o'}, label='open')
    my_plotter(ax2, x, y2, {'marker': '*'}, label='high')
    my_plotter(ax2, x, y3, {'marker': '+'}, label='Close')
   # my_plotter(ax2, x, y5, {'marker': '|'}, label='yestClose')
    plt.gcf().autofmt_xdate()
    fig.tight_layout()
    #
    # def scroll(event):
    #     axtemp = event.inaxes
    #     x_min, x_max = axtemp.get_xlim()
    #     fanwei_x = (x_max - x_min) / 10
    #     if event.button == 'up':
    #         axtemp.set(xlim=(x_min + fanwei_x, x_max - fanwei_x))
    #     elif event.button == 'down':
    #         axtemp.set(xlim=(x_min - fanwei_x, x_max + fanwei_x))
    #     fig.canvas.draw_idle()
    #     # 这个函数实时更新图片的显示内容
    #
    # def motion(event):
    #     try:
    #         temp = y[int(np.round(event.xdata))]
    #         for i in range(len_y):
    #             _y[i] = temp
    #         line_x.set_ydata(_y)
    #         line_y.set_xdata(event.xdata)
    #         ######
    #         text0.set_position((event.xdata, temp))
    #         text0.set_text(str(temp))
    #
    #         fig.canvas.draw_idle()  # 绘图动作实时反映在图像上
    #     except:
    #         pass
    #
    # fig.canvas.mpl_connect('scroll_event', scroll)
    # fig.canvas.mpl_connect('motion_notify_event', motion)
    plt.show()

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

def main():
    #symbol = "600030"
    symbol = '600809'
    drawChar(selectData(symbol), symbol='山西汾酒'+symbol)
   # drawChar(selectData('600302'))

if __name__ == '__main__':
    main()