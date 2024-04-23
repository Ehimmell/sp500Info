import pandas as pd
import sqlite3
import dataPrep
import stockPredict
import constants

def sendDailyStock():
    spDB = sqlite3.connect(constants.DB_PATH)

    sp500 = dataPrep.prepare500Data()

    sp500.to_sql(constants.SP500_TABLE, spDB, if_exists='replace')

    spDB.close()

def getDailyStock():
    spDB = sqlite3.connect(constants.DB_PATH)

    sp500 = pd.read_sql_query("SELECT * FROM sp500_table", spDB)

    spDB.close()

    return sp500

def sendDailyPrediction():
    spDB = sqlite3.connect(constants.DB_PATH)

    sp500 = getDailyStock().iloc[-2000:].copy()

    prediction = stockPredict.predict(sp500)

    print(prediction)

    toInsert = [prediction[constants.STOCKPRED_SELL],prediction[constants.STOCKPRED_BUY],pd.Timestamp.today().strftime('%Y-%m-%d')]

    toInsert = pd.DataFrame([toInsert])

    # Check if the table exists
    cursor = spDB.cursor()
    table_exists = cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{constants.STOCKPRED_TABLE}'").fetchone()

    if table_exists:
        # If the table exists, append the data
        toInsert.to_sql(constants.STOCKPRED_TABLE, spDB, if_exists='append', index=False)
    else:
        # If the table does not exist, create it
        toInsert.to_sql(constants.STOCKPRED_TABLE, spDB, if_exists='fail', index=False)

    spDB.close()

sendDailyPrediction()


