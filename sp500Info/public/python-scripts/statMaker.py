#Description: This file contains functions that create graphs for the S&P 500 stock data

#Imports
import matplotlib.pyplot as plt
import dataInteract
import io
import base64
import urllib.parse
import pandas as pd

#Method to create a trend graph
def trendGraph(timeFrame):
    #get the last 20 years of stock data
    sp500 = dataInteract.getDailyStock()

    sp500["Tomorrow"] = sp500["Close"].shift(-1)
    sp500["Target"] = (sp500["Tomorrow"] > sp500["Close"]).astype(int)

    #get the last x days of stock data
    trend_column = f"Trend_{timeFrame}"
    sp500[trend_column] = sp500.shift(1).rolling(timeFrame).sum()["Target"]

    sp500 = sp500.iloc[-timeFrame:]

    # Check if the column exists and is a Series or DataFrame
    trend = sp500[f'Trend_{timeFrame}']
    if isinstance(trend, (pd.Series, pd.DataFrame)):
        plt.clf()
        #plot the trend
        trend.plot(figsize=(10, 6))

        #set the title
        plt.title(f'S&P 500 Day Trend Over {timeFrame} Days')

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)

        string = base64.b64encode(buf.read())

        uri = urllib.parse.quote(string)

        return uri
    else:
        print(f"Cannot plot 'Trend_{timeFrame}' as it is not a Series or DataFrame.")

#Method to create a price graph
def priceRatioGraph(timeFrame):

    #get the last 20 years of stock data
    sp500 = dataInteract.getDailyStock()

    sp500["Tomorrow"] = sp500["Close"].shift(-1)
    sp500["Target"] = (sp500["Tomorrow"] > sp500["Close"]).astype(int)

    #get the last x days of stock data
    sp500 = sp500.iloc[-timeFrame - 2000:]

    rolling_averages = sp500.rolling(timeFrame).mean()
    ratio_column = f"Price_Ratio_{timeFrame}"
    sp500[ratio_column] = sp500["Close"] / rolling_averages["Close"]
    sp500 = sp500.dropna(subset=[f'Price_Ratio_{timeFrame}'])

    sp500 = sp500.iloc[-timeFrame:]

    ratio = sp500[f'Price_Ratio_{timeFrame}']

    # Check if the column exists and is a Series or DataFrame
    if isinstance(ratio, (pd.Series, pd.DataFrame)):
        plt.clf()
        #plot the price
        ratio.plot(figsize=(10, 6))

        #set the title
        plt.title(f'S&P 500 Price Ratio Over {timeFrame}  Days')

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)

        string = base64.b64encode(buf.read())

        uri = urllib.parse.quote(string)

        return uri
    else:
        print(f"Cannot plot 'Price_Ratio_{timeFrame}' as it is not a Series or DataFrame.")


def priceGraph(timeFrame):
    plt.clf()

    sp500 = dataInteract.getDailyStock()

    sp500 = pd.DataFrame(sp500)

    sp500 = sp500.iloc[-timeFrame:]

    if isinstance(sp500['Close'], (pd.Series, pd.DataFrame)):
        sp500['Close'].plot(figsize=(10, 6))

        plt.title(f'S&P 500 Price Over {timeFrame} Days')

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)

        string = base64.b64encode(buf.read())

        uri = urllib.parse.quote(string)

        return uri

    else:
        print(f"Cannot plot 'Close' as it is not a Series or DataFrame.")


def getGraph(timeFrame, type):
    if(type == 'price_ratio'):
        return priceRatioGraph(timeFrame)
    elif(type == 'trend'):
        return trendGraph(timeFrame)
    elif(type == 'price'):
        return priceGraph(timeFrame)
