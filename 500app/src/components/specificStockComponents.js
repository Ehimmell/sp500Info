import React from 'react';
import './css/common.css';
import './css/bio.css';
import './css/preds.css';
import './css/help.css';

export function SpecificDescription() {
    return (
        <div className="bio-pitch">
            <h1 className="h1-bio">
                Specific Stock
            </h1>
            <p className="simple-bottom-space">
                <strong>Info on specific stocks:</strong> Uses consolidated features to provide a comprehensive analysis of a specific stock.
            </p>
        </div>
    )
}

export function SpecificStockComponents() {
    const [ticker, setTicker] = React.useState('');

    const handleTickerChange = () => {
        setTicker(document.getElementById("ticker").value);
    }

    const handleSearch = () => {

    }

    return (
        <div className={"bio-container"}>
            <input className = {"pred-rounded-button"} type="text" id="ticker" placeholder="Enter a stock's ticker" onChange={handleTickerChange}/>
            <button className = {"pred-rounded-button"} onClick={handleTickerChange}>Search</button>
        </div>
    )
}