

import pandas as pd



def main():
    # data = pd.read_csv("/Users/wanghuamin/Documents/repository/stock-analysis/china_city_aqi.csv")
    # print(data.head())
    r = []
    for i in range(1, 101):
        r.append(i*i)

    print(r)


if __name__ == '__main__':
    main()
