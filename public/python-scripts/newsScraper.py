from bs4 import BeautifulSoup as bs
import requests as rq
import csv
import datetime
import dataPrep


def scrape():


    req_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip',
        'DNT': '1',
        'Connection': 'close'}
    response = rq.get('https://www.wsj.com', headers=req_headers)

    if response.status_code == 200:

        clean = bs(response.text, 'lxml')

        articles = []

        for item in clean.select('.WSJTheme--headline--7VCzo7Ay'):
            headline = item.select_one("h2, h3").get_text()

            articles += [headline]

        for item in clean.select('.WSJTheme--bullet-item--5c1Mqfdr'):
            headline = item.select_one("h4").get_text()

            articles += [headline]

        with open('../headLines.csv', 'r') as file:
            reader = csv.reader(file)
            existing_articles = list(reader)

        existing_articles = [item for sublist in existing_articles for item in sublist]

        for article in articles:
            if article not in existing_articles:
                existing_articles.append(article)
        existing_articles = dataPrep.clean(existing_articles)

        with open('../headLines.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for article in existing_articles:
                writer.writerow([article])
            writer.writerow(["    "])

        with open('../runTimes.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            now = datetime.datetime.now()
            writer.writerow([now.strftime("%Y-%m-%d %H:%M:%S")])
            writer.writerow(["size: " + str(len(existing_articles))])
