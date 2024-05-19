# Purpose: This script is used to run the daily jobs that need to be run for the stock prediction model.
import dataInteract
import newsScraper

scrape = input("Scrape the news? (y or n): ")
sendPrediction = input("Would you like to send the daily prediction to the db? (y or n): ")
#Scrape the news
if(scrape == 'y'):
    newsScraper.scrapeAll()
#Send the daily stock data to heroku postgres db
#Send the daily prediction to heroku postgres db
if(sendPrediction == 'y'):
    dataInteract.sendDailyPrediction()
    dataInteract.sendPredPrice()