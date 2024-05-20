import React, {useState, useEffect} from 'react';
import '../index.css';
import ai from '../pictures/NNPrediction.png';
import price from '../pictures/stockPrice.png';
import news from '../pictures/news.png';
export function Features() {
    return (
        <div>
            <div className={"function"}>
                <img src={news} alt="News" className="function-image"/>
                <div className="function-description">
                    <h3 className="desc-top">News Intelligence</h3>
                    <p className="desc-bottom">Assessments of the sway of stock market news</p>
                    <p className="desc-bottom"><strong>Try</strong></p>
                </div>
            </div>
            <div className={"function"}>
                <img src={ai} alt="Predict" className="function-image"/>
                <div className="function-description">
                    <h3 className="desc-top">S&P 500 Predictions</h3>
                    <p className="desc-bottom">Predictive analysis of stock market trends</p>
                    <p className="desc-bottom"><strong>Try</strong></p>
                </div>
            </div>
            <div className={"function"}>
                <img src={price} alt="Analyze" className={"function-image"}/>
                <div className="function-description">
                    <h3 className="desc-top">Stock Analysis</h3>
                    <p className="desc-bottom">In-depth analysis of stock market data, including statistics and
                        graphs</p>
                    <p className="desc-bottom"><strong>Try</strong></p>
                </div>
            </div>
        </div>
    );
}
export function Brief() {
    return (
        <div className="desc-brief">
            <div className="brief-header">
                <h1> A Brief Description</h1>
            </div>
            <div className="brief-content">
                <p>
                    500Info streamlines stock market decision-making with robust tools and a user-friendly interface. It
                    offers news updates,
                    predictive analysis, and thorough data examination to assist users at every level of experience.
                </p>
            </div>
        </div>
    );
}
