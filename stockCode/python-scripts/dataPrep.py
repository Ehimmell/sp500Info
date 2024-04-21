import pandas as pd
import yfinance as yf
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob

def prepare500Data():

    sp500 = yf.Ticker("^GSPC")

    sp500 = sp500.history(period="20y")

    sp500.index

    horizons = [2,5,60,250,1000]

    sp500["Tomorrow"] = sp500["Close"].shift(-1)
    sp500["Target"] = (sp500["Tomorrow"] > sp500["Close"]).astype(int)

    for horizon in horizons:
        rolling_averages = sp500.rolling(horizon).mean()

        ratio_column = f"Close_Ratio_{horizon}"
        sp500[ratio_column] = sp500["Close"] / rolling_averages["Close"]

        trend_column = f"Trend_{horizon}"
        sp500[trend_column] = sp500.shift(1).rolling(horizon).sum()["Target"]

    del sp500["Tomorrow"]
    del sp500["Target"]

    tickers = ['AAPL', 'MSFT', 'JNJ', 'AMZN', 'GOOGL', 'BRK-A']

    stocks = {ticker: yf.Ticker(ticker).history(period="max") for ticker in tickers}

    import pandas as pd
    import numpy as np

    for ticker, data in stocks.items():
        data['Price Change'] = np.sign(data['Close'] - data['Open'])

    all_price_changes = pd.concat([data.reset_index()[['Date', 'Price Change']] for data in stocks.values()])

    mode_price_change = all_price_changes.groupby('Date')['Price Change'].apply(lambda x: x.mode()[0])

    sp500 = sp500.merge(mode_price_change.rename('Mode Price Change'), left_index=True, right_index=True, how='left')

    sp500 = sp500.dropna()

    horizons = [2, 5, 60, 250, 1000]
    for horizon in horizons:
        trend_key_change = f'Trend_Key_Change_{horizon}'
        sp500[trend_key_change] = sp500['Mode Price Change'].shift(1).rolling(horizon).sum()

    del sp500['Mode Price Change']

    return sp500

def clean(titles):
    nltk.download('punkt')
    nltk.download('wordnet')
    nltk.download('stopwords')

    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()

    cleaned_titles = []
    for title in titles:
        tokens = word_tokenize(title)

        words = [word for word in tokens if word not in stop_words]
        words = [lemmatizer.lemmatize(word) for word in words]

        cleaned_titles.append(' '.join(words))

    return cleaned_titles