
import dataInteract
import newsScraper

newsScraper.scrape()
dataInteract.sendDailyStock()
dataInteract.sendDailyPrediction()