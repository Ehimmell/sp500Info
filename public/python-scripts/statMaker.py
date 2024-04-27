#Description: This file contains functions that create graphs for the S&P 500 stock data

#Imports
import matplotlib.pyplot as plt
import dataInteract

#Method to create a trend graph
def trendGraph(timeFrame):

    #get the last 20 years of stock data
    sp500 = dataInteract.getDailyStock()

    #get the last x days of stock data
    sp500 = sp500.iloc[-timeFrame]

    #plot the trend
    sp500[f'Trend_{timeFrame}'].plot(figsize=(10, 6))

    #set the title
    plt.title(f'S&P 500 Day Trend Over {timeFrame} Days')

    #show the plot
    plt.show()

#Method to create a price graph
def priceGraph(timeFrame):

    #get the last 20 years of stock data
    sp500 = dataInteract.getDailyStock()

    #get the last x days of stock data
    sp500 = sp500.iloc[-timeFrame:]

    #plot the price
    sp500['Close'].plot(figsize=(10, 6))

    #set the title
    plt.title(f'S&P 500 Price Over {timeFrame}  Days')

    #show the plot
    plt.show()
