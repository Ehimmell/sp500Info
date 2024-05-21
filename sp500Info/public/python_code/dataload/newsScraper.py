# Description: Scrapes the Wall Street Journal for headlines and writes them to a csv file

#Imports
from bs4 import BeautifulSoup as bs
import requests as rq
import csv
import datetime
from stock.sp500Info.public.python_code.dataload import dataPrep
from stock.sp500Info.public.python_code import constants

#Method to scrape the wsj for headlines
def scrapeWSJ():

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

        #clean

        return articles


def scrapeCNNBiz():
    #get the response from the wsj
    response = rq.get(constants.CNN_URL, headers=constants.REQ_HEADERS)


    #if the response is good, parse the response and get the headlines
    if response.status_code == 200:

        #parse the response
        clean = bs(response.text, 'lxml')

        #initilize empty articles array for later
        articles = []

        for item in clean.select(f'span.{constants.HEADLINE_TEXT}'):
            headline = item.get_text()
            articles += [headline]


        return articles

def scrapeYahooFinance():

    response = rq.get(constants.YFINANCE_URL, headers=constants.REQ_HEADERS)

    if response.status_code == 200:

        clean = bs(response.text, 'lxml')

        articles = []

        for item in clean.select(f'h3.{constants.CLAMP}'):
            headline = item.get_text()
            articles += [headline]

        return articles

def scrapeAll():

    wsj = scrapeWSJ()
    cnn = scrapeCNNBiz()
    yahoo = scrapeYahooFinance()

    return wsj + cnn + yahoo
