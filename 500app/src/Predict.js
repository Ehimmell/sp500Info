import {PredictBio, TodayPrediction} from "./commonComponents.js";
import {React, useState} from "react";
import './index.css';
function Predict() {
    return (
        <div>
            <PredictBio />
            <TodayPrediction />
        </div>
    );
}

export default Predict;