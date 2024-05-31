import './css/index.css';
import {getSpecificStockInfo, getSpecialGraph} from '../api.js';
import React, {useState} from "react";

export function SpecificDescription() {
    return (
        <div className="bio-pitch">
            <h1 className="h1-bio">
                Specific Stock
            </h1>
            <p className="simple-bottom-space">
            </p>
        </div>
    )
}

export function SpecificStockComponents() {

    const [direction, setDirection] = useState('');
    const [lPredPrice, setLPredPrice] = useState('');
    const [sPredPrice, setSPredPrice] = useState('');
    const [price, setPrice] = useState('');
    const [graph, setGraph] = useState('none');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const handle = async () => {
        setLoading(true);
        setError(null);
        try {
            await handleSearch();
            await handleGraph();
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    }

    const handleSearch = async () => {
        const response = await getSpecificStockInfo(document.getElementById("ticker").value);
        if (response[0] > 0) setDirection("Up");
        if(response[0] < 0) setDirection("Down");
        setLPredPrice(parseFloat(response[1]).toFixed(2));
        setSPredPrice(parseFloat(response[3]).toFixed(2));
        setPrice(parseFloat(response[2]).toFixed(2));
    }

    const handleGraph = async () => {
        const response = await getSpecialGraph(document.getElementById("ticker").value);
        setGraph(`data:image/png;base64,${response}`)
    }
    if(price === '') {
        return (
            <div>
                <div className={"bio-container"}>
                    <input className={"feedback-element"} type="text" id="ticker"
                           placeholder="Enter a valid stock ticker"/>
                    <button className={"pred-rounded-button"} onClick={handle}>Search</button>
                </div>
            </div>
        )
    }
    return (
        <div>
            {loading ? (
                <div>Loading...</div>
            ) : error ? (
                <div>Error: {error}</div>
            ) : (
                <div>
                    <div className={"bio-container"}>
                        <input className={"feedback-element"} type="text" id="ticker"
                               placeholder="Enter a valid stock ticker"/>
                        <button className={"pred-rounded-button"} onClick={handle}>Search</button>
                    </div>
                    <div className={"bio-container"}>
                        <img src={graph} alt="Stock Price Graph" className="stretched-graph"/>
                        <div className={"dashboard"}>
                            <div>
                                <p>Current Price:</p>
                                <p>{price}</p>
                            </div>
                            <div>
                                <p>Direction for Long Term:</p>
                                <p>{direction}</p>
                            </div>
                            <div>
                                <p>Long Term Predicted Price:</p>
                                <p>{lPredPrice}</p>
                            </div>
                            <div>
                                <p>Confidence Stock will Increase Tomorrow:</p>
                                <p>{sPredPrice}</p>
                            </div>
                        </div>
                    </div>
                </div>
            )}
        </div>
    )
}