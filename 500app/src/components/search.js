import id from "./constants.cjs";
import axios from "axios";
export const getSearchedTicker = (query = "apple") => {
    return axios.get('https://www.googleapis.com/customsearch/v1', {
        params: {
            key: process.env.REACT_APP_API_KEY,
            cx: process.env.REACT_APP_ENGINE_ID,
            q: query
        }
    })
    .then(response => {
        if (response.data.items) {
            return response.data.items.map(item => {
                const { title, link, snippet } = item;
                return title;
            });
        } else {
            console.log("No search results found"); // print a message if no search results were found
            return [];
        }
    })
    .catch(error => {
        console.error("Error during search:", error); // print the error
        return [];
    });

}
