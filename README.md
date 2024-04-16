
Welcome to the sp500Info repository, home of the simplest stock summary out there!

Here, the only two metrics are whether the stock market news is good or bad, and whether to buy and sell or not.
____________________________________________________________________________________________________________________

**Behind the Curtain-**

This repository is a project to summarize the S&P 500 using two simple metrics- whether to buy or sell, and whether the news surrounding the market is good or not.

**Stock Rise or Fall Predictions-**

To get Stock Market Data, Yahoo finance is used to retrieve data from the last ten years. Why ten years? Because in addition to metrics, users will have the option to create their own graphs or simple summaries using all the data retrieved, and ten years is more than enough data for anyone's graphing needs. To make predictions, two new metrics are created for every day in the stock market- the trend (going up or down a certain number of days), and the proportion of day x's closing price over the average closing price. This helps to indicate that a trend might end, or the price is so high it won't get much higher. This is then given to the model in order to make an accurate prediction of price change.

**Stock Model Acccuracy - <57%**

This model is correct about the rise and fall of stocks 64% of the time, meaning that money can be made off of it. However, it's not a guarantee, and is only slightly more likely to be right than wrong.

**News Analysis-**

Request is used to request the front page of the WSJ, which features the most relevant stock stories for the day. Each story is then classified as good for stock market, bad for stock market, or not about stock. The Not Abouts are removed, and then the code parses through each good or bad, adding 1 to a "tick variable" for every good news story it comes across. The tick variable, which at this point is equal to the number of good stories, is then divided by the total number to get the proportion of good stories. If the proportion is higher than 0.5, the code treats the news as having a positive outlook on the stock market.

**Model Accuaracy - <94%**

This model is trained by classifying fake news headlines as good, bad or not about stock, which is easier than going off of purely numerical data, like the stock model. For this reason, it's able to be a lot more accurate about the outlook of the news. Also, the large sample of stories (>50) makes the law of large of large numbers come into play, making the number of hallucinations (wrong predictions) in the sample closer to the average number overall. 
