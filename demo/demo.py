

import pandas as pd



def main():
    data = pd.read_csv("/Users/wanghuamin/Documents/repository/stock-analysis/china_city_aqi.csv")
    print(data.head())



if __name__ == '__main__':
    main()
