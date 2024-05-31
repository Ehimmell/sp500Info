#Description: This file contains functions that create graphs for the S&P 500 stock dataload

#Imports
import matplotlib.pyplot as plt
import io
import base64
import urllib.parse
import pandas as pd
from stock.sp500Info.public.python_code.dataload import dataPrep

#Method to create a trend graph
def trendGraph(timeFrame):
    #get the last 20 years of stock dataload
    sp500 = dataPrep.prepare500Data()

    sp500["Tomorrow"] = sp500["Close"].shift(-1)
    sp500["Target"] = (sp500["Tomorrow"] > sp500["Close"]).astype(int)

    #get the last x days of stock dataload
    trend_column = f"Trend_{timeFrame}"
    sp500[trend_column] = sp500.shift(1).rolling(timeFrame).sum()["Target"]

    sp500 = sp500.iloc[-timeFrame:]

    return savePlot(f'Trend_{timeFrame}', sp500)

#Method to create a price graph
def priceRatioGraph(timeFrame):

    #get the last 20 years of stock dataload
    sp500 = dataPrep.prepare500Data()

    sp500["Tomorrow"] = sp500["Close"].shift(-1)
    sp500["Target"] = (sp500["Tomorrow"] > sp500["Close"]).astype(int)

    #get the last x days of stock dataload
    sp500 = sp500.iloc[-timeFrame - 2000:]

    rolling_averages = sp500.rolling(timeFrame).mean()
    ratio_column = f"Price_Ratio_{timeFrame}"
    sp500[ratio_column] = sp500["Close"] / rolling_averages["Close"]
    sp500 = sp500.dropna(subset=[f'Price_Ratio_{timeFrame}'])

    sp500 = sp500.iloc[-timeFrame:]

    return savePlot(f'Price_Ratio_{timeFrame}', sp500)


def priceGraph(timeFrame):
    sp500 = dataPrep.prepare500Data()

    sp500 = sp500.iloc[-timeFrame:]

    return savePlot('Close', sp500)

def closeOverOpenGraph(timeFrame):

    sp500 = dataPrep.prepare500Data()

    sp500 = sp500.iloc[-timeFrame:]

    sp500[f'Close_Over_Open_{timeFrame}'] = sp500['Close'] / sp500['Open']

    return savePlot(f'Close_Over_Open_{timeFrame}', sp500)

def prepSpecialGraph(ticker):

    stock = dataPrep.prepGraphData(ticker)

    return savePlot('Close', stock)

def savePlot(column, sp500):

    if isinstance(sp500[column], (pd.Series, pd.DataFrame)):
        plt.clf()
        #plot the trend
        sp500[column].plot(figsize=(10, 6))

        #set the title
        plt.title(f'S&P 500 {column}')

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)

        string = base64.b64encode(buf.read())

        uri = urllib.parse.quote(string)

        return uri
    else:
        print(f"Cannot plot '{column}' as it is not a Series or DataFrame.")

def getMean(timeFrame):
    sp500 = dataPrep.prepare500Data()
    sp500['Close'] = pd.to_numeric(sp500['Close'], errors='coerce')
    sp500 = sp500.iloc[-timeFrame:]
    return sp500['Close'].mean()

def getMedian(timeFrame):
    sp500 = dataPrep.prepare500Data()
    sp500['Close'] = pd.to_numeric(sp500['Close'], errors='coerce')
    sp500 = sp500.iloc[-timeFrame:]
    return sp500['Close'].median()

def getStdDev(timeFrame):
    sp500 = dataPrep.prepare500Data()
    sp500['Close'] = pd.to_numeric(sp500['Close'], errors='coerce')
    sp500 = sp500.iloc[-timeFrame:]
    return sp500['Close'].std()

def getStat(timeFrame, type):
    timeFrame = int(timeFrame)
    if(type == 'mean'):
        return getMean(timeFrame)
    elif(type == 'median'):
        return getMedian(timeFrame)
    elif(type == 'std'):
        return getStdDev(timeFrame)

def getGraph(timeFrame, type):
    timeFrame = int(timeFrame)
    if(type == 'price_ratio'):
        return priceRatioGraph(timeFrame)
    elif(type == 'trend'):
        return trendGraph(timeFrame)
    elif(type == 'price'):
        return priceGraph(timeFrame)
    elif(type == 'close_over_open'):
        return closeOverOpenGraph(timeFrame)
