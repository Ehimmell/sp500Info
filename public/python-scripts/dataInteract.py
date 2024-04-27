import pandas as pd
import sqlite3
import os
import dataPrep
import stockPredict
import constants
from sqlalchemy import create_engine

def connectDB():
    DATABASE_URL = os.getenv("DATABASE_URL").replace("postgres://", "postgresql://")

    engine = create_engine(DATABASE_URL)

    return engine

#This method currently sends the last 20 years of stock market data to the DB every time it is called. Because the last 20 years before today is already on there.
#My initial thought would be to add a parameter for the amount of data to prep, but this would conflict with rolling average computation. Maybe add code
#to call the data from the db, recomputate the rolling average with today + whatever that returns, and then send that to the db.
def sendDailyStock():
    engine = connectDB()

    sp500 = dataPrep.prepare500Data()

    sp500.to_sql(constants.SP500_TABLE, engine, if_exists='replace', index=False)

    engine.dispose()


def getDailyStock():
    engine = connectDB()

    sp500 = pd.read_sql_query(f"SELECT * FROM {constants.SP500_TABLE}", engine)

    engine.dispose()

    return sp500


def sendDailyPrediction():
    engine = connectDB()

    sp500 = getDailyStock()

    sp500=sp500.iloc[-2000:].copy()

    prediction = stockPredict.predict(sp500)

    toInsert = [prediction[constants.STOCKPRED_SELL], prediction[constants.STOCKPRED_BUY],
                pd.Timestamp.today().normalize().timestamp()]

    toInsert = pd.DataFrame([toInsert], columns=['Sell', 'Buy', 'Date'])

    toInsert.to_sql(constants.STOCKPRED_TABLE, engine, if_exists='append', index=False)

    engine.dispose()

#will need to make this method work for every date there is a prediction for
def getDailyPrediction():
    today = pd.Timestamp.today().normalize().timestamp()

    engine = connectDB()

    prediction = pd.read_sql_query(f"SELECT * FROM {constants.STOCKPRED_TABLE} WHERE \"Date\" = {today}", engine)

    engine.dispose()

    return prediction['Buy'].values[0]
