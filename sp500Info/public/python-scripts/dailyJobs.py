# Purpose: This script is used to run the daily jobs that need to be run for the stock prediction model.
import dataInteract
import newsScraper

scrape = input("What news sources would you like to scrape? Seperate by comma. ex: <wsj, yfinance>(wsj, cnn, yfinance, or all): ")
sendStock = input("Would you like to send the daily stock data to the db? (y or n): ")
sendPrediction = input("Would you like to send the daily prediction to the db? (y or n): ")
#Scrape the news
while(len(scrape) > 2):
    nextComma = scrape.find(',')
    if(nextComma != -1): input = scrape[:nextComma]
    else: input = scrape

    if(input == 'wsj'):
        newsScraper.scrapeWSJ()
    elif(input == 'cnn'):
        newsScraper.scrapeCNNBiz()
    elif(input == 'yfinance'):
        newsScraper.scrapeYahooFinance()
    elif(input == 'all'):
        newsScraper.scrapeWSJ()
        newsScraper.scrapeCNNBiz()
        newsScraper.scrapeYahooFinance()
    else:
        print("Invalid input")
        break

    if(nextComma != -1) :scrape = scrape[nextComma+1:]
    else: scrape = ''
#Send the daily stock data to heroku postgres db
if(sendStock == 'y'):
    dataInteract.sendDailyStock()
#Send the daily prediction to heroku postgres db
if(sendPrediction == 'y'):
    dataInteract.sendDailyPrediction()