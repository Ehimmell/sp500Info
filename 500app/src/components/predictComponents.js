import React, {useState} from "react";
import {getDailyPrediction, getDailyPrice, getDailyNews} from "../api.js";

export function PredictBio() {
    return (
        <div className="bio-pitch">
            <h1 className="h1-bio">
                Predict
            </h1>
            <p className="simple-bottom-space">
                <strong>Stock Price prediction:</strong> Uses a Machine Learning model to predict whether the S&P 500 will go up or down the next day, as well as the forecasted points.
            </p>
            <p>
                <strong>News Classification: </strong> Uses a Machine Learning model to classify news articles about the stock market as positive, negative, or neutral.
            </p>
        </div>

    )
}

export function TodayPrediction() {

    const [prediction, setPrediction] = useState('');
    const [price, setPrice] = useState('');
    const [news, setNews] = useState('');
    const handlePredictionClick = async () => {
        const prediction = await getDailyPrediction();
        const price = await getDailyPrice();
        setPrediction(prediction);
        setPrice(price.substring(0, price.indexOf('.') + 3));
    }

    const handleNewsClick = async () => {
        const news = await getDailyNews();
        setNews(news);
    }



    let predNum = parseFloat(prediction);

    const predExplaination = () => {
        if (prediction !== 'Error fetching prediction' && prediction !== 'Error: Failed to fetch daily predictions' && prediction !== '') {
            if (predNum > 0.55) {
                return "The S&P 500 is likely to go up today.";
            } else if (predNum < 0.45) {
                return "The S&P 500 is likely to go down today.";
            } else {
                return "The S&P 500 is likely to stay the same today.";
            }
        } else {
            return "";
        }
    }
    return (
        <div>
            <h1 className="pred-header">Today's Stock Prediction</h1>
            <div className="daily-pred-container">
                <button className="pred-rounded-button" onClick={handlePredictionClick}>Get Today's Prediction</button>
                <p className="pred">{price}</p>
                <p className="pred-explain">{predExplaination()}</p>
            </div>
            <h1 className="pred-header">Today's News Classification</h1>
            <div className="daily-pred-container">
                <button className="pred-rounded-button" onClick={handleNewsClick}>Get Today's News Classification</button>
                <p className="pred">{news}</p>
            </div>
        </div>
    );
}