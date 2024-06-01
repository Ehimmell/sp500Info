# Description: This script is used to predict the stock price of the S&P 500 index for the next day.

#Imports
import pickle as p
from stock.sp500Info.public.python_code import constants
import numpy as np
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
    return tomorrowPred[constants.STOCKPRED_BUY].astype(float)

def pricePredict(sp500):

    model = load_model('/Users/himme/Downloads/git/stock/sp500Info/public/models/stockLSTM.keras')

    with open('/Users/himme/Downloads/git/stock/sp500Info/public/vectorizers/scaler.pkl', 'rb') as scaler:
        scaler = p.load(scaler)

    sp_save = sp500.iloc[-1].copy()

    sp500 = scaler.transform(np.array(sp500.reset_index()['Close']).reshape(-1, 1))

    X = []
    for i in range(len(sp500) - 99):
        a = sp500[i:(i + 100), 0]
        X.append(a)

    X = np.array(X)

    predictions = scaler.inverse_transform(model.predict(X))

    change_direction = "up" if predictions[-1] > sp_save['Close'] else "down"

    return predictions[-1][0], change_direction

def consolidatedPred(sp500):

    lstm_pred = pricePredict(sp500)[0]

    stock_pred = predict(sp500)

    stock_pred = 1 if stock_pred > 0.5 else 0

    return (((lstm_pred * 1.5) + stock_pred) / 2.5).astype(float)


