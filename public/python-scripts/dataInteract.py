import pandas as pd
import sqlite3
import dataPrep
import stockPredict
import constants

def sendDailyStock():
    spDB = sqlite3.connect(constants.DBPATH)

    sp500 = dataPrep.prepare500Data()

    sp500.to_sql(constants.SP500_TABLE, spDB, if_exists='replace')

    spDB.close()

def getDailyStock():
    spDB = sqlite3.connect(constants.DBPATH)

    sp500 = pd.read_sql_query("SELECT * FROM sp500_table", spDB)

    spDB.close()

    return sp500

def sendDailyPrediction():
    spDB = sqlite3.connect(constants.DBPATH)

    sp500 = getDailyStock().iloc[-2000:].copy()

    prediction = stockPredict.predict(sp500)

    print(prediction)

    toInsert = [prediction[constants.STOCKPRED_SELL],prediction[constants.STOCKPRED_BUY],pd.Timestamp.today().strftime('%Y-%m-%d')]

    toInsert = pd.DataFrame([toInsert], columns=['Sell','Buy','Date'])

    # Convert the 'Date' column to Unix timestamps
    toInsert['Date'] = toInsert['Date'].apply(lambda x: pd.to_datetime(x).timestamp())

    # Check if the table exists
    cursor = spDB.cursor()
    cursor.execute("BEGIN TRANSACTION;")
    table_exists = cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{constants.STOCKPRED_TABLE}'").fetchone()

    if table_exists:
        # If the table exists, append the data
        toInsert.to_sql(constants.STOCKPRED_TABLE, spDB, if_exists='append', index=False)
    else:
        # If the table does not exist, create it
        toInsert.to_sql(constants.STOCKPRED_TABLE, spDB, if_exists='fail', index=False)

    spDB.close()

def getDailyPrediction():

    today = pd.Timestamp.today().strptime('%Y-%m-%d')

    spDB = sqlite3.connect(constants.DBPATH)

    prediction = pd.read_sql_query(f"SELECT * FROM {constants.STOCKPRED_TABLE} WHERE Date = {today}", spDB)

    print(prediction)

    spDB.close()

    return prediction['Buy'].values[0]


