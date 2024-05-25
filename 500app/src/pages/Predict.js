import {PredictBio, TodayPrediction} from "../components/predictComponents.js";
import React from "react";
import '../components/css/index.css';
function Predict() {
    return (
        <div>
            <PredictBio />
            <TodayPrediction />
        </div>
    );
}

export default Predict;