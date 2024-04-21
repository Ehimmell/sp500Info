import matplotlib.pyplot as plt
import dataInteract

def trendGraph(timeFrame):

    sp500 = dataInteract.getDailyStock()

    sp500 = sp500.iloc[-timeFrame]

    sp500[f'Trend_{timeFrame}'].plot(figsize=(10, 6))

    plt.title(f'S&P 500 Day Trend Over {timeFrame} Days')

    plt.show()

def priceGraph(timeFrame):

    sp500 = dataInteract.getDailyStock()

    sp500 = sp500.iloc[-timeFrame:]

    sp500['Close'].plot(figsize=(10, 6))

    plt.title(f'S&P 500 Price Over {timeFrame}  Days')

    plt.show()


