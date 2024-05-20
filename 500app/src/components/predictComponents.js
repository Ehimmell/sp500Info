import React, {useState} from "react";
import {getDailyPrediction, getDailyPrice} from "../api.js";

export function PredictBio() {
    return (
        <div className="bio-pitch">
            <h1 className="h1-bio">
                Predict
            </h1>
            <p>
                Uses a Machine Learning model to predict whether the S&P 500 will go up or down the next day.
            </p>
        </div>

    )
}

export function TodayPrediction() {

    const [prediction, setPrediction] = useState('');
    const [price, setPrice] = useState('');
    const handleClick = async () => {
        const prediction = await getDailyPrediction();
        const price = await getDailyPrice();
        setPrediction(prediction);
        setPrice(price.substring(0, price.indexOf('.') + 3));
    }

    let predNum = parseFloat(prediction);

    const predExplaination = () => {
        if (!prediction.equals('Error fetching prediction') && !prediction.equals('Error: Failed to fetch daily predictions') && !prediction.equals('')) {
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
                <button className="pred-rounded-button" onClick={handleClick}>Get Today's Prediction</button>
                <p className="pred">{price}</p>
                <p className="pred-explain">{predExplaination()}</p>
            </div>
        </div>
    )
}