from bs4 import BeautifulSoup as bs
import requests as rq
import csv
import datetime
import dataPrep
import constants


def scrape():
    response = rq.get(constants.WSJ_URL, headers=constants.REQ_HEADERS)

    if response.status_code == 200:

        clean = bs(response.text, 'lxml')

        articles = []

        for item in clean.select(constants.HEADLINE):
            headline = item.select_one("h2, h3").get_text()

            articles += [headline]

        for item in clean.select(constants.BULLET
            headline = item.select_one("h4").get_text()

            articles += [headline]

        with open(constants.HEADLINES_PATH, 'r') as file:
            reader = csv.reader(file)
            existing_articles = list(reader)

        existing_articles = [item for sublist in existing_articles for item in sublist]

        for article in articles:
            if article not in existing_articles:
                existing_articles.append(article)
        existing_articles = dataPrep.clean(existing_articles)

        with open(constants.HEADLINES_PATH, 'w', newline='') as file:
            writer = csv.writer(file)
            for article in existing_articles:
                writer.writerow([article])
            writer.writerow(["    "])

        with open(constants.RUNTIMES_PATH, 'a', newline='') as file:
            writer = csv.writer(file)
            now = datetime.datetime.now()
            writer.writerow([now.strftime("%Y-%m-%d %H:%M:%S")])
            writer.writerow(["size: " + str(len(existing_articles))])
