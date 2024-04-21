import pandas as pd
import sqlite3
import dataPrep

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

sendDailyStock()


