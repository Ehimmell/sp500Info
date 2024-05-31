import React, {useEffect, useState} from "react";
import {getStat, getTrendGraph} from "../api.js";
import './css/index.css';

export function AnalyzeExplain() {
    const [analyzeMode, setAnalyzeMode] = useState('graph');
    const [graphSource, setGraphSource] = useState(null);
    const [graphType, setGraphType] = useState('price');
    const [statType, setStatType] = useState('mean');
    const [statData, setStatData] = useState(null);

    const handleSelect = (e) => {
        setAnalyzeMode(e.target.value);
    }

    const handleTypeSelect = (e) => {
        setGraphType(e.target.value)
    }

    const handleStatTypeSelect = (e) => {
        setStatType(e.target.value);
    }


    const [timeFrame, setTimeFrame] = useState(5);
    const [statFrame, setStatFrame] = useState(5);

    const [apiTrigger, setApiTrigger] = useState(false);

    const handleTimeFrameChange = (e) => {
        setTimeFrame(e.target.value);
    }

    const handleStatFrameChange = (e) => {
        setStatFrame(e.target.value);
    }

    useEffect(() => {
        if(analyzeMode === 'graph') {
            const src = async () => {
                try {
                    const data = await getTrendGraph(timeFrame, graphType);
                    setGraphSource(`data:image/png;base64,${data}`);
                } catch (error) {
                    console.error('Error fetching graph dataload:', error);
                }
            }
            src();
        }
}, [apiTrigger]);

    useEffect(() => {
        if(analyzeMode === 'stat') {
            const statSrc = async () => {
                try {
                    const data = await getStat(statFrame, statType);
                    setStatData(data)
                } catch (error) {
                    console.error('Error fetching statistics:' + error);
                }
            }

            statSrc();
        }
    }, [apiTrigger]);

    const comp = () => {
        if (analyzeMode === 'graph') {
            return (
                <div>
                    <div className="graph-container">
                        <input className="analyze-input" value={timeFrame} onChange={handleTimeFrameChange} type="number"/>
                        <select className={"select-analyze"} onChange={handleTypeSelect}>
                            <option value={'price'}>Price Graph</option>
                            <option value={'price_ratio'}>Price Ratio Graph</option>
                            <option value={'trend'}>Trend Graph</option>
                            <option value={"close_over_open"}>Close Over Open Graph</option>
                        </select>
                    </div>
                    <div className={"graph-container"}>
                        {graphSource && <img src={graphSource} alt="Graph"/>}
                    </div>
                </div>
            )
        } else {
            return (
                <div>
                    <div className={"graph-container"}>
                        <input className = "analyze-input" value={statFrame} onChange={handleStatFrameChange} type="number"/>
                        <select className = {"select-analyze"} onChange={handleStatTypeSelect}>
                            <option value={'mean'}>Mean</option>
                            <option value={'median'}>Median</option>
                            <option value={'std'}>Standard Deviation</option>
                        </select>
                    </div>
                    <div className = "graph-container">
                        <p>{statData}</p>
                    </div>
                </div>
            );
        }
    }

    return (
        <div>
            <div className="bio-pitch">
                <h1 className="h1-bio">
                    Analyze
                </h1>
                <p>
                    Analyze is a tool that allows users to create their own graphs and statistics concerning the stock
                    market.
                </p>
                <p className="p-bio">
                    Here, you can create your own graphs and statistics concerning the stock market. It's a lot simpler
                    on
                    the technical side: all it does is call a built-in library (see stock prediction above) to create
                    graphs, and runs functions, which are sort of like tasks for computers, to calculate statistics.
                    Although much simpler, it too is a vital part of what makes 500Info tick.
                </p>
            </div>
            <div className="bio-container">
                <h3 className="analyze-select-header">Select Analyze Mode</h3>
                <div className = "analyze-main-menu">
                    <select className="analyze-select" onChange={handleSelect}>
                        <option value="graph">Graph</option>
                        <option value="stat">Statistics</option>
                    </select>
                    <button className = "analyze-rounded-buttonrounded-button" onClick={() => setApiTrigger(!apiTrigger)}>Get Data</button>
                </div>
                <div>{comp()}</div>
            </div>
        </div>
    )
}