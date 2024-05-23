import ReactDOM from 'react-dom/client';
import './index.css';
import App from './pages/Main.js';
import About from './pages/About.js';
import Predict from './pages/Predict.js';
import {StickyHeader} from './components/commonComponents.js';
import React, { useState } from 'react';
import Analyze from "./pages/Analyze.js";
import Help from "./pages/Help.js";

function Index() {
  const [help, setHelp] = useState(false);
  const [about, setAbout] = useState(false);
  const [predict, setPredict] = useState(false);
  const [analyze, setAnalyze] = useState(false);

  const handleClick = (buttonId) => {
    const isAbout = buttonId === 'about';
    const isPredict = buttonId === 'predict';
    const isAnalyze = buttonId === 'analyze';
    const isHelp = buttonId === 'help';
    setAbout(isAbout);
    setPredict(isPredict);
    setAnalyze(isAnalyze);
    setHelp(isHelp);
  };

  const renderPage = () => {
    if (about)
      return <About />;
    if (predict)
      return <Predict/>;
    if (analyze)
      return <Analyze />;
    if (help)
      return <Help />;
    return <App />;
  }

  return (
    <React.StrictMode>
        <StickyHeader onButtonClick={handleClick} />
        {renderPage()}
    </React.StrictMode>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Index />);