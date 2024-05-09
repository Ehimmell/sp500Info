import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App.js';
import About from './About.js';
import Predict from './Predict.js';
import {StickyHeader} from './commonComponents.js';
import React, { useState } from 'react';
import Analyze from "./Analyze.js";

function Index() {
  const [about, setAbout] = useState(false);
  const [predict, setPredict] = useState(false);
  const [analyze, setAnalyze] = useState(false);

  const handleClick = (buttonId) => {
  const isAbout = buttonId === 'about';
  const isPredict = buttonId === 'predict';
  const isAnalyze = buttonId === 'analyze';
  setAbout(isAbout);
  setPredict(isPredict);
  setAnalyze(isAnalyze);
  console.log(`handleAboutClick called with ${buttonId}, setting about to ${isAbout}`);
};

  const renderPage = () => {
    if (about) {
      return <About />;
    } else if (predict) {
      return <Predict/>;
    } else if (analyze) {
      return <Analyze />;
    } else {
      return <App />;
    }
  };

  return (
    <React.StrictMode>
        <StickyHeader onButtonClick={handleClick} />
        {renderPage()}
    </React.StrictMode>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Index />);