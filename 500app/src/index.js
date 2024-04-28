import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App.js';
import About from './About.js';
import {StickyHeader} from './commonComponents.js';
import React, { useState } from 'react';

function Index() {
  const [about, setAbout] = useState(false);

  const handleAboutClick = (isAbout) => {
    setAbout(isAbout);
  };

  const renderPage = () => {
    if (about) {
      return <About />;
    } else {
      return <App />;
    }
  };

  return (
    <React.StrictMode>
        <StickyHeader onAboutClick={handleAboutClick} />
        {renderPage()}
    </React.StrictMode>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Index />);