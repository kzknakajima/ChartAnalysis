from matplotlib import pyplot as plt
import datetime as dt
import numpy as np
import pandas_datareader.data as web
import pandas as pd

# ax.set_yscale('log')

def main():
    symbol = 'TSLA'#AAPL,TSLA,MSFT,NVDA
    start = dt.date(2020,1,1)
    end = dt.date.today().strftime("%Y-%m-%d")

    df = web.DataReader(symbol,"yahoo",start,end)
    df_xy = pd.DataFrame({symbol: df['Close']})#'Close' is the closing price
    df_xy.plot()
    plt.grid(color="gray",linestyle="--")
    plt.xticks(rotation=30)
    plt.legend().remove()
    plt.title('Historical Stock Price '+symbol)
    plt.show()

if __name__ == '__main__':
    main()
