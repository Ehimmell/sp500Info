import React, {useState, useEffect} from 'react';
import './css/index.css';
import {getDailyPrediction, getTrendGraph, getStat, getDailyPrice} from '../api.js';
import logo from '../pictures/logo.png';

export function StickyHeader({onButtonClick}) {
    const [clickedButton, setClickedButton] = useState(null)
    const handleClick = (buttonId) => {
        setClickedButton(buttonId);
        onButtonClick(buttonId);
    }

    return (
        <div className="sticky-top">
            <img className="logo-header" src={logo} alt="500Info Logo" onClick={() => window.scrollTo(0, 0)}/>
            <div>
                <button className={`menu-button ${clickedButton === 'home' ? 'clicked' : ''}`}
                        onClick={() => handleClick('home')}>info<strong>S&P</strong>
                </button>
                <p className="title-add">Top Stock Metrics, <strong>Made Simple.</strong></p>
            </div>
            <button className={`menu-button ${clickedButton === 'predict' ? 'clicked' : ''}`}
                    onClick={() => handleClick('predict')}>Predict
            </button>
            <button className={`menu-button ${clickedButton === 'analyze' ? 'clicked' : ''}`}
                    onClick={() => handleClick('analyze')}>Analyze
            </button>
            <button className={`menu-button ${clickedButton === 'about' ? 'clicked' : ''}`}
                    onClick={() => handleClick('about')}>About
            </button>
            <button className={`menu-button ${clickedButton === 'help' ? 'clicked' : ''}`}
                    onClick={() => handleClick('help')}>Help
            </button>
            <button className={`menu-button ${clickedButton === 'support' ? 'clicked' : ''}`}
                    onClick={() => handleClick('support')}>Support Us
            </button>
            <button className={`menu-button ${clickedButton === 'spec' ? 'clicked' : ''}`}
                    onClick={() => handleClick('spec')}>Specific Stock
            </button>
        </div>
    );
}

//     About page components


