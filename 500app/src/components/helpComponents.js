import React, {useState} from "react";
import "../index.css";
import graph1 from "../pictures/GraphGuide/GraphFirstStep.png"
import graph2 from "../pictures/GraphGuide/GraphSecondStep.png"
import graph3 from "../pictures/GraphGuide/GraphThirdStep.png"

import stock1 from "../pictures/StockGuide/StockFirstStep.png"
import stock2 from "../pictures/StockGuide/StockSecondStep.png"

import news1 from "../pictures/NewsGuide/NewsFirstStep.png"
import news2 from "../pictures/NewsGuide/NewsSecondStep.png"



export function HelpBio() {
    const [tutorial, setTutorial] = useState("analyze");
    const handleTutorialChange = () => {
        if (tutorial === "analyze") {
            setTutorial("predict");
        } else {
            setTutorial("analyze");
        }
    }
    return (
        <div>
            <div className="bio-pitch">
                <h1 className="h1-bio">
                    Help
                </h1>
                <p className={"p-bio"}>
                    Need help with the app? here are some common tutorials to help you get started.
                </p>
            </div>
            <div className="bio-container">
                <div className={"bio-content"}>
                    <select className={"select-help"} onChange={handleTutorialChange}>
                        <option value={"analyze"}>Analyze</option>
                        <option value={"predict"}>Predict</option>
                    </select>
                    <ConsolidatedTutorial tutorial={tutorial}/>
                </div>
            </div>
        </div>
    );
}

export function HelpAnalyze() {
    return (
        <div className={"analyze-explain"}>
            <h1 className={"help-header"}>
                Analyze
            </h1>
            <p className={"p-analyze"}>
                Analyze generates easily interpretable stock market data. Each mode takes in certain specifications to
                allow for a highly customizable experience. Here's how to use it:
            </p>
            <p className={"p-analyze"}>
                First, select the mode you'd like to use. Both are similar in terms of use, but tutorials for both are
                included here.
            </p>
            <h2 className={"help-header"}>
                Graph
            </h2>
            <img src={graph1} alt="Graph Guide 1" className="help-pic"/>
            <p className={"p-analyze"}>
                First, select the type of graph you'd like to create. You can choose from a price graph, price ratio
                graph, trend graph, and close over open graph.
            </p>
            <img src={graph2} alt="Graph Guide 2" className="help-pic"/>
            <p className={"p-analyze"}>
                Next, input the time frame you'd like to view. This will determine the length of time the graph will
                display.
            </p>
            <img src={graph3} alt="Graph Guide 3" className="help-pic"/>
            <p className={"p-analyze"}>
                Finally, click the "Get Data" button to generate the graph.
            </p>
        </div>
    )
}

export function HelpPredict() {
    return (
        <div className={"analyze-explain"}>
            <h1 className={"help-header"}>
                Predict
            </h1>
            <p className={"p-analyze"}>
                Predict is infoS&P's artificial intelligence tool that predicts the future of the stock market. Here's a
                quick rundown of how to use it:
            </p>
            <h2 className={"help-header"}>
                Predict Price
            </h2>
            <div className={"optional-help"}>
                <h3 className={"help-header"}>
                    <em>Optional: </em> Get a Prediction for a Specific Date
                </h3>
                <p className={"p-analyze"}>
                    Getting a prediction for a specific date is similar to getting today's prediction, but with one
                    extra step. Instead of just clicking the "Get Prediction" button, you'll need to input the date
                    you'd like to predict in the input box. The date should be in the format "YYYY-MM-DD".
                </p>
                <img className={"help-pic"} src={stock2} alt="Stock Guide 2"/>
            </div>
            <p>
                If you don't want to predict a specific date, you can just click the "Get Prediction" button to get the
                predicted price for tomorrow, and whether the price is higher or lower than today's price.
            </p>
            <img className={"help-pic"} src={stock1} alt="Stock Guide 1"/>
            <h2 className={"help-header"}>News Classification</h2>
            <p>
                News classification is a tool that uses an artificial intelligence to classify today's stock news as
                good or bad. It works like this:
            </p>
            <div className = "optional-help">
                <h3 className={"help-header"}>
                    <em>Optional: </em> Get a Prediction for a Specific Date
                </h3>
                <p className={"p-analyze"}>
                    Getting a prediction for a specific date is similar to getting today's prediction, but with one
                    extra step. Instead of just clicking the "Get Prediction" button, you'll need to input the date
                    you'd like to predict in the input box. The date should be in the format "YYYY-MM-DD".
                </p>
                <img src={news2} alt="News Guide 2" className="help-pic"/>
            </div>
            <p>
                If you don't want to predict a specific date, you can just click the "Get Prediction" button to get the
                predicted price for tomorrow, and whether the price is higher or lower than today's price.
            </p>
            <img src={news1} alt="News Guide 1" className="help-pic"/>=
        </div>
    )
}

export function ConsolidatedTutorial({tutorial}) {
    if (tutorial === "analyze") {
        return (
            <HelpAnalyze/>
        )
    } else {
        return (
            <HelpPredict/>
        )
    }
}