import {Bio, Pitch} from "../components/bioComponents.js";
import React from "react";
import '../index.css';

function About() {
    return (
        <div>
            <Pitch />
            <Bio />
        </div>
    );
}

export default About;