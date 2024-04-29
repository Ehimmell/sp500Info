import {Bio, Pitch} from "./commonComponents.js";
import React from "react";
import './index.css';

function About() {
    return (
        <div>
            <Pitch />
            <Bio />
        </div>
    );
}

export default About;