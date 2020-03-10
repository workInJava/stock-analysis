

import pandas as pd
from db_mysql import db_mysql_detail

dbconn = db_mysql_detail('python')



def main():
    print(pd.read_csv("/Users/wanghuamin/Documents/repository/stock-analysis/china_city_aqi.csv"))



if __name__ == '__main__':
    main()
