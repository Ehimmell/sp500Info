# Purpose: This script is used to run the daily jobs that need to be run for the stock prediction model.
import dataInteract
import newsScraper

#Scrape the news
newsScraper.scrape()
#Send the daily stock data to heroku postgres db
#dataInteract.sendDailyStock()
#Send the daily prediction to heroku postgres db
#dataInteract.sendDailyPrediction()