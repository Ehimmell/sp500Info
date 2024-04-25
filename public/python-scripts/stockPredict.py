import pandas as pd
import pickle as p
import constants

def predict(sp500):

  with open(constants.STOCK_MODEL_PATH, 'rb') as model:
      model = p.load(model)

  preds = model.predict_proba(sp500[constants.PREDICTORS])

  tomorrowPred = preds[-1]

  return tomorrowPred