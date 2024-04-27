#class to prepare and clean any data for the models

#Imports
import pandas as pd
import yfinance as yf
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import constants

#Method to prepare the last 20 years of S&P 500 data
def prepare500Data():

    #get sp500 data
    sp500 = yf.Ticker(constants.SP500_TICKER)

    #get the history of the S&P 500
    sp500 = sp500.history(period="20y")

    #get the index of the sp500
    sp500.index

    #create a column for the target and the next day's close
    sp500["Tomorrow"] = sp500["Close"].shift(-1)
    sp500["Target"] = (sp500["Tomorrow"] > sp500["Close"]).astype(int)

    #create columns for the rolling averages and trends, including the daily closing price over mean closing price, up or down streaks
    for horizon in constants.ROLLING_HORIZONS:
        #create the rolling averages
        rolling_averages = sp500.rolling(horizon).mean()

        #create the close ratio column, daily close / mean close
        ratio_column = f"Close_Ratio_{horizon}"
        sp500[ratio_column] = sp500["Close"] / rolling_averages["Close"]

        #create the trend column, sum of the target column over the horizon
        trend_column = f"Trend_{horizon}"
        sp500[trend_column] = sp500.shift(1).rolling(horizon).sum()["Target"]

    #drop the columns that are not predictors and could cause data leakage
    del sp500["Tomorrow"]
    del sp500["Target"]

    stocks = {ticker: yf.Ticker(ticker).history(period="max") for ticker in constants.KEYSTOCKS_TICKERS}

    #create a column for the price change over the day
    for ticker, data in stocks.items():
        data['Price Change'] = np.sign(data['Close'] - data['Open'])

    #get concatenated price change for all stocks
    all_price_changes = pd.concat([data.reset_index()[['Date', 'Price Change']] for data in stocks.values()])

    #get the mode price change by grouping by day and taking the mode
    mode_price_change = all_price_changes.groupby('Date')['Price Change'].apply(lambda x: x.mode()[0])

    #merge the mode price change with the sp500 data
    sp500 = sp500.merge(mode_price_change.rename('Mode Price Change'), left_index=True, right_index=True, how='left')

    #create columns for the rolling mode price change for key stocks
    for horizon in constants.ROLLING_HORIZONS:
        trend_key_change = f'Trend_Key_Change_{horizon}'
        sp500[trend_key_change] = sp500['Mode Price Change'].shift(1).rolling(horizon).sum()

    #drop the mode price change column to avoid data leakage
    del sp500['Mode Price Change']


    #drop the rows with NaN values
    sp500 = sp500.dropna()

    #return the prepared data
    return sp500

#Method to clean the headlines
def clean(titles):

    #get the stop words and lemmatizer
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()

    #clean the titles
    cleaned_titles = []
    for title in titles:
        tokens = word_tokenize(title)

        #remove stop words and lemmatize
        words = [word for word in tokens if word not in stop_words]
        words = [lemmatizer.lemmatize(word) for word in words]

        cleaned_titles.append(' '.join(words))

    return cleaned_titles