# Description: This script is used to predict the stock price of the S&P 500 index for the next day.

#Imports
import pickle as p
import constants

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