
import pickle
import pandas as pd
import yfinance as yf
import datetime as dt
from datetime import date, timedelta

with open('sp500_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

sp500 = yf.Ticker("^GSPC")
sp500 = sp500.history(period="10y")

del sp500["Dividends"]
del sp500["Stock Splits"]

horizons = [2,5,60,250,1000]
new_predictors = []

sp500["Tomorrow"] = sp500["Close"].shift(-1)
sp500["Target"] = (sp500["Tomorrow"] > sp500["Close"]).astype(int)

for horizon in horizons:
    rolling_averages = sp500.rolling(horizon).mean()

    ratio_column = f"Close_Ratio_{horizon}"
    sp500[ratio_column] = sp500["Close"] / rolling_averages["Close"]

    trend_column = f"Trend_{horizon}"
    sp500[trend_column] = sp500.shift(1).rolling(horizon).sum()["Target"]

    new_predictors += [ratio_column, trend_column]

sp500 = sp500.dropna()

data = sp500.iloc[-100]

data_for_prediction = sp500.iloc[-1].copy()
del data_for_prediction["Tomorrow"]
data_for_prediction = data_for_prediction[new_predictors]

print("Predicting...")

prediction = loaded_model.predict(data_for_prediction.values.reshape(1, -1))
def whatToDo():
    if(prediction == 1): return "BUY!!!!!! NOW!!!!!!!"
    return "SELL SELL SELL!!!!!!!!!!!!!"

print("Prediction for tomorrow's stock:", whatToDo())


