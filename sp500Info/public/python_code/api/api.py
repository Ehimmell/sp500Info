from flask import Flask, request, jsonify
from stock.sp500Info.public.python_code.dataload import dataInteract as di
from flask_cors import CORS
from stock.sp500Info.public.python_code.dataload import statMaker
from stock.sp500Info.public.python_code.dataload import dataPrep as dp
from stock.sp500Info.public.python_code.predictions import stockPredict as sp
import pandas as pd
from dotenv import load_dotenv
import os
import requests


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST", "PUT", "DELETE"], "allow_headers": "*"}})

@app.route('/api/daily-prediction', methods=['GET'])
def get_prediction():
    inputDate = request.args.get('date', default=pd.Timestamp.today().normalize(), type=str)
    prediction = di.getDailyPrediction(inputDate)
    return jsonify(prediction)

@app.route('/api/daily-stock', methods=['GET'])
def get_price_graph():
    time_frame = request.args.get('timeFrame', default=5, type=int)
    graph_type = request.args.get('type', default='price', type=str)
    return jsonify(statMaker.getGraph(time_frame, graph_type))

@app.route('/api/daily-stats', methods=['GET'])
def get_stats():
    time_frame = request.args.get('timeFrame', default=5, type=int)
    stat_type = request.args.get('type', default='mean', type=str)
    stat = statMaker.getStat(time_frame, stat_type)
    return jsonify(stat.tolist())

@app.route('/api/daily-price', methods=['GET'])
def get_price():
    price, pred = di.getPredPrice()
    return jsonify(price)

@app.route('/api/daily-news', methods=['GET'])
def get_news():
    inputDate = request.args.get('date', default=pd.Timestamp.today().normalize(), type=str)
    price = di.getPredPrice(inputDate)
    return jsonify(price)

@app.route('/api/search', methods=['GET'])
def search():
    ticker = request.args.get('query', default='AAPL', type=str)
    load_dotenv()
    api_key = os.getenv('API_KEY')
    engine_id = os.getenv('ENGINE_ID')
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': api_key,
        'cx': engine_id,
        'q': 'stock symbol for ' + ticker
    }
    response = requests.get(url, params=params)
    response_json = response.json()
    items = response_json.get('items', [])  # Get 'items' if it exists, otherwise return an empty list
    print(items)
    return jsonify(items)

@app.route('/api/specific-stock-info', methods=['GET'])
def searchSpecStock():
    ## still in progress
    ticker = request.args.get('ticker', default='AAPL', type=str)
    print(ticker)
    stock = dp.prepareSpecData(ticker)
    consolidatedPred = sp.consolidatedPred(stock)
    pred = sp.predict(stock)
    predPrice = sp.pricePredict(stock)
    currPrice = stock['Close'].iloc[-1]
    toReturn = [float(consolidatedPred), float(predPrice[0]), float(currPrice), float(pred)]
    return jsonify(toReturn)

##needs work
@app.route('/api/spec-graph', methods=['GET'])
def getSpecGraph():
    ticker = request.args.get('ticker', default='AAPL', type=str)
    graph = statMaker.prepSpecialGraph(ticker)
    return jsonify(graph)


if __name__ == '__main__':
    app.run(debug=True)