import requests as rq
from bs4 import BeautifulSoup as bs
import pickle as p
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

with open('newsModel.pkl', 'rb') as file:

        loaded_model = p.load(file)

with open('newsVectorizer.pkl', 'rb') as file:

    v = p.load(file)


req_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language' : 'en-US,en;q=0.5',
    'Accept-Encoding' : 'gzip',
    'DNT' : '1', # Do Not Track Request Header
    'Connection' : 'close'}

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

    fit = v.transform(articles)

    preds = loaded_model.predict(fit)

    preds = preds[preds != 'NA']

    length = len(preds)

    total = 0;

    for pred in preds:

        if(pred == 'Good'): total += 1

    if(total / length >= 0.5): print("Good News!")

    else: print("Bad News!")


