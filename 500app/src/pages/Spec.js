import React from 'react';
import {SpecificDescription, Dashboard, SpecificStockComponents} from '../components/specificStockComponents.js'
import '../components/css/index.css';
function Spec() {
    return (
        <div>
            <SpecificDescription />
            <SpecificStockComponents />
        </div>
    );
}

export default Spec;