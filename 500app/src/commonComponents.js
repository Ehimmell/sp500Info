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
        <a className="sticky-option" href="about.html">About</a>
        <h3 className="sticky-option">Help</h3>
        <h3 className="sticky-option">Support Us</h3>
    </div>
    );
}