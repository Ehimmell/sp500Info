# Description: Scrapes the Wall Street Journal for headlines and writes them to a csv file

#Imports
from bs4 import BeautifulSoup as bs
import requests as rq
import csv
import datetime
import dataPrep
import constants

#Method to scrape the wsj for headlines
def scrape():

    #get the response from the wsj
    response = rq.get(constants.WSJ_URL, headers=constants.REQ_HEADERS)


    #if the response is good, parse the response and get the headlines
    if response.status_code == 200:

        #parse the response
        clean = bs(response.text, 'lxml')

        #initilize empty articles array for later
        articles = []

        #get the headlines
        for item in clean.select(constants.HEADLINE):
            headline = item.select_one("h2, h3").get_text()

            articles += [headline]

        #get the bullet points
        for item in clean.select(constants.BULLET):
            headline = item.select_one("h4").get_text()

            articles += [headline]

        #get the existing articles
        with open(constants.HEADLINES_PATH, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            existing_articles = list(reader)

        #flatten the existing articles
        existing_articles = [item for sublist in existing_articles for item in sublist]

        #clean the articles by checking if an article that was scraped is already in the existing articles
        for article in articles:
            if article not in existing_articles:
                existing_articles.append(article)
        #clean the articles
        existing_articles = dataPrep.clean(existing_articles)

        #write the cleaned articles to the csv file
        with open(constants.HEADLINES_PATH, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for article in existing_articles:
                writer.writerow([article])
            writer.writerow(["    "])

        #write the runtime to the csv file
        with open(constants.RUNTIMES_PATH, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            now = datetime.datetime.now()
            writer.writerow([now.strftime("%Y-%m-%d %H:%M:%S")])
            writer.writerow(["size: " + str(len(existing_articles))])