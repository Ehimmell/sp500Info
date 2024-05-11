import pandas as pd
import numpy as np
import pickle as p
import newsScraper as ns
import constants

model = p.load(open('../newsModel4.0.pkl', 'rb'))

tf = p.load(open('../vectorizers/newsTFVectorizer4.0.pkl', 'rb'))
sia = p.load(open('../vectorizers/newsSIA4.0.pkl', 'rb'))
good_vc = p.load(open('../vectorizers/newsGoodVectorizer4.0.pkl', 'rb'))
bad_vc = p.load(open('../vectorizers/newsBadVectorizer4.0.pkl', 'rb'))
neutral_vc = p.load(open('../vectorizers/newsNeutralVectorizer4.0.pkl', 'rb'))

news = ns.scrapeAll()

news = pd.DataFrame(news, columns=['Headlines'])

news_good = good_vc.transform(news['Headlines'])
news_bad = bad_vc.transform(news['Headlines'])
news_neutral = neutral_vc.transform(news['Headlines'])

news_tf = tf.transform(news['Headlines'])

news_sia = news['Headlines'].apply(lambda x: pd.Series(sia.polarity_scores(x)))

news = np.hstack([news_sia.apply(pd.Series).values, news_good.toarray(), news_bad.toarray(), news_neutral.toarray(), news_tf.toarray()])

preds = model.predict(news)
preds_proba = model.predict_proba(news)

sum = 0

news = ns.scrapeAll()

for pred, proba, headline in zip(preds, preds_proba, news):
    if(max(proba) < 0.5): continue
    print(pred, headline, max(proba))
    sum += pred * (pow(1/max(proba), 2))

print(sum)

