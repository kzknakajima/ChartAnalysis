from matplotlib import pyplot as plt
import datetime as dt
import numpy as np
import pandas_datareader.data as web
import pandas as pd

def trans_xy(start,end):
    df = web.DataReader(symbol,"yahoo",start,end)
    df_xy = pd.DataFrame({symbol: df['Close']})#'Close' is the closing price
    return df_xy

def plt_subset():
    plt.grid(color="gray",linestyle="--")
    plt.xticks(rotation=30)
    plt.legend().remove()
    plt.title('Historical Stock Price '+symbol)

def main():
    global symbol
    symbol = 'TSLA'#AAPL,TSLA,MSFT,NVDA
    start = dt.date(2018,1,1)
    end = dt.date.today().strftime("%Y-%m-%d")

    trans_xy(start,end).plot()
    plt_subset()
    # plt.yscale('log')#y軸を対数表示したい場合
    plt.show()

if __name__ == '__main__':
    main()
