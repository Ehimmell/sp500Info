#Class for inertacting with the database. This class will be used to send and recieve data from the database.

#Imports
import pandas as pd
import os
import stockPredict
import constants
from sqlalchemy import create_engine
import dataPrep
import newsPredict


#Method to connect to the database and return the engine
def connectDB():
    try:
        #replace path inconsistencies between local and heroku
        DATABASE_URL = os.getenv("DATABASE_URL").replace("postgres://", "postgresql://")

        #create the engine
        engine = create_engine(DATABASE_URL)

        #return the engine
        return engine
    except AttributeError:
        print("Could not establish a connection to the database", AttributeError)
        return None


#This method currently sends the last 20 years of stock market data to the DB every time it is called. Because the last 20 years before today is already on there.
#My initial thought would be to add a parameter for the amount of data to prep, but this would conflict with rolling average computation. Maybe add code
#to call the data from the db, recomputate the rolling average with today + whatever that returns, and then send that to the db.
#This method sends the daily prediction to the db
def sendDailyPrediction():
    try:

        #get the engine to connect to the db
        engine = connectDB()

        #get the last 20 years of stock data
        sp500 = dataPrep.prepare500Data()

        #get the last 2000 days of stock data
        sp500 = sp500.iloc[-2000:].copy()

        #get the prediction
        prediction = stockPredict.predict(sp500)

        #preapre insert- the buy proba, sell proba, and date in unix timestamp format with no time
        toInsert = [prediction[constants.STOCKPRED_SELL], prediction[constants.STOCKPRED_BUY],
                    pd.Timestamp.today().normalize().timestamp()]

        #convert to a dataframe
        toInsert = pd.DataFrame([toInsert], columns=['Sell', 'Buy', 'Date'])

        #send the data to the db
        toInsert.to_sql(constants.STOCKPRED_TABLE, engine, if_exists='append', index=False)

        #close the connection
        engine.dispose()

    except (AttributeError, TypeError):
        print("Could not establish a connection to the database", AttributeError, TypeError)

    #will need to make this method work for every date there is a prediction for


#This method gets the daily prediction from the db
def getDailyPrediction():

    try:
    #get the date with no time in unix timestamp format
        today = pd.Timestamp.today().normalize().timestamp()

        #get the engine to connect to the db
        engine = connectDB()

        #get the prediction for today by date index
        prediction = pd.read_sql_query(f"SELECT * FROM {constants.STOCKPRED_TABLE} WHERE \"Date\" = {today}", engine)

        #close the connection
        engine.dispose()

        #return the prediction's buy proba
        return prediction['Buy'].values[0]

    except (AttributeError, TypeError):
        print("Could not establish a connection to the database", AttributeError, TypeError)
        return None


def sendPredPrice():

    try:
        engine = connectDB()

        sp500 = dataPrep.prepare500Data()

        sp500 = sp500.iloc[-2000:].copy()

        price, prediction = stockPredict.pricePredict(sp500)

        price = price.item()

        toInsert = [price, prediction, pd.Timestamp.today().normalize().timestamp()]

        toInsert = pd.DataFrame([toInsert], columns=['Price', 'Prediction', 'Date'])

        toInsert.to_sql(constants.STOCKPRICE_TABLE, engine, if_exists='append', index=False)

        engine.dispose()

    except (AttributeError, TypeError):
        print("Could not establish a connection to the database", AttributeError, TypeError)


def getPredPrice():
    try:
        today = pd.Timestamp.today().normalize().timestamp()

        engine = connectDB()

        price = pd.read_sql_query(f"SELECT * FROM {constants.STOCKPRICE_TABLE} WHERE \"Date\" = {today}", engine)

        engine.dispose()

        return price['Price'].values[0], price['Prediction'].values[0]

    except (AttributeError, TypeError):
        print("Could not establish a connection to the database", AttributeError, TypeError)
        return None, None


def sendNewsClass():
    try:
        newsClass = newsPredict.getNewsPred()

        engine = connectDB()

        toInsert = [newsClass, pd.Timestamp.today().normalize().timestamp()]

        toInsert = pd.DataFrame([toInsert], columns=['Class', 'Date'])

        toInsert.to_sql(constants.NEWS_TABLE, engine, if_exists='append', index=False)

        engine.dispose()

    except (AttributeError, TypeError):
        print("Could not establish a connection to the database", AttributeError, TypeError)


def getNewsClass():
    try:
        today = pd.Timestamp.today().normalize().timestamp()

        engine = connectDB()

        newsClass = pd.read_sql_query(f"SELECT * FROM {constants.NEWS_TABLE} WHERE \"Date\" = {today}", engine)

        engine.dispose()

        return newsClass['Class'].values[0]

    except (AttributeError, TypeError):
        print("Could not establish a connection to the database", AttributeError, TypeError)
        return None
