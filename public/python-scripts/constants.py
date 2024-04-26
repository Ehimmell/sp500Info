STOCKPRED_BUY = 1
STOCKPRED_SELL = 0

STOCK_MODEL_PATH = '/Users/himme/Downloads/git/stock/sp500Info/public/updatedSPModel.pkl'

DBPATH = "/Users/himme/Downloads/git/stock/sp500Info/public/500Data.sqlite3"
SP500_TABLE = "sp500_table"
STOCKPRED_TABLE = "stock_pred_table"

HEADLINES_PATH = "/Users/himme/Downloads/git/stock/sp500Info/public/headLines.csv"
RUNTIMES_PATH = "/Users/himme/Downloads/git/stock/sp500Info/public/runtimes.csv"

BUY_THRESH = 0.57

ROLLING_HORIZONS = [2,5,60,250,1000]

KEYSTOCKS_TICKERS = ['AAPL', 'MSFT', 'JNJ', 'AMZN', 'GOOGL', 'BRK-A']
SP500_TICKER = "^GSPC"

REQ_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip',
    'DNT': '1',
    'Connection': 'close'
}

WSJ_URL = 'https://www.wsj.com'
HEADLINE = '.WSJTheme--headline--7VCzo7Ay'
BULLET = '.WSJTheme--bullet-item--5c1Mqfdr'

PREDICTORS = ['Close_Ratio_2', 'Trend_2', 'Close_Ratio_5', 'Trend_5',
         'Close_Ratio_60', 'Trend_60', 'Close_Ratio_250', 'Trend_250',
         'Close_Ratio_1000', 'Trend_1000', 'Trend_Key_Change_2',
         'Trend_Key_Change_5', 'Trend_Key_Change_60', 'Trend_Key_Change_250',
         'Trend_Key_Change_1000']



