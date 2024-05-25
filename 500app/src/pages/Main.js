
import '../components/css/index.css';
import {Features, Brief} from '../components/mainPageComponents.js';
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