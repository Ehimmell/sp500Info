
import './index.css';
import {Features, Brief} from './commonComponents.js';
import React from 'react';
import ReactDOM from 'react-dom/client';

function MainPage() {
    return (
        <div>
            <Features />
            <Brief />
        </div>
    );
}

export default MainPage;