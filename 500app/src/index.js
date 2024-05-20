import ReactDOM from 'react-dom/client';
import './index.css';
import App from './pages/Main.js';
import About from './pages/About.js';
import Predict from './pages/Predict.js';
import {StickyHeader} from './components/commonComponents.js';
import React, { useState } from 'react';
import Analyze from "./pages/Analyze.js";

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