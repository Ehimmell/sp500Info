import React from 'react';
import './css/index.css';
import {getSpecificStockInfo} from "../api.js";

import squidward from '../pictures/Squidward_Tentacles_(fair_use).svg.png';

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

    const handleSearch = () => {
        const response = getSpecificStockInfo(document.getElementById("ticker").value);
    }

    return (
        <div>
            <div className={"bio-container"}>
                <input className = {"pred-rounded-button"} type="text" id="ticker" placeholder="Enter a valid stock ticker"/>
                <button className = {"pred-rounded-button"} onClick={handleSearch}>Search</button>
            </div>
            <Dashboard results={"poo"} priceGraph={squidward}/>
        </div>
    )
}

export function Dashboard({results, priceGraph}) {
    if(results === undefined)
        return (<div></div>);
    if(priceGraph === undefined) return (
        <div className = {"bio-container"}>
            <p>test</p>
        </div>
    )
    return (
        <div className = {"bio-container"}>
            <img src = {priceGraph} alt = "Stock Price Graph" className = "stretched-graph"/>
            <div className={"dashboard"}>
                <div>
                    <p>peepee</p>
                    <p>penis</p>
                </div>
                <div>
                    <p>poopoo</p>
                    <p>butt</p>
                </div>
            </div>
        </div>
    )
}