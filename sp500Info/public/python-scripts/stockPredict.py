# Description: This script is used to predict the stock price of the S&P 500 index for the next day.

#Imports
import pickle as p
import constants
import numpy as np
import dataPrep as dp
import yfinance as yf
from tensorflow.keras.models import load_model

#Method to predict the stock price of the S&P 500 index for the next day
def predict(sp500):

    #load the model
    with open(constants.STOCK_MODEL_PATH, 'rb') as model:
        model = p.load(model)

    #predict the stock price for the next day
    preds = model.predict_proba(sp500[constants.PREDICTORS])

    #get the prediction for the next day
    tomorrowPred = preds[-1]

    #return the prediction
    return tomorrowPred

def pricePredict(sp500):

    model = load_model('../stockLSTM.keras')

    with open('../vectorizers/scaler.pkl', 'rb') as scaler:
        scaler = p.load(scaler)

    print(model.summary())

    sp500 = sp500.reset_index()['Close']

    sp500 = scaler.transform(np.array(sp500).reshape(-1, 1))

    X = []
    for i in range(len(sp500) - 99):
        a = sp500[i:(i + 100), 0]
        X.append(a)

    X = np.array(X)

    preds = model.predict(X)

    preds = scaler.inverse_transform(preds)

    return preds[-1]

