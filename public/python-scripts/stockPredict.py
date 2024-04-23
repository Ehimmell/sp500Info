import pandas as pd
import pickle as p

def predict(sp500):

  with open('C:/code/Git/stockCode/public/updatedSPModel.pkl', 'rb') as model:
      model = p.load(model)

  newPreds= ['Close_Ratio_2', 'Trend_2', 'Close_Ratio_5', 'Trend_5',
         'Close_Ratio_60', 'Trend_60', 'Close_Ratio_250', 'Trend_250',
         'Close_Ratio_1000', 'Trend_1000', 'Trend_Key_Change_2',
         'Trend_Key_Change_5', 'Trend_Key_Change_60', 'Trend_Key_Change_250',
         'Trend_Key_Change_1000']

  preds = model.predict_proba(sp500[newPreds])

  preds[:, 1] = (preds[:, 1] >= 0.57).astype(int)

  tomorrowPred = preds[-1]

  return tomorrowPred





