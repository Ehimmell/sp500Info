import React from 'react';
import './index.css';
import ReactDOM from 'react-dom/client';

export function StickyHeader() {
    return (
    <div className="sticky-top">
        <img className="logo-header" src="./logo.png" alt="500Info Logo" onclick="window.scrollTo(0, 0)"/>
        <div>
            <h3 className="title">500<strong><em>Info</em></strong></h3>
            <p className="title-add">Top Stock Metrics, <strong>Made Simple.</strong></p>
        </div>
        <h3 className="sticky-option">Predict</h3>
        <h3 className="sticky-option">Analyze</h3>
        <h3 className="sticky-option">About</h3>
        <h3 className="sticky-option">Help</h3>
        <h3 className="sticky-option">Support Us</h3>
    </div>
    );
}

export function Features() {

    return (<div className="function">
        <img src="News.jpg" alt="News" width="300" height="200"/>
        <div className="function-description">
            <h3 className="desc-top">News Intelligence</h3>
            <p className="desc-bottom">Assessments of the sway of stock market news</p>
            <p className="desc-bottom"><strong>Try</strong></p>
        </div>
        <img src="download.jpg" alt="Predict" width="300" height="200"/>
        <div className="function-description">
            <h3 className="desc-top">S&P 500 Predictions</h3>
            <p className="desc-bottom">Predictive analysis of stock market trends</p>
            <p className="desc-bottom"><strong>Try</strong></p>
        </div>
        <img src="download.png" alt="Analyze" width="300" height="200"/>
        <div className="function-description">
            <h3 className="desc-top">Stock Analysis</h3>
            <p className="desc-bottom">In-depth analysis of stock market data, including statistics and graphs</p>
            <p className="desc-bottom"><strong>Try</strong></p>
        </div>
    </div>
    );
}

export function Brief() {
    return (
        <div class="desc-brief">
            <div class="brief-header">
                <h1> A Brief Description</h1>
            </div>
            <div class="brief-content">
                <p>
                    500Info streamlines stock market decision-making with robust tools and a user-friendly interface. It
                    offers news updates,
                    predictive analysis, and thorough data examination to assist users at every level of experience.
                </p>
            </div>
        </div>
    );
}