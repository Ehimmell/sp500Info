import pandas as pd
import sqlite3
import dataPrep
import stockPredict

def sendDailyStock():
    spDB = sqlite3.connect("C:/code/Git/stockCode/public/sp500Data.db")

    sp500 = dataPrep.prepare500Data()

    sp500.to_sql('sp500_table', spDB, if_exists='replace')

    spDB.close()

def getDailyStock():
    spDB = sqlite3.connect("C:/code/Git/stockCode/public/sp500Data.db")

    sp500 = pd.read_sql_query("SELECT * FROM sp500_table", spDB)

    spDB.close()

    return sp500

def sendDailyPrediction():
    spDB = sqlite3.connect("C:/code/Git/stockCode/public/sp500Data.db")

    sp500 = getDailyStock().iloc[-2000:].copy()

    prediction = [stockPredict.predict(sp500), pd.Timestamp.today().strftime('%Y-%m-%d %H:%M:%S')]

    print(prediction)

    prediction = pd.DataFrame(prediction).T  # Transpose the DataFrame

    # Check if the table exists
    cursor = spDB.cursor()
    table_exists = cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='stock_pred_table'").fetchone()

    if table_exists:
        # If the table exists, append the data
        prediction.to_sql('stock_pred_table', spDB, if_exists='append', index=False)
    else:
        # If the table does not exist, create it
        prediction.to_sql('stock_pred_table', spDB, if_exists='fail', index=False)

    spDB.close()

sendDailyPrediction()


